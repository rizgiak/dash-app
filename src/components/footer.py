# notes
'''
This file is for creating a simple footer element.
This component will sit at the bottom of each page of the application.
'''

# package imports
from dash import html
import dash_bootstrap_components as dbc

footer = html.Footer(
    dbc.Container(
        [
            html.Hr(),
            '2023 Simulation Group',
            # html.Br(),
            # 'Footer item 2',
            # html.Br(),
            # 'Footer item 3'
        ]
    )
)
