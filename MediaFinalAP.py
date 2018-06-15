num = int(input())
ap1 = []
ap2 = []
ap3 = []
mediaAlunos = 0

for i in range(0, num, 1):
    ap1.append(float(input()))
for i in range(0, num, 1):
    ap2.append(float(input()))
for i in range(0, num, 1):
    ap3.append(float(input()))

for k in range(0, num, 1):
    mediaAlunos += (ap1[k] + ap2[k] + ap3[k])/3
mediaAlunos /= num

for j in range(0, num, 1):
    if (ap1[j] + ap2[j] + ap3[j])/3 >= mediaAlunos:
        print '%.2f' % ((ap1[j] + ap2[j] + ap3[j])/3)
