import pandas as pd
from pandas.testing import assert_frame_equal
from dags.csv_processor import calculate_metrics

def test_calculate_metrics():
    test_raw_df = pd.DataFrame(
        [
            {"number_1": 1, "number_2": 3,},
            {"number_1": 4.5, "number_2": 2,},
            {"number_1": 6, "number_2": 4,},
        ],
    )
    expected_report_df = pd.DataFrame(
        [
            {"multiply": 3,}, {"multiply": 9.0,},{"multiply": 24,},
        ],
    )
    report_df = calculate_metrics(test_raw_df)

    assert_frame_equal(expected_report_df, report_df)

