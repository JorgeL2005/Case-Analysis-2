import streamlit as st
import joblib
import pandas as pd
import numpy as np
import time

@st.cache_resource
def load_model():
    model = joblib.load("best_model.pkl")
    return model

model = load_model()

st.set_page_config(page_title="🎓 Student GPA Predictor", layout="wide")
st.title("🎓 Student GPA Predictor")

view = st.sidebar.selectbox("Selecciona la vista", ["Estudiante", "Coordinador"])
st.header(f"Vista: {view}")

col1, col2 = st.columns([1,1])

with col1:
    Age = st.number_input("🎂 Edad", min_value=15, max_value=18, value=18)
    StudyTimeWeekly = st.number_input("📚 Horas Estudio/Semana", min_value=0, max_value=20, value=5)
    Absences = st.number_input("🚪 Ausencias", min_value=0, max_value=30, value=2)
    ParentalSupport = st.selectbox(
        "👨‍👩‍👦 Apoyo Parental",
        options=[0,1,2,3,4],
        format_func=lambda x: {0:"Ninguno",1:"Bajo",2:"Moderado",3:"Alto",4:"Muy alto"}[x]
    )

with col2:
    Tutoring = 1 if st.checkbox("👩‍🏫 Tutoría", value=False) else 0
    Extracurricular = 1 if st.checkbox("🎭 Actividades Extracurriculares", value=False) else 0
    Sports = 1 if st.checkbox("⚽ Deportes", value=False) else 0
    Music = 1 if st.checkbox("🎵 Música", value=False) else 0
    Volunteering = 1 if st.checkbox("🤝 Voluntariado", value=False) else 0

if st.button("📌 Calcular GPA"):
    input_dict = {
        'Age':[Age],
        'StudyTimeWeekly':[StudyTimeWeekly],
        'Absences':[Absences],
        'ParentalSupport':[ParentalSupport],
        'Tutoring':[Tutoring],
        'Extracurricular':[Extracurricular],
        'Sports':[Sports],
        'Music':[Music],
        'Volunteering':[Volunteering]
    }

    df_input = pd.DataFrame(input_dict)
    model_columns = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else df_input.columns
    for col in model_columns:
        if col not in df_input.columns:
            df_input[col] = 0
    df_input = df_input[model_columns]

    pred_gpa = round(model.predict(df_input)[0],2)

    st.metric("🎯 GPA Predicho", f"{pred_gpa:.2f}")

    if pred_gpa >= 3.5: grade = "A"; color="green"
    elif pred_gpa >= 3.0: grade="B"; color="blue"
    elif pred_gpa >= 2.5: grade="C"; color="orange"
    elif pred_gpa >= 2.0: grade="D"; color="red"
    else: grade="F"; color="purple"

    st.markdown(
        f"""
        <div style="text-align:center; font-size:36px; font-weight:bold;">
            <span style="color:{'green' if grade=='A' else '#ccc'};">A</span>&nbsp;&nbsp;
            <span style="color:{'blue' if grade=='B' else '#ccc'};">B</span>&nbsp;&nbsp;
            <span style="color:{'orange' if grade=='C' else '#ccc'};">C</span>&nbsp;&nbsp;
            <span style="color:{'red' if grade=='D' else '#ccc'};">D</span>&nbsp;&nbsp;
            <span style="color:{'purple' if grade=='F' else '#ccc'};">F</span>
        </div>
        <div style="text-align:center; font-size:64px; font-weight:bold; color:{color}; margin-top:10px;">
            {grade}
        </div>
        """, unsafe_allow_html=True
    )

    if view=="Estudiante":
        st.subheader("💡 Consejos motivacionales y recomendaciones")
        if pred_gpa < 3.0:
            st.success("¡Puedes mejorar! Aquí algunas acciones para aumentar tu GPA:")
            st.write("- Incrementa gradualmente tus horas de estudio semanales.")
            st.write("- Participa en tutorías para reforzar tus conocimientos.")
            st.write("- Reduce ausencias y mantén constancia en clases.")
            st.write("- Únete a actividades extracurriculares que te motiven.")
        else:
            st.success("¡Excelente desempeño! Mantén estos hábitos:")
            st.write("- Continúa con tu dedicación al estudio.")
            st.write("- Participa en actividades que disfrutes y te inspiren.")
            st.write("- Comparte tus estrategias exitosas con compañeros.")

    if view=="Coordinador":
        st.subheader("📌 Análisis para Coordinadores")
        if pred_gpa < 3.0:
            st.warning("Estudiante identificado con riesgo académico.")
            st.write("- Considerar seguimiento personalizado y tutorías.")
            st.write("- Ofrecer recursos motivacionales y programas de apoyo.")
        else:
            st.info("Estudiante con desempeño adecuado. Mantener seguimiento motivacional.")
