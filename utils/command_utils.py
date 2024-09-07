import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

# 定义模式
patterns = {
    "停止": "停止|停下来|别动|不要|不",
    "前进": "向前|前进|往前|走前面|前",
    "后退": "向后|后退|往后|走后面|后",
    "向左": "向左|往左|走左边|左",
    "向右": "向右|往右|走右边|右",
    "右转": "转右圈|右转一圈|右旋转|右绕圈|右转",
    "左转": "转左圈|左转一圈|左旋转|左绕圈|左转",
    "坐下": "坐下|坐下来|坐着|坐下去|趴下|坐|趴",
    "站起来": "站起来|起立|站起|站起来|站",
    "伸懒腰": "伸懒腰|伸展|拉伸|舒展|懒"
}

def map_sentence_to_command(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)

    for command, pattern in patterns.items():
        for keyword in pattern.split("|"):
            if keyword in sentence:
                return command

    return "未识别的指令"