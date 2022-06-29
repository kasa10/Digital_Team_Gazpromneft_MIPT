import pandas as pd
import numpy as np

from fedot.api.main import Fedot
from fedot.core.repository.tasks import TsForecastingParams
from tqdm import tqdm

FORECAST_HORIZON = 90


def make_fit_predict(historical_values: pd.DataFrame,
                     forecast_horizon: int = FORECAST_HORIZON):
    """
    Используется одномерный временной ряд для обучения FEDOT модели
    Затем используется временной ряд как предыстория для формирования прогноза
    в будущее
    """
    time_series = np.array(historical_values["Дебит нефти"])

    model = Fedot(problem='ts_forecasting',
                  task_params=TsForecastingParams(forecast_length=forecast_horizon),
                  timeout=0.5, preset='fast_train', n_jobs=-1)

    # run AutoML model design in the same way
    pipeline = model.fit(features=time_series, target=time_series,
                         predefined_model='auto')
    forecast = model.predict(time_series)

    # Generate pipeline with datetime and predicted column
    date_range = pd.date_range(start='1992-04-11', freq='1D', periods=FORECAST_HORIZON)
    forecast_df = pd.DataFrame({'datetime': date_range, 'forecast': forecast})
    return forecast_df


def launch_baseline():
    train_df = pd.read_csv('../data/train.csv')
    wells = list(train_df["Номер скважины"].unique())

    all_forecasts = []
    with tqdm(total=len(wells)) as pbar:
        for well in wells:
            well_df = train_df[train_df["Номер скважины"] == well]

            # Make predictions with FEDOT framework
            forecats_df = make_fit_predict(well_df)
            forecats_df["Номер скважины"] = [well] * len(forecats_df)
            all_forecasts.append(forecats_df)

            pbar.update(1)

    all_forecasts = pd.concat(all_forecasts)
    all_forecasts.to_csv('baseline_forecast.csv', index=False)


if __name__ == '__main__':
    launch_baseline()
