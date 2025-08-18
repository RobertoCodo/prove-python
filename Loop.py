run = True
Counter = 0
Stop = 100000
while run:
    Counter += 1
    print(Counter)
    if Counter >= Stop:
        print("Loop stopped at", Counter)
        break