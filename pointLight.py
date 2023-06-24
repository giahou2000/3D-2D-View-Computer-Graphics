import numpy as np

def light(point, normal, vcolor, cam_pos, mat, lights, light_amb):
    """
    point: the 3d coordinates of the point on which the light arrives
    normal: coordinates of the normal vector of the surface at the point
    vcolor: the color of the point
    cam_pos: coordinates of the camera
    mat: PhongMaterial object
    lights: list of PointLight objects
    """

    # Ambient light component
    ambiance = mat.ka * light_amb

    # Diffuse light component
    diffusions = []
    for i in range(len(lights)):
        # Compute the L vector that is parallel to light beams
        L = lights[i].pos - point
        # Compute the fatt attenuation coefficient
        fatt = 1/np.linalg.norm(L)
        L = L / np.linalg.norm(L)
        diffusions.append(lights[i].intensity * mat.kd * min(1, fatt) * np.dot(normal, L))

    # Specular light component
    speculars = []
    V = (cam_pos - point) / np.linalg.norm(cam_pos - point)
    dotNL = np.dot(normal, L)
    for i in range(len(lights)):
        L = (lights[i].pos - point)
        # Compute the fatt attenuation coefficient
        fatt = 1/np.linalg.norm(L)
        L = L / np.linalg.norm(L)
        dotNL = np.dot(normal, L)
        speculars.append(lights[i].intensity * min(1, fatt) * mat.ks * (np.dot((2 * normal * dotNL - L), V) ** mat.n))

    # Combination
    I = vcolor + ambiance + np.sum(diffusions) + np.sum(speculars)
    return I