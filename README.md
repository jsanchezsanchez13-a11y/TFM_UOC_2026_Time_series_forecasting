# TFM_UOC_2026_Time_series_forecasting

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

Trabajo de Fin de Máster centrado en la predicción de demanda mediante técnicas de series temporales y modelos de *machine learning*, con el objetivo de optimizar la gestión de inventarios y reducir costes asociados al stock.

---

# 📌 Descripción del proyecto

Este proyecto analiza distintos enfoques de predicción de demanda aplicados a datos reales de ventas e inventario. Se comparan modelos tradicionales y modelos avanzados de aprendizaje automático para evaluar su capacidad predictiva sobre diferentes patrones de demanda.

El trabajo incluye:

- Análisis exploratorio de datos (*EDA*)
- Preprocesamiento y limpieza de datos
- Segmentación de productos mediante *clustering*
- Ingeniería de características (*feature engineering*)
- Entrenamiento y evaluación de modelos predictivos
- Evaluación del impacto económico en la gestión de inventario

---

# 🧠 Modelos implementados

Los principales modelos evaluados en el proyecto son:

- Random Forest
- XGBoost
- LightGBM
- Modelo base Naive Bias Mean

Las métricas utilizadas para la evaluación incluyen:

- MAE (*Mean Absolute Error*)
- RMSE (*Root Mean Squared Error*)
- Varianza explicada

---

# 📂 Estructura del proyecto

```bash
.
├── Clustering/          # Segmentación de productos
├── Costes/              # Análisis económico y cálculo de costes
├── Data/                # Datos utilizados en el proyecto
├── data_preprocess/     # Limpieza y transformación de datos
├── EDA/                 # Análisis exploratorio de datos
├── Models/              # Entrenamiento y evaluación de modelos
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🐳 Entorno Docker

Todo el proyecto se ejecuta dentro de un contenedor Docker configurado específicamente para garantizar la reproducibilidad del entorno de trabajo y simplificar la instalación de dependencias.

El contenedor incluye:

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- Matplotlib
- Seaborn
- Otras dependencias definidas en `requirements.txt`

---

# ⚙️ Instalación y ejecución

## 1. Clonar el repositorio

```bash
git clone https://github.com/jsanchezsanchez13-a11y/TFM_UOC_2026_Time_series_forecasting.git
cd TFM_UOC_2026_Time_series_forecasting
```

## 2. Construir el contenedor Docker

```bash
docker-compose build
```

## 3. Ejecutar el entorno

```bash
docker-compose up
```

---

# 📓 Uso de Jupyter Notebook

El entorno Docker incluye un servidor de Jupyter Notebook para facilitar el desarrollo y análisis de los experimentos realizados en el TFM.

Una vez iniciado el contenedor, Jupyter Notebook estará disponible desde el navegador en:

```text
http://localhost:8888
```

Desde ahí es posible ejecutar y modificar los notebooks relacionados con:

- EDA
- Preprocesamiento
- Clustering
- Entrenamiento de modelos
- Evaluación de resultados

---

# 📊 Resultados principales

Los resultados obtenidos muestran que:

- **LightGBM** ofrece mejores resultados en productos con demanda estable.
- **Random Forest** presenta un comportamiento más robusto en demandas irregulares o volátiles.
- El modelo propuesto permite reducir el coste anual de inventario en aproximadamente:

```text
911.580,59 €
```

respecto al escenario basado en el modelo *Naive*.

---

# 🎓 Contexto académico

Este repositorio contiene el desarrollo práctico asociado al Trabajo Fin de Máster realizado en la Universitat Oberta de Catalunya (UOC).

---

# 📄 Licencia

Este proyecto se distribuye bajo la licencia GNU General Public License v3.0 (GPL-3.0).

Para más información, consultar el archivo `LICENSE` incluido en el repositorio.

---

# 👤 Autor

José Andrés Sánchez

GitHub: https://github.com/jsanchezsanchez13-a11y