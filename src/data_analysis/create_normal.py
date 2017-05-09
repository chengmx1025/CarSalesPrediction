import pandas as pd

def main():
    df = pd.read_csv("car_info.csv", encoding='GBK')
    sales = df.loc[:, ['car_id', 'sales']]

    mean = pd.DataFrame(sales.groupby('car_id').sales.mean())
    min = pd.DataFrame(sales.groupby('car_id').sales.min())
    max = pd.DataFrame(sales.groupby('car_id').sales.max())
    mean['car_id'] = mean.index
    min['car_id'] = min.index
    max['car_id'] = max.index
    mean.rename(columns={'sales': 'mean'}, inplace=True)
    min.rename(columns={'sales': 'min'}, inplace=True)
    max.rename(columns={'sales': 'max'}, inplace=True)
    result = pd.merge(mean, min, on='car_id')
    result = pd.merge(result, max, on='car_id')
    result.to_csv('normalize.csv', encoding='GBK')

if __name__ == '__main__':
    main()