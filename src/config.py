# src/config.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "food_data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

REPORTS_DIR = BASE_DIR / "reports"
CHARTS_DIR = BASE_DIR / "charts"

# Important Nutrient IDs

PROTEIN_ID = 1003
FAT_ID = 1004
CARB_ID = 1005
ENERGY_ID = 1008