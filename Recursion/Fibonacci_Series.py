def fibo(num):
    if num in [0,1]:
        return num
    else:
        return fibo(num-1) + fibo(num-2)
nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibo(i))