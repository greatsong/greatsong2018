import random
f = open('eng.txt')
quiz = open('quiz.txt','w')
cnt = 0
ans = []
for row in f :
    if cnt % 2 == 0 :
        row = row.split()
        no = random.randrange(len(row))
        ans.append(row[no])
        row[no] = '[     ]'
    cnt += 1

    for i in row :
        quiz.write(i + ' ')
    quiz.write('\n')

f.close()
quiz.close()

r = open('quiz.txt')
print(r.read())
r.close()

random.shuffle(ans)
print(ans)

f = open('quiz.txt','a')
f.write('\n[보기]\n')
for i in ans :
    msg = i + ' '
    f.write(msg)
f.close()
