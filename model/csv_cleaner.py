import pandas as pd


def replace_hiány_with_mean(file_path: object) -> object:
    df = pd.read_csv(file_path)
    df.replace("hiány", pd.NA, inplace=True)
    df = df.apply(pd.to_numeric, errors='ignore')
    df.fillna(df.mean(), inplace=True)

    return df
