def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
        print()

def fib2(n):
    result=[]
    a,b=0,1
    while a < n:
        result.append(a)
        a,b=b,a+b
    return result

pi = 3.14

if __name__=="__main__":
    print("Estoy ejecutando desde fibo.py")