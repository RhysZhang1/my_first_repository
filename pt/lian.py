# import torch
#
# # 1. 检查 CUDA 是否可用
# print("CUDA available:", torch.cuda.is_available())
#
# if torch.cuda.is_available():
#     # 2. 查看 GPU 数量
#     print("GPU count:", torch.cuda.device_count())
#     # 3. 获取当前 GPU 名称
#     print("Current GPU:", torch.cuda.get_device_name(torch.cuda.current_device()))
#
#     # 4. 创建一个张量并移动到 GPU
#     x = torch.tensor([1.0, 2.0, 3.0]).cuda()
#     print("Tensor on GPU:", x)
#
#     # 5. 执行简单运算
#     y = x * 2
#     print("Result on GPU:", y)
#
#     # 6. 将结果移回 CPU
#     print("Result on CPU:", y.cpu())
# else:
#     print("CUDA not available. Please check your PyTorch installation.")
#
#测试
# print(torch.__version__)               # 应显示类似 2.5.0+cu124（或 cu121）
# print(torch.cuda.is_available())        # 应为 True
# print(torch.cuda.get_device_name(0))    # 应显示 GPU 名称 "NVIDIA GeForce RTX 5060"

#数据读取
# from torch.utils.data import Dataset
# from PIL import Image
# import os
# class mydata(Dataset):
#     def __init__(self,root_dir,label_dir):
#         self.root_dir=root_dir
#         self.label_dir=label_dir
#         self.path=os.path.join(self.root_dir,self.label_dir)
#         self.img_path=os.listdir(self.path)
#     def __getitem__(self, idx):
#         img_name=self.img_path[idx]
#         img_item_path=os.path.join(self.root_dir,self.label_dir,img_name)
#         img=Image.open(img_item_path)
#         label=self.label_dir
#         return img,label
#     def __len__(self):
#         return len(self.img_path)
#
# root_dir='C:\\Users\\rhys1\\Desktop\\zane_project\\python\\pt\\pra\\hymenoptera_data\\train'
# ants_label_dir='ants'
# bees_label_dir='bees'
# ants_dataset=mydata(root_dir,ants_label_dir)
# bees_dataset=mydata(root_dir,bees_label_dir)
# train_dataset=ants_dataset+bees_dataset
# img,label=train_dataset[0]
# img.show()

from torch.utils.tensorboard import SummaryWriter
writer=SummaryWriter('logs')
# writer.add_image()
for i in range(100):
    writer.add_scalar('y=2x',3*i,i)
writer.close()
# #tensorboard --logdir=logs  查看

