import streamlit as st
import joblib
import pandas as pd
import time

@st.cache_resource
def load_model():
    return joblib.load("linear_regression_model.pkl")

model = load_model()

st.set_page_config(page_title="Student GPA Predictor", layout="wide")
st.title("🎓 Student GPA Predictor")

st.markdown("## 📋 Parámetros del Estudiante")

col1, col_spacer, col2, col_spacer2, col3 = st.columns([1,0.3,1,0.3,1])

with col1:
    Age = st.number_input("🎂 Edad", min_value=15, max_value=18, value=18)
    StudyTimeWeekly = st.number_input("📚 Horas Estudio/Semana", min_value=0, max_value=20, value=5)
    Absences = st.number_input("🚪 Ausencias", min_value=0, max_value=30, value=2)
    ParentalSupport = st.selectbox(
        "👨‍👩‍👦 Apoyo Parental",
        options=[0,1,2,3,4],
        format_func=lambda x: {
            0: "Ninguno",
            1: "Bajo",
            2: "Moderado",
            3: "Alto",
            4: "Muy alto"
        }[x]
    )

with col2:
    Tutoring = 1 if st.toggle("👩‍🏫 Tutoría", value=False) else 0
    Extracurricular = 1 if st.toggle("🎭 Actividades Extracurriculares", value=False) else 0
    Sports = 1 if st.toggle("⚽ Deportes", value=False) else 0
    Music = 1 if st.toggle("🎵 Música", value=False) else 0
    Volunteering = 1 if st.toggle("🤝 Voluntariado", value=False) else 0

with col3:
    if st.button("📌 Calcular GPA", use_container_width=True):
        new_data = pd.DataFrame({
            'Age': [Age],
            'StudyTimeWeekly': [StudyTimeWeekly],
            'Absences': [Absences],
            'Tutoring': [Tutoring],
            'ParentalSupport': [ParentalSupport],
            'Extracurricular': [Extracurricular],
            'Sports': [Sports],
            'Music': [Music],
            'Volunteering': [Volunteering]
        })

        start = time.time()
        prediction = model.predict(new_data)[0]
        end = time.time()

        st.metric("🎯 GPA Predicho", f"{prediction:.2f}")
        st.info(f"⏱ Tiempo de cálculo: {round(end - start, 3)} segundos")

        if prediction >= 3.5:
            grade = "A"; color = "green"
        elif prediction >= 3.0:
            grade = "B"; color = "blue"
        elif prediction >= 2.5:
            grade = "C"; color = "orange"
        elif prediction >= 2.0:
            grade = "D"; color = "red"
        else:
            grade = "F"; color = "black"

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
            """,
            unsafe_allow_html=True
        )
