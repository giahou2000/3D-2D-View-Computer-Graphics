def shade_phong(vertsp, vertsn, vertsc, bcoords, cam_pos, mat, lights, light_amb, X):
    """
    vertsp = 2x3 array, the 2d coordinates for each vertex
    vertsn = 3x3 array, the normal vectors of the triangle
    vertsc = 3x3 array, the colors of the vertices
    bcoords = 3x1 array, the gravity center of the triangle
    cam_pos = 3x1 array, the coordinates of the camera center
    mat = a PhongMaterial object
    lights = a list of PointLight objects
    light_amb = the ambiance
    X = the partially painted canvas
    """



    return X