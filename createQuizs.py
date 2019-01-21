import random
'''
随机生成测试题，考察对省份和省会的认识。
练习文件的读取与写入。
'''


# 测试数据，键是省份，值是省会
capitals = {'北京市': '北京',
            '上海市': '上海',
            '天津市': '天津',
            '重庆市': '重庆',
            '黑龙江省': '哈尔滨',
            '吉林省': '长春',
            '辽宁省': '沈阳',
            '河北省': '石家庄',
            '河南省': '郑州',
            '山东省': '济南',
            '江苏省': '南京',
            '安徽省': '合肥',
            '浙江省': '杭州',
            '湖北省': '武汉',
            '福建省': '福州',
            '江西省': '南昌',
            '湖南省': '长沙',
            '广东省': '广州',
            '广西壮族自治区': '南宁',
            '台湾省': '台北',
            '贵州省': '贵阳',
            '四川省': '成都',
            '陕西省': '西安',
            '山西省': '太原',
            '甘肃省': '兰州',
            '云南省': '昆明',
            '宁夏回族自治区': '银川',
            '新疆维吾尔自治区': '乌鲁木齐',
            '西藏自治区': '拉萨',
            '青海省': '西宁',
            '内蒙古自治区': '呼和浩特',
            '海南省': '海口',
            '香港特别行政区': '香港',
            '澳门特别行政区': '澳门',
            }

# 创建 n 份试卷
n = 2
for quizNum in range(n):
    # 分别创建试卷和答案文档
    quizFile = open('省会测试{}.doc'.format(quizNum + 1), 'w', encoding="utf-8")
    answerKeyFile = open('省会测试_答案{}.doc'.format(quizNum + 1), 'w', encoding="utf-8")

    # 写入试卷头
    quizFile.write('姓名：\n日期：\n')
    quizFile.write(' '*20 + '省会测试试卷（{}）\n\n'.format(quizNum + 1))

    # 随机生成省会列表
    province = list(capitals.keys())
    random.shuffle(province)

    # 遍历 33 个省会，每个出 1 道测试题，答案有 4 个选项，包括 1 个正确答案和 3 个错误答案
    for questionNum in range(33):
        correctAnswer = capitals[province[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # 将题目写入试卷文档
        quizFile.write('{}. {}的省会是？\n'.format((questionNum + 1), province[questionNum]))
        for i in range(4):
            quizFile.write('{}. {}\n'.format('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # 将正确答案写入答案文档
        answerKeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
