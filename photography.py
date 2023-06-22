from calculate_normals import *
from PerspectiveCamera import *
from gouraud import *
from phong import *

def render_object(shader, focal, eye, lookat, up, bg_color, M, N, H, W, verts, vert_colors, faces, mat, n, lights, light_amb):
    # Calculate normal vectors
    normals = calculate_normals(verts, faces)

    # Calculate the projection
    p2d, depth = CameraLookingAt(focal, eye, lookat, up, p3d)

    # Paint the triangles
    if shader == "gouraud":
        img = shade_gouraud(vertsp, vertsn, vertsc, bcoords, cam_pos, mat, lights, light_amb, X)
    elif shader == "phong":
        img = shade_phong(vertsp, vertsn, vertsc, bcoords, cam_pos, mat, lights, light_ambX)
    return img