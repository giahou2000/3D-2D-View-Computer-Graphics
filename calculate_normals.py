import numpy as np

def calculate_normals(verts, faces):
    """
    verts: object vertex coordinates
    faces: for each triangle the indices of the vertices of the verts matrix
    """
    crosses = []
    for i in range(faces.shape[1]):
        # Compute the 3 edges and find the cross 
        point1 = verts[faces[0][i]]
        point2 = verts[faces[1][i]]
        point3 = verts[faces[2][i]]
        cross = np.cross(point1 - point2, point1 - point3)
        crosses.append(cross)

    normals = []
    for i in range(verts.shape[1]):
        # Find the new faces
        new_faces = np.logical_or.reduce((faces[:, 0] == i, faces[:, 1] == i, faces[:, 2] == i))
        n = np.sum(crosses[:, new_faces], axis=1)
        normals[:, i] = n / np.linalg.norm(n)

    return normals