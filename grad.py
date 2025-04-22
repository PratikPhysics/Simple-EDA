#Gradient Decent for Linear Regression
# yhat = mx + c
# loss  = ((y-yhat)**2)/N
import numpy as np




# initialise some parameters
x = np.random.randn(10,1)
y = 2*x + np.random.rand()

# Parameters
m = 0.0
c = 0.0

#Hyperparemeter 
learning_rate = 0.01

#Creating Gradient Decent Function
def decent(x,y,m,c,leaning_rate):
    dldm = 0.0
    dldc = 0.0
    N = x.shape[0]
    #interationg the loss function
    #loss = ((y-(mx+c))**2)/N
    for xi,yi in zip(x,y):
        dldm += -2*xi*(yi-(m*xi+c))
        dldc += -2*(yi - (m*xi+c))

    #Making updates to m and c
    m = m - learning_rate*(1/N)*dldm
    c = c - learning_rate*(1/N)*dldc
    return m,c

#Making updates to m,c
for epoch in range(400):
    m,c = decent(x,y,m,c,learning_rate)
    yhat = m*x + c
    loss = np.divide(np.sum((y-yhat)**2,axis=0),x.shape[0])
    print(f'{epoch} : loss is {loss} , parameter m in {m} and c in {c}')
        
