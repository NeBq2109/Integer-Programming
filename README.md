# Integer-Programming

Program which uses PuLP (https://pypi.org/project/PuLP/) to solve integer programming problem using "Divide and constraint" method.
Method used in script uses linear programming solver provided by PuLP, and then appends subproblems to the list when at least one of
calculated variable is not integer.When solution is: (x1,x2,x3,x4)=(0,1,1,0.34), then there are created 2 new subproblems 
with new constraints: x4>=0 and x4<=1.

Upgrades for the future:
- end proceeding branch when some integer solution is better than actually solved subproblem
- create GUI for initializing problems (appending and poping constraints) and presenting solutions
