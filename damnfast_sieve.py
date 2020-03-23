# https://w3resource.com/python-exercises/list/python-data-type-list-exercise-34.php
# this one is incredibally fast

import time
def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
t1 = t.time()
prime_eratosthenes(10*19)
print(t.time()-t1)
# prime_eratosthenes(1000)
