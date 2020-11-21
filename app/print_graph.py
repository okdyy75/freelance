import datetime
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
共通変数・定数設定
"""
DATA_PATH = 'data'
now = datetime.datetime.today()
CATEGORIES = {
    'Language',
    'FrameWork',
    'DB',
    'OS',
    'Cloud'
}

"""
 メイン処理
"""
def main() -> None:

    make_date = now.strftime("%Y%m%d")

    # ディレクトリ作成
    os.makedirs(DATA_PATH + '/graphs/' + make_date, exist_ok=True)

    price_graph(make_date)
    count_graph(make_date)
    mix_graph(make_date)


"""
 単価グラフ作成
"""
def price_graph(make_date: str) -> None:

    for category_key in CATEGORIES:
        df = pd.read_csv(DATA_PATH + '/levtech/' + category_key + '.csv')
        df = df.sort_values(by=['avg_price'], ascending=False)
        labels = df['skill'].str.replace('[ぁ-んァ-ン一-龥]+', '', regex=True)  # 日本語削除
        y_list1 = df['avg_price']

        fig = plt.figure(figsize=(14, 7))

        ax1 = fig.add_subplot(1, 1, 1)
        ax1.bar(labels, y_list1, color='tab:blue')
        ax1.set_ylabel('price')
        ax1.set_title(category_key)

        # X軸を縦書き表示
        ax1.set_xticklabels(labels, rotation=90)

        # 棒グラフに数値追記
        for x, y in zip(labels, y_list1):
            ax1.text(x, y, y, ha='center', va='bottom')

        # plt.show()
        fig.savefig(DATA_PATH + '/graphs/' + make_date + '/levtech-' + category_key + '-price.png', bbox_inches='tight', format='png', dpi=300)


"""
 案件数グラフ作成
"""
def count_graph(make_date: str) -> None:

    for category_key in CATEGORIES:
        df = pd.read_csv(DATA_PATH + '/levtech/' + category_key + '.csv')
        df = df.sort_values(by=['count'], ascending=False)
        labels = df['skill'].str.replace('[ぁ-んァ-ン一-龥]+', '', regex=True)  # 日本語削除
        y_list1 = df['count']

        fig = plt.figure(figsize=(14, 7))

        ax1 = fig.add_subplot(1, 1, 1)
        ax1.bar(labels, y_list1, color='tab:orange')
        ax1.set_ylabel('count')
        ax1.set_title(category_key)

        # X軸を縦書き表示
        ax1.set_xticklabels(labels, rotation=90)

        # 棒グラフに数値追記
        for x, y in zip(labels, y_list1):
            ax1.text(x, y, y, ha='center', va='bottom', fontsize='small')

        # plt.show()
        fig.savefig(DATA_PATH + '/graphs/' + make_date + '/levtech-' + category_key + '-count.png', bbox_inches='tight', format='png', dpi=300)


"""
 単価＆案件数グラフ作成
"""
def mix_graph(make_date: str) -> None:

    for category_key in CATEGORIES:
        df = pd.read_csv(DATA_PATH + '/levtech/' + category_key + '.csv')
        df = df.sort_values(by=['avg_price'], ascending=False)

        labels = df['skill'].str.replace('[ぁ-んァ-ン一-龥]+', '', regex=True)  # 日本語削除
        y_list1 = df['avg_price']
        y_list2 = df['count']

        fig = plt.figure(figsize=(14, 7))

        left = np.arange(len(labels))
        width = 0.3

        ax1 = fig.add_subplot(1, 1, 1)
        ax1.bar(labels, y_list1, width=width, color='tab:blue', label='price')
        ax1.set_ylabel('price')
        ax1.set_title(category_key)

        ax2 = ax1.twinx()
        ax2.bar(left + width, y_list2, width=width, color='tab:orange', label='count')
        ax2.set_ylabel('count')

        # X軸を縦書き表示
        ax1.set_xticklabels(labels, rotation=90)

        # 棒グラフに数値追記
        for x, y in zip(labels, y_list1):
            ax1.text(x, y, y, ha='center', va='bottom')

        for x, y in zip(left + width, y_list2):
            ax2.text(x, y, y, ha='center', va='bottom', fontsize='small')

        # 凡例を出力
        handler1, label1 = ax1.get_legend_handles_labels()
        handler2, label2 = ax2.get_legend_handles_labels()
        ax1.legend(handler1 + handler2, label1 + label2)

        # plt.show()
        fig.savefig(DATA_PATH + '/graphs/' + make_date + '/levtech-' + category_key + '-mix.png', bbox_inches='tight', format='png', dpi=300)


if __name__ == '__main__':
    main()
