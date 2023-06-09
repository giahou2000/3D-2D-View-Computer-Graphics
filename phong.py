import numpy as np
import interpolate_vector as interpol
from pointLight import light

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

    # Compute the actual color based on the lights for the 3 points
    color = []
    for i in range(3):
        color.append(light(bcoords, vertsn[i], vertsc[i], cam_pos, mat, lights, light_amb))

    # Gouraud painting procedure
    global right_color
    global right_norm

    # find the minimums and maximums for each acme
    # we define acmes by their number (0, 1, 2)
    # acme 0 has peaks 0 and 1
    # acme 1 has peaks 1 and 2
    # acme 2 has peaks 2 and 0
    verts2d = np.array(vertsp)
    xkmin = np.zeros(3)
    xkmax = np.zeros(3)
    ykmin = np.zeros(3)
    ykmax = np.zeros(3)
    for k in range(3):
        xkmin[k] = min(verts2d[k][0], verts2d[(k + 1) % 3][0])
        xkmax[k] = max(verts2d[k][0], verts2d[(k + 1) % 3][0])
        ykmin[k] = min(verts2d[k][1], verts2d[(k + 1) % 3][1])
        ykmax[k] = max(verts2d[k][1], verts2d[(k + 1) % 3][1])
    ymin = int(min(ykmin))
    ymax = int(max(ykmax))
    xmin = int(min(xkmin))
    xmax = int(max(xkmax))

    # find the active peaks and keep some more info for later processing
    activ_peaks = []
    peaks_y_max = []
    middle_peak = []
    for i in range(3):
        # store the active peaks for ymin
        if int(verts2d[i][1]) == ymin:
            activ_peaks.append(verts2d[i])
        # store the peaks for ymax
        elif int(verts2d[i][1]) == ymax:
            peaks_y_max.append(verts2d[i])
        else:
            middle_peak = verts2d[i]
    
    activ_peaks = np.array(activ_peaks)
    peaks_y_max = np.array(peaks_y_max)
    middle_peak = np.array(middle_peak)

    # if the triangle is a single point
    if (xmin == xmax) and (ymin == ymax):
        X[ymin][xmin] = color[0]

    # if the triangle is a horizontal line
    elif ymin == ymax:
        for i in range(3):
            if verts2d[i][0] == xmin:
                left_color = color[i]
                left_norm = vertsn[i]
                left_peak = verts2d[i]
            elif verts2d[i][0] == xmax:
                right_color = color[i]
                right_norm = vertsn[i]
                right_peak = verts2d[i]
        for x in range(xmin, xmax + 1):
            point_normal = interpol.interpolate_vectors(left_peak, right_peak, [x, ymin], left_norm, right_norm)
            point_color = interpol.interpolate_vectors(left_peak, right_peak, [x, ymin], left_color, right_color)
            X[ymin][x] = light(bcoords, point_normal, point_color, cam_pos, mat, lights, light_amb)

    # if the triangle is a vertical line
    elif xmin == xmax:
        for i in range(3):
            if verts2d[i][1] == ymax:
                upper_color = color[i]
                upper_norm = vertsn[i]
                up_peak = verts2d[i]
            elif verts2d[i][1] == ymin:
                lower_color = color[i]
                lower_norm = vertsn[i]
                down_peak = verts2d[i]
        for y in range(ymin, ymax + 1):
            point_normal = interpol.interpolate_vectors(down_peak, up_peak, [xmin, y], lower_norm, upper_norm)
            point_color = interpol.interpolate_vectors(down_peak, up_peak, [xmin, y], lower_color, upper_color)
            X[y][xmin] = light(bcoords, point_normal, point_color, cam_pos, mat, lights, light_amb)

    # if the triangle has a lower horizontal edge
    elif len(activ_peaks) == 2:
        # sort to left and right lower peaks
        activ_peaks = sorted(activ_peaks, key=lambda ap: ap[0])
        # compute the 2 slopes of the edges (inverse slopes to get rid of division by zero and simplify things)
        left_slope = (peaks_y_max[0][0] - activ_peaks[0][0])/(peaks_y_max[0][1] - activ_peaks[0][1])
        right_slope = (activ_peaks[1][0] - peaks_y_max[0][0])/(activ_peaks[1][1] - peaks_y_max[0][1])
        # find the right color for the right peak
        for i in range(3):
            if (verts2d[i][0] == activ_peaks[0][0]) and (verts2d[i][1] == ymin):
                left_color = color[i]
                left_norm = vertsn[i]
            elif (verts2d[i][0] == activ_peaks[1][0]) and (verts2d[i][1] == ymin):
                right_color = color[i]
                right_norm = vertsn[i]
            else:
                upper_color = color[i]
                upper_norm = vertsn[i]
        # paint for each point
        xsmall = activ_peaks[0][0]
        xbig = activ_peaks[1][0]
        for y in range(ymin, ymax + 1):
            color1 = interpol.interpolate_vectors(activ_peaks[0], peaks_y_max[0], [xsmall, y], left_color, upper_color)
            norm1 = interpol.interpolate_vectors(activ_peaks[0], peaks_y_max[0], [xsmall, y], left_norm, upper_norm)
            color2 = interpol.interpolate_vectors(activ_peaks[1], peaks_y_max[0], [xbig, y], right_color, upper_color)
            norm2 = interpol.interpolate_vectors(activ_peaks[1], peaks_y_max[0], [xbig, y], right_norm, upper_norm)
            for x in range(int(xsmall), int(xbig + 1)):
                point_color = interpol.interpolate_vectors([xsmall, y], [xbig, y], [x, y], color1, color2)
                point_normal = interpol.interpolate_vectors([xsmall, y], [xbig, y], [x, y], norm1, norm2)
                X[y][x] = light(bcoords, point_normal, point_color, cam_pos, mat, lights, light_amb)
            xsmall = (y + 1 - ymin) * left_slope + activ_peaks[0][0]
            xbig = (y + 1 - ymin) * right_slope + activ_peaks[1][0]

    # if the triangle has an upper horizontal edge
    elif len(peaks_y_max) == 2:
        # sort to left and right lower peaks
        peaks_y_max = sorted(peaks_y_max, key=lambda ap: ap[0])
        # compute the 2 slopes of the acmes (inverse slopes to get rid of division by zero)
        left_slope = (peaks_y_max[0][0] - activ_peaks[0][0])/(peaks_y_max[0][1] - activ_peaks[0][1])
        right_slope = (activ_peaks[0][0] - peaks_y_max[1][0])/(activ_peaks[0][1] - peaks_y_max[1][1])
        # find the right color for the right peak
        for i in range(3):
            if (verts2d[i][0] == peaks_y_max[0][0]) and (verts2d[i][1] == ymax):
                left_color = color[i]
                left_norm = vertsn[i]
            elif (verts2d[i][0] == peaks_y_max[1][0]) and (verts2d[i][1] == ymax):
                right_color = color[i]
                right_norm = vertsn[i]
            else:
                down_color = color[i]
                down_norm = vertsn[i]
                xsmall = verts2d[i][0]
        # paint for each point
        xsmall = activ_peaks[0][0]
        xbig = xsmall
        for y in range(ymin, ymax + 1):
            color1 = interpol.interpolate_vectors(peaks_y_max[0], activ_peaks[0], [xsmall, y], left_color, down_color)
            norm1 = interpol.interpolate_vectors(peaks_y_max[0], activ_peaks[0], [xsmall, y], left_norm, down_norm)
            color2 = interpol.interpolate_vectors(peaks_y_max[1], activ_peaks[0], [xbig, y], right_color, down_color)
            norm2 = interpol.interpolate_vectors(peaks_y_max[1], activ_peaks[0], [xbig, y], right_norm, down_norm)
            for x in range(int(xsmall), int(xbig + 1)):
                point_color = interpol.interpolate_vectors([xsmall, y], [xbig, y], [x, y], color1, color2)
                point_normal = interpol.interpolate_vectors([xsmall, y], [xbig, y], [x, y], norm1, norm2)
                X[y][x] = light(bcoords, point_normal, point_color, cam_pos, mat, lights, light_amb)
            xsmall = (y + 1 - ymax) * left_slope + peaks_y_max[0][0]
            xbig = (y + 1 - ymax) * right_slope + peaks_y_max[1][0]

    # if the triangle is just any other triangle
    else:
        # compute the x at which there will be the cut
        y_diff = peaks_y_max[0][0] - activ_peaks[0][0]
        slope = 0
        if y_diff == 0:
            x_new = peaks_y_max[0][0]
        else:
            slope = (ymax-ymin)/y_diff
            x_new = peaks_y_max[0][0] + (middle_peak[1] - ymax)/slope
        # the new cut peak
        new_peak = [x_new, middle_peak[1]]
        # create the new triangles after the cut
        # compute the colors
        for i in range(3):
            if (verts2d[i][1] == ymax):
                upper_color = color[i]
                upper_norm = vertsn[i]
            elif (verts2d[i][1] == ymin):
                down_color = color[i]
                down_norm = vertsn[i]
            else:
                middle_color = color[i]
                middle_norm = vertsn[i]
        new_peak = [x_new, middle_peak[1]]
        # create the new triangles after the cut
        vertsp1 = np.array([peaks_y_max[0], middle_peak, new_peak])
        vertsp2 = np.array([middle_peak, new_peak, activ_peaks[0]])
        new_color = interpol.interpolate_vectors(peaks_y_max[0], activ_peaks[0], new_peak, upper_color, down_color)
        new_norm = interpol.interpolate_vectors(peaks_y_max[0], activ_peaks[0], new_peak, upper_norm, down_norm)
        colors1 = [upper_color, middle_color, new_color]
        colors2 = [middle_color, new_color, down_color]
        new_normals1 = [upper_norm, middle_norm, new_norm]
        new_normals2 = [middle_norm, new_norm, down_norm]
        # fill first triangle
        X = shade_phong(vertsp1, new_normals1, colors1, bcoords, cam_pos, mat, lights, light_amb, X)
        # fill second triangle
        X = shade_phong(vertsp2, new_normals2, colors2, bcoords, cam_pos, mat, lights, light_amb, X)

    return X