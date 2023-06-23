from calculate_normals import *
from PerspectiveCamera import *
from gouraud import *
from phong import *
from Imaging import rasterize
import statistics as stats

def render_object(shader, focal, eye, lookat, up, bg_color, M, N, H, W, verts, vert_colors, faces, mat, lights, light_amb):
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
    p2d, depth = CameraLookingAt(focal, eye, lookat, up, verts)

    # Rasterize the 2D image
    n2d = rasterize(p2d, M, N, H, W)

    # Create the canvas
    img = np.full((M, N, 3), bg_color)

    # Find the depths of the triangles
    k = faces.shape[1]
    tri_depths = np.zeros(k)
    for i in range(k):
        depths = [depth[faces[0][i]], depth[faces[1][i]], depth[faces[2][i]]]
        tri_depths[i] = stats.mean(depths)

    # Sort the depths and keep the indices' changes
    indices = np.argsort(tri_depths)

    # Paint the triangles
    if shader == "gouraud":
        # paint the triangles
        for i in reversed(range(k)):
            tri_face = faces[indices[i]]
            vertsp = [verts[tri_face[0]], verts[tri_face[1]], verts[tri_face[2]]]
            vertsn = [normals[tri_face[0]], normals[tri_face[1]], normals[tri_face[2]]]
            vertsc = [vert_colors[tri_face[0]], vert_colors[tri_face[1]], vert_colors[tri_face[2]]]
            bcoords = np.mean(vertsp, axis=0)
            img = shade_gouraud(vertsp, vertsn, vertsc, bcoords, eye, mat, lights, light_amb, img)
    elif shader == "phong":
        # paint the triangles
        for i in reversed(range(k)):
            tri_face = faces[indices[i]]
            vertsp = [verts[tri_face[0]], verts[tri_face[1]], verts[tri_face[2]]]
            vertsn = [normals[tri_face[0]], normals[tri_face[1]], normals[tri_face[2]]]
            vertsc = [vert_colors[tri_face[0]], vert_colors[tri_face[1]], vert_colors[tri_face[2]]]
            bcoords = np.mean(vertsp, axis=0)
            img = shade_phong(vertsp, vertsn, vertsc, bcoords, eye, mat, lights, light_amb, img)
    return img