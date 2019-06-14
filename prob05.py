# 문제5.
# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.

l = [ 5, 9, 3, 8, 60, 20, 1 ]

def swap(m,n):
    temp = m
    m=n
    n=temp
    return m,n

a = 1
b = 2
a,b = swap(a,b)

for loop in range(len(l),0,-1):
    for n in range(len(l)-1-loop,0,-1):
        if l[n-1]<l[n]:
            l[n-1],l[n] = swap(l[n-1],l[n])

print(l)