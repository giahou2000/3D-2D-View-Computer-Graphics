import numpy as np
from CoordinateSystems import ChangeCoordinateSystem

def PinHole(f, cv, cx, cy, cz, p3d):
    """
    f: distance between the camera canvas and the camera center
    cv: camera center
    cx: x vector of the camera
    cy: y vector of the camera
    cz: z vector of the camera
    p3d: 3D points
    
    It computes the perspective projections of the 3D points onto the virtual camera sensor.

    """
    
    # Find the rotation matrix for the change coordinates
    rotation_matrix = np.column_stack((cx, cy, cz))

    # Change coordinate system centered to the camera center
    new_p3d = ChangeCoordinateSystem(p3d, rotation_matrix, cv)

    # Compute the projections and the depth for each point
    points_num = new_p3d.shape[0]
    p2d = []
    depth = []
    for i in range(points_num):
        p2d.append([(f * new_p3d[i][0]) / new_p3d[i][2], (f * new_p3d[i][1]) / new_p3d[i][2]])
        depth.append(new_p3d[i][2])
    
    return p2d, depth


def CameraLookingAt(f, cv, cK, cup, p3d):

    """
    f: distance between the camera canvas and the camera center
    cv: camera center
    cK: the point where the camera is directed
    cup: unit up vector
    p3d: 3D points

    It does the same thing as the PinHole camera function, but it computes the cameras vectors first.
    
    """

    # cz component computation
    CK = cK - cv
    CKnorm = np.linalg.norm(CK)
    cz = CK/CKnorm
    cz = np.reshape(cz, (3,))

    # cy component computation
    cup = np.reshape(cup, (3,))
    cz = np.reshape(cz, (3,))
    dot_product = np.dot(cup, cz)
    cz_norm = np.linalg.norm(cz)
    projection = (dot_product / (cz_norm**2)) * cz
    t = cup - projection
    cy = t / np.linalg.norm(t)
    cy = np.reshape(cy, (3,))

    # cx component computation
    cx = np.cross(cy, cz)

    # get the projection
    p2d, depth = PinHole(f, cv, cx, cy, cz, p3d)

    return p2d, depth