import numpy as np

def calculate_normals(verts, faces):
    """
    verts: object vertex coordinates
    faces: for each triangle the indices of the vertices of the verts matrix
    """
    crosses = []
    for i in range(faces.shape[1]):
        # Compute the 3 edges and then the cross products
        point1 = verts[faces[0][i]]
        point2 = verts[faces[1][i]]
        point3 = verts[faces[2][i]]
        cross = np.cross(point1 - point2, point1 - point3)
        crosses.append(cross)

    normals = []
    for i in range(verts.shape[1]):
        # Find the new faces
        # First find to which triangles the point exists
        new_faces = []
        for j in range(faces.shape[1]):
            new_faces.append = np.logical_or.reduce((faces[0][j] == i, faces[1][j] == i, faces[2][j] == i))
        # Then add all the vectors of the point vertical to each triangle
        n = np.sum(crosses[new_faces], axis=0)
        # Finally normalize the vector and store it
        normals.append(n / np.linalg.norm(n))

    return normals