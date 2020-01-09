import numpy as np
import matplotlib.pyplot as plt



arrx = []
arrx2 = []
arry = []
arry2 = []
print("Enter the first signal x[n] \n")
num = int(input("how many points do you want to add ? : "))
for i in range(0, num):
    x = float(input("x : "))
    arrx.append(x)
    y = float(input("y : "))
    arry.append(y)
print("Enter the second signal h[n] \n")
num2 = int(input("how many points do you want to add ? : "))
for i in range(0, num2):
    x = float(input("x : "))
    arrx2.append(x)
    y = float(input("y : "))
    arry2.append(y)

for i in range(0,num2):
    if(arrx2[i] != 0):
        arrx2[i]  = arrx2[i] * (-1.0)

arrx2 = sorted(arrx2)
arry2.reverse()
while(True):
    if(arrx2[num2-1] !=arrx[0]) :
        if(arrx2[num2- 1] > arrx[0]):
            for i in range(0,num2):
                arrx2[i] = arrx2[i] - 1
        else :
            for i in range(0,num2):
                arrx2[i] = arrx2[i] + 1
    else:
        False
        break
newarr = []
counter = 0
counter2 = 0
x = num2
sum = 0
while(arrx2[0] < arrx[num- 1]):

    x = num2
    sum = 0
    for j in range(0,num2):
        counter = 0
        x -= 1
        for i in range(0,num):
            if(arrx[counter] == arrx2[x-1]):
                sum += arry[i] * arry2[x - 1]

            counter += 1
    newarr.append(sum)
    counter2 += 1
    for i in range(0, num2):
        arrx2[i] = arrx2[i] + 1

'''newarr.remove(newarr[counter2 - 1])
counter2-=1'''
newarrx = []
for i in range(0,counter2):
    print(newarr[i])
    newarrx.append(i)
arrx.append(0)
plt.axhline(y=0, color='k')
plt.axvline(0,color='k')
plt.plot(arrx,newarr,'ro')
plt.show()
