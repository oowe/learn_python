#來辦場Party吧! 輸入十個整數、存入一個名為people清單中 (表示我們的宴客人數)；之後會有五次詢問，每次會輸入清單開始和結束的位置，再輸出從開始到結束位置的總和。

def main():
    
    people = []
    for i in range(1,11):
        print("請輸入第{}個數字:".format(i))
        people.append(int(input()))
    print(people)
    for i in range(1,6):
        print("請輸入第%d個的開始和結束位置:" % i)
        start = int(input('頭:'))
        end = int(input("尾:"))
        print(sum(people[start:end]))
    
if __name__ == '__main__':
    main()