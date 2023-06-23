import numpy as np
import matplotlib.pyplot
from lightSource import *
from photography import *
from material import *

# Load and separate the data of the 3D imaging system
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
light_amb = data[()]['Ia']
M, N, W, H = data[()]['M'], data[()]['N'], data[()]['W'], data[()]['H']
bg_color = data[()]['bg_color']
focal = data[()]['focal']

# Create the light source objects list
lights = []
for i in range(len(light_positions)):
    obj = PointLight(light_positions[i], light_intensities[i])
    lights.append(obj)

# Let's see!!!
k = face_indices.shape[1]
print('The image has ')
print(k)
print('triangles')

# # Gouraud shader
shader = "gouraud"

# ambiance
mat = PhongMaterial(ka, 0, 0, n)
img = render_object(shader, focal, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, lights, light_amb)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.savefig('gouraud_ambiance.png')
matplotlib.pyplot.show()

# diffusion
mat = PhongMaterial(0, kd, 0, n)
img = render_object(shader, focal, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, lights, light_amb)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.savefig('gouraud_diffusion.png')
matplotlib.pyplot.show()

# specular
mat = PhongMaterial(0, 0, ks, n)
img = render_object(shader, focal, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, lights, light_amb)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.savefig('gouraud_specular.png')
matplotlib.pyplot.show()

# combination
mat = PhongMaterial(ka, kd, ks, n)
img = render_object(shader, focal, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, lights, light_amb)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.savefig('gouraud_combination.png')
matplotlib.pyplot.show()


# # Phong shader
shader = "phong"

# # ambient
# mat = PhongMaterial(ka, 0, 0, n)
# img = render_object(shader, focal, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, lights, light_amb)
# matplotlib.pyplot.imshow(img)
# matplotlib.pyplot.savefig('phong_ambiance.png')
# matplotlib.pyplot.show()

# # diffusion
# mat = PhongMaterial(0, kd, 0, n)
# img = render_object(shader, focal, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, lights, light_amb)
# matplotlib.pyplot.imshow(img)
# matplotlib.pyplot.savefig('phong_diffusion.png')
# matplotlib.pyplot.show()

# # specular
# mat = PhongMaterial(0, 0, ks, n)
# img = render_object(shader, focal, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, lights, light_amb)
# matplotlib.pyplot.imshow(img)
# matplotlib.pyplot.savefig('phong_specular.png')
# matplotlib.pyplot.show()

# # combination
# mat = PhongMaterial(ka, kd, ks, n)
# img = render_object(shader, focal, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, lights, light_amb)
# matplotlib.pyplot.imshow(img)
# matplotlib.pyplot.savefig('phong_combination.png')
# matplotlib.pyplot.show()