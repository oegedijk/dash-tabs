import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from dash_tabs import app

@app.callback(
    Output('dropdown_b', 'options'),
    [Input('dropdown_a', 'value')])
def set_dropdown_b_options(value):
    """
    Set the options for dropdown B conditional on the value of dropdown A.
    """
    options_b = []
    if value=='A':
        options_b = [{'label': 'C', 'value': 'C'},
                     {'label': 'D', 'value': 'D'}]
    if value == 'B':
        options_b = [{'label': 'E', 'value': 'E'},
                     {'label': 'F', 'value': 'F'}]
    return options_b

@app.callback(
    Output('dropdown_b', 'value'),
    [Input('dropdown_a', 'value')])
def set_dropdown_b_value(value):
    """
    Set the default value for dropdown B conditional on the value of dropdown A.
    """
    value_b = None
    if value=='A': value_b = 'C'
    if value == 'B': value_b = 'E'
    return value_b

@app.callback(
    Output('dropdown_c', 'options'),
    [Input('dropdown_b', 'value')])
def set_dropdown_b_options(value):
    """
    Set the options for dropdown C conditional on the value of dropdown B.
    """
    options_c = []
    if value=='C':
        options_c = [{'label': '1', 'value': '1'},
                     {'label': '2', 'value': '2'}]
    if value == 'D':
        options_c = [{'label': '3', 'value': '3'},
                     {'label': '4', 'value': '4'}]
    if value=='E':
        options_c = [{'label': '5', 'value': '5'},
                     {'label': '6', 'value': '6'}]
    if value == 'F':
        options_c = [{'label': '7', 'value': '7'},
                     {'label': '8', 'value': '8'}]
    return options_c

@app.callback(
    Output('dropdown_c', 'value'),
    [Input('dropdown_b', 'value')])
def set_dropdown_b_options(value):
    """
    Set the default value for dropdown C conditional on the value of
    dropdown B.
    """
    value_c = None
    if value=='C': value_c = '1'
    if value == 'D': value_c = '3'
    if value=='E': value_c = '5'
    if value == 'F': value_c = '7'
    return value_c

@app.callback(
    Output('output_area', 'children'),
    [Input('dropdown_c', 'value')],
    [State('dropdown_b', 'value'),
     State('dropdown_a', 'value')])
def print_test(value_c, value_b, value_a):
    """
    Display the value of dropdown A, B and C.
    """
    return f'a: {str(value_a)} b: {str(value_b)} + c: {str(value_c)}' 
