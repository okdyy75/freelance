import pandas as pd
import matplotlib.pyplot as plt

"""
 メイン処理
"""
def main() -> None:
    df = pd.read_csv('data/freelance-start/all.csv')
    df = df.sort_values(by=['avg_price'], ascending=False)
    x_skill = df['skill']
    y_avg_price = df['avg_price']

    plt.figure(figsize=(14, 7))
    plt.bar(x_skill, y_avg_price)

    # 棒グラフ内に数値を書く
    for x, y in zip(x_skill, y_avg_price):
        plt.text(x, y, y, ha='center', va='bottom')

    # X軸を縦書き表示
    plt.xticks(rotation=90)

    plt.show()


if __name__ == "__main__":
    main()
