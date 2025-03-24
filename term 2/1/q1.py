import numpy as np

#Q1
mat1=np.array([[3,2,1,5],[9,1,3,0]])
mat2=np.array([[2,9,0],[1,3,5],[2,4,7],[8,1,5]])
mulmat=np.dot(mat1,mat2)
print(f"A*B={mulmat}")

#Q2
A=np.array([[3,8,-6],[4,10,-1],[-1,9,7]])
detA=np.linalg.det(A)
print(f'A={A}\ndet(A)={detA}')

#Q3
A=np.array([[2,3,1],[3,4,1],[3,7,2]])
inversA=np.linalg.inv(A)
print(f'A={A}\nInvers(A)={inversA}')

#Q4
A=np.array([[0,1],[-2,-3]])
w,v=np.linalg.eig(A)
print(f'EigenVector={w}\nEigenValues={v}')

#Q5
A=np.array([[5,3,6],[0,-2,1],[4,7,2]])
print(f'MatrixNorm={np.linalg.norm(A)}\nRowNorm={np.linalg.norm(A,axis=1)}\nColumnNorm={np.linalg.norm(A,axis=0)}')

#Q6
a=np.array([[1,-1],[2,-1]])
b=np.array([-1,-5])
x=np.linalg.solve(a,b)
print(x)

#Q7
a=np.array([[1,-1,1],[3,1,2],[-5,2,-1]])
b=np.array([10,34,-14])
x=np.linalg.solve(a,b)
print(f'   x  y  z')
print(x)