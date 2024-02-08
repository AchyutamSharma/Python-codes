from sqlite3 import Timestamp
import time
# a = input("Enter the Time in hrs {like 12pm} : ")
Timestamp = time.strftime('%H:%M:%S')
print(Timestamp)
hour = int(time.strftime('%H'))
mins = int(time.strftime('%M'))
sec = int(time.strftime('%S'))

print("Time :",hour,"hr",mins,"min",sec,"sec")