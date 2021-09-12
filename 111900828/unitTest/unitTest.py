import unittest
import re

import main
from main import Filter
from main import Word

file_words = "./unitTest/words.txt"

global map_cnt

class MyTestCase(unittest.TestCase):
    def test_filter_line_1(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "你好世界"
        ans_set = {0}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_2(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "nihao世界"
        ans_set = {0}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_3(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "泥濠世界"
        ans_set = {0}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_4(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "泥  h&*%^&世界he^&l^(&lo"
        ans_set = {0, 11}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_5(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "nhhello"
        ans_set = {0, 2}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_6(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "亻尔濠,hELlO,世界"
        ans_set = {0, 4}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_7(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "亻 尔 濠 , h E L l O , 世 界 ，亻 尔 女 子"
        ans_set = {0, 8, 25}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_8(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "サ・ワールド 時間よ止まれ！"
        ans_set = {7}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_9(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "你女子世界"
        ans_set = {0}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_10(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = ""
        ans_set = set()

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_confuse_1(self):
        s = "你好"
        w = Word(s)

        ans = [
            ['ni', 'hao'],
            ['n', 'i', 'hao'],
            ['n', 'hao'],
            ['ni', 'h', 'a', 'o'],
            ['n', 'i', 'h', 'a', 'o'],
            ['n', 'h', 'a', 'o'],
            ['ni', 'h'],
            ['n', 'i', 'h'],
            ['n', 'h'],
            ['亻', '尔', '女', '子'],
            ['亻', '尔', 'hao'],
            ['亻', '尔', 'h', 'a', 'o'],
            ['亻', '尔', 'h'],
            ['ni', '女', '子'],
            ['n', 'i', '女', '子'],
            ['n', '女', '子']
        ]

        result = w.confuse()

        flag = True
        for i in ans:
            if i not in result:
                flag = False
                break

        self.assertEqual(flag, True)

    def test_confuse_2(self):
        s = "人类"
        w = Word(s)

        ans = [
            ['ren', 'lei'],
            ['r', 'e', 'n', 'lei'],
            ['r', 'lei'],
            ['ren', 'l', 'e', 'i'],
            ['r', 'e', 'n', 'l', 'e', 'i'],
            ['r', 'l', 'e', 'i'],
            ['ren', 'l'],
            ['r', 'e', 'n', 'l'],
            ['r', 'l']
        ]

        result = w.confuse()

        flag = True
        for i in ans:
            if i not in result:
                flag = False
                break

        self.assertEqual(flag, True)

    def test_file_read(self):
        main.clear_status()
        main.init_pinyin_alpha_map()
        f = Filter()

        try:
            f.read_sensitive_words("./nofile.txt")
        except IOError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
