#請做出一支能猜數字的程式：每次讓使用者猜一個整數，若猜對就輸出Bingo；使用者最多可以猜3次。


import random


def main():
    
    ans = random.randint(1,10)
    for i in range(3):
        print('猜數字(1-10)請輸入:')
        a = int(input())
        if a == ans:
            print('答對了! 答案是:' + str(ans))
            break
        elif a < ans:
            print('不對! [提示]答案比較大')
        elif a > ans:
            print('不對! [提示]答案比較小')
    print('公佈答案是:' + str(ans))


if __name__ == '__main__':
    main()