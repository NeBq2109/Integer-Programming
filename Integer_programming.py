import pulp as p
import numpy as np
import math

def solve_LP(Lp_prob):
    status = Lp_prob.solve()   # Solver 
    #print(p.LpStatus[status])   # Solver status

    result= [p.value(x1), p.value(x2), p.value(x3), p.value(x4), p.value(x5), p.value(x6),p.value(x7), p.value(x8),
    p.value(x9),p.value(x10),p.value(x11), p.value(Lp_prob.objective)]

    if p.LpStatus[status]=='Optimal': return result
    else: return 0 # Solution not found

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


# Create a LP Maximization problem
Lp_copy = p.LpProblem('Problem', p.LpMaximize)  
  
# Knapsack problem
x1 = p.LpVariable("x1", lowBound = 0, upBound=1)
x2 = p.LpVariable("x2", lowBound = 0, upBound=1)
x3 = p.LpVariable("x3", lowBound = 0, upBound=1)
x4 = p.LpVariable("x4", lowBound = 0, upBound=1)
x5 = p.LpVariable("x5", lowBound = 0, upBound=1)
x6 = p.LpVariable("x6", lowBound = 0, upBound=1)
x7 = p.LpVariable("x7", lowBound = 0, upBound=1)
x8 = p.LpVariable("x8", lowBound = 0, upBound=1)
x9 = p.LpVariable("x9", lowBound = 0, upBound=1)
x10 = p.LpVariable("x10", lowBound = 0, upBound=1)
x11 = p.LpVariable("x11", lowBound = 0, upBound=1)

x=[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

# Funkcja celu
Lp_copy += 10 * x1 + 7 * x2 + 2 * x3 + 1 * x4 + 2 * x5 + 4 * x6 + 3 * x7 + 6 * x8 + 3 * x9 + 7 * x10 + 6 * x11            

# Ograniczenia
Lp_copy += 1 * x1 + 1 * x2 >=1
Lp_copy += 1 * x3 + 1 * x4 >=1
Lp_copy += 1 * x5 + 1 * x6 >=1
Lp_copy += 1 * x7 + 1 * x8 >=1
Lp_copy += 1 * x9 + 1 * x10 >=1
Lp_copy += 1000 * x1 + 340 * x2 + 550 * x3 + 380 * x4 + 80 * x5 + 320 * x6 + 780 * x7 + 1500 * x8 + 830 * x9 + 1420 * x10 + 160 * x11<=4000
Lp_copy += 2 * x1 + 2 * x2 + 4 * x3 + 4 * x4 + 2 * x5 + 3 * x6 + 7 * x7 + 9 * x8 + 5 * x9 + 5 * x10 + 1 * x11<=40    
Lp_prob = Lp_copy
   
wynik1=solve_LP(Lp_prob)
print(wynik1)

def check(wynik1, Lp_copy, x):
    k=0
    output=[]
    for idx, value in enumerate(wynik1[:-1]):
        if value.is_integer() == False:
            Lp_var1 = Lp_copy.deepcopy()
            Lp_var2 = Lp_copy.deepcopy()
            limit=truncate(value)
            Lp_var1 += 1*x[idx] <= limit
            limit=round_up(value)
            Lp_var2 += 1*x[idx] >=limit
            k=1
            output.append(Lp_var1)
            output.append(Lp_var2)

    return output, k

output=[]
result, k = check(wynik1,Lp_prob, x)
output.append(result)

output1=[]
rozwiazania1=[]
maximum1=0
for idx, value in enumerate(result):
    wynik=solve_LP(output[0][idx])
    if wynik!=0:
        if wynik[11]>=maximum1: maximum1=wynik[11]
        result1, k = check(wynik,output[0][idx], x)
        output1.append(result1)
        if k==0: rozwiazania1.append(wynik)

output2=[]
rozwiazania2=[]
maximum2=0
for idx, value in enumerate(output1):
    for idy, value1 in enumerate(value):
        wynik=solve_LP(output1[idx][idy])
        if wynik!=0:
            if wynik[11]>=maximum2: maximum2=wynik[11]
            result1, k = check(wynik,output1[idx][idy], x)
            output2.append(result1)
            if k==0: rozwiazania2.append(wynik)
output3=[]
rozwiazania3=[]
maximum3=0
for idx, value in enumerate(output2):
    for idy, value1 in enumerate(value):
        wynik=solve_LP(output2[idx][idy])
        if wynik!=0:
            if wynik[11]>=maximum3: maximum3=wynik[11]
            result2, k = check(wynik,output2[idx][idy], x)
            output3.append(result2)
            if k==0: rozwiazania3.append(wynik)

output4=[]
rozwiazania4=[]
maximum4=0
for idx, value in enumerate(output3):
    for idy, value1 in enumerate(value):
        wynik=solve_LP(output3[idx][idy])
        if wynik!=0:
            if wynik[11]>=maximum4: maximum4=wynik[11]
            result3, k = check(wynik,output3[idx][idy], x)
            output4.append(result3)
            if k==0: rozwiazania4.append(wynik)

output5=[]
rozwiazania5=[]
maximum5=0
for idx, value in enumerate(output4):
    for idy, value1 in enumerate(value):
        wynik=solve_LP(output4[idx][idy])
        if wynik!=0:
            if wynik[11]>=maximum5: maximum5=wynik[11]
            result4, k = check(wynik,output4[idx][idy], x)
            output5.append(result4)
            if k==0: rozwiazania5.append(wynik)


print("maksimum w iteracji pierwszej: ", maximum1)
print("maksimum w iteracji drugiej: ", maximum2)
print("maksimum w iteracji trzeciej: ", maximum3)
print("maksimum w iteracji czwartej: ", maximum4)

print("\n Rozwiazania 1 iteracja")
print(rozwiazania1)
print("\n Rozwiazania 2 iteracja")
print(rozwiazania2)
print("\n Rozwiazania 3 iteracja")
print(rozwiazania3)
print("\n Rozwiazania 4 iteracja")
print(rozwiazania4)
print("\n")
