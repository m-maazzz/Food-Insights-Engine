# src/cleaner.py

import pandas as pd


class NutritionCleaner:

    def get_missing_values_report(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        report = pd.DataFrame({
            "column": df.columns,
            "missing_count": df.isnull().sum().values,
            "missing_percentage": (
                df.isnull().mean() * 100
            ).round(2).values
        })

        return report.sort_values(
            by="missing_count",
            ascending=False
        )

    def get_duplicate_count(
        self,
        df: pd.DataFrame
    ) -> int:

        return df.duplicated().sum()

    def remove_duplicates(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        return df.drop_duplicates()

    def get_basic_summary(
        self,
        df: pd.DataFrame
    ) -> dict:

        return {
            "rows": len(df),
            "columns": len(df.columns),
            "duplicates": self.get_duplicate_count(df),
            "missing_cells": int(
                df.isnull().sum().sum()
            )
        }