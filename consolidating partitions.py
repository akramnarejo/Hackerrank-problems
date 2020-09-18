""" Consolidating partitions program, returns the minimium partitions 
    by allocating the space to the partitions.  used list contains the space used in the paritions and capacity list shows
    the capacity of the partitions."""

used = [1024,200,500,2024,2024]
capacity = [2024,1024,1024,2024,2024]

parts = [] #partitions
maxval = 0
total = sum(used)
val1 = 0
val2 = 0
difference = 0

for i in range(len(capacity)):
    if capacity[i] == total or capacity[i] > total:
        parts.append(capacity[i])
        break

if len(parts) == 0:
    if len(capacity) > 1:
        for i in range(len(capacity)-1):
            if capacity[i]+capacity[i+1] > maxval:
                maxval = capacity[i]+capacity[i+1]
                val1 = capacity[i]
                val2 = capacity[i+1]
        parts.append(val1)
        parts.append(val2)
    else:
        parts.append(capacity[0])
    difference = total - maxval
    if difference > 0:
        for i in range(len(capacity)):
            if difference < capacity[i]:
                parts.append(capacity[i])
                break
            elif difference > capacity[i]:
                difference = difference-capacity[i]
                parts.append(capacity[i])
                
print("partitions: ",len(parts))
