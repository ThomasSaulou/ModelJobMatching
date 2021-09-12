import numpy.linalg
import numpy as np
from numpy import diag
A = np.array([[1, 2, 3], [4, 5, 6],[4, 5, 2],[3,2,4]])
b = np.array([10,11,12,14])

U, D, Vt = np.linalg.svd(A, full_matrices=True)
S=diag(D)
bprim=np.dot(np.transpose(U), b)
print(D)
y=bprim[:len(D)]/D
h=np.dot(np.transpose(Vt),y)
print('h',h)



# for i in range(len(S)):
#     bprim[i]/=D[i]
# y=bprim[:3,:3]
# print(Vt)
# h=np.transpose(Vt)*y
# print(h)

# import numpy as np

# z = np.linalg.solve(A,b)
# print(z)




