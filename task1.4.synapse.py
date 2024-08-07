def waiting(customers):
    waitingtime = []
    sum = 0
    free_time=0

    for arrival, prep in customers:
        if arrival > free_time:#if customer arrives after the free time then chef can prepare food at that time without delay
            free_time = arrival
        wait = free_time + prep - arrival#else chef will be free at free_time 
        #to prepare and will take prep time
        waitingtime.append(wait)#indivdual waiting time is added in the list
        free_time = free_time + prep

    print("Therefore the individual waiting times are: ", waitingtime)

    for i in waitingtime:
        sum += i

    avg = sum / len(waitingtime)
    return avg

customers = [[5, 6], [5, 7], [10, 14], [20, 21]]
a = waiting(customers)
print("Average waiting time hence taken is ", a)

# Now Iroh understands the efficiency in making tea for customers and understands customer satisfaction.
