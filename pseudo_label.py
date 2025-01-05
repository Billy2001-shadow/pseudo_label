import argparse
import cv2
import glob
import matplotlib
import numpy as np
import os
import torch

from depth_anything_v2.dpt import DepthAnythingV2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Depth Anything V2')
    
    parser.add_argument('--img-path', default='imagenet21k.txt' ,type=str)
    parser.add_argument('--input-size', type=int, default=518)
    
    parser.add_argument('--encoder', type=str, default='vitl', choices=['vits', 'vitb', 'vitl', 'vitg'])
    
    args = parser.parse_args()
    
    DEVICE = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
    
    model_configs = {
        'vits': {'encoder': 'vits', 'features': 64, 'out_channels': [48, 96, 192, 384]},
        'vitb': {'encoder': 'vitb', 'features': 128, 'out_channels': [96, 192, 384, 768]},
        'vitl': {'encoder': 'vitl', 'features': 256, 'out_channels': [256, 512, 1024, 1024]},
        'vitg': {'encoder': 'vitg', 'features': 384, 'out_channels': [1536, 1536, 1536, 1536]}
    }
    
    depth_anything = DepthAnythingV2(**model_configs[args.encoder])
    depth_anything.load_state_dict(torch.load(f'checkpoints/depth_anything_v2_{args.encoder}.pth', map_location='cpu'))
    depth_anything = depth_anything.to(DEVICE).eval()
    
    if os.path.isfile(args.img_path):
        if args.img_path.endswith('txt'):
            with open(args.img_path, 'r') as f:
                filenames = f.read().splitlines() 
        else:
            filenames = [args.img_path]
    else:
        filenames = glob.glob(os.path.join(args.img_path, '**/*'), recursive=True)
    
  
    
    cmap = matplotlib.colormaps.get_cmap('Spectral_r')
    
    for k, filename in enumerate(filenames):
        print(f'Progress {k+1}/{len(filenames)}: {filename}')
        raw_image = cv2.imread(filename)
        
        depth = depth_anything.infer_image(raw_image, args.input_size) 
        
        # 将深度图线性缩放到 uint16 的动态范围 [0, 65535]
        depth_scaled = (depth - depth.min()) / (depth.max() - depth.min()) * 65535.0
        depth_scaled = depth_scaled.astype(np.uint16)

        save_name = os.path.splitext(os.path.basename(filename))[0] + '.png'
        outdir =  os.path.join(os.path.dirname(os.path.dirname(filename)) ,'pseudo_label')
        save_path = os.path.join(outdir, save_name)
      
        cv2.imwrite(save_path, depth_scaled)
       


      