import csv
import datetime
import glob
import os
import pandas as pd

"""
 メイン処理
"""
def main() -> None:

    files = glob.glob('data/freelance-start/*.csv')

    list = []
    for file in files:
        if 'all.csv' in file:
            continue 
        
        df = pd.read_csv(file, index_col='created_at')
        list.append(df.loc[[20201119]])

    df = pd.concat(list, sort=False)
    df.to_csv('data/freelance-start/all.csv')


if __name__ == "__main__":
    main()
