import numpy as np

def ChangeCoordinateSystem(cp, R, c0):
    """
    cp: the point(s) of the 3D space that will change its coordinates to another coordinate system
    R: the rotation matrix
    c0: the dispacement vector

    It converts (cp -> dp) the coordinates of the points to a different coordinate system
    
    """

    # Compute the rotation
    temp = []
    if len(cp.shape) == 1:
        dp = np.dot(cp, R)
    else:
        for i in range(cp.shape[0]):
            temp.append(np.dot(cp[i], R))
        dp = np.array(temp)

    # Compute the displacement
    dp = dp + c0.T

    return dp