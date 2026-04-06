import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
#reads and loads images
chad_image = cv2.imread('chad.jpg')
image = cv2.imread('yuji.jpg')
#checks if images are there or not
if chad_image is None or image is None:
    print("Error: one or both images not found.")
    exit()
#gets image dimensions and extracts them
chad_image_H, chad_image_W = chad_image.shape[:2]
image_H, image_W = image.shape[:2]
#resize  the bigger image to fit small one
if chad_image_H * chad_image_W < image_H * image_W:
    image = cv2.resize(image, (chad_image_W, chad_image_H))
else:
    chad_image = cv2.resize(chad_image, (image_W, image_H))

cell_size = 5
h, w = chad_image.shape[:2]
rows = h // cell_size
cols = w // cell_size
#calculates brightness of every cell in chad image and image to be chadified
image_brightness=[]
chad_brightness=[]
for r in range(rows):
    for c in range(cols):
        image_cell = image[r*cell_size:(r+1)*cell_size, c*cell_size:(c+1)*cell_size]
        brightness = np.mean(image_cell)
        image_brightness.append(brightness)

for r in range(rows):
    for c in range(cols):
        chad_cell = chad_image[r*cell_size:(r+1)*cell_size, c*cell_size:(c+1)*cell_size]
        brightness = np.mean(chad_cell)
        chad_brightness.append(brightness)
#looks for the pixel in image with similar brightnes to pixel in chad
matches=[]
for i in range(len(chad_brightness)):
    diffrences=np.abs(np.array(image_brightness) - chad_brightness[i])
    best_match=np.argmin(diffrences)
    matches.append(best_match)
#animation
num_frames=60
fig, ax=plt.subplots()
#wait to show image before tranfromation
ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
ax.set_title('Before...')
ax.axis('off')
plt.pause(3)

def update(frame):
    ax.clear()
    t = frame / (num_frames - 1)
    canvas = np.zeros_like(chad_image)
    for i in range(len(chad_brightness)):
        chad_r = i // cols
        chad_c = i % cols
        image_r = matches[i] // cols
        image_c = matches[i] % cols
        current_r = int(image_r + (chad_r - image_r) * t)
        current_c = int(image_c + (chad_c - image_c) * t)
        current_r = np.clip(current_r, 0, rows - 1)
        current_c = np.clip(current_c, 0, cols - 1)
        image_cell = image[image_r*cell_size:(image_r+1)*cell_size, image_c*cell_size:(image_c+1)*cell_size]
        canvas[current_r*cell_size:(current_r+1)*cell_size, current_c*cell_size:(current_c+1)*cell_size] = image_cell
    ax.imshow(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
    ax.set_title(f'Chadifying... {int(t*100)}%')
    ax.axis('off')

ani = FuncAnimation(fig, update, frames=num_frames, interval=50,repeat=False)
plt.show()