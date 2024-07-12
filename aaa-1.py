import random

lst = random.sample([1,2,3,4,5,6,7,8,9],k=4)
print(lst)

cnt_strike = 0
while cnt_strike <= 3:
    a = list(input("4자리 숫자를 입력하세요 : "))
    cnt_out = 0
    cnt_ball = 0
    # s = input("string:")
    #print(list(map(int,s)))
    for i in range(1,len(a)+1):
        if int(a[i-1]) in lst:
            for z in range(1,len(lst)+1):
                #print(int(a[i-1]),lst[z-1])
                if int(a[i-1]) == lst[z-1]:
                    if i == z:
                        cnt_strike += 1
                    else:
                        cnt_ball += 1
            #print("입력",i,"번째 자리")
            #print("랜덤",len(lst),"번째 자리")
        else:
            cnt_out += 1
    print("Strike =",cnt_strike,"Ball =",cnt_ball,"Out =",cnt_out,)
  
