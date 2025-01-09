import os

def count_images_in_datasets(file_path):
    datasets = {
        "ApolloScapeExtra": 0,
        "BDD100K": 0,
        "Cityscapes": 0,
        "DIML_indoor": 0,
        "GoogleLandmark": 0,
        "Holopix50k": 0,
        "NYU": 0,
        "Object365": 0
    }

    total_images = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # 跳过空行
            parts = line.split()
            if len(parts) != 2:
                print(f"格式错误的行: {line}")
                continue  # 跳过格式错误的行
            rgb_path, depth_path = parts
            for dataset in datasets:
                if dataset in rgb_path:
                    datasets[dataset] += 1
                    total_images += 1
                    break

    return datasets, total_images

if __name__ == "__main__":
    file_path = "/home/chenwu/pseudo_label/train.txt"  # 替换为你的文件路径

    if os.path.exists(file_path):
        datasets, total_images = count_images_in_datasets(file_path)
        for dataset, count in datasets.items():
            print(f"{dataset}: {count} 张图片")
        print(f"总共: {total_images} 张图片")
    else:
        print(f"文件 {file_path} 不存在")

# 自动驾驶数据集再弄30w张
# Object365和GoogleLandmark分别再弄10w张