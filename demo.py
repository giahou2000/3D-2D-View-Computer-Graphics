import numpy as np
import matplotlib.pyplot
from lightSource import *

# Load and separate the data of the 3D image
data = np.load('h3.npy', allow_pickle=True)
verts = data[()]['verts']
face_indices = data[()]['face_indices']
vertex_colors = data[()]['vertex_colors']
cam_eye = data[()]['cam_eye']
cam_up = data[()]['cam_up']
cam_lookat = data[()]['cam_lookat']
ka = data[()]['ka']
kd, ks, n = data[()]['kd'], data[()]['ks'], data[()]['n']
light_positions = data[()]['light_positions']
light_intensities = data[()]['light_intensities']
M, N, W, H = data[()]['M'], data[()]['N'], data[()]['W'], data[()]['H']
bg_color = data[()]['bg_color']
focal = data[()]['focal']

# Create the light source objects list
lights = []
for i in range(len(light_positions)):
    obj = PointLight(light_positions[i], light_intensities[i])
    lights.append(obj)

# Gouraud shader

# ambient

# diffusion

# specular

# combination

# Phong shader

# ambient

# diffusion

# specular

# combination