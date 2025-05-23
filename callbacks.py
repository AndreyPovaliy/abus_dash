from dash import html, Input, State, Output
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html
import settings as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score

df = pd.read_csv('data/us_data.csv')
df_us = df[['age_patient',
            'diagnosis_primary',
            'side',
            'satus_reproductive',
            'complaints',
            'breast_surgery_before', 
            'skin_symptoms',
            'nipple_retraction', 
            'nipple_release',
            'quadrant', 
            'genetics',
            'hormonal_medications',
            'hist_is_tumor']]
df_us_jn = df_us[df_us['age_patient'] < 40]
df_us1 = df[['age_patient',
            'diagnosis_primary',
            'side',
            'satus_reproductive',
            'complaints',
            'breast_surgery_before', 
            'skin_symptoms',
            'nipple_retraction', 
            'nipple_release',
            'quadrant', 
            'genetics',
            'hormonal_medications',
            'mmg_conclusion_skin',
            'mmg_areola',
            'mmg_nipple',
            'mmg_background_breast',
            'mmg_nodle',
            'mmg_nodle_contour',
            'mmg_nodle_size',
            'mmg_calcifications',
            'mmg_number_formations_visualized',
            'mmg_axillary_lymph_nodes',
            'mmg_conclusion',
            'type_structure_acr',
            'mmg_number_nodles',
            'mmg_category_birads',
            'hist_is_tumor']]
df_us_snr = df_us1[df_us1['age_patient'] >= 40]



def register_callbacks(app):
    @app.callback(
    Output("collapse-an", "is_open"),
    [Input("collapse-button-anamnesis", "n_clicks")],
    [State("collapse-an", "is_open")],
)
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
    
    @app.callback(
    Output("collapse-us", "is_open"),
    [Input("collapse-button-us", "n_clicks")],
    [State("collapse-us", "is_open")],
)
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
    
    @app.callback(
    Output("collapse-mmg", "is_open"),
    [Input("collapse-button-mmg", "n_clicks")],
    [State("collapse-mmg", "is_open")],
)
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
    
    @app.callback(
    Output("collapse-abus", "is_open"),
    [Input("collapse-button-abus", "n_clicks")],
    [State("collapse-abus", "is_open")],
)
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
    
    @app.callback(
    Output("collapse-hist", "is_open"),
    [Input("collapse-button-hist", "n_clicks")],
    [State("collapse-hist", "is_open")],
)
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
    Output("collapse-prob", "is_open"),
    [Input("collapse-button-prob", "n_clicks")],
    [State("collapse-prob", "is_open")],
)
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
    
    @app.callback(
    Output("collapse-pred", "is_open"),
    [Input("collapse-button-pred", "n_clicks")],
    [State("collapse-pred", "is_open")],
)
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
    
    @app.callback(
    Output("collapse-pred1", "is_open"),
    [Input("collapse-button-pred1", "n_clicks")],
    [State("collapse-pred1", "is_open")],
)
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

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
                        dbc.Col(dcc.Graph(figure=data["diagnosis_primary"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["group_separation"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["satus_reproductive"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["complaints"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["breast_surgery_before"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["skin_symptoms"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["nipple_retraction"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["nipple_release"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["genetics"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["hormonal_medications"]), width=12),
                    ]
                )]
                                    

            
            elif active_tab == "us_data":
                return [
                    dbc.Row(dbc.Col(html.Div(data["stats-panel"]))),
                    dbc.Row(
                    [
                        dbc.Col(dcc.Graph(figure=data["us_nodle_contour"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_ducts"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_background"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_formation"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_nodle_size"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_echogenicity_formation"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_structure"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_formation_blood_flow"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_elastography"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_region_lymph_nodes"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_number_nodles"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_category_birads"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["us_calcinates_micro_pure"]), width=12)

                    ]
                )]
           
            elif active_tab == "mmg_data":
                return [
                    dbc.Row(dbc.Col(html.Div(data["stats-panel"]))),
                    dbc.Row(
                    [
                        dbc.Col(dcc.Graph(figure=data["mmg_background_breast"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["mmg_nodle"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["mmg_nodle_contour"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["mmg_nodle_size"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["mmg_calcifications"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["mmg_number_formations_visualized"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["mmg_axillary_lymph_nodes"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["type_structure_acr"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["mmg_category_birads"]), width=12)
                    ]
                )]
            elif active_tab == "abus_data":
                return [
                    dbc.Row(dbc.Col(html.Div(data["stats-panel"]))),
                    dbc.Row(
                    [
                        dbc.Col(dcc.Graph(figure=data["abus_nodle_size"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["abus_nodle_contours"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["abus_echogenicity_formation"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["abus_structure"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["abus_symptom_retraction"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["abus_formation"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["abus_category_birads"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["abus_calcinates"]), width=12)

                    ]
                )]
            elif active_tab == "hist_data":
                return [
                    dbc.Row(dbc.Col(html.Div(data["stats-panel"]))),
                    dbc.Col(
                    [
                        dbc.Col(dcc.Graph(figure=data["tumor_morphology_structure"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["cytological_conclusion"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["degree_malignancy"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["mutation_brca"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["tumor_receptors"]), width=12),
                        dbc.Col(dcc.Graph(figure=data["hist_is_tumor"]), width=12)

                    ]
                )]
            elif active_tab == "prob_data":
                return [
                    dbc.Col(dbc.Col(html.Div(data["stats-panel"]))),
                    
                    dbc.Col(
                    [
                        
                        dbc.Col(dcc.Graph(figure=data["us_probabilityCalc"]), width=12)
                    ]),
                     dbc.Col(
                    [
                        
                        dbc.Col(dcc.Graph(figure=data["abus_probabilityCalc"]), width=12)
                     ]),
                     dbc.Col(
                    [
                        
                        dbc.Col(dcc.Graph(figure=data["us_probabilityNeoCa"]), width=12),
                         ]),
                     dbc.Col(
                    [
                        
                        dbc.Col(dcc.Graph(figure=data["abus_probabilityNeoCa"]), width=12),
                         ]),
                     dbc.Col(
                    [
                        dbc.Col(dcc.Graph(figure=data["mmg_probabilityNeoCa"]), width=12)

                    ]
                )]
            elif active_tab == "pred_data":
                return [dbc.Row(dbc.Col(html.Div(data["ml-panel_jun"]))),
                        dbc.Row(dbc.Col(html.Div(data["ml-panel_snr"]))),
                ]
        return "No tab selected"


    @app.callback(Output("store", "data"),
                Input('diagnosis_primary-filter', 'value'),
                Input('satus_reproductive-filter', 'value'),
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
                Input('us_calcinates_micro_pure-filter', 'value'),
                Input('mmg_background_breast-filter', 'value'),
                Input('mmg_nodle-filter', 'value'),
                Input('mmg_nodle_contour-filter', 'value'),
                Input('mmg_nodle_size-filter', 'value'),
                Input('mmg_calcifications-filter', 'value'),
                Input('mmg_number_formations_visualized-filter', 'value'),
                Input('mmg_axillary_lymph_nodes-filter', 'value'),
                Input('type_structure_acr-filter', 'value'),
                Input('mmg_category_birads-filter', 'value'),
                Input('abus_nodle_size-filter', 'value'),
                Input('abus_nodle_contours-filter', 'value'),
                Input('abus_echogenicity_formation-filter', 'value'),
                Input('abus_structure-filter', 'value'),
                Input('abus_symptom_retraction-filter', 'value'),
                Input('abus_formation-filter', 'value'),
                Input('abus_category_birads-filter', 'value'),
                Input('abus_calcinates-filter', 'value'),
                Input('tumor_morphology_structure-filter', 'value'),
                Input('cytological_conclusion-filter', 'value'),
                Input('degree_malignancy-filter', 'value'),
                Input('mutation_brca-filter', 'value'),
                Input('tumor_receptors-filter', 'value'),
                Input('hist_is_tumor-filter', 'value'),
                Input('us_probabilityCalc-filter', 'value'),
                Input('abus_probabilityCalc-filter', 'value'),
                Input('us_probabilityNeoCa-filter', 'value'),
                Input('abus_probabilityNeoCa-filter', 'value'),
                Input('mmg_probabilityNeoCa-filter', 'value'),
                Input("age_patient_pr_jun-filter", 'value'),
                Input("diagnosis_primary_pr_jun-filter", 'value'),
                Input("side_pr_jun-filter", 'value'),
                Input("satus_reproductive_pr_jun-filter", 'value'),
                Input("complaints_pr_jun-filter", 'value'),
                Input("breast_surgery_before_pr_jun-filter", 'value'),
                Input("skin_symptoms_pr_jun-filter",  'value'),
                Input("nipple_retraction_pr_jun-filter",   'value'),
                Input("nipple_release_pr_jun-filter",  'value'),
                Input("quadrant_pr_jun-filter",  'value'),
                Input("hormonal_medications_pr_jun-filter", 'value'),
                Input("genetics_pr_jun-filter", 'value'),
                Input("age_patient_pr_snr-filter", 'value'),
                Input("diagnosis_primary_pr_snr-filter", 'value'),
                Input("side_pr_snr-filter", 'value'),
                Input("satus_reproductive_pr_snr-filter", 'value'),
                Input("complaints_pr_snr-filter", 'value'),
                Input("breast_surgery_before_pr_snr-filter",  'value'),
                Input("skin_symptoms_pr_snr-filter", 'value'),
                Input("nipple_retraction_pr_snr-filter",  'value'),
                Input("nipple_release_pr_snr-filter", 'value'),
                Input("quadrant_pr_snr-filter",  'value'),
                Input("genetics_pr_snr-filter", 'value'),
                Input("hormonal_medications_pr_snr-filter", 'value'),
                Input("mmg_conclusion_skin_snr-filter", 'value'),
                Input("mmg_areola_pr_snr-filter", 'value'),
                Input("mmg_nipple_pr_snr-filter", 'value'),
                Input("mmg_background_breast_pr_snr-filter", 'value'),
                Input("mmg_nodle_pr_snr-filter", 'value'),
                Input("mmg_nodle_contour_pr_snr-filter", 'value'),
                Input("mmg_nodle_size_pr_snr-filter", 'value'),
                Input("mmg_calcifications_pr_snr-filter", 'value'),
                Input("mmg_number_formations_visualized_pr_snr-filter", 'value'),
                Input("mmg_axillary_lymph_nodes_pr_snr-filter", 'value'),
                Input("mmg_conclusion_pr_snr-filter", 'value'),
                Input("type_structure_acr_pr_snr-filter", 'value'),
                Input("mmg_number_nodles_pr_snr-filter", 'value'),
                Input("mmg_category_birads_pr_snr-filter", 'value')
                )


    def generate_graphs(selected_diagnosis_primary,
                        selected_diagnosis_satus_reproductive,
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
                        selected_us_calcinates_micro_pure,
                        selected_mmg_background_breast,
                        selected_mmg_nodle,
                        selected_mmg_nodle_contour,
                        selected_mmg_nodle_size,
                        selected_mmg_calcifications,
                        selected_mmg_number_formations_visualized,
                        selected_mmg_axillary_lymph_nodes,
                        selected_type_structure_acr,
                        selected_mmg_category_birads,
                        selected_abus_nodle_size,
                        selected_abus_nodle_contours,
                        selected_abus_echogenicity_formation,
                        selected_abus_structure,
                        selected_abus_symptom_retraction,
                        selected_abus_formation,
                        selected_abus_category_birads,
                        selected_abus_calcinates,
                        selected_tumor_morphology_structure,
                        selected_cytological_conclusion,
                        selected_degree_malignancy,
                        selected_mutation_brca,
                        selected_tumor_receptors,
                        selected_hist_is_tumor,
                        selected_us_probabilityCalc,
                        selected_abus_probabilityCalc,
                        selected_us_probabilityNeoCa,
                        selected_abus_probabilityNeoCa,
                        selected_mmg_probabilityNeoCa,
                        selected_age_patient_pr_jun,
                        selected_diagnosis_primary_pr_jun,
                        selected_side_pr_jun,
                        selected_satus_reproductive_pr_jun,
                        selected_complaints_pr_jun,
                        selected_breast_surgery_before_pr_jun,
                        selected_skin_symptoms_pr_jun,
                        selected_nipple_retraction_pr_jun,
                        selected_nipple_release_pr_jun,
                        selected_quadrant_pr_jun,
                        selected_hormonal_medications_pr_jun,
                        selected_genetics_pr_jun,
                        selected_age_patient_pr_snr,
                        selected_diagnosis_primary_pr_snr,
                        selected_side_pr_snr,
                        selected_satus_reproductive_pr_snr,
                        selected_complaints_pr_snr,
                        selected_breast_surgery_before_pr_snr, 
                        selected_skin_symptoms_pr_snr,
                        selected_nipple_retraction_pr_snr, 
                        selected_nipple_release_pr_snr,
                        selected_quadrant_pr_snr, 
                        selected_genetics_pr_snr,
                        selected_hormonal_medications_pr_snr,
                        selected_mmg_conclusion_skin_snr,
                        selected_mmg_areola_pr_snr,
                        selected_mmg_nipple_pr_snr,
                        selected_mmg_background_breast_pr_snr,
                        selected_mmg_nodle_pr_snr,
                        selected_mmg_nodle_contour_pr_snr,
                        selected_mmg_nodle_size_pr_snr,
                        selected_mmg_calcifications_pr_snr,
                        selected_mmg_number_formations_visualized_pr_snr,
                        selected_mmg_axillary_lymph_nodes_pr_snr,
                        selected_mmg_conclusion_pr_snr,
                        selected_type_structure_acr_pr_snr,
                        selected_mmg_number_nodles_pr_snr,
                        selected_mmg_category_birads_pr_snr
                        ):

        
        filtered_df = df[
                (df['diagnosis_primary'].isin(selected_diagnosis_primary)) & 
                (df['satus_reproductive'].isin(selected_diagnosis_satus_reproductive)) & 
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
                (df['us_calcinates_micro_pure'].isin(selected_us_calcinates_micro_pure)) &
                (df['mmg_background_breast'].isin(selected_mmg_background_breast)) &
                (df['mmg_nodle'].isin(selected_mmg_nodle)) &
                (df['mmg_nodle_contour'].isin(selected_mmg_nodle_contour)) &
                (df['mmg_nodle_size'].isin(selected_mmg_nodle_size)) &
                (df['mmg_calcifications'].isin(selected_mmg_calcifications)) &
                (df['mmg_number_formations_visualized'].isin(selected_mmg_number_formations_visualized)) &
                (df['mmg_axillary_lymph_nodes'].isin(selected_mmg_axillary_lymph_nodes)) &
                (df['type_structure_acr'].isin(selected_type_structure_acr)) &
                (df['mmg_category_birads'].isin(selected_mmg_category_birads)) &
                (df['abus_nodle_size'].isin(selected_abus_nodle_size)) &
                (df['abus_nodle_contours'].isin(selected_abus_nodle_contours)) &
                (df['abus_echogenicity_formation'].isin(selected_abus_echogenicity_formation)) &
                (df['abus_structure'].isin(selected_abus_structure)) &
                (df['abus_symptom_retraction'].isin(selected_abus_symptom_retraction)) &
                (df['abus_formation'].isin(selected_abus_formation)) &
                (df['abus_category_birads'].isin(selected_abus_category_birads)) &
                (df['abus_calcinates'].isin(selected_abus_calcinates)) &
                (df['tumor_morphology_structure'].isin(selected_tumor_morphology_structure)) &
                (df['cytological_conclusion'].isin(selected_cytological_conclusion)) &
                (df['degree_malignancy'].isin(selected_degree_malignancy)) &
                (df['mutation_brca'].isin(selected_mutation_brca)) &
                (df['tumor_receptors'].isin(selected_tumor_receptors)) &
                (df['hist_is_tumor'].isin(selected_hist_is_tumor)) &
                (df['us_probabilityCalc'] >= selected_us_probabilityCalc) &
                (df['abus_probabilityCalc'] >= selected_abus_probabilityCalc)&
                (df['us_probabilityNeoCa'] >= selected_us_probabilityNeoCa)&
                (df['abus_probabilityNeoCa'] >= selected_abus_probabilityNeoCa)&
                (df['mmg_probabilityNeoCa'] >= selected_mmg_probabilityNeoCa)
                ]
            

        total_patients = len(filtered_df)
        avg_age = filtered_df['age_patient'].mean()
        avg_us_probabilityCalc = filtered_df['us_probabilityCalc'].mean()
        avg_abus_probabilityCalc = filtered_df['abus_probabilityCalc'].mean()
        avg_us_probabilityNeoCa= filtered_df['us_probabilityNeoCa'].mean()
        avg_abus_probabilityNeoCa= filtered_df['abus_probabilityNeoCa'].mean()
        avg_mmg_probabilityNeoCa= filtered_df['mmg_probabilityNeoCa'].mean()


        diagnosis_primary_counts =filtered_df['diagnosis_primary'].value_counts()
        group_separation_counts =filtered_df['group_separation'].value_counts()
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

        mmg_background_breast_counts =filtered_df['mmg_background_breast'].value_counts()
        mmg_nodle_counts =filtered_df['mmg_nodle'].value_counts()
        mmg_nodle_contour_counts =filtered_df['mmg_nodle_contour'].value_counts()
        mmg_nodle_size_counts =filtered_df['mmg_nodle_size'].value_counts()
        mmg_calcifications_counts =filtered_df['mmg_calcifications'].value_counts()
        mmg_number_formations_visualized_counts =filtered_df['mmg_number_formations_visualized'].value_counts()
        mmg_axillary_lymph_nodes_counts =filtered_df['mmg_axillary_lymph_nodes'].value_counts()
        type_structure_acr_counts =filtered_df['type_structure_acr'].value_counts()
        mmg_category_birads_counts =filtered_df['mmg_category_birads'].value_counts()


        abus_nodle_size_counts =filtered_df['abus_nodle_size'].value_counts()
        abus_nodle_contours_counts =filtered_df['abus_nodle_contours'].value_counts()
        abus_echogenicity_formation_counts =filtered_df['abus_echogenicity_formation'].value_counts()
        abus_structure_counts =filtered_df['abus_structure'].value_counts()
        abus_symptom_retraction_counts =filtered_df['abus_symptom_retraction'].value_counts()
        abus_formation_counts =filtered_df['abus_formation'].value_counts()
        abus_category_birads_counts =filtered_df['abus_category_birads'].value_counts()
        abus_calcinates_counts =filtered_df['abus_calcinates'].value_counts()


        tumor_morphology_structure_counts =filtered_df['tumor_morphology_structure'].value_counts()
        cytological_conclusion_counts =filtered_df['cytological_conclusion'].value_counts()
        degree_malignancy_counts =filtered_df['degree_malignancy'].value_counts()
        mutation_brca_counts =filtered_df['mutation_brca'].value_counts()
        tumor_receptors_counts =filtered_df['tumor_receptors'].value_counts()
        hist_is_tumor_counts =filtered_df['hist_is_tumor'].value_counts()



        diagnosis_primary_fig = go.Figure(
                go.Pie(
                    labels=diagnosis_primary_counts.index,
                    values=diagnosis_primary_counts.values,
                    textinfo='percent'
                )
            )
        diagnosis_primary_fig.update_layout(
            title='Первичный диагноз',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        group_separation_fig = go.Figure(
                go.Pie(
                    labels=group_separation_counts.index,
                    values=group_separation_counts.values,
                    textinfo='percent'
                )
            )
        
        group_separation_fig.update_layout(
            title='Группа',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        satus_reproductive_fig = go.Figure(
                go.Bar(
                    x=satus_reproductive_counts.index,
                    y=satus_reproductive_counts.values
                )
            )
        satus_reproductive_fig.update_layout(
            title='Репродуктивный статус',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        complaints_fig = go.Figure(
                go.Pie(
                    labels=complaints_counts.index,
                    values=complaints_counts.values,
                    textinfo='percent'
                )
            )
        complaints_fig.update_layout(
            title='Жалобы',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        breast_surgery_before_fig = go.Figure(
                go.Bar(
                    x=breast_surgery_before_counts.index,
                    y=breast_surgery_before_counts.values
                )
            )
        breast_surgery_before_fig.update_layout(
            title='Операции в анамнезе',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        skin_symptoms_fig = go.Figure(
                go.Pie(
                    labels=skin_symptoms_counts.index,
                    values=skin_symptoms_counts.values,
                    textinfo='percent'
                )
            )
        skin_symptoms_fig.update_layout(
            title='Кожные симптомы',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        nipple_retraction_fig = go.Figure(
                go.Bar(
                    x=nipple_retraction_counts.index,
                    y=nipple_retraction_counts.values
                )
            )
        nipple_retraction_fig.update_layout(
            title='Симтом ретракции',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        nipple_release_fig = go.Figure(
                go.Bar(
                    x=nipple_release_counts.index,
                    y=nipple_release_counts.values
                )
            )
        nipple_release_fig.update_layout(
            title='Выделения из соска',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        

        genetics_fig = go.Figure(
                go.Pie(
                    labels=genetics_counts.index,
                    values=genetics_counts.values,
                    textinfo='percent'
                )
            )
        
        genetics_fig.update_layout(
            title='Наследственность',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        

        hormonal_medications_fig = go.Figure(
                go.Pie(
                    labels=hormonal_medications_counts.index,
                    values=hormonal_medications_counts.values,
                    textinfo='percent'
                )
            )
        
        hormonal_medications_fig.update_layout(
            title='Прием гормональных препаратов',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )


        us_nodle_contour_fig = go.Figure(
                go.Pie(
                    labels=us_nodle_contour_counts.index,
                    values=us_nodle_contour_counts.values,
                    textinfo='percent'
                )
            )
        
        us_nodle_contour_fig.update_layout(
            title='Контур',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        us_ducts_fig = go.Figure(
                go.Pie(
                    labels=us_ducts_counts.index,
                    values=us_ducts_counts.values,
                    textinfo='percent'
                )
            )
        
        us_ducts_fig.update_layout(
            title='Протоки',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_background_fig = go.Figure(
                go.Pie(
                    labels=us_background_counts.index,
                    values=us_background_counts.values,
                    textinfo='percent'
                )
            )
        
        us_background_fig.update_layout(
            title='Фон',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_formation_fig = go.Figure(
                go.Pie(
                    labels=us_formation_counts.index,
                    values=us_formation_counts.values,
                    textinfo='percent'
                )
            )
        us_formation_fig.update_layout(
            title='Форма узлов',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_form_fig = go.Figure(
                go.Pie(
                    labels=us_form_counts.index,
                    values=us_form_counts.values,
                    textinfo='percent'
                )
            )
        
        us_form_fig.update_layout(
            title='Характер узлов',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_nodle_size_fig = go.Figure(
                go.Pie(
                    labels=us_nodle_size_counts.index,
                    values=us_nodle_size_counts.values,
                    textinfo='percent'
                )
            )
        us_nodle_size_fig.update_layout(
            title='Размер узлов',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_echogenicity_formation_fig = go.Figure(
                go.Pie(
                    labels=us_echogenicity_formation_counts.index,
                    values=us_echogenicity_formation_counts.values,
                    textinfo='percent'
                )
            )
        us_echogenicity_formation_fig.update_layout(
            title='Эхогенность',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_structure_fig = go.Figure(
                go.Pie(
                    labels=us_structure_counts.index,
                    values=us_structure_counts.values,
                    textinfo='percent'
                )
            )
        us_structure_fig.update_layout(
            title='Структура',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_formation_blood_flow_fig = go.Figure(
                go.Pie(
                    labels=us_formation_blood_flow_counts.index,
                    values=us_formation_blood_flow_counts.values,
                    textinfo='percent'
                )
            )
        us_formation_blood_flow_fig.update_layout(
            title='Кровоток в образовании',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_elastography_fig = go.Figure(
                go.Pie(
                    labels=us_elastography_counts.index,
                    values=us_elastography_counts.values,
                    textinfo='percent'
                )
            )
        us_elastography_fig.update_layout(
            title='Эластография',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        us_region_lymph_nodes_fig = go.Figure(
                go.Pie(
                    labels=us_region_lymph_nodes_counts.index,
                    values=us_region_lymph_nodes_counts.values,
                    textinfo='percent'
                )
            )
        
        us_region_lymph_nodes_fig.update_layout(
            title='Регионарные лимфоузлы',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_number_nodles_fig = go.Figure(
                go.Pie(
                    labels=us_number_nodles_counts.index,
                    values=us_number_nodles_counts.values,
                    textinfo='percent'
                )
            )
        
        us_number_nodles_fig.update_layout(
            title='Количество узлов',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_category_birads_fig = go.Figure(
                go.Pie(
                    labels=us_category_birads_counts.index,
                    values=us_category_birads_counts.values,
                    textinfo='percent'
                )
            )
        us_category_birads_fig.update_layout(
            title='Категория BIRADS',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        us_calcinates_micro_pure_fig = go.Figure(
                go.Pie(
                    labels=us_calcinates_micro_pure_counts.index,
                    values=us_calcinates_micro_pure_counts.values,
                    textinfo='percent'
                )
            )
        
        us_calcinates_micro_pure_fig.update_layout(
            title='Кальцинаты',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        mmg_background_breast_fig = go.Figure(
                go.Pie(
                    labels=mmg_background_breast_counts.index,
                    values=mmg_background_breast_counts.values,
                    textinfo='percent'
                )
            )
        
        mmg_background_breast_fig.update_layout(
            title='Фон',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        mmg_nodle_fig = go.Figure(
                go.Pie(
                    labels=mmg_nodle_counts.index,
                    values=mmg_nodle_counts.values,
                    textinfo='percent'
                )
            )
        mmg_nodle_fig.update_layout(
            title='Характер узла',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        mmg_nodle_contour_fig = go.Figure(
                go.Pie(
                    labels=mmg_nodle_contour_counts.index,
                    values=mmg_nodle_contour_counts.values,
                    textinfo='percent'
                )
            )
            
        mmg_nodle_contour_fig.update_layout(
            title='Контур',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        mmg_nodle_size_fig = go.Figure(
                go.Pie(
                    labels=mmg_nodle_size_counts.index,
                    values=mmg_nodle_size_counts.values,
                    textinfo='percent'
                )
            )
        
       
        
        mmg_nodle_size_fig.update_layout(
            title='Размеры узлов',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        mmg_calcifications_fig = go.Figure(
                go.Pie(
                    labels=mmg_calcifications_counts.index,
                    values=mmg_calcifications_counts.values,
                    textinfo='percent'
                )
            )
        
        mmg_calcifications_fig.update_layout(
            title='Кальцификаты',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        mmg_number_formations_visualized_fig = go.Figure(
                go.Pie(
                    labels=mmg_number_formations_visualized_counts.index,
                    values=mmg_number_formations_visualized_counts.values,
                    textinfo='percent'
                )
            )
        
        mmg_number_formations_visualized_fig.update_layout(
            title='Количество лимфоузлов',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        mmg_axillary_lymph_nodes_fig = go.Figure(
                go.Pie(
                    labels=mmg_axillary_lymph_nodes_counts.index,
                    values=mmg_axillary_lymph_nodes_counts.values,
                    textinfo='percent'
                )
            )
        
        mmg_axillary_lymph_nodes_fig.update_layout(
            title='Подмышечные лимфоузлы',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        type_structure_acr_fig = go.Figure(
                go.Pie(
                    labels=type_structure_acr_counts.index,
                    values=type_structure_acr_counts.values,
                    textinfo='percent'
                )
            )
        
        type_structure_acr_fig.update_layout(
            title='Тип структуры ACR',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        mmg_category_birads_fig = go.Figure(
                go.Pie(
                    labels=mmg_category_birads_counts.index,
                    values=mmg_category_birads_counts.values,
                    textinfo='percent'
                )
            )
        
        mmg_category_birads_fig.update_layout(
            title='Категория BIRADS',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        abus_nodle_size_fig = go.Figure(
                go.Pie(
                    labels=abus_nodle_size_counts.index,
                    values=abus_nodle_size_counts.values,
                    textinfo='percent'
                )
            )
        
        abus_nodle_size_fig.update_layout(
            title='Размер',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        abus_nodle_contours_fig = go.Figure(
                go.Pie(
                    labels=abus_nodle_contours_counts.index,
                    values=abus_nodle_contours_counts.values,
                    textinfo='percent'
                )
            )
        
        abus_nodle_contours_fig.update_layout(
            title='Контуры',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        abus_echogenicity_formation_fig = go.Figure(
                go.Pie(
                    labels=abus_echogenicity_formation_counts.index,
                    values=abus_echogenicity_formation_counts.values,
                    textinfo='percent'
                )
            )
        
        abus_echogenicity_formation_fig.update_layout(
            title='Эхогенность',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        abus_structure_fig = go.Figure(
                go.Pie(
                    labels=abus_structure_counts.index,
                    values=abus_structure_counts.values,
                    textinfo='percent'
                )
            )
        
       
        
        abus_structure_fig.update_layout(
            title='Структура',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        abus_symptom_retraction_fig = go.Figure(
                go.Pie(
                    labels=abus_symptom_retraction_counts.index,
                    values=abus_symptom_retraction_counts.values,
                    textinfo='percent'
                )
            )
        abus_symptom_retraction_fig.update_layout(
            title='Симптом ретракции',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        abus_formation_fig = go.Figure(
                go.Pie(
                    labels=abus_formation_counts.index,
                    values=abus_formation_counts.values,
                    textinfo='percent'
                )
            )
        
        abus_formation_fig.update_layout(
            title='Локализация',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        abus_category_birads_fig = go.Figure(
                go.Pie(
                    labels=abus_category_birads_counts.index,
                    values=abus_category_birads_counts.values,
                    textinfo='percent'
                )
            )
        
        abus_category_birads_fig.update_layout(
            title='Категория BIRADS',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        abus_calcinates_fig = go.Figure(
                go.Pie(
                    labels=abus_calcinates_counts.index,
                    values=abus_calcinates_counts.values,
                    textinfo='percent'
                )
        )

        abus_calcinates_fig.update_layout(
            title='Кальцинаты',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        tumor_morphology_structure_fig = go.Figure(
                go.Pie(
                    labels=tumor_morphology_structure_counts.index,
                    values=tumor_morphology_structure_counts.values,
                    textinfo='percent'
                )
        )

        tumor_morphology_structure_fig.update_layout(
            title='Морфологическая структура',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        cytological_conclusion_fig = go.Figure(
                go.Pie(
                    labels=cytological_conclusion_counts.index,
                    values=cytological_conclusion_counts.values,
                    textinfo='percent'
                )
        )

        cytological_conclusion_fig.update_layout(
            title='Заключение цитологии',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        degree_malignancy_fig = go.Figure(
                go.Pie(
                    labels=degree_malignancy_counts.index,
                    values=degree_malignancy_counts.values,
                    textinfo='percent'
                )
        )

        degree_malignancy_fig.update_layout(
            title='Уровень малигнизации',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        mutation_brca_fig = go.Figure(
                go.Pie(
                    labels=mutation_brca_counts.index,
                    values=mutation_brca_counts.values,
                    textinfo='percent'
                )
                )
        mutation_brca_fig.update_layout(
            title='Мутация BRCA',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        tumor_receptors_fig = go.Figure(
                go.Pie(
                    labels=tumor_receptors_counts.index,
                    values=tumor_receptors_counts.values,
                    textinfo='percent'
                )
                )
        
        tumor_receptors_fig.update_layout(
            title='Рецрепторы к опухоли',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        hist_is_tumor_fig = go.Figure(
                go.Pie(
                    labels=hist_is_tumor_counts.index,
                    values=hist_is_tumor_counts.values,
                    textinfo='percent'
                )
                )
        hist_is_tumor_fig.update_layout(
            title='Наличие ЗНО',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )
        
        us_probabilityCalc_fig = go.Figure(go.Histogram(
                x=filtered_df['us_probabilityCalc'],
                opacity=0.7,
                marker=dict(line=dict(width=1, color='DarkSlateGrey'))
            ))
        
        us_probabilityCalc_fig.update_layout(
            title="Вероятность определения кальцинатов методом УЗИ",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Вероятность",
            yaxis_title="Количество",
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
            font=dict(family="Roboto, sans-serif"),
            barmode='overlay',
        )

        abus_probabilityCalc_fig = go.Figure(go.Histogram(
                x=filtered_df['abus_probabilityCalc'],
                opacity=0.7,
                marker=dict(line=dict(width=1, color='DarkSlateGrey'))
            ))
        
        abus_probabilityCalc_fig.update_layout(
            title="Вероятность определения кальцинатов методом 3d УЗИ",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Вероятность",
            yaxis_title="Количество",
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
            font=dict(family="Roboto, sans-serif"),
            barmode='overlay',
        )
        

        us_probabilityNeoCa_fig = go.Figure(go.Histogram(
                x=filtered_df['us_probabilityNeoCa'],
                opacity=0.7,
                marker=dict(line=dict(width=1, color='DarkSlateGrey'))
            ))
        
        us_probabilityNeoCa_fig.update_layout(
            title="Вероятность определения ЗНО методом УЗИ",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Вероятность",
            yaxis_title="Количество",
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
            font=dict(family="Roboto, sans-serif"),
            barmode='overlay',
        )

        abus_probabilityNeoCa_fig = go.Figure(go.Histogram(
                x=filtered_df['abus_probabilityNeoCa'],
                opacity=0.7,
                marker=dict(line=dict(width=1, color='DarkSlateGrey'))
            ))
        abus_probabilityNeoCa_fig.update_layout(
            title="Вероятность определения ЗНО методом 3d УЗИ",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Вероятность",
            yaxis_title="Количество",
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
            font=dict(family="Roboto, sans-serif"),
            barmode='overlay',
        )

        mmg_probabilityNeoCa_fig = go.Figure(go.Histogram(
                x=filtered_df['mmg_probabilityNeoCa'],
                opacity=0.7,
                marker=dict(line=dict(width=1, color='DarkSlateGrey'))
            ))
        
        mmg_probabilityNeoCa_fig.update_layout(
            title="Вероятность опропределенияедления ЗНО методом ММГ",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Вероятность",
            yaxis_title="Количество",
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
            font=dict(family="Roboto, sans-serif"),
            barmode='overlay',
        )

        
        

        stats_panel = dbc.Card([
                dbc.CardHeader("Статистика выборки", className="h2-label"),
                dbc.CardBody([
                    dcc.Markdown(f"*Всего пациентов:* **{total_patients}** \n ---"),
                    dcc.Markdown(f"*Средний возраст:* **{avg_age:.0f}** \n ---"),
                    dcc.Markdown(f"*Средняя вероятность обнаружения кальцинатов по УЗИ:* **{avg_us_probabilityCalc:.5f}** \n ---"),
                    dcc.Markdown(f"*Средняя вероятность обнаружения кальцинатов по 3d УЗИ:* **{avg_abus_probabilityCalc:.5f}** \n ---"),
                    dcc.Markdown(f"*Средняя вероятность обнаружения ЗНО по УЗИ:* **{avg_us_probabilityNeoCa:.5f}** \n ---"),
                    dcc.Markdown(f"*Средняя вероятность обнаружения ЗНО по 3d УЗИ:* **{avg_abus_probabilityNeoCa:.5f}** \n ---"),
                    dcc.Markdown(f"*Средняя вероятность обнаружения ЗНО по ММГ:* **{avg_mmg_probabilityNeoCa:.5f}** \n ---")
                ], className="stats-body")])
        
        df_us_jn_pred = pd.DataFrame({
            'age_patient':[selected_age_patient_pr_jun],
            'diagnosis_primary':[selected_diagnosis_primary_pr_jun],
            'side':[selected_side_pr_jun],
            'satus_reproductive':[selected_satus_reproductive_pr_jun],
            'complaints':[selected_complaints_pr_jun],
            'breast_surgery_before':[selected_breast_surgery_before_pr_jun],
            'skin_symptoms':[selected_skin_symptoms_pr_jun],
            'nipple_retraction':[selected_nipple_retraction_pr_jun], 
            'nipple_release':[selected_nipple_release_pr_jun],
            'quadrant':[selected_quadrant_pr_jun],
            'genetics':[selected_genetics_pr_jun],
            'hormonal_medications':[selected_hormonal_medications_pr_jun]})
        
        df_us_jn_pred["diagnosis_primary"] = df_us_jn_pred['diagnosis_primary'].apply(lambda x: 1 if x == df_us_jn["diagnosis_primary"].unique()[0]
                                    else 2 if x == df_us_jn["diagnosis_primary"].unique()[1]
                                    else 3 if x == df_us_jn["diagnosis_primary"].unique()[2]
                                    else 4 if x == df_us_jn["diagnosis_primary"].unique()[3]
                                    else 5 if x == df_us_jn["diagnosis_primary"].unique()[4]
                                    else 6 if x == df_us_jn["diagnosis_primary"].unique()[5]
                                    else 7 if x == df_us_jn["diagnosis_primary"].unique()[6]
                                    else 8 if x == df_us_jn["diagnosis_primary"].unique()[7]
                                    else 9 if x == df_us_jn["diagnosis_primary"].unique()[8]                                    
                                    else 10)
        df_us_jn_pred["satus_reproductive"] = df_us_jn_pred["satus_reproductive"].apply(lambda x: 1 if x == df_us_jn["diagnosis_primary"].unique()[0]
                                            else 2)
        df_us_jn_pred["side"] = df_us_jn_pred['side'].apply(lambda x: 1 if x == df_us_jn["side"].unique()[0]
                                            else 2 if x == df_us_jn["side"].unique()[1]
                                            else 3 if x == df_us_jn["side"].unique()[2]
                                            else 4)
        df_us_jn_pred["complaints"] = df_us_jn_pred['complaints'].apply(lambda x: 1 if x == df_us_jn["complaints"].unique()[0]
                                            else 2 if x == df_us_jn["complaints"].unique()[1]
                                            else 3 if x == df_us_jn["complaints"].unique()[2]
                                            else 4)
        df_us_jn_pred["breast_surgery_before"] = df_us_jn_pred["breast_surgery_before"].apply(lambda x: 1 if x == df_us_jn["breast_surgery_before"].unique()[0]
                                            else 2)
        df_us_jn_pred["skin_symptoms"] = df_us_jn_pred["skin_symptoms"].apply(lambda x: 1 if x == df_us_jn["skin_symptoms"].unique()[0]
                                            else 2)
        df_us_jn_pred["nipple_retraction"] = df_us_jn_pred["nipple_retraction"].apply(lambda x: 1 if x == df_us_jn["nipple_retraction"].unique()[0]
                                            else 2)
        df_us_jn_pred["nipple_release"] = df_us_jn_pred["nipple_release"].apply(lambda x: 1 if x == df_us_jn["nipple_release"].unique()[0]
                                            else 2)
        df_us_jn_pred["quadrant"] = df_us_jn_pred['quadrant'].apply(lambda x: 1 if x == df_us_jn["quadrant"].unique()[0]
                                            else 2 if x == df_us_jn["quadrant"].unique()[1]
                                            else 3 if x == df_us_jn["quadrant"].unique()[2]
                                            else 4 if x == df_us_jn["quadrant"].unique()[3]
                                            else 5 if x == df_us_jn["quadrant"].unique()[4]
                                            else 6 if x == df_us_jn["quadrant"].unique()[5]
                                            else 7 if x == df_us_jn["quadrant"].unique()[6]
                                            else 8 if x == df_us_jn["quadrant"].unique()[7]
                                            else 9 if x == df_us_jn["quadrant"].unique()[8]                                    
                                            else 10)
        df_us_jn_pred["genetics"] = df_us_jn_pred["genetics"].apply(lambda x: 1 if x == df_us_jn["genetics"].unique()[0]
                                            else 2)
        df_us_jn_pred["hormonal_medications"] = df_us_jn_pred["hormonal_medications"].apply(lambda x: 1 if x == df_us_jn["hormonal_medications"].unique()[0]
                                            else 2)
        
        df_us_jn_num = df_us_jn
        df_us_jn_num["diagnosis_primary"] = df_us_jn_num['diagnosis_primary'].apply(lambda x: 1 if x == df_us_jn_num["diagnosis_primary"].unique()[0]
                                    else 2 if x == df_us_jn_num["diagnosis_primary"].unique()[1]
                                    else 3 if x == df_us_jn_num["diagnosis_primary"].unique()[2]
                                    else 4 if x == df_us_jn_num["diagnosis_primary"].unique()[3]
                                    else 5 if x == df_us_jn_num["diagnosis_primary"].unique()[4]
                                    else 6 if x == df_us_jn_num["diagnosis_primary"].unique()[5]
                                    else 7 if x == df_us_jn_num["diagnosis_primary"].unique()[6]
                                    else 8 if x == df_us_jn_num["diagnosis_primary"].unique()[7]
                                    else 9 if x == df_us_jn_num["diagnosis_primary"].unique()[8]                                    
                                    else 10)
        df_us_jn_num["satus_reproductive"] = df_us_jn_num["satus_reproductive"].apply(lambda x: 1 if x == df_us_jn_num["diagnosis_primary"].unique()[0]
                                    else 2)
        df_us_jn_num["side"] = df_us_jn_num['side'].apply(lambda x: 1 if x == df_us_jn_num["side"].unique()[0]
                                    else 2 if x == df_us_jn_num["side"].unique()[1]
                                    else 3 if x == df_us_jn_num["side"].unique()[2]
                                    else 4)
        df_us_jn_num["complaints"] = df_us_jn_num['complaints'].apply(lambda x: 1 if x == df_us_jn_num["complaints"].unique()[0]
                                    else 2 if x == df_us_jn_num["complaints"].unique()[1]
                                    else 3 if x == df_us_jn_num["complaints"].unique()[2]
                                    else 4)
        df_us_jn_num["breast_surgery_before"] = df_us_jn_num["breast_surgery_before"].apply(lambda x: 1 if x == df_us_jn_num["breast_surgery_before"].unique()[0]
                                    else 2)
        df_us_jn_num["skin_symptoms"] = df_us_jn_num["skin_symptoms"].apply(lambda x: 1 if x == df_us_jn_num["skin_symptoms"].unique()[0]
                                    else 2)
        df_us_jn_num["nipple_retraction"] = df_us_jn_num["nipple_retraction"].apply(lambda x: 1 if x == df_us_jn_num["nipple_retraction"].unique()[0]
                                    else 2)
        df_us_jn_num["nipple_release"] = df_us_jn_num["nipple_release"].apply(lambda x: 1 if x == df_us_jn_num["nipple_release"].unique()[0]
                                    else 2)
        df_us_jn_num["quadrant"] = df_us_jn_num['quadrant'].apply(lambda x: 1 if x == df_us_jn_num["quadrant"].unique()[0]
                                    else 2 if x == df_us_jn_num["quadrant"].unique()[1]
                                    else 3 if x == df_us_jn_num["quadrant"].unique()[2]
                                    else 4 if x == df_us_jn_num["quadrant"].unique()[3]
                                    else 5 if x == df_us_jn_num["quadrant"].unique()[4]
                                    else 6 if x == df_us_jn_num["quadrant"].unique()[5]
                                    else 7 if x == df_us_jn_num["quadrant"].unique()[6]
                                    else 8 if x == df_us_jn_num["quadrant"].unique()[7]
                                    else 9 if x == df_us_jn_num["quadrant"].unique()[8]                                    
                                    else 10)
        df_us_jn_num["genetics"] = df_us_jn_num["genetics"].apply(lambda x: 1 if x == df_us_jn_num["genetics"].unique()[0]
                                    else 2)
        df_us_jn_num["hormonal_medications"] = df_us_jn_num["hormonal_medications"].apply(lambda x: 1 if x == df_us_jn_num["hormonal_medications"].unique()[0]
                                    else 2)
        df_us_jn_num["hist_is_tumor"] = df_us_jn_num["hist_is_tumor"].apply(lambda x: 1 if x == df_us_jn_num["hist_is_tumor"].unique()[0]
                                    else 2)
        
        
        X = df_us_jn_num.drop('hist_is_tumor', axis=1)
        y = df_us_jn_num['hist_is_tumor']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

        rf = RandomForestClassifier(
            n_estimators=500, 
            max_depth=5, 
            max_features=None, 
            bootstrap=True, 
            min_samples_split=5,
            min_samples_leaf=2, 
            random_state=42,
            class_weight=None,
            verbose=1,
            n_jobs=-1
)

        rf.fit(X_train, y_train)


        
        df_us_jn_pred["hist_is_tumor"] = rf.predict(df_us_jn_pred)

        
       

        

        df_us_jn_pred["way"] = df_us_jn_pred["hist_is_tumor"].apply(lambda x: '3d УЗИ' if x == 1
                                            else 'традиционное УЗИ')
        way_to = df_us_jn_pred["way"][0]

        
        ml_panel_jun = dbc.Card([
                dbc.CardHeader("Маршрутизация пациентки до 40 лет", className="h2-label"),
                dbc.CardBody([
                    dcc.Markdown(f"*Направление:* **{way_to}** \n ---"),
                    dcc.Markdown(f"*Возраст:* **{selected_age_patient_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Диагноз:* **{selected_diagnosis_primary_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Сторона:* **{selected_side_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Репродуктивный статус:* **{selected_satus_reproductive_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Жалобы:* **{selected_complaints_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Операции до:* **{selected_breast_surgery_before_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Симптомы на коже:* **{selected_skin_symptoms_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Симптом ретракции:* **{selected_nipple_retraction_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Симптом выделения:* **{selected_nipple_release_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Кавадрант:* **{selected_quadrant_pr_jun}** \n ---"),
                    dcc.Markdown(f"*Наследственность:* **{selected_genetics_pr_jun}** \n ---")
                    
                ], className="stats-body")])
        df_us_snr_pred = pd.DataFrame({
            'age_patient':[selected_age_patient_pr_snr],
            'diagnosis_primary':[selected_diagnosis_primary_pr_snr],
            'side':[selected_side_pr_snr],
            'satus_reproductive':[selected_satus_reproductive_pr_snr],
            'complaints':[selected_complaints_pr_snr],
            'breast_surgery_before':[selected_breast_surgery_before_pr_snr],
            'skin_symptoms':[selected_skin_symptoms_pr_snr],
            'nipple_retraction':[selected_nipple_retraction_pr_snr], 
            'nipple_release':[selected_nipple_release_pr_snr],
            'quadrant':[selected_quadrant_pr_snr],
            'genetics':[selected_genetics_pr_snr],
            'hormonal_medications':[selected_hormonal_medications_pr_snr],
            'mmg_conclusion_skin':[selected_mmg_conclusion_skin_snr],
            'mmg_areola':[selected_mmg_areola_pr_snr],
            'mmg_nipple':[selected_mmg_nipple_pr_snr],
            'mmg_background_breast':[selected_mmg_background_breast_pr_snr],
            'mmg_nodle':[selected_mmg_nodle_pr_snr],
            'mmg_nodle_contour':[selected_mmg_nodle_contour_pr_snr],
            'mmg_nodle_size':[selected_mmg_nodle_size_pr_snr],
            'mmg_calcifications':[selected_mmg_calcifications_pr_snr],
            'mmg_number_formations_visualized':[selected_mmg_number_formations_visualized_pr_snr],
            'mmg_axillary_lymph_nodes':[selected_mmg_axillary_lymph_nodes_pr_snr],
            'mmg_conclusion':[selected_mmg_conclusion_pr_snr],
            'type_structure_acr':[selected_type_structure_acr_pr_snr],
            'mmg_number_nodles':[selected_mmg_number_nodles_pr_snr],
            'mmg_category_birads':[selected_mmg_category_birads_pr_snr]
            })
        
        df_us_snr_pred["diagnosis_primary"] = df_us_snr_pred['diagnosis_primary'].apply(lambda x: 1 if x == df_us_snr["diagnosis_primary"].unique()[0]
                                    else 2 if x == df_us_snr["diagnosis_primary"].unique()[1]
                                    else 3 if x == df_us_snr["diagnosis_primary"].unique()[2]
                                    else 4 if x == df_us_snr["diagnosis_primary"].unique()[3]
                                    else 5 if x == df_us_snr["diagnosis_primary"].unique()[4]
                                    else 6 if x == df_us_snr["diagnosis_primary"].unique()[5]
                                    else 7 if x == df_us_snr["diagnosis_primary"].unique()[6]
                                    else 8 if x == df_us_snr["diagnosis_primary"].unique()[7]
                                    else 9 if x == df_us_snr["diagnosis_primary"].unique()[8]                                    
                                    else 10)
        df_us_snr_pred["satus_reproductive"] = df_us_snr_pred["satus_reproductive"].apply(lambda x: 1 if x == df_us_snr["diagnosis_primary"].unique()[0]
                                            else 2)
        df_us_snr_pred["side"] = df_us_snr_pred['side'].apply(lambda x: 1 if x == df_us_snr["side"].unique()[0]
                                            else 2 if x == df_us_snr["side"].unique()[1]
                                            else 3 if x == df_us_snr["side"].unique()[2]
                                            else 4)
        df_us_snr_pred["complaints"] = df_us_snr_pred['complaints'].apply(lambda x: 1 if x == df_us_snr["complaints"].unique()[0]
                                            else 2 if x == df_us_snr["complaints"].unique()[1]
                                            else 3 if x == df_us_snr["complaints"].unique()[2]
                                            else 4)
        df_us_snr_pred["breast_surgery_before"] = df_us_snr_pred["breast_surgery_before"].apply(lambda x: 1 if x == df_us_snr["breast_surgery_before"].unique()[0]
                                            else 2)
        df_us_snr_pred["skin_symptoms"] = df_us_snr_pred["skin_symptoms"].apply(lambda x: 1 if x == df_us_snr["skin_symptoms"].unique()[0]
                                            else 2)
        df_us_snr_pred["nipple_retraction"] = df_us_snr_pred["nipple_retraction"].apply(lambda x: 1 if x == df_us_snr["nipple_retraction"].unique()[0]
                                            else 2)
        df_us_snr_pred["nipple_release"] = df_us_snr_pred["nipple_release"].apply(lambda x: 1 if x == df_us_snr["nipple_release"].unique()[0]
                                            else 2)
        df_us_snr_pred["quadrant"] = df_us_snr_pred['quadrant'].apply(lambda x: 1 if x == df_us_snr["quadrant"].unique()[0]
                                            else 2 if x == df_us_snr["quadrant"].unique()[1]
                                            else 3 if x == df_us_snr["quadrant"].unique()[2]
                                            else 4 if x == df_us_snr["quadrant"].unique()[3]
                                            else 5 if x == df_us_snr["quadrant"].unique()[4]
                                            else 6 if x == df_us_snr["quadrant"].unique()[5]
                                            else 7 if x == df_us_snr["quadrant"].unique()[6]
                                            else 8 if x == df_us_snr["quadrant"].unique()[7]
                                            else 9 if x == df_us_snr["quadrant"].unique()[8]                                    
                                            else 10)
        df_us_snr_pred["genetics"] = df_us_snr_pred["genetics"].apply(lambda x: 1 if x == df_us_snr["genetics"].unique()[0]
                                            else 2)
        df_us_snr_pred["hormonal_medications"] = df_us_snr_pred["hormonal_medications"].apply(lambda x: 1 if x == df_us_snr["hormonal_medications"].unique()[0]
                                            else 2)
        df_us_snr_pred["mmg_conclusion_skin"] = df_us_snr_pred['mmg_conclusion_skin'].apply(lambda x: 1 if x == df_us_snr["mmg_conclusion_skin"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_conclusion_skin"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_conclusion_skin"].unique()[2]
                                            else 4)
        df_us_snr_pred["mmg_areola"] = df_us_snr_pred['mmg_areola'].apply(lambda x: 1 if x == df_us_snr["mmg_areola"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_areola"].unique()[1]
                                            else 3)
        df_us_snr_pred["mmg_nipple"] = df_us_snr_pred['mmg_nipple'].apply(lambda x: 1 if x == df_us_snr["mmg_nipple"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_nipple"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_nipple"].unique()[2]
                                            else 4)
        df_us_snr_pred["mmg_background_breast"] = df_us_snr_pred['mmg_background_breast'].apply(lambda x: 1 if x == df_us_snr["mmg_background_breast"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_background_breast"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_background_breast"].unique()[2]
                                            else 4 if x == df_us_snr["mmg_background_breast"].unique()[3]
                                            else 5)
        df_us_snr_pred["mmg_nodle"] = df_us_snr_pred['mmg_nodle'].apply(lambda x: 1 if x == df_us_snr["mmg_nodle"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_nodle"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_nodle"].unique()[2]
                                            else 4 if x == df_us_snr["mmg_nodle"].unique()[3]
                                            else 5 if x == df_us_snr["mmg_nodle"].unique()[4]
                                            else 6 if x == df_us_snr["mmg_nodle"].unique()[5]
                                            else 7 if x == df_us_snr["mmg_nodle"].unique()[6]
                                            else 8 if x == df_us_snr["mmg_nodle"].unique()[7]
                                            else 9 if x == df_us_snr["mmg_nodle"].unique()[8]                                    
                                            else 10)
        df_us_snr_pred["mmg_nodle_contour"] = df_us_snr_pred['mmg_nodle_contour'].apply(lambda x: 1 if x == df_us_snr["mmg_nodle_contour"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_nodle_contour"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_nodle_contour"].unique()[2]
                                            else 4 if x == df_us_snr["mmg_nodle_contour"].unique()[3]
                                            else 5)
        df_us_snr_pred["mmg_nodle_size"] = df_us_snr_pred['mmg_nodle_size'].apply(lambda x: 1 if x == df_us_snr["mmg_nodle_size"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_nodle_size"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_nodle_size"].unique()[2]
                                            else 4 if x == df_us_snr["mmg_nodle_size"].unique()[3]
                                            else 5 if x == df_us_snr["mmg_nodle_size"].unique()[4]
                                            else 6 if x == df_us_snr["mmg_nodle_size"].unique()[5]
                                            else 7)
        df_us_snr_pred["mmg_calcifications"] = df_us_snr_pred['mmg_calcifications'].apply(lambda x: 1 if x == df_us_snr["mmg_calcifications"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_calcifications"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_calcifications"].unique()[2]
                                            else 4 if x == df_us_snr["mmg_calcifications"].unique()[3]
                                            else 5 if x == df_us_snr["mmg_calcifications"].unique()[4]
                                            else 6 if x == df_us_snr["mmg_calcifications"].unique()[5]
                                            else 7 if x == df_us_snr["mmg_calcifications"].unique()[6]
                                            else 8 if x == df_us_snr["mmg_calcifications"].unique()[7]
                                            else 9 if x == df_us_snr["mmg_calcifications"].unique()[8]                                    
                                            else 10 if x == df_us_snr["mmg_calcifications"].unique()[9]
                                            else 11)
        df_us_snr_pred["mmg_number_formations_visualized"] = df_us_snr_pred['mmg_number_formations_visualized'].apply(lambda x: 1 if x == df_us_snr["mmg_number_formations_visualized"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_number_formations_visualized"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_number_formations_visualized"].unique()[2]
                                            else 4 if x == df_us_snr["mmg_number_formations_visualized"].unique()[3]
                                            else 5)
        df_us_snr_pred["mmg_axillary_lymph_nodes"] = df_us_snr_pred['mmg_axillary_lymph_nodes'].apply(lambda x: 1 if x == df_us_snr["mmg_axillary_lymph_nodes"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_axillary_lymph_nodes"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_axillary_lymph_nodes"].unique()[2]
                                            else 4)
        df_us_snr_pred["mmg_conclusion"] = df_us_snr_pred['mmg_conclusion'].apply(lambda x: 1 if x == df_us_snr["mmg_conclusion"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_conclusion"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_conclusion"].unique()[2]
                                            else 4 if x == df_us_snr["mmg_conclusion"].unique()[3]
                                            else 5 if x == df_us_snr["mmg_conclusion"].unique()[4]
                                            else 6 if x == df_us_snr["mmg_conclusion"].unique()[5]
                                            else 7 if x == df_us_snr["mmg_conclusion"].unique()[6]
                                            else 8 if x == df_us_snr["mmg_conclusion"].unique()[7]
                                            else 9)
        df_us_snr_pred["type_structure_acr"] = df_us_snr_pred['type_structure_acr'].apply(lambda x: 1 if x == df_us_snr["type_structure_acr"].unique()[0]
                                            else 2)
        df_us_snr_pred["mmg_number_nodles"] = df_us_snr_pred['mmg_number_nodles'].apply(lambda x: 1 if x == df_us_snr["mmg_number_nodles"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_number_nodles"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_number_nodles"].unique()[2]
                                            else 4 if x == df_us_snr["mmg_number_nodles"].unique()[3]
                                            else 5)
        df_us_snr_pred["mmg_category_birads"] = df_us_snr_pred['mmg_category_birads'].apply(lambda x: 1 if x == df_us_snr["mmg_category_birads"].unique()[0]
                                            else 2 if x == df_us_snr["mmg_category_birads"].unique()[1]
                                            else 3 if x == df_us_snr["mmg_category_birads"].unique()[2]
                                            else 4 if x == df_us_snr["mmg_category_birads"].unique()[3]
                                            else 5 if x == df_us_snr["mmg_category_birads"].unique()[4]
                                            else 6 if x == df_us_snr["mmg_category_birads"].unique()[5]
                                            else 7 if x == df_us_snr["mmg_category_birads"].unique()[6]
                                            else 8 if x == df_us_snr["mmg_category_birads"].unique()[7]
                                            else 9)
        df_us_snr_num = df_us_snr

        df_us_snr_num["diagnosis_primary"] = df_us_snr_num['diagnosis_primary'].apply(lambda x: 1 if x == df_us_snr_num["diagnosis_primary"].unique()[0]
                                    else 2 if x == df_us_snr_num["diagnosis_primary"].unique()[1]
                                    else 3 if x == df_us_snr_num["diagnosis_primary"].unique()[2]
                                    else 4 if x == df_us_snr_num["diagnosis_primary"].unique()[3]
                                    else 5 if x == df_us_snr_num["diagnosis_primary"].unique()[4]
                                    else 6 if x == df_us_snr_num["diagnosis_primary"].unique()[5]
                                    else 7 if x == df_us_snr_num["diagnosis_primary"].unique()[6]
                                    else 8 if x == df_us_snr_num["diagnosis_primary"].unique()[7]
                                    else 9 if x == df_us_snr_num["diagnosis_primary"].unique()[8]                                    
                                    else 10)
        df_us_snr_num["satus_reproductive"] = df_us_snr_num["satus_reproductive"].apply(lambda x: 1 if x == df_us_snr_num["diagnosis_primary"].unique()[0]
                                            else 2)
        df_us_snr_num["side"] = df_us_snr_num['side'].apply(lambda x: 1 if x == df_us_snr_num["side"].unique()[0]
                                            else 2 if x == df_us_snr_num["side"].unique()[1]
                                            else 3 if x == df_us_snr_num["side"].unique()[2]
                                            else 4)
        df_us_snr_num["complaints"] = df_us_snr_num['complaints'].apply(lambda x: 1 if x == df_us_snr_num["complaints"].unique()[0]
                                            else 2 if x == df_us_snr_num["complaints"].unique()[1]
                                            else 3 if x == df_us_snr_num["complaints"].unique()[2]
                                            else 4)
        df_us_snr_num["breast_surgery_before"] = df_us_snr_num["breast_surgery_before"].apply(lambda x: 1 if x == df_us_snr_num["breast_surgery_before"].unique()[0]
                                            else 2)
        df_us_snr_num["skin_symptoms"] = df_us_snr_num["skin_symptoms"].apply(lambda x: 1 if x == df_us_snr_num["skin_symptoms"].unique()[0]
                                            else 2)
        df_us_snr_num["nipple_retraction"] = df_us_snr_num["nipple_retraction"].apply(lambda x: 1 if x == df_us_snr_num["nipple_retraction"].unique()[0]
                                            else 2)
        df_us_snr_num["nipple_release"] = df_us_snr_num["nipple_release"].apply(lambda x: 1 if x == df_us_snr_num["nipple_release"].unique()[0]
                                            else 2)
        df_us_snr_num["quadrant"] = df_us_snr_num['quadrant'].apply(lambda x: 1 if x == df_us_snr_num["quadrant"].unique()[0]
                                            else 2 if x == df_us_snr_num["quadrant"].unique()[1]
                                            else 3 if x == df_us_snr_num["quadrant"].unique()[2]
                                            else 4 if x == df_us_snr_num["quadrant"].unique()[3]
                                            else 5 if x == df_us_snr_num["quadrant"].unique()[4]
                                            else 6 if x == df_us_snr_num["quadrant"].unique()[5]
                                            else 7 if x == df_us_snr_num["quadrant"].unique()[6]
                                            else 8 if x == df_us_snr_num["quadrant"].unique()[7]
                                            else 9 if x == df_us_snr_num["quadrant"].unique()[8]                                    
                                            else 10)
        df_us_snr_num["genetics"] = df_us_snr_num["genetics"].apply(lambda x: 1 if x == df_us_snr_num["genetics"].unique()[0]
                                            else 2)
        df_us_snr_num["hormonal_medications"] = df_us_snr_num["hormonal_medications"].apply(lambda x: 1 if x == df_us_snr_num["hormonal_medications"].unique()[0]
                                            else 2)
        df_us_snr_num["hist_is_tumor"] = df_us_snr_num["hist_is_tumor"].apply(lambda x: 1 if x == df_us_snr_num["hist_is_tumor"].unique()[0]
                                            else 2)
        df_us_snr_num["mmg_conclusion_skin"] = df_us_snr_num['mmg_conclusion_skin'].apply(lambda x: 1 if x == df_us_snr_num["mmg_conclusion_skin"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_conclusion_skin"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_conclusion_skin"].unique()[2]
                                            else 4)
        df_us_snr_num["mmg_areola"] = df_us_snr_num['mmg_areola'].apply(lambda x: 1 if x == df_us_snr_num["mmg_areola"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_areola"].unique()[1]
                                            else 3)
        df_us_snr_num["mmg_nipple"] = df_us_snr_num['mmg_nipple'].apply(lambda x: 1 if x == df_us_snr_num["mmg_nipple"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_nipple"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_nipple"].unique()[2]
                                            else 4)
        df_us_snr_num["mmg_background_breast"] = df_us_snr_num['mmg_background_breast'].apply(lambda x: 1 if x == df_us_snr_num["mmg_background_breast"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_background_breast"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_background_breast"].unique()[2]
                                            else 4 if x == df_us_snr_num["mmg_background_breast"].unique()[3]
                                            else 5)
        df_us_snr_num["mmg_nodle"] = df_us_snr_num['mmg_nodle'].apply(lambda x: 1 if x == df_us_snr_num["mmg_nodle"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_nodle"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_nodle"].unique()[2]
                                            else 4 if x == df_us_snr_num["mmg_nodle"].unique()[3]
                                            else 5 if x == df_us_snr_num["mmg_nodle"].unique()[4]
                                            else 6 if x == df_us_snr_num["mmg_nodle"].unique()[5]
                                            else 7 if x == df_us_snr_num["mmg_nodle"].unique()[6]
                                            else 8 if x == df_us_snr_num["mmg_nodle"].unique()[7]
                                            else 9 if x == df_us_snr_num["mmg_nodle"].unique()[8]                                    
                                            else 10)
        df_us_snr_num["mmg_nodle_contour"] = df_us_snr_num['mmg_nodle_contour'].apply(lambda x: 1 if x == df_us_snr_num["mmg_nodle_contour"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_nodle_contour"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_nodle_contour"].unique()[2]
                                            else 4 if x == df_us_snr_num["mmg_nodle_contour"].unique()[3]
                                            else 5)
        df_us_snr_num["mmg_nodle_size"] = df_us_snr_num['mmg_nodle_size'].apply(lambda x: 1 if x == df_us_snr_num["mmg_nodle_size"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_nodle_size"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_nodle_size"].unique()[2]
                                            else 4 if x == df_us_snr_num["mmg_nodle_size"].unique()[3]
                                            else 5 if x == df_us_snr_num["mmg_nodle_size"].unique()[4]
                                            else 6 if x == df_us_snr_num["mmg_nodle_size"].unique()[5]
                                            else 7)
        df_us_snr_num["mmg_calcifications"] = df_us_snr_num['mmg_calcifications'].apply(lambda x: 1 if x == df_us_snr_num["mmg_calcifications"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_calcifications"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_calcifications"].unique()[2]
                                            else 4 if x == df_us_snr_num["mmg_calcifications"].unique()[3]
                                            else 5 if x == df_us_snr_num["mmg_calcifications"].unique()[4]
                                            else 6 if x == df_us_snr_num["mmg_calcifications"].unique()[5]
                                            else 7 if x == df_us_snr_num["mmg_calcifications"].unique()[6]
                                            else 8 if x == df_us_snr_num["mmg_calcifications"].unique()[7]
                                            else 9 if x == df_us_snr_num["mmg_calcifications"].unique()[8]                                    
                                            else 10 if x == df_us_snr_num["mmg_calcifications"].unique()[9]
                                            else 11)
        df_us_snr_num["mmg_number_formations_visualized"] = df_us_snr_num['mmg_number_formations_visualized'].apply(lambda x: 1 if x == df_us_snr_num["mmg_number_formations_visualized"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_number_formations_visualized"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_number_formations_visualized"].unique()[2]
                                            else 4 if x == df_us_snr_num["mmg_number_formations_visualized"].unique()[3]
                                            else 5)
        df_us_snr_num["mmg_axillary_lymph_nodes"] = df_us_snr_num['mmg_axillary_lymph_nodes'].apply(lambda x: 1 if x == df_us_snr_num["mmg_axillary_lymph_nodes"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_axillary_lymph_nodes"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_axillary_lymph_nodes"].unique()[2]
                                            else 4)
        df_us_snr_num["mmg_conclusion"] = df_us_snr_num['mmg_conclusion'].apply(lambda x: 1 if x == df_us_snr_num["mmg_conclusion"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_conclusion"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_conclusion"].unique()[2]
                                            else 4 if x == df_us_snr_num["mmg_conclusion"].unique()[3]
                                            else 5 if x == df_us_snr_num["mmg_conclusion"].unique()[4]
                                            else 6 if x == df_us_snr_num["mmg_conclusion"].unique()[5]
                                            else 7 if x == df_us_snr_num["mmg_conclusion"].unique()[6]
                                            else 8 if x == df_us_snr_num["mmg_conclusion"].unique()[7]
                                            else 9)
        df_us_snr_num["type_structure_acr"] = df_us_snr_num['type_structure_acr'].apply(lambda x: 1 if x == df_us_snr_num["type_structure_acr"].unique()[0]
                                            else 2)
        df_us_snr_num["mmg_number_nodles"] = df_us_snr_num['mmg_number_nodles'].apply(lambda x: 1 if x == df_us_snr_num["mmg_number_nodles"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_number_nodles"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_number_nodles"].unique()[2]
                                            else 4 if x == df_us_snr_num["mmg_number_nodles"].unique()[3]
                                            else 5)
        df_us_snr_num["mmg_category_birads"] = df_us_snr_num['mmg_category_birads'].apply(lambda x: 1 if x == df_us_snr_num["mmg_category_birads"].unique()[0]
                                            else 2 if x == df_us_snr_num["mmg_category_birads"].unique()[1]
                                            else 3 if x == df_us_snr_num["mmg_category_birads"].unique()[2]
                                            else 4 if x == df_us_snr_num["mmg_category_birads"].unique()[3]
                                            else 5 if x == df_us_snr_num["mmg_category_birads"].unique()[4]
                                            else 6 if x == df_us_snr_num["mmg_category_birads"].unique()[5]
                                            else 7 if x == df_us_snr_num["mmg_category_birads"].unique()[6]
                                            else 8 if x == df_us_snr_num["mmg_category_birads"].unique()[7]
                                            else 9)
        
        X_snr = df_us_snr_num.drop('hist_is_tumor', axis=1)
        y_snr = df_us_snr_num['hist_is_tumor']

        X_train_snr, X_test_snr, y_train_snr, y_test_snr = train_test_split(X_snr, y_snr, test_size=0.20, random_state=42, stratify=y_snr)

        rf = RandomForestClassifier(
            n_estimators=500, 
            max_depth=5, 
            max_features=None, 
            bootstrap=True, 
            min_samples_split=5,
            min_samples_leaf=2, 
            random_state=42,
            class_weight=None,
            verbose=1,
            n_jobs=-1
)

        rf.fit(X_train_snr, y_train_snr)


        
        df_us_snr_pred["hist_is_tumor"] = rf.predict(df_us_snr_pred)

        
       

        

        df_us_snr_pred["way"] = df_us_snr_pred["hist_is_tumor"].apply(lambda x: '3d УЗИ' if x == 1
                                            else 'традиционное УЗИ')
        way_to_snr = df_us_snr_pred["way"][0]

        
        ml_panel_snr = dbc.Card([
                dbc.CardHeader("Маршрутизация пациентки 40 лет и старше", className="h2-label"),
                dbc.CardBody([
                    dcc.Markdown(f"*Направление:* **{way_to_snr}** \n ---"),
                    dcc.Markdown(f"*Возраст:* **{selected_age_patient_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Диагноз:* **{selected_diagnosis_primary_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Сторона:* **{selected_side_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Репродуктивный статус:* **{selected_satus_reproductive_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Жалобы:* **{selected_complaints_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Операции до:* **{selected_breast_surgery_before_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Симптомы на коже:* **{selected_skin_symptoms_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Симптом ретракции:* **{selected_nipple_retraction_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Симптом выделения:* **{selected_nipple_release_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Кавадрант:* **{selected_quadrant_pr_snr}** \n ---"),
                    dcc.Markdown(f"*Наследственность:* **{selected_genetics_pr_snr}** \n ---")
                    
                ], className="stats-body")])

        return {"diagnosis_primary": diagnosis_primary_fig, 
                "group_separation": group_separation_fig,
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
                "mmg_background_breast":mmg_background_breast_fig,
                "mmg_nodle":mmg_nodle_fig,
                "mmg_nodle_contour":mmg_nodle_contour_fig,
                "mmg_nodle_size":mmg_nodle_size_fig,
                "mmg_calcifications":mmg_calcifications_fig,
                "mmg_number_formations_visualized":mmg_number_formations_visualized_fig,
                "mmg_axillary_lymph_nodes":mmg_axillary_lymph_nodes_fig,
                "type_structure_acr":type_structure_acr_fig,
                "mmg_category_birads":mmg_category_birads_fig,
                "abus_nodle_size":abus_nodle_size_fig,
                "abus_nodle_contours":abus_nodle_contours_fig,
                "abus_echogenicity_formation":abus_echogenicity_formation_fig,
                "abus_structure":abus_structure_fig,
                "abus_symptom_retraction":abus_symptom_retraction_fig,
                "abus_formation":abus_formation_fig,
                "abus_category_birads":abus_category_birads_fig,
                "abus_calcinates":abus_calcinates_fig,
                "tumor_morphology_structure":tumor_morphology_structure_fig,
                "cytological_conclusion":cytological_conclusion_fig,
                "degree_malignancy":degree_malignancy_fig,
                "mutation_brca":mutation_brca_fig,
                "tumor_receptors":tumor_receptors_fig,
                "hist_is_tumor":hist_is_tumor_fig,
                "us_probabilityCalc":us_probabilityCalc_fig,
                "abus_probabilityCalc":abus_probabilityCalc_fig,
                "us_probabilityNeoCa":us_probabilityNeoCa_fig,
                "abus_probabilityNeoCa":abus_probabilityNeoCa_fig,
                "mmg_probabilityNeoCa":mmg_probabilityNeoCa_fig,
                "stats-panel":stats_panel,
                "ml-panel_jun":ml_panel_jun,
                "ml-panel_snr":ml_panel_snr
                
                
                }
    

