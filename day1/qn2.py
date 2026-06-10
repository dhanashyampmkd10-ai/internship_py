print("enter expence amount in 7 days:")
expences = []
for i in range(1, 8):
    expence = float(input(f"day {i}: "))
    expences.append(expence)
total = sum(expences)
avg = total / 7
highest = max(expences)
lowest = min(expences)    
print("total expence =",+total)
print("average expence =",+avg)
print("highest expence =",+highest)
print("lowest expence =",+lowest)