
def answer():
    s=0
    a=[]
    print("ANSWER")
    print("\n")
    for i in range(n):
        
        for j in range(m):
            if l[i][j]==0:
                
                
                s=s+x1[i][j][2]
                print(i,"---->",j)
                print("\n")
    print(s)
def modify():
    zz=[]
    for i in range(n):
        for j in range(m):
            if l[i][j]==-1 or l[i][j]==0:
                l[i][j]=0
                zz.append([i,j])
    rl=[]
    cl=[]
    sr=set()
    sc=set()
    for i in zz:
        rl.append(i[0])
        sr.add(i[0])
        cl.append(i[1])
        sc.add(i[1])
    rrl=[]
    ccl=[]
    for i in sr:
        rrl.append(['r',i,rl.count(i)])
    for i in sc:
        rrl.append(['c',i,cl.count(i)])
    ccl=sorted(rrl, key = lambda element : element[2],reverse=True)
    
    b1=[]
    b2=[]
    
    c=0
    for i in ccl:
        g=[]
        c1=0
        z=i[1]
        if c==len(zz):
            break
        else:
            if i[0]=='r':
                for j in range(n):
                    if l[z][j]==0:
                        g.append([z,j])
                        
                for  j in g:
                    if j in b2:
                        c1=c1+1
                if i[2]>c1:
                    for j in range(n):
                        if[z,j] not in b2:
                            b2.append([z,j])
                            if l[z][j]==0 :
                                c=c+1
                        else:
                            b1.append([z,j])
            else:
                for j in range(n):
                    if l[j][z]==0:
                        g.append([j,z])
                
                for  j in g:
                    if j in b2:
                        c1=c1+1
                if i[2]>c1:
                    for j in range(n):
                        if [j,z] not in b2:
                            b2.append([j,z])
                            if l[j][z]==0:
                                 c=c+1
                        else:
                            b1.append([j,z])
    b3=[]
    mv=99999999999
    for i in range(n):
        for j in range(n):
            if [i,j] not in b2:
                b3.append([i,j])
    for i in b3:
        a=i[0]
        b=i[1]
        if l[a][b]<mv:
            
            mv=l[a][b]
    for i in range(n):
        for j in range(n):
            if [i,j] in b3:
                l[i][j]=l[i][j]-mv
            if [i,j] in b1:
                l[i][j]=l[i][j]+mv
    step3(l)
            

            
        
        
    
    
        
        
        
    
    
def step1(l):
    print("step:1:")
    print("\n")
    print("select minimum in each row subtract with corresponding row")
    print("\n")
    for i in range(0,n):
        mm=min(l[i])
        for j in range(0,m):
            l[i][j]=l[i][j]-mm
    for i in range(n): 
        for j in range(m): 
            print(l[i][j], end = " ") 
        print()
def step2(l):
    print('\n')
    print("step:2:")
    print("\n")
    print("select minimum in each column subtract with corresponding column")
    print("\n")
    for j in range(m):
            q=[]
            for i in range(n):
                q.append(l[i][j])
            mm=min(q)
            for i in range(n):
                l[i][j]=l[i][j]-mm
    for i in range(n): 
        for j in range(m): 
            print(l[i][j], end = " ") 
        print()
    
    step3(l)

    
def step3(l):
    x=l
    print("\n")
    k=[]
    f=[]
    d=[]
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i][j]==0:
                k.append([i,j])
    for i in range(len(k)):
        a,b=k[i][0],k[i][1]
        c1=-1
        c2=-1
        for j in range(len(l)):
            if x[a][j]==0:
                c1=c1+1
        for p in range(len(l)):
            
            if x[p][b]==0:
                c2=c2+1
        f.append([c1+c2,a,b])
    v=sorted(f, key = lambda element : element[0])
    c=0
    for h in v:
        a=h[1]
        b=h[2]
        if x[a][b]!=-1:
            c=c+1
            for t in range(n):
                if x[a][t]==0 and t!=b:
                    x[a][t]=-1
                    
            for t in range(n):
                if x[t][b]==0 and t!=a:
                    x[t][b]=-1
                    
    if c==n:
        answer()
    else:
        modify()
        
        
print("*******__________ASSIGNMENT PROBLEM__________*******")
print("\n")
n=int(input("enter the row size:"))
print("\n")
m=int(input("enter the column size:"))
print("\n")
print("enter table value based on row wise!!!!")
l=[]
ma=0
for i in range(n):
    for i in input().split(" "):
    l.append(ll)
if n==m:
    print('\n')
    print("\n--------BALANCE-------------\n")
else:
    print("\n")
    print("----------UNBALANCE-----------\n")
    if n>m:
        print("\n")
        print("######-------so add one dummy column\n")
        t=n
        for i in l:
            i.append(0)
        print("\n")
        print("!!!!-------AFTER BALANCE!!!\n")
        for i in range(n): 
            for j in range(m): 
                print(l[i][j], end = " ") 
        print()   
    else:
        print("######-----so add one dummy row\n")
        print("\n")
        ll=[0 for i in range(m)]
        l.append(ll)
        print("!!!!--------AFTER BALANCE!!!\n")
        print("\n")
        display()
for i in range(n):
        for j in range(n):
            if l[i][j]>ma:
                ma=l[i][j]
n=len(l)
print('\n')
print("1.minimization 2.maximization")
k=int(input())
if k==1:
    l=l
else:
    for i in range(n):
        for j in range(n):
            l[i][j]=ma-l[i][j]
    
x1=[]

for i in range(n):
    x2=[]
    for j in range(m):
        x2.append([i,j,l[i][j]])
    x1.append(x2)
if k==1:
    step1(l)
    step2(l)
else:
    ma=0
    for i in range(n):
        if(max(l[i])>ma):
            ma=max(l[i])
    for i in range(n): 
        for j in range(m): 
            l[i][j]=ma-l[i][j]
    step1(l)
    step2(l)
    
