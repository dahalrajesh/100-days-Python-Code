current_population = 10000
growth_rate = 0.1

for year in range(10, 0, -1):
    print(f"{year}th year - {int(current_population)}")
    current_population /= (1 + growth_rate)
