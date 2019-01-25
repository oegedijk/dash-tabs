import dash_html_components as html
import dash_core_components as dcc

tab3_layout1 = html.Div([
    dcc.Dropdown(id='dropdown_a',
                 options = [{'label': 'A', 'value': 'A'},
                            {'label': 'B', 'value': 'B'}]),
    dcc.Dropdown(id='dropdown_b'),
    dcc.Dropdown(id='dropdown_c'),
    html.Div(id='output_area')
])
