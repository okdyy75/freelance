import os
import glob
import shutil

def main() -> None:
    """メイン処理
    :rtype: None
    """

    move_freelance_start()

    print('処理が終了しました')


def move_freelance_start() -> None:
    """フリーランススタートのCSVを、カテゴリごとにディレクトリ移動。一時バッチ
    :rtype: None
    """

    categories_skills = {
        'etc': [
            'Abstract',
            'Cisco',
            'CodeDeploy',
            'CodePipeline',
            'SAP',
        ],
        'design': [
            'Adobe XD',
            'After Effects',
            'Illustrator',
            'Maya',
            'Photoshop',
        ],
        'Infrastructure': [
            'AWS',
            'Azure',
            'Fargate',
            'Google Cloud Platform',
            'Kubernetes',
            'Linux',
            'Oracle',
            'UNIX',
            'WindowsServer',
        ],
        'Framework': [
            'AngularJS',
            'Backbone.js',
            'CakePHP',
            'Catalyst',
            'CodeIgniter',
            'Django',
            'Ember.js',
            'Ethna',
            'Flask',
            'Flutter',
            'FuelPHP',
            'Knockout.js',
            'Laravel',
            'Node.js',
            'NuxtJS',
            'Phalcon',
            'Pyramid',
            'React',
            'ReactNative',
            'RSpec',
            'Ruby on Rails',
            'SAStruts',
            'Seasar2',
            'Slim',
            'Spark',
            'Spring',
            'SpringBoot',
            'Struts',
            'Symfony',
            'Tornado',
            'Vue.js',
            'Yii',
            'Zend Framework',
        ],
        'Language': [
            'Apex',
            'ASP.NET',
            'C#.NET',
            'C#',
            'C++',
            'COBOL',
            'Cocos2d-x',
            'C言語',
            'Go言語',
            'HTML5',
            'Java',
            'JavaScript',
            'Kotlin',
            'Objective-C',
            'Perl',
            'PHP',
            'PL/SQL',
            'Python',
            'Ruby',
            'R言語',
            'Scala',
            'SQL',
            'Swift',
            'TypeScript',
            'Unity',
            'VB.NET',
            'VB',
            'VBA',
            'VC++',
            'Vuex',
        ]
    }

    files = glob.glob('./data/freelance-start/*.csv')

    for filepath in files:
        dirname, filename = os.path.split(filepath)
        skill, ext = os.path.splitext(filename)

        category = ''
        for key, val in categories_skills.items():
            val2 = map(lambda v: v.replace(' ', '').replace('/', '／'), val)
            if skill in val2:
                category = key
                break

        # ファイル移動
        shutil.move(filepath, dirname + '/' + category + '/' + filename)


if __name__ == "__main__":
    main()
