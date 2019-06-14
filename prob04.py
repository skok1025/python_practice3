# 문제4.
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
import random
import sys

m = random.randint(1,9)
n = random.randint(1,9)
correct = m*n
print(m,"x",n,"= ?")
l = [random.randint(1,100) for num in range(0,9)]
l[random.randint(0,8)] = correct

index = 0;
for i in l:
    if index%3==0: print()
    print(i,end=' ')
    index += 1;
else: print()
correct == int(input("answer:")) and print("정답")
sys.exit()
