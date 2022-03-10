#一年一度的世界歌王大賽來啦！身為評審的你，請輸入五個歌手的名字與成績。接下來會有五次查詢的機會，每次查詢都可以讓觀眾輸入一個名字、來查看心愛的歌手。如果歌手不在名單中，請輸出’這個人沒參賽喲’；如果歌手在名單中，請輸出該歌手的名字與成績。

def main():
    singer = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
    
    for i in range(0, 5):
        guess = str(input("請輸入歌手名稱:"))
        if guess in singer.keys():
            print("滿分五分，而{}的成績為{}分".format(guess, singer[guess]))
        else:
            print("這個人沒參賽喲!")

if __name__ == '__main__':
    main()