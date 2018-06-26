a = [[],[],[]]

for i in range(3) :
    for j in range(5) :
        a[i].append(j**(i+1))
    
print(a)

# [[0, 1, 2, 3, 4], [0, 1, 4, 9, 16], [0, 1, 8, 27, 64]]
