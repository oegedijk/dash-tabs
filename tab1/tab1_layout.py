import dash_html_components as html
import dash_core_components as dcc
import dash_table

from query_string_methods import apply_value_from_querystring

def tab1_layout1(params, states, columns):
    """
    Layout for Tab1:
    - A state selection dropdown menu
    - A button to select all states in the dropdown
    - A DataTable to display data for selected states
    - A div to display a string summarizing the data

    - Two graphs that change whenever you click the button.
    """
    layout = html.Div([
        html.Div([
            html.Button('All States', id='all_states_button'),
            apply_value_from_querystring(params)(dcc.Dropdown)(
                id='tab1_state_dropdown',
                placeholder='Select states to display...',
                options=[{'label': i, 'value': i} for i in states],
                multi=True
            ),
            apply_value_from_querystring(params)(dash_table.DataTable)(
                    id='tab1_table',
                    columns=[{"name": i, "id": i} for i in columns],
                    editable=True,
                    sorting=True,
                    sorting_type="single",
                    row_selectable="single",
                    selected_rows=[],
                ),
             html.Div(id='tab1_datatable-summary'),
        ], className="row"),

        html.Div([
            html.Div([
                html.Button('Switch Graph', id='tab1_button_left'),
                dcc.Graph(id='tab1_graph_left'),
            ], className="col-md-6"),
            html.Div([
                     html.Button('Switch Graph', id='tab1_button_right'),
                     dcc.Graph(id='tab1_graph_right')
            ], className="col-md-6"),
        ], className="row"),
    ])
    return layout
