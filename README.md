# Chadify

Chadify takes any image you give it and transforms it into chad. Not by slapping chad's face on top, but by actually rearranging the pixels of your image to form his face. Your colours, your textures, just moved around until they look like him.

## Example



https://github.com/user-attachments/assets/a848b3ec-d0a1-4328-948a-c85594f40f0b



## How it works

The program starts by loading both images and making sure they are the same size. If one is bigger than the other it shrinks the bigger one down rather than blowing the smaller one up, because stretching a small image makes it blurry and harder to work with.

Once both images are the same size the program lays an invisible grid over each one, cutting them both into hundreds of small squares called cells. The size of these cells is something you can control — smaller cells means more detail in the final result but takes longer to run.

For each cell in both images the program calculates the average brightness of the pixels inside it. This gives two lists of numbers — one describing how bright each part of chad's face is, and one describing how bright each part of your image is.

The program then goes through every cell in chad's image and finds the cell in your image whose brightness is closest to it. Dark parts of chad's face get matched to dark cells from your image, bright parts get matched to bright cells. This is what creates the illusion of chad's face built entirely from your image's pixels.

Once every cell has a match the animation plays. Each cell starts at its original position in your image and slides across the screen to where it needs to be to form chad's face. By the time the animation finishes all the cells have arrived at their destinations and chad is staring back at you, made entirely from your image.

## Installation

Make sure you have Python installed then run:

```
pip install opencv-python numpy matplotlib
```

## Usage

1. Clone the repository
2. Place your input image in the project folder and rename it to `yuji.jpg`
3. Place your chad image in the project folder and rename it to `chad.jpg`
4. Run the script:

```
python main.py
```

Your image will appear for 3 seconds then the transformation will begin.

## Configuration

Open `main.py` and adjust these variables to change how the output looks:

| Variable | What it does | Default |
|---|---|---|
| `cell_size` | Size of each cell in pixels. Lower = more detail, slower | 5 |
| `num_frames` | Number of animation steps. Higher = more gradual | 60 |
| `interval` | Milliseconds between frames. Higher = slower animation | 50 |

## Built with

- OpenCV
- NumPy
- Matplotlib
```
