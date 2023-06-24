import numpy as np
import matplotlib.pyplot

data = np.load('h3.npy', allow_pickle=True)
M, N, W, H = data[()]['M'], data[()]['N'], data[()]['W'], data[()]['H']
bg_color = data[()]['bg_color']

print(bg_color)

img = np.full((M, N, 3), [0.42, 0.734, 0.245])

matplotlib.pyplot.imshow(img)
matplotlib.pyplot.show()