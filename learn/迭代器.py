class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


if __name__ == '__main__':
    myclass = MyNumbers()
    myiter = iter(myclass)
    for i in range(100):
        print(next(myiter), end=',')
        if i == 49:
            print('')