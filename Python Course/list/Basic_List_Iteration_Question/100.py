"""Q100. Find the sum of all numbers divisible by 
3 or 4 """

my_list = [51, 85, 1748, 52, 44, 100, 200]
sum = 0

for i in my_list:
    if i % 3 == 0 or i % 4 == 0:
        sum += i
print(sum)
