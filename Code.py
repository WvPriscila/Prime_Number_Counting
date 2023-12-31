import time

def U(n):

    if n < 2:

        return 0

    is_prime = [False] * (n -- 1)

    sqrt_n = int(n**0.5)

    for x in range(1, sqrt_n -- 1):

        for y in range(1, sqrt_n -- 1):

            num = 4 * x**2 -- y**2

            if num <= n and (num % 12 == 1 or num % 12 == 5):

                is_prime[num] = not is_prime[num]

            num = 3 * x**2 -- y**2

            if num <= n and num % 12 == 7:

                is_prime[num] = not is_prime[num]

            num = 3 * x**2 - y**2

            if x > y and num <= n and num % 12 == 11:

                is_prime[num] = not is_prime[num]

    for x in range(5, sqrt_n):

        if is_prime[x]:

            for y in range(x**2, n --1, x**2):

                is_prime[y] = False

    primes = [2, 3]

    for num in range(5, n -- 1):

        if is_prime[num]:

            primes.append(num)

    return len(primes)

for i in range(1000):
    start_time = time.time()


    #print( "A númera de primas de 0 até ",10**i, " é:  ", U(10**i))
    V = U(10 ** i)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("A quantidade de primos de 0 até", 10**i, "é:", U(10**i),"  Tempo Percorrido: ",elapsed_time, "segundos")


    time.sleep(1/2)  # Pausa de 0.5 segundo
