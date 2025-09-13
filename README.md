# 🎓 Student GPA Predictor

Herramienta predictiva que estima el **GPA final de estudiantes universitarios de primer semestre**, con el objetivo de identificar tempranamente a quienes necesitan apoyo académico.  
El reto principal es diseñar una interfaz que sea **motivacional en lugar de desalentadora**, evitando sesgos por género/etnia/clase social, y que además ofrezca **recomendaciones accionables** tanto para estudiantes como para coordinadores académicos.

---

## 📊 Dataset
**Student Performance Prediction** – Kaggle  

### Variables consideradas en el modelo:
- **Age**: Edad (15–18 años)  
- **StudyTimeWeekly**: Horas de estudio semanales (0–20)  
- **Absences**: Número de ausencias (0–30)  
- **Tutoring**: Tutoría (0 = No, 1 = Sí)  
- **ParentalSupport**: Nivel de apoyo parental (0 = Ninguno, 1 = Bajo, 2 = Moderado, 3 = Alto, 4 = Muy alto)  
- **Extracurricular**: Actividades extracurriculares (0 = No, 1 = Sí)  
- **Sports**: Deportes (0 = No, 1 = Sí)  
- **Music**: Música (0 = No, 1 = Sí)  
- **Volunteering**: Voluntariado (0 = No, 1 = Sí)  

### Variables descartadas:
- `StudentID`, `Gender`, `Ethnicity`, `ParentalEducation`, `GradeClass`, `GPA`

---

## 📌 Clasificación de GPA
- **A** : GPA ≥ 3.5  
- **B** : 3.0 ≤ GPA < 3.5  
- **C** : 2.5 ≤ GPA < 3.0  
- **D** : 2.0 ≤ GPA < 2.5  
- **F** : GPA < 2.0  

---

## ⚙️ Instalación


Crear y activar un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
venv\Scripts\activate     

