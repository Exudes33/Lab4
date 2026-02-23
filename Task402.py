def even_gen(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input().strip())
first = True

for num in even_gen(n):
    if first:
        print(num, end="")
        first = False
    else:
        print(f",{num}", end="")
print()
