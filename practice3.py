#請輸出一個九九乘法表

def main():

    for i in range(1, 10):
        for j in range(1, 10):
            print(i*j, end=' ')
        print(end='\n')

if __name__ == '__main__':
    main()