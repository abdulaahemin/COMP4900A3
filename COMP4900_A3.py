import numpy

a=0.3
b=0.7

f0=[[b,(1-b)/2,(1-b)/2],
    [1-a-b,a,b],
    [1-a-b,b,a]]

f1=[[a,(1-a)/2 ,(1-a)/2],
    [1-a-b,b,a],
    [1-a-b,a,b]]

G= [[0.5,0.5],
    [1,0],
    [0,1]]

f_tilda=[[0, 0, 0],
         [0, 0,0],
         [0,0 ,0]]

pi0=[0.2, 0.4, 0.4]

c=[0.4,0.6]

for i in range(len(f0)):
    for j in range(len(f0[0])):
        f_tilda[i][j]=(f0[i][j] *((G[i][0]*(1-c[0]))+(G[i][1]*(1-c[1])))) + (f1[i][j]*((G[i][0]*c[0])+(G[i][1]*c[1])))

print("F0=",f0)
print("F1=",f1)
print("F tilda=",f_tilda)

prob_0=numpy.matmul(numpy.transpose(G),pi0)
print("P(0)=",prob_0)
pi1=numpy.matmul(numpy.transpose(f_tilda),pi0)
print("Pi(1)=",pi1)
prob_1=numpy.matmul(numpy.transpose(G),pi1)
print("P(1)=",prob_1)


#Making G deterministic
f0=[[b/2,(1-b)/2,0,b/2,0,(1-b)/2],
    [(1-a-b)/2,a,0,(1-a-b)/2,0,b],
    [(1-a-b)/2,b,0,(1-a-b)/2,0,a],
    [b/2,(1-b)/2,0,b/2,0,(1-b)/2],
    [(1-a-b)/2,a,0,(1-a-b)/2,0,b],
    [(1-a-b)/2,b,0,(1-a-b)/2,0,a]]

f1=[[a/2,(1-a)/2,0,a/2,0,(1-a)/2],
    [(1-a-b)/2,b,0,(1-a-b)/2,0,a],
    [(1-a-b)/2,a,0,(1-a-b)/2,0,b],
    [a/2,(1-a)/2,0,a/2,0,(1-a)/2],
    [(1-a-b)/2,b,0,(1-a-b)/2,0,a],
    [(1-a-b)/2,a,0,(1-a-b)/2,0,b]]

f_tilda=[[0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0]]

new_G= [[1,0],  #state 0 action 1
    [1,0],  #state 1 action 1
    [1,0],  #state 2 action 1
    [0,1],  #state 0 action 2
    [0,1],  #state 1 action 2
    [0,1]]  #state 2 action 2


for i in range(len(f0)):
    for j in range(len(f0[0])):
        f_tilda[i][j]=(f0[i][j] *((new_G[i][0]*(1-c[0]))+(new_G[i][1]*(1-c[1])))) + (f1[i][j]*((new_G[i][0]*c[0])+(new_G[i][1]*c[1])))

print("\nNEW F\n"+"-"*10)
print("F0=",f0)
print("F1=",f1)
print("F tilda=",f_tilda)

new_pi0=[0,0,0,0,0,0]
for i in range(len(pi0)):
    new_pi0[i]=pi0[i]*G[i][0]
    new_pi0[i+3]=pi0[i]*G[i][1]

print("Pi(0)=",new_pi0)
prob_0=numpy.matmul(numpy.transpose(new_G),new_pi0)
print("P(0)=",prob_0)
pi1=numpy.matmul(numpy.transpose(f_tilda),new_pi0)
print("Pi(1)=",pi1)
prob_1=numpy.matmul(numpy.transpose(new_G),pi1)
print("P(1)=",prob_1)