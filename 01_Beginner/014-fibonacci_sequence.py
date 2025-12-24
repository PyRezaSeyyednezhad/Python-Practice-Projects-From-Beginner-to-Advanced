def fibonacci_sequence(n):
    stage = 2
    i = 0
    j = 1
    resList = [0, 1]
    print(f"0th of fibonacci_sequence: {i}")
    print(f"1th of fibonacci_sequence: {j}")
    while stage <= n:
        res = i+j
        resList.append(res)
        print(f"{stage}th of fibonacci_sequence: {res}")
        i = j
        j = res
        stage += 1
    print(f"fibonacci_sequence: {resList}")

fibonacci_sequence(9)