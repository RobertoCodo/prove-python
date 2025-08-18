run = True
Counter = 0
Skip = 5
Stop = 100000
while run:
    Counter += 1
    print(Counter)
    if Counter == Skip:
        print("Loop skipped at", Counter)
        # Increment Skip to set the next value at which the loop will be skipped
        Skip += 5
    if Counter >= Stop:
        print("Loop stopped at", Counter)
        break