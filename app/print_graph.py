import pandas as pd
import matplotlib.pyplot as plt

"""
 メイン処理
"""
def main() -> None:
    df = pd.read_csv('../data/freelance-start/all.csv')
    df = df.sort_values(by=['avg_price'], ascending=False)
    print(df)
    plt.bar(df['skill'], df['avg_price'])
    plt.xticks(rotation=90)
    plt.show()


if __name__ == "__main__":
    main()
