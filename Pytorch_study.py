import torch
from torch.autograd import Variable
import numpy as np

np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
print(
    '\nnumpy:\n', np_data,
    '\ntorch:\n', torch_data,
    '\ntensor2array:\n', tensor2array,
)

# abs
data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)

print(
    '\nabs',
    '\nnumpy:', np.abs(data),
    '\ntorch', torch.abs(tensor)
)

print(
    '\nasin',
    '\nnumpy:', np.sin(data),
    '\ntorch', torch.sin(tensor)
)

data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)
data = np.array(data)
print(
    '\nnumpy:', np.matmul(data, data),
    '\nnumpy:', data.dot(data),
    '\ntorch:', torch.mm(tensor, tensor),
    # '\ntorch:', tensor.dot(tensor), 报错，只能计算一维？
)

tensor = torch.rand(3,4)

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

# 判断当前环境GPU是否可用, 然后将tensor导入GPU内运行
if torch.cuda.is_available():
    print('True')
    tensor = tensor.to('cuda')

