'''
#Program to generate the Fibonacci Sequence till n
n=int(input("Enter the value of 'n': "))
#first two terms are first and second
first=0
second=1
sum=0
count=1
print("Fibonacci Sequence: ")
# Count should not be more then n.
while(count<=n):    
  print(sum)
  count+=1
  first=second
  second=sum
  sum=first+second	
'''

'''
#Program to generate Fibonacci sequence recursively 
def Fibonacci(Number):
    if(Number==0):
        return 0
    elif(Number==1):
        return 1
    else:
        return (Fibonacci(Number-2)+Fibonacci(Number-1)) 
#return the sum of two previous terms
n=int(input("Enter the value of 'n': "))
print("Fibonacci Sequence:")
for n in range(0, n):
  print(Fibonacci(n))
'''

'''
# Program to generate fibonacci sequence using dynamic programming approach
def fib_dp(num):
    arr=[0,1]
    print("Fibonacci Sequence: ")
    if num==1:
        print('0')
    elif num==2:
        print('[0,','1]')
    else:
        while(len(arr)<num):  #length of list should be less then num
            arr.append(0)
        if(num==0 or num==1):
            return 1
        else:
            arr[0]=0
            arr[1]=1
            for i in range(2,num):   
                arr[i]=arr[i-1]+arr[i-2]      #New term is equal to sum of two previous terms.
            print(arr)    
            return arr[num-2]
n=int(input("Enter the value of 'n': "))
fib_dp(n)
'''