import datetime
import glob
import pandas as pd

"""
共通変数・定数設定
"""
DATA_PATH = 'data'
CATEGORIES = {
    'Language',
    'Framework',
    'DB',
    'OS',
    'Cloud'
}
now = datetime.datetime.today()

"""
 メイン処理
"""
def main() -> None:

    filter_date = now.strftime("%Y%m%d")

    """ レバテック """
    # スキル別案件集計CSVをマージする(カテゴリ別)
    for category_key in CATEGORIES:
        files = glob.glob(DATA_PATH + '/levtech/' + category_key + '/*.csv')
        putfile = category_key + '.csv'
        list = []
        for file in files:
            if putfile in file:
                continue

            df = pd.read_csv(file, index_col='created_at')
            list.append(df.loc[[int(filter_date)]])

        df = pd.concat(list, sort=False)
        df.to_csv(DATA_PATH + '/levtech/' + putfile)

    # スキル別案件集計CSVをマージする(全体)
    files = glob.glob(DATA_PATH + '/levtech/*.csv')
    putfile = 'levtech.csv'
    list = []
    for file in files:
        if putfile in file:
            continue

        df = pd.read_csv(file, index_col='created_at')
        list.append(df.loc[[int(filter_date)]])

    df = pd.concat(list, sort=False)
    df.to_csv(DATA_PATH + '/' + putfile)

    """ フリーランススタート """
    # スキル別案件集計CSVをマージする(全体)
    files = glob.glob(DATA_PATH + '/freelance-start/*.csv')
    putfile = 'freelance-start.csv'
    list = []
    for file in files:
        if putfile in file:
            continue

        df = pd.read_csv(file, index_col='created_at')
        list.append(df.loc[[int(filter_date)]])

    df = pd.concat(list, sort=False)
    df.to_csv(DATA_PATH + '/' + putfile)


if __name__ == "__main__":
    main()
