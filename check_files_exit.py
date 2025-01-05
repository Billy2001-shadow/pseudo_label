import os

filelist_path = 'imagenet21k.txt'
with open(filelist_path, 'r') as f:
    filelist = [line.strip() for line in f if line.strip()]  # 过滤掉空行

for line in filelist:
    if os.path.exists(line):
        print(f"{line} exists.")
    else:
        print(f"{line} does not exist.")
        exit()


    # img_path = line.split()[0]
    # depth_path = line.split()[1]

    # # depth_path = os.path.splitext(img_path)[0] + '.npy'
    # # img_dir, img_filename = os.path.split(img_path)
    # # depth_filename = os.path.splitext(img_filename)[0] + '.npy'
    # # depth_path = os.path.join(img_dir, depth_filename)
    # if os.path.exists(img_path) and os.path.exists(depth_path):
    #     print(f"Both {img_path} and {depth_path} exist.")
    # else:
    #     print(f"Either {img_path} or {depth_path} does not exist.")
    #     exit()