def limited_cycle(lst, k):
    for _ in range(k):
        for item in lst:
            yield item

elements = input().split()
k = int(input().strip())
print(" ".join(limited_cycle(elements, k)))
