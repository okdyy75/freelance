import copy
import csv
import datetime
import os
import re
import time
import threading
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary

"""
共通変数・定数設定
"""
DATA_PATH = 'data'
now = datetime.datetime.today()

"""
 メイン処理
"""
def main() -> None:

    # フリーランススタートからスキル別の案件集計CSV作成
    thread1 = threading.Thread(target=make_freelance_start)

    # レバテックからスキル別の案件集計CSV作成
    thread2 = threading.Thread(target=make_levtech)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print('処理が終了しました')


"""
 フリーランススタートからスキル別の案件集計CSV作成
"""
def make_freelance_start() -> None:

    # selenium Chrome設定
    options = ChromeOptions()
    options.add_argument('--headless')
    options.page_load_strategy = 'normal'
    driver = Chrome(options=options)

    # スキル一覧を取得
    driver.get('https://freelance-start.com')
    urls = [i.get_attribute('href') for i in driver.find_elements_by_css_selector('.item-skill a')]

    for url in urls:
        # 各スキルページから情報を取得
        time.sleep(1)  # クロールするので連続リクエストは控える
        driver.get(url)

        skill = driver.find_element_by_css_selector('#header_search_tag_field .btn-dark-green').text

        text = driver.find_element_by_css_selector('#job-list').text
        match = re.search(r'全(\d+)件', text)
        if match:
            count = match.group(1)
        else:
            count = len(driver.find_elements_by_css_selector('#job-list .ajax-job-link'))

        text = driver.find_element_by_css_selector('#accordionSentenceHeading').text
        text = re.sub(r'\s', '', text)

        avg_price = re.search(r'平均単価([\d\.]+)万円', text).group(1)
        med_price = re.search(r'中央値単価([\d\.]+)万円', text).group(1)
        max_price = re.search(r'最高単価([\d\.]+)万円', text).group(1)
        min_price = re.search(r'最低単価([\d\.]+)万円', text).group(1)

        filepath = DATA_PATH + '/freelance-start/' + skill.replace(' ', '').replace('/', '／') + '.csv'

        # CSV作成・追加書き込み
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'skill', 'count', 'avg_price', 'med_price', 'max_price', 'min_price', 'created_at'
                ])

        with open(filepath, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([skill, count, avg_price, med_price, max_price, min_price, now.strftime("%Y%m%d")])

    driver.quit()


"""
 レバテックからスキル別の案件集計CSV作成
"""
def make_levtech() -> None:

    # selenium Chrome設定
    options = ChromeOptions()
    options.add_argument('--headless')
    options.page_load_strategy = 'normal'
    driver = Chrome(options=options)

    # 検索ページからスキル一覧を取得
    driver.get('https://freelance.levtech.jp/project/search/')

    # 「言語・スキル」フォーム表示
    driver.find_elements_by_css_selector('.conditionGroup__btn')[1].click()

    # 各タブのチェックボックス数取得
    categories = {
        'Language': {
            'idx': 0
        },
        'Framework': {
            'idx': 1
        },
        'DB': {
            'idx': 2
        },
        'OS': {
            'idx': 3
        },
        'Cloud': {
            'idx': 4
        }
    }

    # 左タブの「言語」
    driver.find_elements_by_css_selector('.modalCategory__item')[categories['Language']['idx']].click()
    categories['Language']['count'] = len(driver.find_elements_by_css_selector('.modalCategoryDetail__item'))

    # 左タブの「フレームワーク」
    driver.find_elements_by_css_selector('.modalCategory__item')[categories['Framework']['idx']].click()
    categories['Framework']['count'] = len(driver.find_elements_by_css_selector('.modalCategoryDetail__item'))

    # 左タブの「DB」
    driver.find_elements_by_css_selector('.modalCategory__item')[categories['DB']['idx']].click()
    categories['DB']['count'] = len(driver.find_elements_by_css_selector('.modalCategoryDetail__item'))

    # 左タブの「OS」
    driver.find_elements_by_css_selector('.modalCategory__item')[categories['OS']['idx']].click()
    categories['OS']['count'] = len(driver.find_elements_by_css_selector('.modalCategoryDetail__item'))

    # 左タブの「Cloud」
    driver.find_elements_by_css_selector('.modalCategory__item')[categories['Cloud']['idx']].click()
    categories['Cloud']['count'] = len(driver.find_elements_by_css_selector('.modalCategoryDetail__item'))

    for category_key, category in categories.items():
        for i in range(category['count'] - 1):
            # 検索ページ表示
            time.sleep(1)  # クロールするので連続リクエストは控える
            driver.get('https://freelance.levtech.jp/project/search/')

            # 「言語・スキル」フォーム表示
            driver.find_elements_by_css_selector('.conditionGroup__btn')[1].click()

            # 左タブの「言語」
            driver.find_elements_by_css_selector('.modalCategory__item')[category['idx']].click()

            # 「言語」選択
            driver.find_elements_by_css_selector('.modalCategoryDetail__item')[i].click()

            # 検索ボタン押下
            time.sleep(1)  # クロールするので連続リクエストは控える
            current_url = driver.current_url
            driver.find_elements_by_css_selector('#activeCount')[3].submit()
            WebDriverWait(driver, 10).until(EC.url_changes(current_url))

            skill = re.search(r'(.*)の絞り込み検索', driver.title).group(1)

            text = driver.find_element_by_css_selector('.searchResult__txt').text
            count = re.search(r'(\d+)件', text).group(1)

            text = driver.find_element_by_css_selector('.projectChartInfo').text
            text = re.sub(r'\s', '', text)

            avg_price = re.search(r'平均単価(\d+)万円', text).group(1)
            max_price = re.search(r'最高単価(\d+)万円', text).group(1)
            min_price = re.search(r'最低単価(\d+)万円', text).group(1)

            filepath = DATA_PATH + '/levtech/' + category_key + '/' + skill.replace(' ', '').replace('/', '／') + '.csv'

            # CSV作成・追加書き込み
            if not os.path.exists(filepath):
                with open(filepath, 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        'skill', 'count', 'avg_price', 'max_price', 'min_price', 'created_at'
                    ])

            with open(filepath, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([skill, count, avg_price, max_price, min_price, now.strftime("%Y%m%d")])

    driver.quit()


if __name__ == "__main__":
    main()
