def main():
    #dict
    a = {'name':'aaron', 'phone':'0912345678'}
    print(a)
    #注意dict的順序是不一定的
    #len
    print(len(a))
    #define
    #a = {}
    #del
    del a['name']
    print(a)
    a['age'] = 18
    print(a)
    #for loop
    for i in a:
        print(i)
        

if __name__ == "__main__":
    main()