#有一個班級的數學段考的成績分別為10、30、50、70、90分，算出平均後，老師發現大家考太爛、只好將成績開根號再乘上10 ，再算出一個新平均。
#請印出: 1. 五次成績; 2. 平均成績; 3. 五次新成績; 4. 新分數的平均。

def main():
    score = [10, 30, 50, 70, 90]
    newScore = []
    for i in score:
        newScore.append(i**0.5*10)

    print("五次成績:", score)
    print("原始成績平均:", sum(score)/len(score))
    print("五次新成績:", newScore)
    print("新成績平均", sum(newScore)/len(newScore))

if __name__ == '__main__':
    main()