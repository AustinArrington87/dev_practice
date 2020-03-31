#  https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

from __future__ import print_function
import torch
import numpy as np

# construct 5x3 matrix, uninitialized 
x = torch.empty(5,3)
print(x)

# randomly initialized matrix
x = torch.rand(5,3)
print(x)

# matrix w 0s - dtype long
x = torch.zeros(5, 3, dtype=torch.long)
print(x)

## create tensor directly from data
x = torch.tensor([5.5, 3])
print(x)

# create tensor from existing tensor
x = x.new_ones(5, 3, dtype=torch.double)
print(x)
# override data type
x = torch.randn_like(x, dtype=torch.float)
print(x)

# get size of matrix / tennsorr
print(x.size())

# Operations syntax
y = torch.rand(5,3)
print(x+y)
# alternatively
print(torch.add(x,y))

# providing output tensor as argument
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

# addition in-place
# adds x to y 
y.add_(x)
print(y)

# numpy indexing 
print(x[:, 1])
print(x[:, 2]) 

## resizing / reshaping Tensor
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)
print(x.size(), y.size(), z.size())

# if you only have 1 element in a tensor, use .item
x = torch.randn(1)
print(x)
print(x.item())

###### NUMPY Bridge
# converting Torch Tensor to NumPy array
a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

# watch numpy change value
a.add_(1)
print(a)
print(b)

### Convert NumPy array to Torch Tensor
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)

# CUDa Tensors
if torch.cuda.is_available():
    device = torch.device("cuda")
    y = torch.ones_like(x, device=device)
    x = x.to(device)
    z = x+y
    print(z)
    print(z.to("cpu", torch.double))














