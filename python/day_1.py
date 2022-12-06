# day one
with open("./day_1_input.txt", "r") as f:
    nums = [s[:-1] for s in f.readlines()]
    results, subtotal = [], 0
    for num in nums:
        if num:
            subtotal += int(num)
        else:
            results.append(subtotal)
            subtotal = 0

print(max(results))
print(sum(sorted(results, reverse=True)[:3]))
