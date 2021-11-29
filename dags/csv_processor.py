import pandas as pd
from dagster import job, op, schedule, repository

EXAMPLE_DATA_PATH = "data/example_numbers.csv"
RESULT_REPORT_DATA_PATH = "data/result_report.csv"

@op
def load_data_to_df():
    raw_df = pd.read_csv(EXAMPLE_DATA_PATH)
    return raw_df 

@op
def calculate_metrics(raw_df):
    raw_df["multiply"] = raw_df["number_1"] * raw_df["number_2"]
    report_df = raw_df.drop(columns=["number_1", "number_2"])
    return report_df
@op
def save_report(report_df):
    report_df.to_csv(RESULT_REPORT_DATA_PATH, encoding="utf-8", index=False)


@op
def display_report_df(context, report_df):
    context.log.info(f"Report df: \n{report_df}")

@job
def csv_processor():
    report_df = calculate_metrics(load_data_to_df())
    save_report(report_df)
    display_report_df(report_df)

@schedule(
    cron_schedule="*/1 * * * *",
    job=csv_processor,
    execution_timezone="utc",
)
def utc_schedule():
    pass

@repository
def csv_processor_repository():
    return [csv_processor, utc_schedule]
