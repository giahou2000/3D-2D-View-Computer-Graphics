import numpy as np

def rasterize(p2d, Rows, Columns, H, W):
    """
    p2d: the coordinates of the points of the camera system
    Rows: height for the final image
    Columns: width for the final image
    H: dimension of the camera canvas in inches
    W: dimension of the camera canvas in inches

    It rasterizes the points of the image and scales them properly to fit in a new canvas.
    
    """
    # Create an empty list
    n2d = []

    # Calculate scaling factors
    scale_y = Rows / H
    scale_x = Columns / W

    # Rasterize image
    for point in p2d:
        x = round((point[0] + W/2) * scale_x)
        y = round((point[1] + H/2) * scale_y)
        n2d.append([x, y])
    n2d = np.array(n2d)
    
    return n2d