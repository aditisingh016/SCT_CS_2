import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# Function to display images
def display_image(image, title):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()


# XOR encryption function
def xor_encrypt(image, key=123):
    return cv2.bitwise_xor(image, key)


# Pixel swapping encryption function
def swap_encrypt(image):
    swapped = image.copy()
    h, w, _ = swapped.shape
    for i in range(0, h - 1, 2):
        for j in range(0, w - 1, 2):
            swapped[i,
                    j], swapped[i + 1,
                                j + 1] = swapped[i + 1, j +
                                                 1].copy(), swapped[i,
                                                                    j].copy()
    return swapped


# Pixel swapping decryption (same as encryption for 2x2 swap)
def swap_decrypt(image):
    return swap_encrypt(image)


# Save encrypted image
def save_image(image, filename):
    cv2.imwrite(filename, image)
    print(f"✅ Saved: {filename}")


# Load image
def load_image():
    path = "tiger.png"  # or ask user input
    if not os.path.exists(path):
        print("❌ Image not found!")
        return None
    return cv2.imread(path)


# Menu
def main():
    while True:
        print("\n=== IMAGE ENCRYPTION TOOL ===")
        print("1. XOR Encryption")
        print("2. Pixel Swap Encryption")
        print("3. XOR Decryption")
        print("4. Pixel Swap Decryption")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("❌ Invalid choice. Try again.")
            continue

        if choice == '5':
            print("👋 Exiting...")
            break

        image = load_image()
        if image is None:
            continue

        if choice == '1':
            encrypted = xor_encrypt(image)
            display_image(encrypted, "🔐 XOR Encrypted Image")
            save_image(encrypted, "xor_encrypted.png")

        elif choice == '2':
            encrypted = swap_encrypt(image)
            display_image(encrypted, "🔀 Swap Encrypted Image")
            save_image(encrypted, "swap_encrypted.png")

        elif choice == '3':
            encrypted = cv2.imread("xor_encrypted.png")
            decrypted = xor_encrypt(encrypted)
            display_image(decrypted, "🔓 XOR Decrypted Image")
            save_image(decrypted, "xor_decrypted.png")

        elif choice == '4':
            encrypted = cv2.imread("swap_encrypted.png")
            decrypted = swap_decrypt(encrypted)
            display_image(decrypted, "🔁 Swap Decrypted Image")
            save_image(decrypted, "swap_decrypted.png")


if __name__ == "__main__":
    main()
