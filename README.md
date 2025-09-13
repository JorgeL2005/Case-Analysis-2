# 🎓 Student GPA Predictor

Herramienta predictiva que estima el **GPA final de estudiantes universitarios de primer semestre**, con el objetivo de identificar tempranamente a quienes necesitan apoyo académico.  
El reto principal es diseñar una interfaz que sea **motivacional en lugar de desalentadora**, evitando sesgos por género/etnia/clase social, y que además ofrezca **recomendaciones accionables** tanto para estudiantes como para coordinadores académicos.

---

## 📊 Dataset
**Student Performance Prediction** – Kaggle  

### Variables consideradas en el modelo:
| Variable | Tipo | Descripción |
|----------|------|------------|
| Age | Numérica | Edad (15–18 años) |
| StudyTimeWeekly | Numérica | Horas de estudio semanales (0–20) |
| Absences | Numérica | Número de ausencias (0–30) |
| Tutoring | Categórica | Tutoría (0 = No, 1 = Sí) |
| ParentalSupport | Categórica | Nivel de apoyo parental (0 = Ninguno, 1 = Bajo, 2 = Moderado, 3 = Alto, 4 = Muy alto) |
| Extracurricular | Categórica | Actividades extracurriculares (0 = No, 1 = Sí) |
| Sports | Categórica | Deportes (0 = No, 1 = Sí) |
| Music | Categórica | Música (0 = No, 1 = Sí) |
| Volunteering | Categórica | Voluntariado (0 = No, 1 = Sí) |

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

## ⚙️ Model
Se utilizó **Regresión Lineal** para predecir el GPA de los estudiantes, considerando únicamente variables relacionadas con estudio, tutoría, actividades extracurriculares y apoyo parental.  

**Flujo del modelo:**  
1. **Carga y preparación de datos**:  
   - Se eliminaron columnas irrelevantes: `StudentID`, `Gender`, `Ethnicity`, `ParentalEducation`, `GradeClass`, `GPA`.  
   - Se definieron `X` como las variables predictoras y `y` como el GPA real.  

2. **División de datos**:  
   - 80% para entrenamiento y 20% para prueba.  

3. **Entrenamiento**:  
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
```

4. **Evaluación del modelo**

```python
from sklearn.metrics import mean_squared_error

# Predecir GPA en el conjunto de prueba
y_pred = model.predict(x_test)

# Calcular error cuadrático medio
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
```

5. **Guardado del modelo entrenado**

```python
import joblib

# Guardar modelo en un archivo .pkl
joblib.dump(model, 'linear_regression_model.pkl')
print("Modelo guardado como 'linear_regression_model.pkl'")
```

## Resultados

- **Modelo entrenado:** Regresión Lineal  
- **Evaluación:** Error Cuadrático Medio (MSE) en el conjunto de prueba: `[valor de mse]`  
- **Variables más influyentes en la predicción del GPA:**  
  1. `StudyTimeWeekly` – horas de estudio semanales  
  2. `Tutoring` – participación en tutorías  
  3. `ParentalSupport` – nivel de apoyo parental  
- **Variables con menor peso pero que aportan:** `Extracurricular`, `Sports`, `Music`, `Volunteering`  

> 🔹 Los coeficientes del modelo permiten interpretar el impacto de cada variable, ayudando a identificar factores clave para mejorar el desempeño académico.

---

## Discusión

- Permite **identificar estudiantes en riesgo temprano**, brindando tiempo para implementar acciones correctivas.  
- **Interfaz motivacional:** en lugar de alertas negativas, mostrar mensajes como “Áreas para mejorar y alcanzar tu potencial”.  
- **Evita sesgos:** el modelo no utiliza datos sensibles como género o etnia.  
- **Recomendaciones prácticas:**  
  - **Para estudiantes:** aumentar horas de estudio, participar en tutorías, actividades extracurriculares o voluntariado.  
  - **Para coordinadores académicos:** enfocar recursos de apoyo en los estudiantes identificados como en riesgo.  

> 🔹 Este enfoque fomenta un **aprendizaje proactivo y equitativo**, centrado en fortalecer oportunidades y mejorar resultados académicos.


