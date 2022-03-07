
def main():
    #list
    # a = [2, 4, 6]
    # print(a)
    # # list length
    # print(len(a))
    # for i in range(0, len(a)):
    #     print("method1:", a[i])
    # # the same
    # for i in a:
    #     print("method2:", i)
    #append
    # a.append(8)
    # print(a)
    # #insert(i,x)
    # #i為位置, x為值
    # a.insert(2,10)
    # print(a)
    # #pop
    # a.pop()
    # print(a)
    # #pop(i)
    # a.pop(0)
    # print(a)
    # #remove(x)
    # #x是實際的值
    # a.remove(10)
    # print(a)
    # #clear
    # a.clear()
    # print(a)
    #max, min, sum
    # print(max(a))
    # print(min(a))
    # print(sum(a))
    #slice 
    #list[start:end]
    #list[start: end]，start和end都可以省略不寫
    #start的預設為0
    #end的預設為len(list)
    #liest[ :end]代表 0~end-1
    #list[start: ]代表start~len(list)-1
    #list[ : ]代表0~len(list)-1
    a = [2, 4, 6]
    print(a[0:2]) #代表0到end-1, 為0,1
    print(a[:])



if __name__ == '__main__':
    main()