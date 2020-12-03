#Tạo 1 số nguyên ngẫu nhiên n trong khoảng [50, 1000] đóng vai trò là số phần tử của List
import random
x = []
x = random.randint(50, 1000)
print(x)
# Sinh ngẫu nhiên 1 List các số nguyên trong khoảng [-1000, 1000]
import numpy as np
x = np.random.randint(-1000, 1000, dtype = int)
print(x)
#Sinh ngẫu nhiên 1 List các số thực trong khoảng [-1000.0, 1000.0]
import numpy as np
x = np.random.uniform(-1000.0,1000.0)
print(x)    
    

