import datetime as dt

import numpy as np
import pandas as pd
import pytest
from pandas._testing import assert_frame_equal

from wetterdienst.provider.noaa.ghcn import NoaaGhcnParameter, NoaaGhcnRequest


@pytest.mark.parametrize(
    "start_date,end_date",
    [
        (dt.datetime(2015, 1, 1), dt.datetime(2022, 1, 1)),
        (dt.datetime(2015, 1, 1, 1), dt.datetime(2022, 1, 1, 1)),
        (dt.datetime(2015, 1, 1, 1, 1), dt.datetime(2022, 1, 1, 1, 1)),
        (dt.datetime(2015, 1, 1, 1, 1, 1), dt.datetime(2022, 1, 1, 1, 1, 1)),
    ],
)
def test_api_amsterdam(start_date, end_date, default_settings):
    request = NoaaGhcnRequest(
        parameter=[NoaaGhcnParameter.DAILY.TEMPERATURE_AIR_MEAN_200],
        start_date=start_date,
        end_date=end_date,
        settings=default_settings,
    ).filter_by_name("DE BILT")
    given_df = request.values.all().df
    given_df_filtered = given_df[given_df["date"] == pd.Timestamp("2021-01-01 23:00:00+00:00")].reset_index(drop=True)
    expected_df = pd.DataFrame(
        {
            "station_id": pd.Categorical(["NLM00006260"]),
            "dataset": pd.Categorical(["daily"]),
            "parameter": pd.Categorical(["temperature_air_mean_200"]),
            "date": [pd.Timestamp("2021-01-01 23:00:00+0000", tz="UTC")],
            "value": [276.84999999999997],
            "quality": [np.nan],
        }
    )
    assert_frame_equal(
        given_df_filtered,
        expected_df,
        check_categorical=False,
    )
