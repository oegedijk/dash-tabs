import dash_html_components as html
import dash_core_components as dcc

from datetime import datetime, date, timedelta

from query_string_methods import apply_value_from_querystring

def tab2_layout1(params):
    return html.Div([
            apply_value_from_querystring(params)(dcc.RadioItems)(
                id='tab2_radiobutton-a',
                options=[{'label': i, 'value': i}
                            for i in ['Canada', 'USA', 'Mexico']],
                value='Canada'
            ),

            html.Div(id='tab2_output-a', children='hello world!'),

            apply_value_from_querystring(params)(dcc.RadioItems)(
                id='tab2_radiobutton-b',
                options=[{'label': i, 'value': i}
                            for i in ['MTL', 'NYC', 'SF']],
                value='MTL',
                labelStyle={'display': 'inline-block'}
            ),
            apply_value_from_querystring(params)(dcc.Dropdown)(
                id='tab2_multidropdown',
                options=[{'label': i, 'value': i}
                            for i in ['Ajax', 'Feyenoord', 'PSV']],
                value='Ajax',
                multi=True
            ),
            apply_value_from_querystring(params)(dcc.DatePickerRange)(
                    id='tab2_datepicker',
                    first_day_of_week=2,
                    start_date=date.today() - timedelta(days=7),
                    end_date=date.today(),

                ),
            apply_value_from_querystring(params)(html.Button)('Submit',
                                                     id='tab2_submit-button',
                                                     n_clicks=0),
            html.Div(id='tab2_output-b')
        ])
