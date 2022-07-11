def print_primes_till_N(N): 
    i, j, flag = 0, 0, 0
    print("Prime numbers between 1 and ", N , " are:")
    for i in range(1, N + 1, 1):
        if (i == 1 or i == 0): 
            continue
        flag = 1
        for j in range(2, ((i // 2) + 1), 1): 
            if (i % j == 0):
                flag = 0
                break
 
        if (flag == 1): 
            print(i, end=' ')
N = 100
print_primes_till_N(N)
print ("Done by Vishal")
