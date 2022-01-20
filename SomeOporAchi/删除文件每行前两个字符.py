file1 = "../learn/mylog.txt"
file2 = "../learn/a.txt"
num = 2

f1 = open(file1, 'r+b')
f2 = open(file2, 'w+b')
for eachline in f1.readlines():
    f2.write(eachline[num:])
f1.close()
f2.close()


# b = input("jianshe::::::>")
# if b.lstrip()[0:1].lower() == 'r':
#     print("hello!")
# else:
#     print('It\'s bad')