import torch
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
# print(torch.__version__)               # 应显示类似 2.5.0+cu124（或 cu121）
# print(torch.cuda.is_available())        # 应为 True
# print(torch.cuda.get_device_name(0))    # 应显示 GPU 名称 "NVIDIA GeForce RTX 5060"

