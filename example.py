import readchar

if __name__ == '__main__':
    print('start... press q to quit')
    while 1:
        k = readchar.readkey()
        print('you pressed ' + str(k))
        if k == 'q':
            break
