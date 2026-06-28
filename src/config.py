from pathlib import Path

PROJ_ROOT = Path(__file__).resolve().parents[1]
#
DATA_DIR = PROJ_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


MODELS_DIR = PROJ_ROOT / "models"


PREDICTIONS_DIR = PROJ_ROOT / "predictions"


REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"


# Features
NUMERICAL_FEATURES = []

CATEGORICAL_FEATURES = []