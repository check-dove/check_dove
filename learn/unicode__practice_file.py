def jka():
    CODEC = "UTF-8"
    FILE = 'unicode.txt'

    hello_out = u'hello world\n'
    bytes_out = hello_out.encode(CODEC)
    f = open(FILE, mode='w+b')
    f.write(bytes_out)
    f.close()

    f = open(FILE, 'r+b')
    bytes_in = f.read()
    f.close()
    hello_in = bytes_in.decode(CODEC)
    print(hello_in,)


if __name__ == '__main__':
    jka()