import copy
import csv
import datetime
import os
import re
import time
from selenium.webdriver import Chrome, ChromeOptions
import chromedriver_binary

"""
共通変数・定数設定
"""
CSV_HEADER = [
    'skill', 'count', 'avg_price', 'med_price', 'max_price', 'min_price', 'created_at'
]
now = datetime.datetime.today()

"""
 メイン処理
"""
def main() -> None:
    # selenium Chrome設定
    options = ChromeOptions()
    options.add_argument('--headless')
    options.page_load_strategy = 'normal'
    driver = Chrome(options=options)

    # フリーランススタートからスキル別に案件情報CSV作成
    make_freelance_start(driver)

    driver.quit()


"""
 フリーランススタートからスキル別に案件情報CSV作成
"""
def make_freelance_start(driver: Chrome) -> None:
    # スキル一覧を取得
    driver.get('https://freelance-start.com')
    urls = [i.get_attribute('href') for i in driver.find_elements_by_css_selector('.item-skill a')]

    for url in urls:
        # 各スキルページから情報を取得
        time.sleep(1) # クロールするので連続リクエストはしないように紳士的対応
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

        filepath = './data/freelance-start/' + skill.replace(' ', '').replace('/', '／') + '.csv'

        # CSV作成・追加書き込み
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(CSV_HEADER)
        
        with open(filepath, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([skill, count, avg_price, med_price, max_price, min_price, now.strftime("%Y%m%d")])


if __name__ == "__main__":
    main()