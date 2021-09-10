import sys
import re
from typing import Dict, Any
import copy

from pypinyin import lazy_pinyin

##################################################
#              variable definition               #
##################################################
"""list and map
    @brief: map pinyin syllable or letter to specified number
"""
PINYIN_LIST = [
    'a', 'o', 'e', 'ba', 'bo', 'bi', 'bu', 'pa', 'po', 'pi', 'pu',
    'ma', 'mo', 'me', 'mi', 'mu', 'fa', 'fo', 'fu', 'da', 'de',
    'di', 'du', 'ta', 'te', 'ti', 'tu', 'na', 'ne', 'ni', 'nu',
    'nv', 'la', 'lo', 'le', 'li', 'lu', 'lv', 'ga', 'ge', 'gu',
    'ka', 'ke', 'ku', 'ha', 'he', 'hu', 'ji', 'ju', 'qi', 'qu',
    'xi', 'xu', 'zha', 'zhe', 'zhi', 'zhu', 'cha', 'che', 'chi',
    'chu', 'sha', 'she', 'shi', 'shu', 'ra', 're', 'ri', 'ru',
    'za', 'ze', 'zi', 'zu', 'ca', 'ce', 'ci', 'cu', 'sa', 'se',
    'si', 'su', 'ya', 'yo', 'ye', 'yi', 'yu', 'wa', 'wo', 'wu',
    'ai', 'ei', 'ao', 'ou', 'er', 'bai', 'bei', 'bao', 'bie',
    'pai', 'pei', 'pao', 'pou', 'pie', 'mai', 'mei', 'mao', 'mou',
    'miu', 'mie', 'fei', 'fou', 'dai', 'dei', 'dui', 'dao', 'dou',
    'diu', 'die', 'tai', 'tei', 'tui', 'tao', 'tou', 'tie', 'nai',
    'nei', 'nao', 'nou', 'niu', 'nie', 'lai', 'lei', 'lao', 'lou',
    'liu', 'lie', 'gai', 'gei', 'gui', 'gao', 'gou', 'kai', 'kei',
    'kui', 'kao', 'kou', 'hai', 'hei', 'hui', 'hao', 'hou', 'jiu',
    'jie', 'jue', 'qiu', 'qie', 'que', 'xiu', 'xie', 'xue', 'zhai',
    'zhei', 'zhui', 'zhao', 'zhou', 'chai', 'chui', 'chao', 'chou',
    'shai', 'shei', 'shui', 'shao', 'shou', 'rui', 'rao', 'rou',
    'zai', 'zei', 'zui', 'zao', 'zou', 'cai', 'cei', 'cui', 'cao',
    'cou', 'sai', 'sui', 'sao', 'sou', 'yao', 'you', 'yue', 'wai',
    'wei', 'an', 'en', 'ang', 'eng', 'ban', 'ben', 'bin', 'bang',
    'beng', 'bing', 'pan', 'pen', 'pin', 'pang', 'peng', 'ping',
    'man', 'men', 'min', 'mang', 'meng', 'ming', 'fan', 'fen',
    'fang', 'feng', 'dan', 'den', 'dun', 'dang', 'deng', 'ding',
    'dong', 'tan', 'tun', 'tang', 'teng', 'ting', 'tong', 'nan',
    'nen', 'nin', 'nun', 'nang', 'neng', 'ning', 'nong', 'lan',
    'lin', 'lun', 'lang', 'leng', 'ling', 'long', 'gan', 'gen',
    'gun', 'gang', 'geng', 'gong', 'kan', 'ken', 'kun', 'kang',
    'keng', 'kong', 'han', 'hen', 'hun', 'hang', 'heng', 'hong',
    'jin', 'jun', 'jing', 'qin', 'qun', 'qing', 'xin', 'xun',
    'xing', 'zhan', 'zhen', 'zhun', 'zhang', 'zheng', 'zhong',
    'chan', 'chen', 'chun', 'chang', 'cheng', 'chong', 'shan',
    'shen', 'shun', 'shang', 'sheng', 'ran', 'ren', 'run', 'rang',
    'reng', 'rong', 'zan', 'zen', 'zun', 'zang', 'zeng', 'zong',
    'can', 'cen', 'cun', 'cang', 'ceng', 'cong', 'san', 'sen',
    'sun', 'sang', 'seng', 'song', 'yan', 'yin', 'yun', 'yang',
    'ying', 'yong', 'wan', 'wen', 'wang', 'weng', 'biao', 'bian',
    'piao', 'pian', 'miao', 'mian', 'dia', 'diao', 'dian', 'duo', 'duan',
    'tiao', 'tian', 'tuo', 'tuan', 'niao', 'nian', 'niang', 'nuo',
    'nuan', 'lia', 'liao', 'lian', 'liang', 'luo', 'luan', 'gua',
    'guo', 'guai', 'guan', 'guang', 'kua', 'kuo', 'kuai', 'kuan',
    'kuang', 'hua', 'huo', 'huai', 'huan', 'huang', 'jia', 'jiao',
    'jian', 'jiang', 'jiong', 'juan', 'qia', 'qiao', 'qian',
    'qiang', 'qiong', 'quan', 'xia', 'xiao', 'xian', 'xiang',
    'xiong', 'xuan', 'zhua', 'zhuo', 'zhuai', 'zhuan', 'zhuang',
    'chua', 'chuo', 'chuai', 'chuan', 'chuang', 'shua', 'shuo',
    'shuai', 'shuan', 'shuang', 'rua', 'ruo', 'ruan', 'zuo',
    'zuan', 'cuo', 'cuan', 'suo', 'suan', 'yuan'
]
ALPHABET_LIST = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]
pinyin_alpha_map: dict[Any, Any] = {}

PINYIN_CNT = len(PINYIN_LIST)
ALPHABET_CNT = len(ALPHABET_LIST)

HANZI_UNICODE_RANGE = u'\u3400-\u4db5\u4e00-\u9fa5'

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
        self.original_word = word

    def confuse_pinyin(self):
        confuse_enum = []
        self.word = list(self.original_word)

        # Enumerate possible confusing forms of Chinese characters
        # - Chinese character
        # - pinyin
        # - initials
        for i in range(len(self.word)):
            c = self.word[i]

            # if it's a Chinese character
            if (u'\u4e00' <= c <= u'\u9fa5') or (u'\u3400' <= c <= u'\u4db5'):
                li = []
                pin = lazy_pinyin(c)
                pin = pin[0]
                li.append(pin)
                li.append(list(pin))
                li.append(pin[0])
                self.word[i] = li
            else:
                pass

        for c in self.word:
            # Latin: no confusions
            if not isinstance(c, list):
                if len(confuse_enum) == 0:
                    confuse_enum.append([c])
                else:
                    for li in confuse_enum:
                        li.append(c)
            # Chinese: muti-confusions
            else:
                if len(confuse_enum) == 0:
                    for one_confuse in c:
                        if not isinstance(one_confuse, list):
                            confuse_enum.append([one_confuse])
                        else:
                            confuse_enum.append(one_confuse)
                else:
                    pre = confuse_enum
                    new_confuse_enum = []
                    for one_confuse in c:
                        new_confuse = copy.deepcopy(pre)
                        # print(new_confuse)
                        if not isinstance(one_confuse, list):
                            for existed_confuse in new_confuse:
                                existed_confuse.append(one_confuse)
                        else:
                            for existed_confuse in new_confuse:
                                for x in one_confuse:
                                    existed_confuse.append(x)
                        new_confuse_enum = new_confuse_enum + new_confuse

                    confuse_enum = new_confuse_enum

        return confuse_enum

    def confuse_split_chinese_character(self):
        pass


class Filter:
    def __init__(self):
        self.lineno = 0

        # sensitive words
        self.original_sensitive_word_list = []
        self.sensitive_word_list = []

        # tree of sensitive words
        self.sensitive_dict = {}

        # output
        self.total = 0
        self.result = []

    def read_sensitive_words(self, filename):
        with open(filename) as words:
            lines = words.readlines()
            # to record the order of sensitive word
            word_count = 0
            for line in lines:
                line = line.replace('\r', '').replace('\n', '')
                self.original_sensitive_word_list.append(line)
                line = line.lower()

                # Latinization:
                # convert Chinese characters to full spelling
                # reserve alphabet string

                confuse = Word(line)
                confused_latin_list = confuse.confuse_pinyin()

                for latin in confused_latin_list:
                    word = []
                    # map pinyin and letter to specific number
                    for i in range(len(latin)):
                        if latin[i] == '':
                            continue
                        if latin[i] not in pinyin_alpha_map:
                            for c in latin[i]:
                                word.append(pinyin_alpha_map[c])
                            continue
                        word.append(pinyin_alpha_map[latin[i]])

                    self.sensitive_word_list.append((word, word_count))

                word_count += 1

    def build_sensitive_word_tree(self):
        for index, word_count_tuple in enumerate(self.sensitive_word_list):
            word = word_count_tuple[0]
            current = self.sensitive_dict
            for i, c in enumerate(word):
                if c not in current:
                    child = {'end': False}
                    current[c] = child
                    current = child
                else:
                    child = current[c]
                    current = child
                if i == len(word) - 1:
                    current['end'] = True
                    current['word'] = word_count_tuple[1]

    def logger(self, begin, end, index):
        self.result.append((
            self.lineno,
            self.original_sensitive_word_list[index],
            self.cline_org[begin:end]
        ))
        self.total += 1

    def output(self, filename):
        with open(filename, 'w+') as ans:
            print("Total: {}".format(self.total), file=ans)

            for i in self.result:
                print('Line{}: <{}> {}'.format(i[0], i[1], i[2]), file=ans)

    def filter_line(self, sentence):
        current = self.sensitive_dict

        word_begin_index = 0

        for i, c in enumerate(sentence):
            if c == 0:
                continue
            if c not in current:
                current = self.sensitive_dict
                word_begin_index = 0
            else:
                if current == self.sensitive_dict:
                    word_begin_index = i

                child = current[c]
                current = child

                if current['end']:
                    self.logger(word_begin_index, i + 1, current['word'])

    def filter(self, filename):
        with open(filename) as org:
            lines = org.readlines()
            for line in lines:
                self.cline_org = line
                self.cline = line.replace('\r', '').replace('\n', '')
                self.lineno += 1

                # Reserve hanzi and letter only
                self.cline = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', self.cline)
                self.cline = self.cline.lower()

                # Latinization
                latin = lazy_pinyin(list(self.cline))
                sentence = []
                # map pinyin and letter to specific number
                for i in range(len(latin)):
                    if latin[i] == '':
                        continue
                    if latin[i] not in pinyin_alpha_map:
                        for c in latin[i]:
                            sentence.append(pinyin_alpha_map[c])
                        continue
                    sentence.append(pinyin_alpha_map[latin[i]])

                self.filter_line(sentence)


##################################################
#              function definition               #
##################################################
def init_pinyin_alpha_map():
    # Placeholder
    pinyin_alpha_map['*'] = 0

    i = 1

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
    f = Filter()
    f.read_sensitive_words(file_words)
    f.build_sensitive_word_tree()
    f.filter(file_org)
    f.output(file_output)


if __name__ == '__main__':
    main()
