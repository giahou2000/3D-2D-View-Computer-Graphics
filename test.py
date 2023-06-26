import numpy as np
import matplotlib.pyplot

data = np.load('h3.npy', allow_pickle=True)
verts = data[()]['verts']
face_indices = data[()]['face_indices']
vertex_colors = data[()]['vertex_colors']
cam_eye = data[()]['cam_eye']
cam_up = data[()]['cam_up']
cam_lookat = data[()]['cam_lookat']
ka, kd, ks, n = data[()]['ka'], data[()]['kd'], data[()]['ks'], data[()]['n']
light_positions = data[()]['light_positions']
light_intensities = data[()]['light_intensities']
light_ambiance = data[()]['Ia']
M, N, W, H = data[()]['M'], data[()]['N'], data[()]['W'], data[()]['H']
bg_color = data[()]['bg_color']
focal = data[()]['focal']

print(kd)
print(ks)
print(n)