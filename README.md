# freelance
フリーランス案件集計バッチ＆web  
https://okdyy75.github.io/freelance-chart/  

1. GitHub Actionsで月数回バッチを定期実行
2. 各サイトから案件情報を収集しCSV作成
3. CSVを元にGatsbyでビルド。web表示
4. GitHub Pagesにwebデプロイ

```
# 各サイトから集計＆CSV作成
pipenv run make_csv

## web
cd ./frontend

# ローカルでweb表示
gatsby develop

# デプロイ
npm run deploy

```

## 使用言語・ツール
- Python v3.9
- Gatsby v2.26
- React v16.12
- TypeScript v4.1
- Theme UI v0.3

## フリーランス案件サイト

レバテックフリーランス  
https://freelance.levtech.jp

フリーランススタート  
https://freelance-start.com

## ディレクトリ構成
```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── app ...pythonソース
├── data ...データ置き場
│   ├── freelance-start ...フリーランススタートのCSV置き場
│   └── levtech ...レバテックのCSV置き場
├── frontend ...web本体
│   ├── gatsby-config.js ...gatsby設定
│   ├── gatsby-node.js ...動的ルーティング
│   └── src
│       ├── components ...コンポーネント置き場
│       ├── gatsby-plugin-theme-ui ...Theme UIのスタイル設定
│       ├── images ...画像置き場
│       ├── layouts ...ページのベースレイアウト
│       ├── pages ...ページ本体
│       ├── styles ...cssスタイル置き場
│       └── templates ...動的ページ置き場
└── requirements.txt
```

## Gatsbyメモ
- GatsbyのGrapqlはリアルタイムで取得できないので、一度全部取得してから各ページで必要なデータをフィルタリングしていくという思考が必要
- 画像ファイルもgraphqlで直接指定して取得する必要あり


## Pipfileアップデート
1. pypiでパッケージのバージョンを確認する（https://pypi.org/）
2. Pipfileを更新
3. `pipenv install`
4. `pipenv lock --requirements > requirements.txt`
