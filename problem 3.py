#Problem statement - To calculate min Calories intake from given input

n = int(input())
calories = list(map(int, input().split()))
calories.sort(reverse=True)
total_min_calories = 0
for i in range(n):
    total_min_calories = total_min_calories + ((2**i)*calories[i])

print(total_min_calories)