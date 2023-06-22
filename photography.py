from calculate_normals import *
from PerspectiveCamera import *
from gouraud import *
from phong import *
from Imaging import rasterize

def render_object(shader, focal, eye, lookat, up, bg_color, M, N, H, W, verts, vert_colors, faces, mat, n, lights, light_amb):
    """
    % shader = the string that defines what shading method is selected
    % focal = the distance of the frame from the camera center
    % eye = the coordinates of the camera
    % lookat = the coordinates of where the camera looks
    % up = the up vector of the camera
    % bg_color = the background color of the canvas
    % M, N = the dimensions of the final image
    % H, W = the dimensions of the frame of the camera
    % verts = 3xNv array, the vertices of the triangles
    % vert_colors = 3xNv array, the color for each vertex
    % faces = 3xNt array, the points that shape the triangles
    % mat = a PhongMaterial object
    % lights = a list of PointLight objects
    % light_amb = the ambiance
    """
    # Calculate normal vectors
    normals = calculate_normals(verts, faces)

    # Calculate the projection
    p2d, depth = CameraLookingAt(focal, eye, lookat, up, p3d)

    # Rasterize the 2D image
    n2d = rasterize(p2d, Rows, Columns, H, W)

    # Paint the triangles
    if shader == "gouraud":
        img = shade_gouraud(vertsp, vertsn, vertsc, bcoords, cam_pos, mat, lights, light_amb, X)
    elif shader == "phong":
        img = shade_phong(vertsp, vertsn, vertsc, bcoords, cam_pos, mat, lights, light_ambX)
    return img