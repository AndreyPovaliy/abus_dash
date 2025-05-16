from dash import html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html

df = pd.read_csv('data/us_data.csv')

def register_callbacks(app):
    @app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)
    def render_tab_content(active_tab, data):

        if active_tab and data is not None:
            if active_tab == "anamnesis":
                return [dbc.Row(dbc.Col(html.Div(data["stats-panel"]))),
            dbc.Row(
                    [
                        dbc.Col(dcc.Graph(figure=data["diagnosis_primary"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["satus_reproductive"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["complaints"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["breast_surgery_before"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["skin_symptoms"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["nipple_retraction"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["nipple_release"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["genetics"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["hormonal_medications"]), width=6),
                    ]
                )]
                                    

            
            elif active_tab == "us_data":
                return [
                    dbc.Row(dbc.Col(html.Div(data["stats-panel"]))),
                    dbc.Row(
                    [
                        dbc.Col(dcc.Graph(figure=data["us_nodle_contour"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_ducts"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_background"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_formation"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_nodle_size"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_echogenicity_formation"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_structure"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_formation_blood_flow"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_elastography"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_region_lymph_nodes"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_number_nodles"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_category_birads"]), width=6),
                        dbc.Col(dcc.Graph(figure=data["us_calcinates_micro_pure"]), width=6)

                    ]
                )]
        return "No tab selected"


    @app.callback(Output("store", "data"),
                Input('diagnosis_primary-filter', 'value'),
                Input('group-filter', 'value'),
                Input('complaints-filter', 'value'),
                Input('breast_surgery_before-filter', 'value'),
                Input('skin_symptoms-filter', 'value'),
                Input('nipple_retraction-filter', 'value'),
                Input('nipple_release-filter', 'value'),
                Input('genetics-filter', 'value'),
                Input('hormonal_medications-filter', 'value'),
                Input('us_nodle_contour-filter', 'value'),
                Input('us_ducts-filter', 'value'),
                Input('us_background-filter', 'value'),
                Input('us_formation-filter', 'value'),
                Input('us_form-filter', 'value'),
                Input('us_nodle_size-filter', 'value'),
                Input('us_echogenicity_formation-filter', 'value'),
                Input('us_structure-filter', 'value'),
                Input('us_formation_blood_flow-filter', 'value'),
                Input('us_elastography-filter', 'value'),
                Input('us_region_lymph_nodes-filter', 'value'),
                Input('us_number_nodles-filter', 'value'),
                Input('us_category_birads-filter', 'value'),
                Input('us_calcinates_micro_pure-filter', 'value')

                )


    def generate_graphs(selected_diagnosis_primary,
                        selected_group_separation,
                        selected_complaints,
                        selected_breast_surgery_before,
                        selected_skin_symptoms,
                        selected_nipple_retraction,
                        selected_nipple_release,
                        selected_genetics,
                        selected_hormonal_medications,
                        selected_us_nodle_contour,
                        selected_us_ducts,
                        selected_us_background,
                        selected_us_formation,
                        selected_us_form,
                        selected_us_nodle_size,
                        selected_us_echogenicity_formation,
                        selected_us_structure,
                        selected_us_formation_blood_flow,
                        selected_us_elastography,
                        selected_us_region_lymph_nodes,
                        selected_us_number_nodles,
                        selected_us_category_birads,
                        selected_us_calcinates_micro_pure):

        
        filtered_df = df[
                (df['diagnosis_primary'].isin(selected_diagnosis_primary)) & 
                (df['group_separation'].isin(selected_group_separation)) &
                (df['complaints'].isin(selected_complaints)) &
                (df['breast_surgery_before'].isin(selected_breast_surgery_before)) &
                (df['skin_symptoms'].isin(selected_skin_symptoms)) &
                (df['nipple_retraction'].isin(selected_nipple_retraction)) &
                (df['nipple_release'].isin(selected_nipple_release)) &
                (df['genetics'].isin(selected_genetics)) &
                (df['hormonal_medications'].isin(selected_hormonal_medications)) &
                (df['us_nodle_contour'].isin(selected_us_nodle_contour)) &
                (df['us_ducts'].isin(selected_us_ducts)) &
                (df['us_background'].isin(selected_us_background)) &
                (df['us_formation'].isin(selected_us_formation)) &
                (df['us_form'].isin(selected_us_form)) &
                (df['us_nodle_size'].isin(selected_us_nodle_size)) &
                (df['us_echogenicity_formation'].isin(selected_us_echogenicity_formation)) &
                (df['us_structure'].isin(selected_us_structure)) &
                (df['us_formation_blood_flow'].isin(selected_us_formation_blood_flow)) &
                (df['us_elastography'].isin(selected_us_elastography)) &
                (df['us_region_lymph_nodes'].isin(selected_us_region_lymph_nodes)) &
                (df['us_number_nodles'].isin(selected_us_number_nodles)) &
                (df['us_category_birads'].isin(selected_us_category_birads)) &
                (df['us_calcinates_micro_pure'].isin(selected_us_calcinates_micro_pure))


                ]
            

        total_patients = len(filtered_df)
        avg_age = filtered_df['age_patient'].mean()

        diagnosis_primary_counts =filtered_df['diagnosis_primary'].value_counts()
        satus_reproductive_counts =filtered_df['satus_reproductive'].value_counts()
        complaints_counts =filtered_df['complaints'].value_counts()
        breast_surgery_before_counts =filtered_df['breast_surgery_before'].value_counts()
        skin_symptoms_counts =filtered_df['skin_symptoms'].value_counts()
        nipple_retraction_counts =filtered_df['nipple_retraction'].value_counts()
        nipple_release_counts =filtered_df['nipple_release'].value_counts()
        genetics_counts =filtered_df['genetics'].value_counts()
        hormonal_medications_counts =filtered_df['hormonal_medications'].value_counts()

        us_nodle_contour_counts =filtered_df['us_nodle_contour'].value_counts()
        us_ducts_counts =filtered_df['us_ducts'].value_counts()
        us_background_counts =filtered_df['us_background'].value_counts()
        us_formation_counts =filtered_df['us_formation'].value_counts()
        us_form_counts =filtered_df['us_form'].value_counts()
        us_nodle_size_counts =filtered_df['us_nodle_size'].value_counts()
        us_echogenicity_formation_counts =filtered_df['us_echogenicity_formation'].value_counts()
        us_structure_counts =filtered_df['us_structure'].value_counts()
        us_formation_blood_flow_counts =filtered_df['us_formation_blood_flow'].value_counts()
        us_elastography_counts =filtered_df['us_elastography'].value_counts()
        us_region_lymph_nodes_counts =filtered_df['us_region_lymph_nodes'].value_counts()
        us_number_nodles_counts =filtered_df['us_number_nodles'].value_counts()
        us_category_birads_counts =filtered_df['us_category_birads'].value_counts()
        us_calcinates_micro_pure_counts =filtered_df['us_calcinates_micro_pure'].value_counts()






        diagnosis_primary_fig = go.Figure(
                go.Pie(
                    labels=diagnosis_primary_counts.index,
                    values=diagnosis_primary_counts.values,
                    textinfo='percent'
                )
            )
        satus_reproductive_fig = go.Figure(
                go.Bar(
                    x=satus_reproductive_counts.index,
                    y=satus_reproductive_counts.values
                )
            )
        
        complaints_fig = go.Figure(
                go.Pie(
                    labels=complaints_counts.index,
                    values=complaints_counts.values,
                    textinfo='percent'
                )
            ) 
        
        breast_surgery_before_fig = go.Figure(
                go.Bar(
                    x=breast_surgery_before_counts.index,
                    y=breast_surgery_before_counts.values
                )
            ) 
        
        skin_symptoms_fig = go.Figure(
                go.Pie(
                    labels=skin_symptoms_counts.index,
                    values=skin_symptoms_counts.values,
                    textinfo='percent'
                )
            )

        nipple_retraction_fig = go.Figure(
                go.Bar(
                    x=nipple_retraction_counts.index,
                    y=nipple_retraction_counts.values
                )
            )
        
        nipple_release_fig = go.Figure(
                go.Bar(
                    x=nipple_release_counts.index,
                    y=nipple_release_counts.values
                )
            )
        

        genetics_fig = go.Figure(
                go.Pie(
                    labels=genetics_counts.index,
                    values=genetics_counts.values,
                    textinfo='percent'
                )
            )
        

        hormonal_medications_fig = go.Figure(
                go.Pie(
                    labels=hormonal_medications_counts.index,
                    values=hormonal_medications_counts.values,
                    textinfo='percent'
                )
            )

        us_nodle_contour_fig = go.Figure(
                go.Pie(
                    labels=us_nodle_contour_counts.index,
                    values=us_nodle_contour_counts.values,
                    textinfo='percent'
                )
            )
        
        us_ducts_fig = go.Figure(
                go.Pie(
                    labels=us_ducts_counts.index,
                    values=us_ducts_counts.values,
                    textinfo='percent'
                )
            )
        us_background_fig = go.Figure(
                go.Pie(
                    labels=us_background_counts.index,
                    values=us_background_counts.values,
                    textinfo='percent'
                )
            )
        us_formation_fig = go.Figure(
                go.Pie(
                    labels=us_formation_counts.index,
                    values=us_formation_counts.values,
                    textinfo='percent'
                )
            )
        us_form_fig = go.Figure(
                go.Pie(
                    labels=us_form_counts.index,
                    values=us_form_counts.values,
                    textinfo='percent'
                )
            )
        us_nodle_size_fig = go.Figure(
                go.Pie(
                    labels=us_nodle_size_counts.index,
                    values=us_nodle_size_counts.values,
                    textinfo='percent'
                )
            )
        us_echogenicity_formation_fig = go.Figure(
                go.Pie(
                    labels=us_echogenicity_formation_counts.index,
                    values=us_echogenicity_formation_counts.values,
                    textinfo='percent'
                )
            )
        us_structure_fig = go.Figure(
                go.Pie(
                    labels=us_structure_counts.index,
                    values=us_structure_counts.values,
                    textinfo='percent'
                )
            )
        us_formation_blood_flow_fig = go.Figure(
                go.Pie(
                    labels=us_formation_blood_flow_counts.index,
                    values=us_formation_blood_flow_counts.values,
                    textinfo='percent'
                )
            )
        us_elastography_fig = go.Figure(
                go.Pie(
                    labels=us_elastography_counts.index,
                    values=us_elastography_counts.values,
                    textinfo='percent'
                )
            )
        
        us_region_lymph_nodes_fig = go.Figure(
                go.Pie(
                    labels=us_region_lymph_nodes_counts.index,
                    values=us_region_lymph_nodes_counts.values,
                    textinfo='percent'
                )
            )
        
        us_number_nodles_fig = go.Figure(
                go.Pie(
                    labels=us_number_nodles_counts.index,
                    values=us_number_nodles_counts.values,
                    textinfo='percent'
                )
            )
        us_category_birads_fig = go.Figure(
                go.Pie(
                    labels=us_category_birads_counts.index,
                    values=us_category_birads_counts.values,
                    textinfo='percent'
                )
            )
        us_calcinates_micro_pure_fig = go.Figure(
                go.Pie(
                    labels=us_calcinates_micro_pure_counts.index,
                    values=us_calcinates_micro_pure_counts.values,
                    textinfo='percent'
                )
            )


        stats_panel = dbc.Card([
                dbc.CardHeader("Статистика выборки", className="stats-header"),
                dbc.CardBody([
                    html.P(f"Всего пациентов: {total_patients}"),
                    html.P(f"Средний возраст: {avg_age:.0f} лет"),
                ])])

        # save figures in a dictionary for sending to the dcc.Store
        return {"diagnosis_primary": diagnosis_primary_fig, 
                "satus_reproductive": satus_reproductive_fig, 
                "complaints":complaints_fig,
                "breast_surgery_before":breast_surgery_before_fig,
                "skin_symptoms":skin_symptoms_fig,
                "nipple_retraction":nipple_retraction_fig,
                "nipple_release":nipple_release_fig,
                "genetics":genetics_fig,
                "hormonal_medications":hormonal_medications_fig,
                "us_nodle_contour": us_nodle_contour_fig,
                "us_ducts":us_ducts_fig,
                "us_background":us_background_fig,
                "us_formation":us_formation_fig,
                "us_form":us_form_fig,
                "us_nodle_size":us_nodle_size_fig,
                "us_echogenicity_formation":us_echogenicity_formation_fig,
                "us_structure":us_structure_fig,
                "us_formation_blood_flow":us_formation_blood_flow_fig,
                "us_elastography":us_elastography_fig,
                "us_region_lymph_nodes":us_region_lymph_nodes_fig,
                "us_number_nodles":us_number_nodles_fig,
                "us_category_birads":us_category_birads_fig,
                "us_calcinates_micro_pure":us_calcinates_micro_pure_fig,
                "stats-panel":stats_panel}
