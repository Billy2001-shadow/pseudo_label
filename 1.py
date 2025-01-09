import os

# 遍历一个目录下的所有文件，包括子目录，然后把文件路径写入到一个 txt 文件中
def list_files_recursive(directory, output_file):
    with open(output_file, 'w') as f:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                f.write(file_path + '\n')
                print(f"写入文件路径: {file_path}")  # 添加调试信息

if __name__ == "__main__":
    directory = "/mnt/chenwu/Relative_depth/ApolloScapeExtra/imgs"  # 替换为你的文件夹路径
    output_file = "ApolloScapeExtra_imgs.txt"  # 替换为你想要输出的txt文件路径

    if os.path.exists(directory):
        list_files_recursive(directory, output_file)
        print(f"文件路径已写入到 {output_file}")
    else:
        print(f"目录 {directory} 不存在")




# import os

# # 指定源目录和输出文件
# src_dir = "/data2/cw/Relative_depth/ImageNet21K/imgs/"
# output_file = "/home/chenwu/pseudo_label/imagenet21k.txt"

# # 获取源目录下的所有 .jpg 文件
# filenames = [f for f in os.listdir(src_dir) if f.endswith('.JPEG')]

# # 将文件名写入到输出文件
# with open(output_file, 'w') as f:
#     for filename in filenames:
#         f.write(f"{filename}\n")

# print(f"All .jpg filenames have been written to '{output_file}'.")


# import os

# def list_files_recursive(directory, output_file):
#     with open(output_file, 'a') as f:
#         for root, _, files in os.walk(directory):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 f.write(file_path + '\n')
#                 print(f"写入文件路径: {file_path}")  # 添加调试信息

# if __name__ == "__main__":
#     directory = "/mnt/chenwu/Relative_depth/ApolloScapeExtra/road03_seg/ColorImage/"  # 替换为你的文件夹路径
#     output_file = "ApolloScapeExtra.txt"  # 替换为你想要输出的txt文件路径

#     if os.path.exists(directory):
#         list_files_recursive(directory, output_file)
#         print(f"文件路径已写入到 {output_file}")
#     else:
#         print(f"目录 {directory} 不存在")




# import os
# import shutil

# def list_and_copy_files_recursive(source_directory, target_directory):
#     if not os.path.exists(target_directory):
#         os.makedirs(target_directory)
    
#     for root, _, files in os.walk(source_directory):
#         for file in files:
#             source_file_path = os.path.join(root, file)
#             target_file_path = os.path.join(target_directory, file)
#             shutil.copy2(source_file_path, target_file_path)
#             print(f"复制文件: {source_file_path} 到 {target_file_path}")

# if __name__ == "__main__":
#     source_directory = "/mnt/chenwu/Relative_depth/Cityscapes/leftImg8bit_trainvaltest/leftImg8bit/"  # 替换为你的源文件夹路径
#     target_directory = "/mnt/chenwu/Relative_depth/Cityscapes/imgs/"  # 替换为你的目标文件夹路径

#     if os.path.exists(source_directory):
#         list_and_copy_files_recursive(source_directory, target_directory)
#         print(f"所有文件已复制到 {target_directory}")
#     else:
#         print(f"源目录 {source_directory} 不存在")

# import os
# import shutil

# def copy_files_from_txt(input_file, target_directory):
#     if not os.path.exists(target_directory):
#         os.makedirs(target_directory)
    
#     with open(input_file, 'r') as infile:
#         for line in infile:
#             file_path = line.strip()
#             if os.path.exists(file_path):
#                 file_name = os.path.basename(file_path)
#                 target_path = os.path.join(target_directory, file_name)
#                 shutil.copy2(file_path, target_path)
#                 print(f"复制文件: {file_path} 到 {target_path}")
#             else:
#                 print(f"文件不存在: {file_path}")

# if __name__ == "__main__":
#     input_file = "Filtered_ApolloScapeExtra.txt"  # 替换为你的输入文件路径
#     target_directory = "/mnt/chenwu/Relative_depth/ApolloScapeExtra/imgs/"  # 替换为你的目标文件夹路径

#     copy_files_from_txt(input_file, target_directory)
#     print(f"所有文件已复制到 {target_directory}")