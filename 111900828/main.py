import sys

##################################################
#              variable definition               #
##################################################
"""list and map
    @brief: map pinyin syllable or letter to specified number
"""
PINYIN_LIST = [
    'ba', 'bo', 'bai', 'bei', 'bao', 'ban', 'ben', 'bang', 'beng', 'bi', 'bie', 'biao',
    'bian', 'bin', 'bing', 'pa', 'po', 'pai', 'pao', 'pou', 'pan', 'pen', 'pang', 'peng',
    'pi', 'pie', 'piao', 'pian', 'pin', 'ping', 'ma', 'mo', 'me', 'mai', 'mao', 'mou',
    'man', 'men', 'mang', 'meng', 'mi', 'mie', 'miao', 'miu', 'mian', 'min', 'ming', 'fa',
    'fo', 'fei', 'fou', 'fan', 'fen', 'fang', 'feng', 'da', 'de', 'dai', 'dei', 'dao',
    'dou', 'dan', 'dang', 'deng', 'di', 'die', 'diao', 'diu', 'dian', 'ding', 'ta', 'te',
    'tai', 'tao', 'tou', 'tan', 'tang', 'teng', 'ti', 'tie', 'tiao', 'tian', 'ting', 'na',
    'nai', 'nei', 'nao', 'no', 'nen', 'nang', 'neng', 'ni', 'nie', 'niao', 'niu', 'nian',
    'nin', 'niang', 'ning', 'la', 'le', 'lai', 'lei', 'lao', 'lou', 'lan', 'lang', 'leng',
    'li', 'lia', 'lie', 'liao', 'liu', 'lian', 'lin', 'liang', 'ling', 'ga', 'ge', 'gai',
    'gei', 'gao', 'gou', 'gan', 'gen', 'gang', 'geng', 'ka', 'ke', 'kai', 'kou', 'kan',
    'ken', 'kang', 'keng', 'ha', 'he', 'hai', 'hei', 'hao', 'hou', 'hen', 'hang', 'heng',
    'ji', 'jia', 'jie', 'jiao', 'jiu', 'jian', 'jin', 'jiang', 'jing', 'qi', 'qia',
    'qie', 'qiao', 'qiu', 'qian', 'qin', 'qiang', 'qing', 'xi', 'xia', 'xie', 'xiao', 'xiu',
    'xian', 'xin', 'xiang', 'xing', 'zha', 'zhe', 'zhi', 'zhai', 'zhao', 'zhou', 'zhan', 'zhen',
    'zhang', 'zheng', 'cha', 'che', 'chi', 'chai', 'chou', 'chan', 'chen', 'chang', 'cheng', 'sha',
    'she', 'shi', 'shai', 'shao', 'shou', 'shan', 'shen', 'shang', 'sheng', 're', 'ri', 'rao',
    'rou', 'ran', 'ren', 'rang', 'reng', 'za', 'ze', 'zi', 'zai', 'zao', 'zou', 'zang',
    'zeng', 'ca', 'ce', 'ci', 'cai', 'cao', 'cou', 'can', 'cen', 'cang', 'ceng', 'sa',
    'se', 'si', 'sai', 'sao', 'sou', 'san', 'sen', 'sang', 'seng', 'ya', 'yao', 'you',
    'yan', 'yang', 'yu', 'ye', 'yue', 'yuan', 'yi', 'yin', 'yun', 'ying', 'wa', 'wo',
    'wai', 'wei', 'wan', 'wen', 'wang', 'weng', 'wu', 'a', 'ai', 'an', 'ang', 'ao',
    'o', 'ou', 'e', 'ei',
]
ALPHABET_LIST = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]

PINYIN_CNT = len(PINYIN_LIST)
ALPHABET_CNT = len(ALPHABET_LIST)

pinyin_alpha_map = {}

"""files
    file_word: sensitive words
    file_org: file to be filtered
    file_output: program output            
"""
file_words = sys.argv[1]
file_org = sys.argv[2]
file_output = sys.argv[3]


##################################################
#                class definition                #
##################################################
class Word:
    def __init__(self, word):
        self.word = word

    def garble_origin(self):
        pass

    def garble_pinyin(self):
        pass

    def garble_split_chinese_character(self):
        pass


class Filter:
    def __init__(self):
        self.line = 1
        self.cur = 1

        # map English words to specified number
        self.english_map = {}

        # Chinese sensitive words
        self.pinyin_word_list = []
        # English sensitive words
        self.en_word_list = []

    def build_sensitive_tree(self, filename):
        with open(file_words) as words:
            line = words.readline()

    def logger(self, function):
        pass

    @logger
    def filter(self):
        pass


##################################################
#              function definition               #
##################################################
def init_pinyin_alpha_map():
    i = 0

    for letter in ALPHABET_LIST:
        pinyin_alpha_map[letter] = i
        i = i + 1

    for pinyin in PINYIN_LIST:
        pinyin_alpha_map[pinyin] = i
        i = i + 1


##################################################
#                   entrance                     #
##################################################
def main():
    init_pinyin_alpha_map()


if __name__ == '__main__':
    main()
