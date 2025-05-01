import math

with (open('input.txt', 'r') as f):
    n = list(map(int, f.readline().strip().split()))[0]
    required_power = list(map(int, f.readline().strip().split()))
    m = list(map(int, f.readline().strip().split()))[0]

    power_price = [math.inf]*1002
    best_price = [math.inf]*1002

    for _ in range(m):
        power, price = list(map(int, f.readline().strip().split()))
        # Always select minimal price for the given power
        if power_price[power] > price:
            power_price[power] = price

# min suffix
for power in range(1000, -1, -1):
    best_price[power] = min(power_price[power], best_price[power + 1])

# No need to sort something!
total_price = 0
for power in required_power:
    total_price += best_price[power]

print(total_price)