run = True
Counter = 0
Skip = 5
Stop = 100000
while run:
    Counter += 1
    print(Counter)
    if Counter == Skip:
        print("Loop skipped at", Counter)
        Skip += 5
    if Counter >= Stop:
        print("Loop stopped at", Counter)
        break