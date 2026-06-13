import pandas as pd

from src.config import (
    PROTEIN_ID,
    FAT_ID,
    CARB_ID,
    ENERGY_ID
)


class NutritionAnalyzer:

    def get_top_foods_by_nutrient(
        self,
        food_df: pd.DataFrame,
        food_nutrient_df: pd.DataFrame,
        nutrient_id: int,
        nutrient_name: str,
        top_n: int = 20
    ) -> pd.DataFrame:

        nutrient_df = food_nutrient_df[
            food_nutrient_df["nutrient_id"] == nutrient_id
        ]

        result = nutrient_df.merge(
            food_df,
            on="fdc_id",
            how="left"
        )

        result = result[
            [
                "fdc_id",
                "description",
                "amount"
            ]
        ]

        result = result.rename(
            columns={
                "amount": nutrient_name
            }
        )

        return result.sort_values(
            by=nutrient_name,
            ascending=False
        ).head(top_n)

    def get_top_protein_foods(
        self,
        food_df: pd.DataFrame,
        food_nutrient_df: pd.DataFrame,
        top_n: int = 20
    ) -> pd.DataFrame:

        return self.get_top_foods_by_nutrient(
            food_df=food_df,
            food_nutrient_df=food_nutrient_df,
            nutrient_id=PROTEIN_ID,
            nutrient_name="protein_g",
            top_n=top_n
        )

    def get_top_fat_foods(
        self,
        food_df: pd.DataFrame,
        food_nutrient_df: pd.DataFrame,
        top_n: int = 20
    ) -> pd.DataFrame:

        return self.get_top_foods_by_nutrient(
            food_df=food_df,
            food_nutrient_df=food_nutrient_df,
            nutrient_id=FAT_ID,
            nutrient_name="fat_g",
            top_n=top_n
        )

    def get_top_calorie_foods(
        self,
        food_df: pd.DataFrame,
        food_nutrient_df: pd.DataFrame,
        top_n: int = 20
    ) -> pd.DataFrame:

        return self.get_top_foods_by_nutrient(
            food_df=food_df,
            food_nutrient_df=food_nutrient_df,
            nutrient_id=ENERGY_ID,
            nutrient_name="calories",
            top_n=top_n
        )

    def get_top_carb_foods(
        self,
        food_df: pd.DataFrame,
        food_nutrient_df: pd.DataFrame,
        top_n: int = 20
    ) -> pd.DataFrame:

        return self.get_top_foods_by_nutrient(
            food_df=food_df,
            food_nutrient_df=food_nutrient_df,
            nutrient_id=CARB_ID,
            nutrient_name="carbs_g",
            top_n=top_n
        )

    def get_dataset_summary(
        self,
        food_df: pd.DataFrame,
        food_nutrient_df: pd.DataFrame
    ) -> dict:

        return {
            "total_foods": len(food_df),
            "total_nutrient_records": len(food_nutrient_df),
            "unique_foods_with_nutrients":
                food_nutrient_df["fdc_id"].nunique(),
            "unique_nutrients":
                food_nutrient_df["nutrient_id"].nunique()
        }