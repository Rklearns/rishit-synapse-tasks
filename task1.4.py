customers=[ [5,6],[5,7],[10,14],[20,21]]
waitingtime=[]
sum=0
for arrival,serving in customers:
    time=serving-arrival
    waitingtime.append(time)#list of waiting time is formed
   
for i in waitingtime:
    sum=sum+i

avg=sum/len(waitingtime)
print("Average waiting time is ",avg)
 #now Irah understands the efficieny in making tea for customers and understands customer satisfaction   
 