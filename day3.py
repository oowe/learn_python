def main():
    #dict
    # a = {'name':'aaron', 'phone':'0912345678'}
    # print(a)
    # #注意dict的順序是不一定的
    # #len
    # print(len(a))
    # #define
    # #a = {}
    # #del
    # del a['name']
    # print(a)
    # a['age'] = 18
    # print(a)
    # #for loop
    # for i in a:
    #     print(i)
    #檢查有沒有包含特定的key
    table = {'a':1, 'b':2, 'c':3}
    print('b' in table)
    print('d' in table)
    print('a' in table.keys())
    print(4 in table.values())
    #get value
    #method1
    print(table['a'])
    #method2
    #這是比較安全的, 如果找不到就回傳default
    print(table.get('z', 123))
    
        

if __name__ == "__main__":
    main()