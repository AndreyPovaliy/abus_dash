import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
import settings as st


df = pd.read_csv('data/us_data.csv')


def create_layout():
    return dbc.Container([
        # Заголовок
        html.Div([
            html.H1("Анализ скрининга новообразований МЖ", className="header-title"),
            html.H2("Исследование характеристик", className="header-description")
        ], className="header"
        ),

        # Фильтры
        dbc.Row([
        
                                  
            dbc.Col([html.Label("Диагноз", className="filter-label"), 
                     dcc.Dropdown(id="diagnosis_primary-filter",
                                  options=[{'label': dp, 'value': dp } for dp in df['diagnosis_primary'].unique()],
                                  value=df['diagnosis_primary'].unique(),
                                  multi=True, 
                                  className="filter-dropdown",
                                  style=st.DROPDOWN_STYLE,
                                  )], md=4),
            dbc.Col([html.Label("Группа", className="filter-label"), 
                     dcc.Dropdown(id="group-filter",
                                  options=[{'label': g, 'value': g } for g in df['group_separation'].unique()],
                                  value=df['group_separation'].unique(),
                                  multi=True, 
                                  className="filter-dropdown",
                                  style=st.DROPDOWN_STYLE,
                                  )], md=4),

            

         
        ], className="filters-row"

        ),

        #информационная панель
        html.Div(id='stats-panel', className="stats-panel"),

        dbc.Tabs(
            [
                dbc.Tab(label="Данные анамнеза", tab_id="anamnesis"),
                dbc.Tab(label="Данные УЗИ", tab_id="us_data"),
            ],
            id="tabs",
            active_tab="anamnesis"
        ),

        # Графики
        dbc.Row([
            
                 dbc.Col([dcc.Graph(id='diagnosis_primary-pie')], md=6),
                 dbc.Col([dcc.Graph(id='satus_reproductive-bar')], md=6)
                 ])     
        ], fluid=True)