import numpy as np 
weekArrangment = np.array([[float( input("Sales Day {:.0f} Week {:.0f} " .format(x+1,y+1)))for x in range (7)] for y in range (4)])

for column in range(7):
    for line in range(4):
             if(weekArrangment[line,column] < 0 ):
                 print("\nInvalid number")
sum = 0
for x in range(4):
    for y in range(7):
        sum = sum + weekArrangment[x,y]
avg = sum/28
print("\n Avarage sales: " + str(avg))

weekend_sum =0
for x in range(4):
    for y in range(-1,1):
         weekend_sum = weekend_sum + weekArrangment[x,y]
weekend_avg = weekend_sum/8
print("\n Avarage sales in the weekend: " + str(weekend_avg))
week_sum = 0
for x in range(4):
    for y in range(1,6):
         week_sum = week_sum + weekArrangment[x,y]
week_avg = week_sum/20
print("\n Avarage sales in the week: " + str(week_avg))

max = 0
for x in range(4):
    for y in range(7):
         if(weekArrangment[x,y]>max):
             max = weekArrangment[x,y]

print("\n Biggest Sale " + str(max))









        
