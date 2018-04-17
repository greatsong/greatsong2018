# 10000 이하의 자연수 중,
# 3의 배수이면서 5의 배수가 아닌 것은 모두 몇 개인가?

cnt = 0
a = []

for i in range(1,10001) :
    if i % 3 == 0 and i % 5 != 0 :
         cnt = cnt + 1
         a.append(i)

print(cnt)
print(len(a))
