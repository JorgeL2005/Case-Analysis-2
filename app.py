import streamlit as st
import joblib
import pandas as pd
import numpy as np
import time

@st.cache_resource
def load_model():
    model = joblib.load("linear_regression_model.pkl")
    cols = joblib.load("model_columns.pkl")
    return model, cols

model, model_columns = load_model()

st.set_page_config(page_title="Student GPA Predictor", layout="wide")
st.title("🎓 Student GPA Predictor")

view = st.sidebar.selectbox("Selecciona la vista", ["Estudiante", "Coordinador"])
st.header(f"Vista: {view}")

# Inputs de usuario
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
        'Tutoring':[Tutoring],
        'ParentalSupport':[ParentalSupport],
        'Extracurricular':[Extracurricular],
        'Sports':[Sports],
        'Music':[Music],
        'Volunteering':[Volunteering]
    }
    df_input = pd.DataFrame(input_dict)
    
    # Asegurar columnas del modelo
    for col in model_columns:
        if col not in df_input.columns:
            df_input[col] = 0
    df_input = df_input[model_columns]
    
    start = time.time()
    pred_gpa = model.predict(df_input)[0]
    end = time.time()
    pred_gpa = round(pred_gpa,2)
    
    st.metric("🎯 GPA Predicho", f"{pred_gpa:.2f}")
    st.info(f"⏱ Tiempo de cálculo: {round(end-start,3)} segundos")
    
    # Asignar letra y color
    if pred_gpa >= 3.5: grade = "A"; color="green"
    elif pred_gpa >= 3.0: grade="B"; color="blue"
    elif pred_gpa >= 2.5: grade="C"; color="orange"
    elif pred_gpa >= 2.0: grade="D"; color="red"
    else: grade="F"; color="black"
    
    st.markdown(
        f"""
        <div style="text-align:center; font-size:36px; font-weight:bold;">
            <span style="color:{'green' if grade=='A' else '#ccc'};">A</span>&nbsp;&nbsp;
            <span style="color:{'blue' if grade=='B' else '#ccc'};">B</span>&nbsp;&nbsp;
            <span style="color:{'orange' if grade=='C' else '#ccc'};">C</span>&nbsp;&nbsp;
            <span style="color:{'red' if grade=='D' else '#ccc'};">D</span>&nbsp;&nbsp;
            <span style="color:{'black' if grade=='F' else '#ccc'};">F</span>
        </div>
        <div style="text-align:center; font-size:64px; font-weight:bold; color:{color}; margin-top:10px;">
            {grade}
        </div>
        """, unsafe_allow_html=True
    )
    
    # Recomendaciones
    if view=="Estudiante":
        st.subheader("💡 Recomendaciones para mejorar")
        if pred_gpa < 3.0:
            if StudyTimeWeekly < 5: st.write("- Incrementa tus horas de estudio semanales.")
            if Tutoring==0: st.write("- Considera participar en tutorías.")
            if Absences>5: st.write("- Reduce tus ausencias para mantener continuidad en clases.")
            if Extracurricular==0: st.write("- Participa en actividades extracurriculares para motivación.")
            st.write("- Mantén comunicación con tus profesores y compañeros.")
        else:
            st.write("- Continúa con tus buenos hábitos de estudio.")
            st.write("- Participa en actividades que te motiven y te diviertan.")
            st.write("- Comparte tus estrategias de éxito con tus compañeros.")
    
    if view=="Coordinador":
        st.subheader("📌 Análisis para Coordinadores")
        if pred_gpa < 3.0:
            st.write("- Estudiante en riesgo académico.")
            st.write("- Recomendar seguimiento personalizado y tutorías adicionales.")
            st.write("- Ofrecer recursos: talleres de estudio, mentorías, programas extracurriculares.")
        else:
            st.write("- Estudiante con desempeño adecuado.")
            st.write("- Mantener monitoreo y motivación continua.")
