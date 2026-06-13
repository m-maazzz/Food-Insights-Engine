from src.data_loader import DataLoader
from src.cleaner import NutritionCleaner
from src.analyzer import NutritionAnalyzer
from src.report_generator import ReportGenerator
from src.visualizer import NutritionVisualizer

visualizer = NutritionVisualizer()
def main():

    print("Loading data...")

    loader = DataLoader()

    food_df = loader.load_foods()
    food_nutrient_df = loader.load_food_nutrients()

    print("Running data quality checks...")

    cleaner = NutritionCleaner()

    summary = cleaner.get_basic_summary(
        food_df
    )

    print(summary)

    print("Running analytics...")

    analyzer = NutritionAnalyzer()

    top_protein_foods = (
        analyzer.get_top_protein_foods(
            food_df,
            food_nutrient_df
        )
    )

    top_fat_foods = (
        analyzer.get_top_fat_foods(
            food_df,
            food_nutrient_df
        )
    )

    top_calorie_foods = (
        analyzer.get_top_calorie_foods(
            food_df,
            food_nutrient_df
        )
    )

    dataset_summary = (
        analyzer.get_dataset_summary(
            food_df,
            food_nutrient_df
        )
    )

    print("Generating reports...")

    report_generator = ReportGenerator()

    report_generator.export_dataframe(
        top_protein_foods,
        "top_protein_foods.csv"
    )

    report_generator.export_dataframe(
        top_fat_foods,
        "top_fat_foods.csv"
    )

    report_generator.export_dataframe(
        top_calorie_foods,
        "top_calorie_foods.csv"
    )

    report_generator.generate_summary_report(
        dataset_summary
    )
    
    visualizer.plot_top_nutrient_foods(
        top_protein_foods,
        "protein_g",
        "Top Protein Foods",
        "top_protein_foods.png"
    )

    visualizer.plot_top_nutrient_foods(
        top_fat_foods,
        "fat_g",
        "Top Fat Foods",
        "top_fat_foods.png"
    )

    visualizer.plot_top_nutrient_foods(
        top_calorie_foods,
        "calories",
        "Top Calorie Foods",
        "top_calorie_foods.png"
    )

    print("Done!")


if __name__ == "__main__":
    main()