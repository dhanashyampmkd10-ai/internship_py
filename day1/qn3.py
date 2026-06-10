sales = [1200, 1500, 900, 1800, 2200, 1700, 1300]
total = sum(sales)
average = total / len(sales)
highest = max(sales)
lowest = min(sales)
x=0
for i in sales:
    if i >1500:
        x+=1
print("Total sales:", total)
print("Highest sales:", highest)
print("Lowest sales:", lowest)
print("Average sales:", average)
print("Number of sales above 1500:", x)
