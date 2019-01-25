import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from dash_tabs import app, df

@app.callback(
    Output('tab1_state_dropdown', 'value'),
    [Input('all_states_button', 'n_clicks')])
def all_states(n_clicks):
    """
    When user clicks on the 'All states' button, populate the dropdown
    with all unique states in the dataset.

    """
    return df.State.unique().tolist()

@app.callback(
    Output('tab1_table', 'data'),
    [Input('tab1_state_dropdown', 'value')])
def fill_datatable(states):
    """
    Fill the DataTable with a dict for all states that were selected.
    """
    return df[df.State.isin(states or [])].to_dict('rows')


@app.callback(
    Output('tab1_datatable-summary', "children"),
    [Input('tab1_table', "data"),
     Input('tab1_table', "selected_rows")])
def summarize_table(rows, selected_rows):
    """
    Summarize the table contents, displaying states listed and selected.
    """

    dtemp = pd.DataFrame(rows) #turn the data into a DataFrame

    state = "no state selected" # default value
    if selected_rows and selected_rows[0] <= len(dtemp):
        state = dtemp.iloc[selected_rows[0]]['State']

    all_states = []
    if len(dtemp)>0:
        all_states = dtemp.State.unique()

    return html.Div(f'all states: {str(all_states)}, selected state: {state}')


for page_side in ['_left', '_right']:
    @app.callback(
        Output('tab1_graph' + page_side, 'figure'),
        [Input('tab1_button' + page_side, 'n_clicks')],
        [State('tabs', 'value')])
    def tab1_update_graph(n_clicks, tab):
        """
        Update the graphs based on the number of clicks:
            - If even number of clicks y=[3,1,1]
            - If uneven number of clicks y =[1,2,3]
        """
        if (n_clicks % 2 == 0):
            trace1 = go.Bar(
                x=[1, 2, 3],
                y=[3, 1, 1]
            )
            data = [trace1]
            layout = go.Layout()
            fig = go.Figure(data=data, layout=layout)

        else:
            trace1 = go.Bar(
                x=[1, 2, 3],
                y=[1, 2, 3]
            )
            data = [trace1]
            layout = go.Layout()
            fig = go.Figure(data=data, layout=layout)

        return fig
