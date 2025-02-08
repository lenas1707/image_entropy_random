from PIL import Image
import numpy as np


def image_entropy(image_path):
    gray_image = Image.open(image_path).convert("L")
    pixels = np.array(gray_image)
    total_pixels = pixels.size

    hist, _ = np.histogram(pixels.flatten(), bins=256, range=(0, 256))
    prob = hist / total_pixels

    entropy = -np.sum(prob * np.log2(prob + 1e-10))  # Evita divisão por zero
    return entropy


entropy = image_entropy("img (43).jpg")
print(f"Entropia da imagem: {entropy:.2f} bits")