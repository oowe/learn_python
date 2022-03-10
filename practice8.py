#讓使用者在名為table的dict中，輸入五組的key-value pair，key是字串、value是數字，最後把這個dict印出來。

def main():
    table = {}
    for i in range(0,5):
        key = str(input("第{}個請輸入字串:".format(i)))
        value = int(input("第{}個請輸入整數:".format(i)))
        table[key] = value
    print(table)


if __name__ == '__main__':
    main()