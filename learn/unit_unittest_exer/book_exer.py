import unittest


class book(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(r"Dict object has no attribute {}".
                                 format(key))

    def __setattr__(self, key, value):
        self[key] = value

    def get_page(self):
        if self.page <= 60:
            return "短篇"
        elif self.page <= 150:
            return "中篇"
        elif self.page > 150:
            return "长篇"


class book_unittest(unittest.TestCase):

    global x
    x = book(name="ForTragediesOfShakespeare", page=442)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_book_yun(self):
        # 值检查
        self.assertEqual(x.name, 'ForTragediesOfShakespeare')
        self.assertEqual(x.page, 442)
        print('yun')

    def test_book_func(self):
        # 方法、属性检查（）
        x.key1 = 'value1'
        self.assertTrue('key1' in x)
        self.assertEqual(x["key1"], 'value1')
        self.assertEqual(x.key1, x["key1"])
        print("function")

    def test_book_error(self):
        # 异常检测
        with self.assertRaises(KeyError):
            x['jack']

        with self.assertRaises(AttributeError):
            x.jack
        print("error")


if __name__ == '__main__':
    unittest.main()
    # 等价于（注：所有的test都加进去的时候）

    # 创建套件实例
    test_suit = unittest.TestSuite()
    # 为实例套件添加测试用例
    test_suit.addTests(map(book_unittest, ['test_book_yun', 'test_book_func', 'test_book_error']))
    # 执行用例
    # 创建运行器
    test_runner = unittest.TextTestRunner()
    # 调用运行器执行实例套件
    test_runner.run(test_suit)
