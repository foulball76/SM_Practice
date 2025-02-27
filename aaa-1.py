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
  
# prime_a = int(input("시작 숫자 : "))
# prime_b = int(input("범위 숫자 : "))

# for i in range(prime_a,prime_b):
#   cnt = 0        
# #   print(i,'들어감')
#   for a in range(2,i+1):
#     # print('              a중',a)
#     if i % a == 0:
#       cnt += 1
#   if cnt == 1:
#     print(i,"는 소수니다.")
import turtle as t

# 게임 화면을 설정합니다.
wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor('black')
wn.setup(width=600, height=400)

# 왼쪽 패들을 생성합니다.
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-250, 0)

# 오른쪽 패들을 생성합니다.
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(250, 0)

# 공을 생성합니다.
ball = turtle.Turtle()
ball.speed(40)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = -6

# 왼쪽 패들을 움직이는 함수를 정의합니다.
def move_left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    if y > 190:
        y = 190
    left_paddle.sety(y)

def move_left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    if y < -190:
        y = -190
    left_paddle.sety(y)

# 오른쪽 패들을 움직이는 함수를 정의합니다.
def move_right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    if y > 190:
        y = 190
    right_paddle.sety(y)

def move_right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    if y < -190:
        y = -190
    right_paddle.sety(y)

# 패들을 움직이는 이벤트를 처리합니다.
wn.listen()
wn.onkeypress(move_left_paddle_up, 'w')
wn.onkeypress(move_left_paddle_down, 's')
wn.onkeypress(move_right_paddle_up, 'Up')
wn.onkeypress(move_right_paddle_down, 'Down')

# 점수를 나타내는 변수를 초기화합니다.
left_score = 0
right_score = 0

# 점수를 표시하는 함수를 정의합니다.
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 170)
score.write(f'Player 1: {left_score}  Player 2: {right_score}', align='center', font=('Courier', 16, 'normal'))

# 게임 루프를 실행합니다.
while True:
    # 공을 움직입니다.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # 공이 벽에 부딪히면 방향을 바꿉니다.
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # 왼쪽 패들과 공이 부딪히면 방향을 바꿉니다.
    if ball.xcor() < -240 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.dx *= -1

    # 오른쪽 패들과 공이 부딪히면 방향을 바꿉니다.
    if ball.xcor() > 240 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.dx *= -1

    # 왼쪽 플레이어가 공을 놓치면 오른쪽 플레이어가 점수를 획득합니다.
    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
        right_score += 1
        score.clear()
        score.write(f'Player 1: {left_score}  Player 2: {right_score}', align='center', font=('Courier', 16, 'normal'))

    # 오른쪽 플레이어가 공을 놓치면 왼쪽 플레이어가 점수를 획득합니다.
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
        left_score += 1
        score.clear()
        score.write(f'Player 1: {left_score}  Player 2: {right_score}', align='center', font=('Courier', 16, 'normal'))

    # 게임을 계속 실행합니다.
    wn.update()

# 소수를 구하시오 함수 응용

# def fn_prime_input():
#     p_lst = []
#     p1_num = int(input("시작 숫자를 입력하세요. :"))
#     p2_num = int(input("범위 숫자를 입력하세요. :"))
#     p_lst.append(p1_num)
#     p_lst.append(p2_num)
#     return p_lst

# def fn_prime_check(user_input):
#     lst = []
#     for i in range(user_input[0],user_input[1]+1):
#         cnt = 0        
#         for a in range(2,i+1):
#             if i % a == 0:
#                 cnt += 1
#         if cnt == 1:
#             print(i,"는 소수입니다.")
#         #     return True
#         # else:
#         #     return False

#     # for i in range(2, prime_num+1):
#     #     if prime_num % i == 0:
#     #         div_count += 1
#     # if div_count == 1:
#     #     return True
#     #     #print(prime_num,"는 소수가 아입입니다.")    
#     # else:
#     #     return False
#     #     #print(prime_num,"는 소수입니다.")

# def disply_result(user_input, i_num):
#     if i_num == False:
#         print(user_input,"는 소수가 아입입니다.")    
#     else:
#         print(user_input,"는 소수입니다.")    

# def fn_prime():

#     #prime_num = int(input("숫자를 입력하세요. :"))
#     user_input = fn_prime_input()
        
#     i_num = fn_prime_check(user_input)

#     disply_result(user_input, i_num)
 
# fn_prime()

def fn_input():
    #return int(input("숫자 입력 : "))
    while True:
        try:
            num = int(input("숫자 입력 : "))
            return num
        except ValueError:
            print("숫자를 입력하세요.")
        '''
        num = input("숫자 입력 : ")
        if num.isdigit():
            return int(num)
        else:
            pass
        '''

def fn_prime(k):
    cnt = 0
    for i in range(2, k):
        if k % i == 0:
            cnt += 1
    if cnt >= 1:
        return 0
    else:
        return 1

def fn_print(lst):
    if 1 in lst:
        lst.remove(1)
    for i in lst:
        print(i,"는 소수입니다.")

def fn_try():
    bCont = True
    while bCont :
        yn = input("Yes or No ? ")
        if yn.strip() == "Y" or yn.strip() == "y":
            return True
        elif yn.strip() == "N" or yn.strip() == "n":
            return False

def fn_start():
    bAgain = True
    while bAgain:
        n1 = fn_input()
        n2 = fn_input()

        lst = []
        for i in range(n1,n2+1):
            b = fn_prime(i)
            if b == 1:
                lst.append(i)

        fn_print(lst)

        bAgain = fn_try()

fn_start()
