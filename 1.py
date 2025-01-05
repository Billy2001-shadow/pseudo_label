import os

# 指定源目录和输出文件
src_dir = "/data2/cw/Relative_depth/ImageNet21K/imgs/"
output_file = "/home/chenwu/pseudo_label/imagenet21k.txt"

# 获取源目录下的所有 .jpg 文件
filenames = [f for f in os.listdir(src_dir) if f.endswith('.JPEG')]

# 将文件名写入到输出文件
with open(output_file, 'w') as f:
    for filename in filenames:
        f.write(f"{filename}\n")

print(f"All .jpg filenames have been written to '{output_file}'.")