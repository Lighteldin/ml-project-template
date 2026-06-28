<a id="readme-top"></a>
<br />
<div align="center">
  <h3 align="center">DATA SCIENCE TEMPLATE</h3>

   A personal, modified template based on the [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) project.
  
</div>

---




## Architecture

```
├── data
│   ├── processed               <- Scaled and encoded datasets ready for machine learning algorithms.
│   ├── interim                 <- Intermediate data that has been transformed.
│   └── raw                     <- The original, immutable data.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks.
│
├── reports            <- Generated analysis 
│   └── figures                 <- Generated graphics and figures 
│
├── requirements.txt   <- `pip freeze > requirements.txt`
│
└── src                <- Source code
    │
    ├── __init__.py
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py
    │
    ├── features.py
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py 
    │   └── train.py
    │
    └── plots.py
```

---

## Installation

### 1. Environment Setup
```bash
git clone https://github.com/Lighteldin/data-science-template.git

cd data-science-template

python -m venv venv
```

### 2. Activation
Windows (CMD): `venv\Scripts\activate`

Windows (PowerShell): `.\venv\Scripts\Activate.ps1`

Linux / macOS: `source venv/bin/activate`

### 3. Dependencies
```bash
pip install -r requirements.txt
```