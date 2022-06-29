import pandas as pd


def explore_data():
    """ Make some visualizations and collect statistics about data in files """
    train = pd.read_csv('../data/train.csv')
    test = pd.read_csv('../data/test.csv')

    print(f'Размер train таблицы {train.shape}')
    print(f'Размер test таблицы {test.shape}')

    print(f'Количество уникальных скважин в train таблице: {len(train["Номер скважины"].unique())}')
    print(f'Количество уникальных скважин в test таблице: {len(test["Номер скважины"].unique())}')

    wells = list(train["Номер скважины"].unique())
    well_df = train[train["Номер скважины"] == wells[0]]
    print(well_df)
    print(f'Размер таблицы с данными для одной скважины {well_df.shape}')


if __name__ == '__main__':
    explore_data()
