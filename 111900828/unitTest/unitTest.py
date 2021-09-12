import unittest
import re

import main
from main import Filter

file_words = "./unitTest/words.txt"


class MyTestCase(unittest.TestCase):
    def test_filter_line_1(self):
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
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "The World 時間よ止まれ！"
        ans_set = {10}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_9(self):
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = "サ・ワールド　時間よ止まれ！"
        ans_set = {7}

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

    def test_filter_line_10(self):
        main.init_pinyin_alpha_map()
        f = Filter()
        f.read_sensitive_words(file_words)

        org = ""
        ans_set = set()

        org = re.sub(u'([^\u3400-\u4db5\u4e00-\u9fa5a-zA-Z])', '*', org)
        org = org.lower()

        ans = f.filter_line(org)
        self.assertEqual(ans_set, ans)

if __name__ == '__main__':
    unittest.main()
