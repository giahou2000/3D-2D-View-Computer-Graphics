def light(point, normal, vcolor, cam_pos, mat, lights):
    I = 0

    # Ambient light component
    ambiance = []
    for i in range(len(lights)):
        ambiance.append(vcolor + mat.ka * lights[0].intensity)

    # Diffuse light component

    # Specular light component

    # Combination

    return I