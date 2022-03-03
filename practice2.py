#寫一支Python整數機，第一步讓使用者輸入想要做的符號運算，比如「+, -, *, /」，第二步讓使用者輸入’整數1’和 ‘整數2’，最後讓這兩個整數進行運算。如果輸入的運算符號不是「+, -, *, /」，便輸出「錯誤」。

def main():

    print('請輸入運算符號:')
    sign = input()
    print('請輸入a:')
    a = int(input())
    print('請輸入b:')
    b = int(input())
    print('結果:')
    if sign == '+':
        print(a+b)
    elif sign == '-':
        print(a-b)
    elif sign == '*':
        print(a*b)
    elif sign == '/':
        print(a/b)
    else:
        print('運算符號輸入錯誤')


if __name__ == '__main__':
    main()