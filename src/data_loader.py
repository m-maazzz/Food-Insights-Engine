import pandas as pd
from src.config import RAW_DATA_DIR


class DataLoader:

    def load_foods(self):
        return pd.read_csv(
            RAW_DATA_DIR / "food.csv"
        )

    def load_food_nutrients(self):
        return pd.read_csv(
            RAW_DATA_DIR / "food_nutrient.csv",
            low_memory=False
        )

    def load_nutrients(self):
        return pd.read_csv(
            RAW_DATA_DIR / "nutrient.csv"
        )

    def load_food_categories(self):
        return pd.read_csv(
            RAW_DATA_DIR / "food_category.csv"
        )