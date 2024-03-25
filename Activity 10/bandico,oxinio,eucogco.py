import numpy as np
import matplotlib.pyplot as plt

INPUT_IMAGE_PATH = "stop.jpg"
IMAGE_SIZE = 256

def compute_2d_complex_sinusoid(size, freq_x, freq_y, coefficient):
    values = np.arange(size)
    x, y = np.meshgrid(values, values)
    return coefficient * np.exp(2j * np.pi / size * (freq_x * x + freq_y * y)) / (size ** 2)

def compute_fft(image):
    return np.fft.fft2(image)

def normalize_image(image):
    return (image - np.min(image)) / (np.max(image) - np.min(image))

def normalize_fft(fft):
    fft_mag = np.abs(fft)
    fft_mag[fft_mag < 1e-20] = 1e-20
    return 10 * np.log10(fft_mag)

def get_fft_pixel_position(size, freq_x, freq_y):
    
    img_x = (freq_x + size // 2) % size
    img_y = (freq_y + size // 2) % size
    return img_x, img_y

def highlight_fft_pixel(ax, freq_x, freq_y, size):
    img_x, img_y = get_fft_pixel_position(size, freq_x, freq_y)
    circle = plt.Circle(
        (img_x, img_y),
        radius=5,
        fill=True,
        linewidth=1,
        facecolor="#ff0000aa",
        edgecolor="#00000055"
    )
    ax.add_patch(circle)

def mark_fft_pixel_as_visited(ax, freq_x, freq_y, size, visited_fft_image):
    img_x, img_y = get_fft_pixel_position(size, freq_x, freq_y)
    visited_fft_image[img_y, img_x] = 1

def animate(step, fft, visited_fft_image, image, layer, ax_fft, ax_layer):
    if step >= len(fft):
        print("Finished")
        return

    x, y = step

    coefficient = fft[y, x] * (1 if x == 0 else 2)
    sinusoid = compute_2d_complex_sinusoid(len(fft), x, y, coefficient)
    sinusoid = np.real(sinusoid)
    image += sinusoid

    vmin, vmax = -np.abs(coefficient) / (len(fft) ** 2), np.abs(coefficient) / (len(fft) ** 2)
    layer[:] = sinusoid
    layer.clip(vmin, vmax, out=layer)
    layer *= 2 ** (layer < 0) * 2 ** (layer > 0)

    ax_layer.imshow(layer, cmap="gray")
    ax_layer.set_title(f"Sinusoid freq x={x} y={y}")

    ax_fft.imshow(visited_fft_image, cmap="gray")
    ax_fft.set_title("FFT")
    highlight_fft_pixel(ax_fft, x, y, len(fft))

image = plt.imread(INPUT_IMAGE_PATH)
image = image.mean(axis=2) / 255.0

image_fft = compute_fft(image)
image_fft_shift = np.fft.fftshift(image_fft)

magnitude_spectrum = 20 * np.log((np.abs(image_fft_shift) + 1))

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image, cmap="gray")
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(magnitude_spectrum, cmap="gray")
ax2.title.set_text('FFT of image')


def reconstruct_image(fft):
    return np.fft.ifft2(fft).real

reconstructed_image = reconstruct_image(image_fft)

reconstructed_fft = compute_fft(reconstructed_image)

normalized_reconstructed_fft = normalize_fft(reconstructed_fft)

ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(reconstructed_image, cmap="gray")
ax3.title.set_text('Reconstructed Image')

ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(normalized_reconstructed_fft, cmap="gray")
ax4.title.set_text('FFT of Reconstructed Image')



plt.show()
