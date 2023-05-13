
with open('PI.txt') as fayl:
    PI=fayl.read()
print(PI)
PI=PI.rstrip()
PI=PI.replace('\n','')
PI=float(PI)

print(PI)


