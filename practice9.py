#除了用key找value，我們也可以反查，用value找出相對應的key

def main():
    table = {'a':1, 'b':2, 'c':3}
    
    for i in range(0, 3):
        value = int(input("請輸入數字:"))
        for j in table:
            if table[j] ==value:
                print("的確有這個value的key叫做{}".format(j))
                break
        

if __name__ == '__main__':
    main()
