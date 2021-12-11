# !/usr/bin/env python
import os


def create_file(fname=None):
    '''makeTextFile.py -- create text file'''
    ls = os.linesep
    # get filename
    while True:
        fname = input('Enter filename: ')
        if os.path.exists(fname):
            print("ERROR: '%s' already exists" % fname)
        else:
            break
    # get file content (text) lines
    all = []
    print("\nEnter lines ('.' by itself to quit).\n")
    # loop until user terminates input
    while True:
        entry = input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)
    # write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print('DONE!')


def read_file():
    '''readTextFile.py -- read and display text file'''
    # get filename
    fname = input('Enter filename: ')
    # attempt to open file for reading
    # try:
    #     fobj = open(fname, 'r')
    # except IOError as e:
    #     print("*** file open error:", e)
    # else:
    #     # display contents to the screen
    #     for eachLine in fobj:
    #         print(eachLine.strip(),)
    #     fobj.close()
    if os.path.exists(fname):
        fobj = open(fname, 'r')
        print('------------------The Start----------------------')
        for eachLine in fobj:
            print(eachLine.strip())
        fobj.close()
        print('------------------The   end----------------------')


if __name__ == '__main__':
    while 1:
        choose = input('please input (1 or 2 or 3)\n'
                       '    1:create a text file'
                       '    2:read a text file'
                       '    3:esc\n'
                       '>>:')
        if choose == '1':
            create_file()
        elif choose == '2':
            read_file()
        elif choose == '3':
            break
        choose = 0
