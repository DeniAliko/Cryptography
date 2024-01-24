fib = [0, 1]
for n in range(int(input("n: "))):
    fib.append(fib[-1] + fib[-2])
print(fib[-1])