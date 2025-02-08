from PIL import Image
import hashlib
import numpy as np
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def image_entropy(image_path):
    gray_image = Image.open(image_path).convert("L")
    pixels = np.array(gray_image)
    total_pixels = pixels.size

    hist, _ = np.histogram(pixels.flatten(), bins=256, range=(0, 256))
    prob = hist / total_pixels

    entropy = -np.sum(prob * np.log2(prob + 1e-10))
    return entropy


entropy = image_entropy("img (43).jpg")
if entropy > 7:
    print(f"Good entropy. Image entropy: {entropy:.2f} bits")
elif 7 > entropy > 3:
    print(f"Not that good. Image entropy: {entropy:.2f} bits")

def extract_bits_from_image(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())
    byte_stream = bytearray()

    for r, g, b in pixels:
        byte_stream.extend([r, g, b])

    return bytes(byte_stream)


def generate_secure_seed(byte_data):
    return hashlib.sha256(byte_data).digest()


def generate_cryptographic_random(seed, num_bytes=16):
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=num_bytes,
        salt=None,
        info=b'image-seed-random',
        backend=default_backend()
    )
    return hkdf.derive(seed)


def main():
    image_path = "img (43).jpg"

    try:
        byte_data = extract_bits_from_image(image_path)

        seed = generate_secure_seed(byte_data)
        print(f"Seed (SHA-256): {seed.hex()}")

        random_bytes = generate_cryptographic_random(seed, num_bytes=16)
        print(f"Random bytes (16 bytes): {random_bytes.hex()}")


        random_int = int.from_bytes(random_bytes, byteorder='big')
        print(f"Random Integer: {random_int}")

    except FileNotFoundError:
        print(f"Archive error '{image_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()