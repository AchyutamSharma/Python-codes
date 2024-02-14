import time
timess = time.strftime('%H:%M:%S')
print(timess)

t = int(time.strftime('%H'))
print(t)


if(t>=0 and t<12):
    print('Good Morning Sir!!')
elif(t>=12 and t<16):
    print("Good Afternoon Sir!!")
elif(t>=16 and t<20):
    print("Good Evening Sir!!")
elif(t>=21 and t<0):
    print("Good Night Sir!!")
