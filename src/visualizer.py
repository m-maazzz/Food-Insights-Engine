# src/visualizer.py

import matplotlib.pyplot as plt
import pandas as pd

from src.config import CHARTS_DIR


class NutritionVisualizer:

    def __init__(self):
        CHARTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    def plot_top_nutrient_foods(
        self,
        df: pd.DataFrame,
        value_column: str,
        chart_title: str,
        output_filename: str
    ):

        plot_df = df.head(10)

        plt.figure(figsize=(12, 6))

        plt.barh(
            plot_df["description"],
            plot_df[value_column]
        )

        plt.title(chart_title)

        plt.xlabel(value_column)

        plt.tight_layout()

        plt.savefig(
            CHARTS_DIR / output_filename
        )

        plt.close()

    def plot_category_distribution(
        self,
        food_with_category_df: pd.DataFrame
    ):

        category_counts = (
            food_with_category_df[
                "description_category"
            ]
            .value_counts()
            .head(10)
        )

        plt.figure(figsize=(12, 6))

        category_counts.plot(
            kind="bar"
        )

        plt.title(
            "Top 10 Food Categories"
        )

        plt.ylabel("Count")

        plt.tight_layout()

        plt.savefig(
            CHARTS_DIR /
            "category_distribution.png"
        )

        plt.close()