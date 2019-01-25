import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd

from urllib.parse import urlparse, parse_qsl, urlencode

import json
from base64 import urlsafe_b64encode, urlsafe_b64decode

from query_string_methods import apply_value_from_querystring
from query_string_methods import parse_state, encode_state

# Load the tab layouts from the appropriate directories:
from tab1.tab1_layout import tab1_layout1
from tab2.tab2_layout import tab2_layout1
from tab3.tab3_layout import tab3_layout1

# Load a sample database to display
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')


# have to add __name__ in order to load the css from /assets/
app = dash.Dash(__name__)

# this config is necessary for multi file dash apps
app.config['suppress_callback_exceptions']=True


# The overall layout. Will be build properly in a callback triggered by the
# querystring
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-layout')
])
# The layout build function. Takes in values from the querystring in params,
# defines two parent tabs, then three subtabs, and call the layout function
# for each tab.
#
# The params get passed on to each param function.
def build_layout(params):
    """
    The layout build function. Takes in values from the querystring in params,
    defines two parent tabs, then three subtabs, and call the layout function
    for each tab.

    The params get passed on to each tab layout function.
    """
    return dcc.Tabs(id='parent_tab', value='tab_a', children = [
        dcc.Tab(label='Tabs A', id='tab_a', value='tab1',
            children = apply_value_from_querystring(params)(dcc.Tabs)(
                        id="tabs",
                        value='tab1',
                        children=[
                            dcc.Tab(label='Tab One',
                                    value='tab1',
                                    children=tab1_layout1(
                                                # querystring params:
                                                params,
                                                # States to add to state dropdown:
                                                df['State'].unique().tolist(),
                                                # Columns to display in DataTable:
                                                df.columns)
                                    ),
                            dcc.Tab(label='Tab Two',
                                    value='tab2',
                                    children=tab2_layout1(params)
                                   ),
                            dcc.Tab(label='Tab Three',
                                    value='tab3',
                                    children=tab3_layout1
                                   ),
                        ]),
        ),
        dcc.Tab(label='Tabs B', id='tab_b', children=html.Div([]))
        ])


@app.callback(Output('page-layout', 'children'),
              [Input('url', 'href')])
def page_load(href):
    """
    Upon page load, take the url, parse the querystring, and use the
    resulting state dictionary to build up the layout.
    """
    if not href:
        return []
    state = parse_state(href)
    return build_layout(state)

component_ids = [
    ('tabs', 'value'),
    ('tab1_state_dropdown', 'value'),
    ('tab1_table', 'selected_rows'),
    ('tab2_radiobutton-a', 'value'),
    ('tab2_radiobutton-b', 'value'),
    ('tab2_multidropdown', 'value'),
    ('tab2_datepicker', 'start_date'),
    ('tab2_submit-button', 'n_clicks')
]

component_ids_zipped= list(zip(*component_ids))

@app.callback(Output('url', 'search'),
              inputs=[Input(id, param) for id, param in component_ids])
def update_url_state(*values):
    return encode_state(component_ids, values)


# Import the callbacks after having defined the layout.
from tab1.tab1_callbacks import *
from tab2.tab2_callbacks import *
from tab3.tab3_callbacks import *


if __name__ == '__main__':
    app.run_server(debug=True)
