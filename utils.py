import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

from sklearn.metrics import mean_squared_error
from tqdm import tqdm


def get_project_path() -> str:
    return Path(__file__).parent


def calculate_final_score(path_to_csv_file: str, vis: bool = False):
    """ Расчет метрики по таблице с предсказаниями алгоритма """
    df_with_metrics = pd.read_csv(path_to_csv_file, parse_dates=['datetime'])
    wells = list(df_with_metrics["Номер скважины"].unique())

    train_df = pd.read_csv(os.path.join(get_project_path(), 'data', 'train.csv'), parse_dates=['datetime'])
    test_df = pd.read_csv(os.path.join(get_project_path(), 'data', 'test.csv'), parse_dates=['datetime'])
    metrics = []
    with tqdm(total=len(wells)) as pbar:
        for well in wells:
            well_forecast_df = df_with_metrics[df_with_metrics["Номер скважины"] == well]
            well_forecast_df = well_forecast_df.sort_values(by='datetime')

            well_actual_df = test_df[test_df["Номер скважины"] == well]
            well_actual_df = well_actual_df.sort_values(by='datetime')

            rmse_metric = mean_squared_error(np.array(well_actual_df['Дебит нефти']),
                                             np.array(well_forecast_df['forecast']),
                                             squared=False)
            metrics.append(rmse_metric)

            if vis:
                # Create plot
                historical_df = train_df[train_df["Номер скважины"] == well]

                plt.plot(historical_df['datetime'], historical_df['Дебит нефти'], label='Train')
                plt.plot(well_actual_df['datetime'], well_actual_df['Дебит нефти'], label='Test')
                plt.plot(well_forecast_df['datetime'], well_forecast_df['forecast'], label='Forecast')
                plt.grid()
                plt.legend()
                plt.xlabel('Дата')
                plt.ylabel('Дебит нефти')
                plt.show()
            pbar.update(1)

    metrics = np.array(metrics)
    return np.mean(metrics)


if __name__ == '__main__':
    metric = calculate_final_score(path_to_csv_file='./baseline/baseline_forecast.csv', vis=True)
    print(f'Метрика RMSE {metric:.2f}')
