# https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html#sphx-glr-beginner-blitz-autograd-tutorial-py

# autograd - automatic differientation

from __future__ import print_function
import torch
import numpy as np

# track computation on a tensor
x = torch.ones(2, 2, requires_grad=True)
print(x)
# tensor operation 
y = x+2
print(y)
# do more operations
z = y * y * 3
out = z.mean()
print(z, out)
###
a = torch.randn(2,2)
a = ((a * 3) / (a - 1))
print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b = (a * a).sum()
print(b.grad_fn)
# backdrop
out.backward()
print(x.grad)

# vector Jacobian product
x = torch.randn(3, requires_grad=True)
y = x*2
while y.data.norm() < 1000:
    y = y*2
print(y)

# pass vector bakwards arg
v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)
print(x.grad)

# stop autograd 
print(x.requires_grad)
print((x ** 2).requires_grad)

with torch.no_grad():
    print((x ** 2).requires_grad)

# can also use 'detach'
print(x.requires_grad)
y = x.detach()
print(y.requires_grad)
print(x.eq(y).all())





