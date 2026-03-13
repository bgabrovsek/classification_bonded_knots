import knotpy as kp

pd1 = "V[0,1,2],V[3,4,5],X[0,6,7,3],X[6,2,8,9],X[10,5,11,12],X[12,8,1,10],X[9,11,4,7]"
pd2= "V[0,1,2],V[3,4,5],X[0,6,7,8],X[6,9,5,7],X[10,8,4,11],X[12,3,9,2],X[1,10,11,12]"

k1 = kp.from_pd_notation(pd1)
k2 = kp.from_pd_notation(pd2)

print(kp.yamada(k1))
print(kp.yamada(k2))