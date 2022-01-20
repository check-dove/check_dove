from HTMLTestRunner import HTMLTestRunner
import unittest

directory = r'../unit_unittest_exer'


def createsuite():
    # 创建unittest实例
    test_suit = unittest.TestSuite()
    # 从文件夹目录中查找需要执行的测试用例
    discover = unittest.defaultTestLoader.discover(
        directory, pattern='book_exer.py', top_level_dir=None)

    # 计数器
    count = 0
    for i in discover:
        count += 1
        print("已发现{}个测试实例需要执行".format(count))
        for j in i:
            # 添加测试单元
            print(j)
            test_suit.addTests(j)
    return test_suit


def main():
    # 输出HTML文件位置
    filename = ".\\result.html"
    with open(filename, 'wb+') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f, title='测试报告', description='实际执行情况：')
        runner.run(createsuite())

    f.close()


if __name__ == '__main__':
    main()
