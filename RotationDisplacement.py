from RotationMatrix import rotmat
import numpy as np

def RotateTranslate(cp, theta, u, A, t):

    """
    cp: a point in 3D space
    theta: the angle of clockwise rotation
    u: vector parallel to the axis of rotation
    A: point of the axis of rotation
    t: displacement vector

    It rotates the given points at a 3D plain by computing the rotation matrix and then it shifts them by t.
    
    """

    # Calculate the rotation matrix
    R = rotmat(theta, u)
    
    # Shift the point cp to a coordinate system centered at point A
    shifted_cp = cp - A

    # Rotate the shifted points
    temp = []
    for i in range(shifted_cp.shape[0]):
        temp.append(np.dot(shifted_cp[i], R))
    rotated_cp = np.array(temp)
    
    # Shift the rotated point back to the original coordinate system
    rotated_cp = rotated_cp + A

    # Shift the points about a distance of t
    cq = rotated_cp + t

    return cq