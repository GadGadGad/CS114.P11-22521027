import re

prices = [int(cost) for cost in input().split()]

online_prices = prices.copy()
offline_prices = prices.copy()

for i in range(len(prices)):
    temp = input().strip()
    # Em hoc cach dung thu vien nay trong link: https://www.py4e.com/lessons/regex
    higher_percent = re.findall(r'([0-9.]+)\% higher', temp)
    lower_percent = re.findall(r'([0-9.]+)\% lower', temp)

    higher_percent = [float(per) for per in higher_percent]
    lower_percent = [float(per) for per in lower_percent]

    # print(higher_percent)
    # print(lower_percent)

    total_percent_increase = sum(higher_percent) if len(higher_percent) > 0 else 0
    total_percent_decrease = sum(lower_percent) if len(lower_percent) > 0 else 0

    online_prices[i] = online_prices[i] * (1 + total_percent_increase / 100) 
    offline_prices[i] = offline_prices[i] * (1 - total_percent_decrease / 100)

money = int(input())
higher_prices = min(sum(online_prices), sum(offline_prices))

res = 'true' if money >= higher_prices else 'false'
print(res)
        
