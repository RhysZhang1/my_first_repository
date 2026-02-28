import numpy as np
# a=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# a=np.array(a,dtype=int)               #转换为np的数组,dtype定义数据类型：int,float, int默认32，float默认64
# print(a)
# x=a.ndim   ;print(x) #几维数组
# y=a.shape  ;print(y) #形状（行，列）
# z=a.size   ;print(z) #其中有多少个元素

# a=np.zeros((x,y),dtype=int)  #生成一个x行y列全为零的数组(zero全为0，ones全为1)
a=np.arange(12).reshape(3,4)       #用法等同于range,reshape规定行列
print(a)