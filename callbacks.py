from dash import html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
import settings as st
import plotly.io as pio
from dash import dcc, html

# загрузка данных
df = pd.read_csv('data/us_data.csv')

def register_callbacks(app):
    @app.callback(
        Output('diagnosis_primary-pie', 'figure'),
        Output('satus_reproductive-bar', 'figure'),
        Output('stats-panel', 'children'),
        Input('diagnosis_primary-filter', 'value'),
        Input('group-filter', 'value')
        
    )

    def render_tab_content(active_tab):
        if active_tab is not None:
            if active_tab == "anamnesis":
                return "anamnesis tab selected"

            elif active_tab == "us_data":
                return "US tab selected"
            
        return "No tab selected"

    def update_graphs(selected_diagnosis_primary,selected_group_separation):
        # фильтрация данных
        filtered_df = df[
            (df['diagnosis_primary'].isin(selected_diagnosis_primary)) & 
            (df['group_separation'].isin(selected_group_separation))
            ]
        

         # считаем статистику

        total_patients = len(filtered_df)
        avg_age = filtered_df['age_patient'].mean()
        diagnosis_primary_counts =filtered_df['diagnosis_primary'].value_counts()
        satus_reproductive_counts =filtered_df['satus_reproductive'].value_counts()

        stats_panel = dbc.Card([
            dbc.CardHeader("Статистика выборки", className="stats-header"),
            dbc.CardBody([
                html.P(f"Всего пациентов: {total_patients}"),
                html.P(f"Средний возраст: {avg_age:.0f} лет"),
            ])

        ])

        # Pie

        
        pie_fig_diagnosis_primary = go.Figure(
            go.Pie(
                labels=diagnosis_primary_counts.index,
                values=diagnosis_primary_counts.values,
                textinfo='percent'
            )
        )
        # pie_fig_diagnosis_primary.update_layout(
        #     title='Распределение по диагнозам',
        #     title_font_size=st.GRAPH_TITLE_FONT_SIZE,
        #     title_x=st.GRAPH_TITLE_ALIGN,
        #     title_font_weight=st.GRAPH_TITLE_WEIGHT,
        #     font=dict(family="Roboto, sans-serif"),
        #     legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
        #     plot_bgcolor=st.PLOT_BACKGROUND,
        #     paper_bgcolor=st.PAPER_BACKGROUND,
        # )

        bar_fig_atus_reproductive = go.Figure(
            go.Bar(
                x=satus_reproductive_counts.index,
                y=satus_reproductive_counts.values
            )
        )

        return  pie_fig_diagnosis_primary, bar_fig_atus_reproductive, stats_panel