#現在有一個 list a = [1, 3, 5, 7, 9]，請對每一個元素都平方後印出來，且須將 a 也變成 [1, 9, 25, 49, 81]。

def main():
    a = [1, 3, 5, 7, 9]
    for i in a:
        #method1
        #print(i*i)
        #method2
        print(i**2)


if __name__ == '__main__':
    main()