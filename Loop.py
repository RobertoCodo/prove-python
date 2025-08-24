run = True
Counter = 0
Skip = 5
Stop = 100000
while run:
    Counter += 1
    print(Counter)
    # The following block skips at every multiple of 5 because 'Skip' starts at 5 and is incremented by 5 each time.
    if Counter == Skip:
        # Set next skip point to every 5th iteration
        Skip += 5
        Skip += 5
    if Counter >= Stop:
        print(f"Loop stopped at {Counter}")
        break