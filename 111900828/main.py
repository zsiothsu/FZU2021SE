import sys
import re
import copy

from pypinyin import lazy_pinyin

import hanziBreaker

##################################################
#              variable definition               #
##################################################
"""list and map
    @brief: map pinyin syllable, glyph or letter to specified number
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
pinyin_alpha_map = {}
glyph_code_map = {}

"""map count
    @brief: global counter for map of pinyin, alphabet and glyph code
"""
map_cnt = 0

HANZI_UNICODE_RANGE = u'\u3400-\u4db5\u4e00-\u9fa5'

"""files
    file_word: sensitive words
    file_org: file to be filtered
    file_output: program output            
"""
file_words = sys.argv[1]
file_org = sys.argv[2]
file_output = sys.argv[3]


# for test
# file_words = './example/words.txt'
# file_org = './example/org.txt'
# file_output = './output.txt'


##################################################
#                class definition                #
##################################################
class Word:
    """Word

    Word class, for enumerating various confusing of words

    :attributes:
        original_word[string]: store thr original word
    """

    def __init__(self, word):
        """ create a Word object
        :arg
            word[string]: word to be processed
        """
        self.original_word = word

    def confuse(self):
        """ enumerate various confusing of words

        for chinese, confusing can be: single Chinese character,
        full spelling pinyin, initial pinyin and dismantling of
        Chinese characters
        There is no confusing on English, a word will be processed
        in letter

        :arg
            self.original_word[string]: word to be processed
        :return -> list
            a list of all confusing
            for example, '你好':
                [['ni', 'hao'], ['n', 'i', 'hao'], ['n', 'hao'],
                 ['亻', '尔', 'hao'], ['ni', 'h', 'a', 'o'], ['n', 'i', 'h', 'a', 'o'],
                 ['n', 'h', 'a', 'o'], ['亻', '尔', 'h', 'a', 'o'], ['ni', 'h'],
                 ['n', 'i', 'h'], ['n', 'h'], ['亻', '尔', 'h'],
                 ['ni', '女', '子'], ['n', 'i', '女', '子'], ['n', '女', '子'],
                 ['亻', '尔', '女', '子']]
        """
        global map_cnt

        confuse_enum = []
        word = list(self.original_word)

        # Enumerate possible confusing forms of Chinese characters
        # - Chinese character
        # - pinyin
        # - initials
        for i in range(len(word)):
            c = word[i]

            # if it's a Chinese character
            if (u'\u4e00' <= c <= u'\u9fa5') or (u'\u3400' <= c <= u'\u4db5'):
                li = []

                # pinyin
                pin = lazy_pinyin(c)
                pin = pin[0]
                li.append(pin)
                li.append(list(pin))
                li.append(pin[0])

                # split of Chinese character
                if hanziBreaker.is_breakable(c):
                    hanzi_part = hanziBreaker.get(c)
                    glyph = []
                    for part in hanzi_part:
                        if part not in glyph_code_map:
                            glyph_code_map[part] = map_cnt
                            map_cnt = map_cnt + 1
                        glyph.append(part)
                    li.append(glyph)

                word[i] = li
            else:
                pass

        for c in word:
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


class Filter:
    """ Filter

    Main class of sensitive word detector

    :attributes
        original_sensitive_word_list[list]: list of original sensitive words
        sensitive_word_list[list]: list of sensitive words mapped to specific number
        sensitive_dict[dict]: a Trie, main data structure for scanning sensitive words
        total[int]: counter for words detected
        result[list]: store result
    """

    def __init__(self):
        # sensitive words
        self.original_sensitive_word_list = []
        self.sensitive_word_list = []

        # tree of sensitive words
        self.sensitive_dict = {}

        # output
        self.total = 0
        self.result = []

        # status, private usage
        self.__cline_org = ''
        self.__lineno = 0

    def read_sensitive_words(self, filename):
        """ sensitive words reader

        read sensitive words from given file and put into sensitive_word_list

        :arg
            filename[string]: file name

        :return none

        :exception
            IOError: unable to open the given file
        """
        try:
            with open(filename, 'r+', encoding='utf-8') as words:
                lines = words.readlines()
                # to record the order of sensitive word
                word_count = 0
                for line in lines:
                    line = line.replace('\r', '').replace('\n', '')
                    self.original_sensitive_word_list.append(line)
                    line = line.lower()

                    # Enumerate all possible variants of a word
                    # including latin, pinyin and glyph
                    confuse = Word(line)
                    confused_word_list = confuse.confuse()

                    for confused_word in confused_word_list:
                        word = []
                        # map pinyin and letter to specific number
                        for i in range(len(confused_word)):
                            if confused_word[i] == '':
                                continue
                            if confused_word[i] in pinyin_alpha_map:
                                word.append(pinyin_alpha_map[confused_word[i]])
                            elif confused_word[i] in glyph_code_map:
                                word.append(glyph_code_map[confused_word[i]])

                        self.sensitive_word_list.append((word, word_count))

                    word_count += 1
        except IOError:
            raise IOError("[word reader] Unable to open the word file")

        else:
            self.build_sensitive_word_tree()

    def build_sensitive_word_tree(self):
        """ build words tree

        using a trie tree as main structure storing sensitive words

        :return none
        """
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
        """ logger

        Record results

        :arg
            begin: begin index of the word at original text
            end: end index of the word at original text
            index: the order of word in sensitive words list

        :return none
        """
        if len(self.result) != 0:
            if begin == (self.result[-1])[3] and self.__lineno == (self.result[-1])[0]:
                self.result.pop()
                self.total -= 1
        self.result.append((
            self.__lineno,
            self.original_sensitive_word_list[index],
            self.__cline_org[begin:end],
            begin,
        ))
        self.total += 1

    def output(self, filename):
        """ answer export

        export answer

        :arg
            filename[string]: output file

        :return none
        """
        try:
            with open(filename, 'w+', encoding='utf-8') as ans:
                print("Total: {}".format(self.total), file=ans)

                for i in self.result:
                    print('Line{}: <{}> {}'.format(i[0], i[1], i[2]), file=ans)
        except IOError:
            raise IOError("[answer export] Unable to open ans file")

    def filter_line(self, sentence):
        """ filter a single line

        filter a single line. cannot detect sensitive words in
        two different lines at the same time

        :arg
            sentence[string]: text to be detected

        :return -> set
            the starting index of the answer
        """
        current = self.sensitive_dict
        word_begin_index = 0

        # a set storing answer for unit test
        ans_set = set()

        # fail pointer:
        #   fail_pointer_stack(position, dict of glyph code branch, curren word_begin_index)

        #   When the Chinese character has both pinyin code and glyph code,
        #   pinyin code is preferred for matching.When it cannot be matched,
        #   the fail pointer is used to switch to the branch of glyph code.
        fail_pointer_stack: (int, dict, int) = []

        i = 0

        while i < len(sentence):
            c = sentence[i]

            if c == '*':
                i = i + 1
                continue

            # is a breakable hanzi
            if c in glyph_code_map:
                pinyin_code = pinyin_alpha_map[lazy_pinyin(c)[0]]
                glyph_code = glyph_code_map[c]

                is_pinyin_code_in_current = pinyin_code in current
                is_glyph_code_in_current = glyph_code in current

                # if not matched, try to return dict to root
                if (not is_pinyin_code_in_current) and (not is_glyph_code_in_current):
                    current = self.sensitive_dict
                    word_begin_index = 0

                if is_pinyin_code_in_current:
                    if current == self.sensitive_dict:
                        word_begin_index = i

                    # append fail pointer for glyph code branch
                    if is_glyph_code_in_current:
                        fail_pointer_stack.append((i + 1, current[glyph_code], word_begin_index))

                    current = current[pinyin_code]
                    if current['end']:
                        self.logger(word_begin_index, i + 1, current['word'])
                        ans_set.add(word_begin_index)

                elif is_glyph_code_in_current:
                    if current == self.sensitive_dict:
                        word_begin_index = i

                    current = current[glyph_code]
                    if current['end']:
                        self.logger(word_begin_index, i + 1, current['word'])
                        ans_set.add(word_begin_index)

                # failed to match
                else:
                    # switch to last glyph code branch
                    if len(fail_pointer_stack) != 0:
                        i = fail_pointer_stack[-1][0]
                        current = fail_pointer_stack[-1][1]
                        word_begin_index = fail_pointer_stack[-1][2]
                        fail_pointer_stack.pop()
                        continue
                    else:
                        current = self.sensitive_dict
                        word_begin_index = 0

            # is a unbreakable hanzi or a latin letter
            else:
                pinyin_code = pinyin_alpha_map[lazy_pinyin(c)[0]]
                if pinyin_code not in current:
                    current = self.sensitive_dict
                    word_begin_index = 0

                if pinyin_code in current:
                    if current == self.sensitive_dict:
                        word_begin_index = i

                    current = current[pinyin_code]
                    if current['end']:
                        self.logger(word_begin_index, i + 1, current['word'])
                        ans_set.add(word_begin_index)
                    i = i + 1
                    continue

                # switch to last glyph code branch
                if len(fail_pointer_stack) != 0:
                    i = (fail_pointer_stack[-1])[0]
                    current = (fail_pointer_stack[-1])[1]
                    word_begin_index = fail_pointer_stack[-1][2]
                    fail_pointer_stack.pop()
                else:
                    current = self.sensitive_dict
                    word_begin_index = 0

            i += 1

        return ans_set

    def filter(self, filename):
        try:
            with open(filename, 'r+', encoding='utf-8') as org:
                lines = org.readlines()
                for line in lines:
                    self.__cline_org = line
                    cline = line.replace('\r', '').replace('\n', '')
                    self.__lineno += 1

                    # Reserve hanzi and letter only
                    cline = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', cline)
                    cline = cline.lower()

                    self.filter_line(cline)
        except IOError:
            raise IOError("[filter] Unable to open the file to be detected")


##################################################
#              function definition               #
##################################################
def init_pinyin_alpha_map():
    """ initialize map

    map pinyin and alphabet to specific number
    
    :return none
    """
    global map_cnt

    # Placeholder
    pinyin_alpha_map['*'] = 0

    map_cnt = 1

    for letter in ALPHABET_LIST:
        pinyin_alpha_map[letter] = map_cnt
        map_cnt += 1

    for pinyin in PINYIN_LIST:
        pinyin_alpha_map[pinyin] = map_cnt
        map_cnt += 1


def clear_status():
    global map_cnt
    global pinyin_alpha_map
    global glyph_code_map

    map_cnt = 0
    pinyin_alpha_map.clear()
    glyph_code_map.clear()


##################################################
#                   entrance                     #
##################################################
def main():
    init_pinyin_alpha_map()

    f = Filter()
    f.read_sensitive_words(file_words)
    f.filter(file_org)
    f.output(file_output)


if __name__ == '__main__':
    main()
