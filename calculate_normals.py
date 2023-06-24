import numpy as np

def calculate_normals(verts, faces):
    """
    verts: object vertex coordinates
    faces: for each triangle the indices of the vertices of the verts matrix
    """
    # For each triangle compute the cross products/vertical vectors to the surfaces
    crosses = []
    verts = np.transpose(verts)
    for i in range(faces.shape[1]):
        # Compute the 3 edges and then the cross products of the 2 vertices
        point1 = verts[faces[0][i]]
        point2 = verts[faces[1][i]]
        point3 = verts[faces[2][i]]
        crosses.append(np.cross(point1 - point2, point1 - point3))
    crosses = np.array(crosses)

    normals = []
    for i in range(verts.shape[0]):
        # Find the faces where vertex belongs
        vert_faces = []
        for j in range(faces.shape[1]):
            vert_faces.append(np.logical_or.reduce((faces[0][j] == i, faces[1][j] == i, faces[2][j] == i)))
        # Then add all the vectors of the point vertical to each triangle
        vert_faces = np.array(vert_faces)
        n = np.sum(crosses[vert_faces], axis=0)
        # Finally normalize the vector and store it
        normals.append(n / np.linalg.norm(n))

    return normals