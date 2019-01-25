import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from dash_tabs import app

@app.callback(
    Output('tab2_output-a', 'children'),
    [Input('tab2_radiobutton-a', 'value')],
    [State('tabs', 'value')])
def callback_a(radio_button_a_value, tab):
    """
    Display the value selected of radiobutton-a.
    """
    return f'Country selected: {radio_button_a_value}'


@app.callback(
    Output('tab2_output-b', 'children'),
    [Input('tab2_submit-button', 'n_clicks')],
    [State('tab2_radiobutton-b', 'value'),
     State('tab2_multidropdown', 'value'),
     State('tab2_datepicker', 'start_date'),
     State('tabs', 'value')])
def callback_b(n_clicks,
               radio_button_b_value,
               multidropdown_value,
               startdate,
               tab):
    """
    When user clicks on the submit button, display the value of dropdown-b
    """
    if n_clicks > 0:
        return f"""City Selected: {radio_button_b_value}
                   Clubs selected: {str(multidropdown_value)}
                   Starting date: {str(startdate)}"""
