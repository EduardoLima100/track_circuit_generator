import random
import matplotlib.pyplot as plt
import numpy as np 
from scipy import interpolate
plt.rcParams['figure.figsize'] = (10,10)

comprimento = 20 #mínimo 20
tamanho = comprimento/4
npontos = 500

fim = 0
while fim==0:
    X = [0]
    Y = [0]
    
    i = 0
    k = 0
    while i<comprimento-1:
        a = X[-1]+random.randint(-1,1)
        b = Y[-1]+random.randint(-1,1)
        
        f = 0
        for j in range(len(X)-1):
            if ((X[j]-a)**2+(Y[j]-b)**2)**(1/2)<=1:
                f = 1
        
        if len(X)>1:
            if ((X[-2]-a)**2+(Y[-2]-b)**2)**(1/2)<=2:
                f = 1
        
        if f == 0 and abs(a)<tamanho and abs(b)<tamanho:
            X.append(a)
            Y.append(b)
            i=i+1
            k = 0
            
        k=k+1
        
        if k > 10:
            del X[-1]
            del Y[-1]
            i = i-1

  
        if i>=comprimento*0.7:
            if X[1]*-1==X[-1] and Y[1]*-1==Y[-1]:
                X.append(0)
                Y.append(0)
                if ((X[-3])**2+(Y[-3])**2)**(1/2)>2:
                    fim = 1
                    i = comprimento
    

plt.plot(X, Y, "-",0,0,'.')
plt.autoscale(enable=True, axis='both', tight=None)
plt.axis('square')
plt.grid()
plt.show()

print("Comprimento = ",len(X))

X.append(X[1])
Y.append(Y[1])
#X.append(X[2])
#Y.append(Y[2])

x = np.array(X)
y = np.array(Y)
tck, u = interpolate.splprep([x, y], s=0)
unew = np.arange(0, 1, 1/npontos)
out = interpolate.splev(unew, tck)

X4 = []
Y4 = []
med_X=[]
med_Y=[]
for i in range(len(out[0])):
    if X[1]>0:
        if Y[1]>0:
            if out[0][i]>=0 and out[0][i]<=1 and out[1][i]>=0 and out[1][i]<=1:
                med_X.append(out[0][i])
                med_Y.append(out[1][i])
            else:
                X4.append(out[0][i])
                Y4.append(out[1][i])
                
            
        else:
            if out[0][i]>=0 and out[0][i]<=1 and out[1][i]<=0 and out[1][i]>=-1:
                med_X.append(out[0][i])
                med_Y.append(out[1][i])
            else:
                X4.append(out[0][i])
                Y4.append(out[1][i])
               
    else:
        if Y[1]>0:
            if out[0][i]>=-1 and out[0][i]<=0 and out[1][i]>=0 and out[1][i]<=1:
                med_X.append(out[0][i])
                med_Y.append(out[1][i])
            else:
                X4.append(out[0][i])
                Y4.append(out[1][i])
                
        else:
            if out[0][i]>=-1 and out[0][i]<=0 and out[1][i]<=0 and out[1][i]>=-1:
                med_X.append(out[0][i])
                med_Y.append(out[1][i])
            else:
                X4.append(out[0][i])
                Y4.append(out[1][i])
                
X1 = []
Y1 = []
X2 = []
Y2 = []
i = 0
while i < 1000:
    if ((med_X[i]-med_X[i+1])**2+(med_Y[i]-med_Y[i+1])**2)**(1/2)<0.5:
        X1.append(med_X[i])
        Y1.append(med_Y[i])
    else:
        i = i + 1
        for j in range(i,len(med_X)):
            X2.append(med_X[j])
            Y2.append(med_Y[j])
        i = 1000
    i = i + 1
    


X3 = []
Y3 = []
for i in range(len(X1)):
    X3.append((X1[i]+X2[i])/2)
    Y3.append((Y1[i]+Y2[i])/2)

plt.plot(X3,Y3,'-r',out[0], out[1],'-',0,0,'.')
plt.axis('square')
plt.grid()
plt.show()

del(X4[0])
del(Y4[0])

for i in range(len(X3)):
    X4.append(X3[i])
    Y4.append(Y3[i])

X4.append((X4[-1]+X4[0])/2)
Y4.append((Y4[-1]+Y4[0])/2)

plt.plot(X4,Y4,'-',0,0,'.')
plt.axis('square')
plt.grid()
plt.show()
    
pontos = []
for i in range(len(X4)):
    pontos.append(np.array([X4[i],Y4[i]]))



