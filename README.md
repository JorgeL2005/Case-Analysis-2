# 🎓 Student GPA Predictor

## Problema
Desarrollar una herramienta predictiva que estime el **GPA final** de estudiantes universitarios de primer semestre, con el objetivo de **identificar tempranamente a quienes podrían necesitar apoyo académico**. La solución debe ser ética, motivacional y ofrecer recomendaciones prácticas para mejorar el desempeño.

## Tarea (Task)
- Predecir un **valor numérico continuo**: el GPA final de cada estudiante.  
- El enfoque principal será la **regresión**, utilizando técnicas lineales o no lineales según corresponda.  
- La solución debe ser escalable y permitir futuras mejoras, como incluir interacciones entre variables o transformar la regresión lineal en una más compleja si se detectan relaciones no lineales.

## Métrica (Metric)
- Evaluar la calidad del modelo usando métricas de regresión, como:  
  - **MSE (Mean Squared Error / Error Cuadrático Medio)**: informa sobre la magnitud promedio de los errores.  
  - **R² (Coeficiente de Determinación)**: indica qué proporción de la variabilidad del GPA es explicada por el modelo.  
- La métrica debe ser **informativa y práctica**, permitiendo comparar versiones del modelo y monitorear mejoras post-deployment.

## Experiencia del Usuario (Experience)
- La herramienta debe ser **motivacional y no desalentadora**:  
  - Evitar mensajes negativos que puedan generar frustración.  
  - Generar recomendaciones **específicas y accionables** para cada estudiante (por ejemplo, horas de estudio semanales, participación en tutorías, hábitos de aprendizaje).  
- Evitar **sesgos por género, raza o clase social**:  
  - El modelo no debe discriminar ni generar predicciones que dependan de estas variables.  
- Diseñar **dos vistas distintas**:  
  1. **Vista para estudiantes**: enfocada en motivación, progreso y mejora continua.  
  2. **Vista para coordinadores académicos**: enfocada en identificación de riesgo, priorización de intervenciones y recursos disponibles.  
- La interfaz debe ser **útil y accesible**, resolviendo el problema central de los stakeholders: estudiantes y coordinadores académicos.


---

## 📊 Dataset
[Student Performance Prediction - Kaggle](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)  

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


---

## 📌 Clasificación de GPA
- **A** : GPA ≥ 3.5  
- **B** : 3.0 ≤ GPA < 3.5  
- **C** : 2.5 ≤ GPA < 3.0  
- **D** : 2.0 ≤ GPA < 2.5  
- **F** : GPA < 2.0  

---

## ⚙️ Modelo
Se utilizó **Regresión Lineal** para predecir el GPA de los estudiantes, considerando únicamente variables relacionadas con estudio, tutoría, actividades extracurriculares y apoyo parental.  

**Flujo del modelo:**  
1. **Carga y preparación de datos**:  
   - Se eliminaron columnas irrelevantes para el estudio: `StudentID`, `GradeClass`, `GPA`. 
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

print("\n=== Importancia de variables ===")
if best_model[0] == "Lineal":
    for var, peso in zip(x_train.columns, linear.coef_):
        print(f"{var}: {peso:.4f}")
elif best_model[0] == "Polinómica (deg=2)":
    # Obtener nombres de features polinómicas
    feature_names = poly2.named_steps['poly'].get_feature_names_out(x_train.columns)
    for var, peso in zip(feature_names, poly2.named_steps['lin'].coef_):
        print(f"{var}: {peso:.4f}")
elif best_model[0] in ["Tree", "RandomForest"]:
    model_to_use = tree if best_model[0]=="Tree" else forest
    for var, imp in zip(x_train.columns, model_to_use.feature_importances_):
        print(f"{var}: {imp:.4f}")
```

## Resultados

- **Modelo entrenado:** Regresión Lineal  
- **Evaluación:** RMSE = 0.196, R² = 0.953 (mejor modelo según R²)  
- **Comparación de modelos:**  
  - Lineal: RMSE=0.196, R²=0.953  
  - Polinómica (deg=2): RMSE=0.207, R²=0.948  
  - Árbol de decisión: RMSE=0.337, R²=0.863  
  - Random Forest: RMSE=0.243, R²=0.929  

- **Variables más influyentes en la predicción del GPA:**  
  1. `StudyTimeWeekly` – horas de estudio semanales (+0.0290)  
  2. `Tutoring` – participación en tutorías (+0.2581)  
  3. `ParentalSupport` – nivel de apoyo parental (+0.1479)  

- **Otras variables que aportan al modelo:**  
  - `Extracurricular` (+0.1898)  
  - `Sports` (+0.1843)  
  - `Music` (+0.1518)  
  - `Volunteering` (-0.0050)  
  - `Age` (-0.0058)  
  - `Gender` (+0.0107)  
  - `Ethnicity_1` (+0.0097), `Ethnicity_2` (+0.0093), `Ethnicity_3` (+0.0121)  
  - `ParentalEducation_1` (-0.0022), `ParentalEducation_2` (+0.0073), `ParentalEducation_3` (-0.0126), `ParentalEducation_4` (+0.0139)  

- **Consideraciones en la app:**  
  > 🔹 En la implementación de `app.py`, se **omitieron las variables demográficas** `Gender`, `Ethnicity` y `ParentalEducation`. Esto significa que, aunque el modelo las utiliza internamente para análisis y cálculo de coeficientes, la interfaz de usuario **no considera estas variables** para la predicción de GPA.  
  > 🔹 Esto garantiza que la herramienta sea motivacional, justa y libre de sesgos por género, raza o nivel educativo de los padres, enfocándose únicamente en variables de comportamiento y apoyo académico (`StudyTimeWeekly`, `Tutoring`, `ParentalSupport`, `Extracurricular`, `Sports`, `Music`, `Volunteering`, `Age`, `Absences`).

---

## Discusión

El desarrollo de la herramienta predictiva de GPA permitió analizar y modelar de manera efectiva el desempeño académico de estudiantes de primer semestre. A partir de los modelos evaluados (Lineal, Polinómica, Árbol de Decisión y Random Forest), la **Regresión Lineal** se identificó como la opción más adecuada, con un R² de 0.953 y RMSE de 0.196, demostrando un ajuste muy preciso a los datos.

### Interpretación de resultados
Las variables con mayor impacto en la predicción del GPA fueron:

- `Tutoring`: La participación en tutorías mostró la mayor influencia positiva, indicando que el acompañamiento académico directo tiene un efecto significativo en el desempeño.  
- `StudyTimeWeekly`: Las horas de estudio semanales se correlacionan positivamente con un mejor GPA, confirmando la importancia de la dedicación al estudio.  
- `ParentalSupport`: El apoyo familiar también mostró un impacto relevante, aunque menor que la participación activa en actividades académicas.  

Otras variables, como `Extracurricular`, `Sports`, `Music` y `Volunteering`, también aportan al modelo, reflejando cómo la participación en actividades complementarias puede contribuir al bienestar y motivación del estudiante. Variables demográficas (`Gender`, `Ethnicity`, `ParentalEducation`) tienen coeficientes menores, y **no se consideraron en la app** para evitar sesgos.

### Ética y diseño de la app
Un aspecto crítico del proyecto fue garantizar que la herramienta **sea motivacional y libre de sesgos**. Para lograrlo:

- La interfaz de usuario **no solicita ni utiliza información sobre género, etnia o nivel educativo de los padres**, evitando cualquier sesgo indirecto en la predicción.  
- Se proporciona retroalimentación constructiva, diferenciando entre estudiantes que necesitan apoyo y aquellos con buen desempeño, **enfocándose en acciones concretas y motivacionales**.  
- La app ofrece dos vistas:  
  - **Estudiante:** Consejos personalizados y motivacionales.  
  - **Coordinador:** Identificación de estudiantes en riesgo y recomendaciones de intervención.

### Limitaciones
- El modelo se entrenó con datos de primer semestre, por lo que su generalización a otros ciclos podría ser limitada.  
- La omisión de variables demográficas, si bien ética, puede eliminar información estadísticamente relevante; sin embargo, esto fue un compromiso necesario para priorizar la equidad.  
- La herramienta depende de la correcta entrada de datos por parte del usuario; errores en el registro de horas de estudio o ausencias podrían afectar la predicción.

### Conclusión
La herramienta demuestra que es posible crear un sistema predictivo de desempeño académico **preciso, motivacional y ético**. La selección de variables de comportamiento y apoyo académico permite generar recomendaciones útiles sin introducir sesgos, cumpliendo con el objetivo de identificar estudiantes que requieren intervención temprana y fomentar hábitos positivos desde el inicio de su vida universitaria.



