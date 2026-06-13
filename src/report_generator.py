from pathlib import Path
import pandas as pd

from src.config import REPORTS_DIR


class ReportGenerator:

    def __init__(self):
        REPORTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    def export_dataframe(
        self,
        df: pd.DataFrame,
        filename: str
    ) -> str:

        filepath = REPORTS_DIR / filename

        df.to_csv(
            filepath,
            index=False
        )

        return str(filepath)

    def generate_summary_report(
        self,
        summary_data: dict,
        output_file: str = "nutrition_summary.txt"
    ) -> str:

        filepath = REPORTS_DIR / output_file

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "=" * 50 + "\n"
            )

            file.write(
                "FOOD INSIGHTS ENGINE REPORT\n"
            )

            file.write(
                "=" * 50 + "\n\n"
            )

            for key, value in summary_data.items():
                file.write(
                    f"{key}: {value}\n"
                )

        return str(filepath)