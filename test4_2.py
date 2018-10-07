__author__ = 'Сафин Ильшат'

# coding: utf-8

# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм 
# решето Эратосфена. Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

# Решето
def prime_eratosfen(n):
    n = int(input('До какого числа искать простые числа: '))
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i

    sieve = [i for i in sieve if i != 0]
    print(sieve)
    
prime_eratosfen(50)
    
    
# Без решета (алгоритм нашёл в сети)
def prime_not_eratosfen(n):
    n = int(input('До какого числа искать простые числа: '))
    lst_=[2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst_:
            if j*j-1 > i:
                lst_.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst_.append(i)
    print(lst_)

prime_not_eratosfen(50)



# Судя по замерам - программа с решетом Эратосфена работает быстрее.

# C:\Program Files (x86)\Python36-32>python.exe -m timeit -n 1000 -s "import test4_2" "test4_2.prime_eratosfen"
# 1000 loops, best of 3: 0.0693 usec per loop

# C:\Program Files (x86)\Python36-32>python.exe -m timeit -n 1000 -s "import test4_2" "test4_2.prime_not_eratosfen"
# 1000 loops, best of 3: 0.0817 usec per loop
