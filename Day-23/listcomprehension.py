'''
#listcomp-->concise way to create a new list
res=[i for i in range(1,11)]
print(res)

n=12
res=[i for i in range(1,n+1) if n%i==0]
print(res)

r=[12,23,45,687,34,123,34,12,43,90]
res=[i if i%2==0 else 0 for i in r]
print(res)

r=[[12,23,45],[687,34,123],[34,43,90]]
res=[j for i in r for j in i if j%2==0]
print(res)
'''
#set comprehension
'''
res={i for i in range(1,11)}
print(res)

n=12
res={i for i in range(1,n+1) if n%i==0}
print(res)

r={12,23,45,687,34,123,34,12,43,90}
res={i if i%2==0 else 0 for i in r}
print(res)

r={{12,23,45},{687,34,123},{34,43,90}}
res={j for i in r for j in i if j%2==0}
print(res)
'''
'''
#syntax
l=[updating for loop]      #single loop
l=[updating for loop if cond]  #for and if
l=[upd1 if cond else upd2 for loop]   #for if else
l=[upd for loop1 for loop2]     #loop in a loop
l=[upd for loop1 for loop2 if cond]  #loop in a loop and if cond
'''
'''
l=[int(input(f"ENter the number - {i+1}: ")) for i in range(10)]
print(l)
'''
'''
l=[(input(f"Enter the name of stud - {i+1}: "),int(input(f"Enter the stud marks- {i+1}: "))) for i in range(5)]
print(l)
'''
res={i:i*i for i in range(1,11)}
print(res)