def ft_count_harvest_recursive(day=None, current=1):
    if day is None:
        day = int(input("Days until harvest: "))
    if current > day:
        print("Harvest time!")
        return
    print(f"Day: {current}")
    ft_count_harvest_recursive(day, current + 1)
