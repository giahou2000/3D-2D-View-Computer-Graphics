import numpy as np

def light(point, normal, vcolor, cam_pos, mat, lights, light_amb):
    """
    point: the 3d coordinates of the point on which the light arrives
    normal: coordinates of the normal vector of the surface at the point
    vcolor: the color of the point
    cam_pos: coordinates of the camera
    mat: PhongMaterial object
    lights: list of PointLight objects
    light_amb: ambiance vector
    """

    # Ambient light component
    ambiance = mat.ka * light_amb

    # Diffuse light component
    diffusions = []
    for i in range(len(lights)):
        # Compute the L vector that is parallel to incoming light beams
        L = lights[i].pos - point
        # Compute the fatt attenuation coefficient
        L = L / np.linalg.norm(L)
        diffusions.append(lights[i].intensity * mat.kd * np.dot(normal, L))

    # Specular light component
    speculars = []
    V = (cam_pos - point) / np.linalg.norm(cam_pos - point)
    for i in range(len(lights)):
        L = (lights[i].pos - point)
        # Compute the fatt attenuation coefficient
        L = L / np.linalg.norm(L)
        dotNL = np.dot(normal, L)
        speculars.append(lights[i].intensity * mat.ks * (np.dot((2 * normal * dotNL - L), V) ** mat.n))

    # Combination
    I = ambiance + np.sum(diffusions, axis=0) + np.sum(speculars, axis=0)
    return I