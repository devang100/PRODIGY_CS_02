import numpy as np
from PIL import Image
import os

def load_image(image_path):
    image = Image.open(image_path)
    return np.array(image)

def save_image(image_array, output_path):
    image = Image.fromarray(image_array)
    image.save(output_path)

def encrypt_image(image_array, key):
    np.random.seed(key)
    shuffled_indices = np.random.permutation(image_array.size)
    flattened_image = image_array.flatten()
    encrypted_flattened_image = flattened_image[shuffled_indices]
    encrypted_image = encrypted_flattened_image.reshape(image_array.shape)
    return encrypted_image, shuffled_indices

def decrypt_image(encrypted_image_array, key, shuffled_indices):
    np.random.seed(key)
    unshuffled_indices = np.argsort(shuffled_indices)
    flattened_encrypted_image = encrypted_image_array.flatten()
    decrypted_flattened_image = flattened_encrypted_image[unshuffled_indices]
    decrypted_image = decrypted_flattened_image.reshape(encrypted_image_array.shape)
    return decrypted_image

def main():
    print("Image Encryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice.")
        return

    image_path = input("Enter the path to the image: ")
    if not os.path.exists(image_path):
        print("Image not found.")
        return

    key = int(input("Enter an encryption key (integer): "))
    
    if choice == '1':
        image_array = load_image(image_path)
        encrypted_image, shuffled_indices = encrypt_image(image_array, key)
        output_path = "encrypted_" + os.path.basename(image_path)
        save_image(encrypted_image, output_path)
        print(f"Encrypted image saved as {output_path}")

        # Save the shuffled indices to a file for decryption
        np.save("shuffled_indices.npy", shuffled_indices)
        print("Shuffled indices saved as shuffled_indices.npy")

    elif choice == '2':
        encrypted_image_array = load_image(image_path)
        shuffled_indices = np.load("shuffled_indices.npy")
        decrypted_image = decrypt_image(encrypted_image_array, key, shuffled_indices)
        output_path = "decrypted_" + os.path.basename(image_path)
        save_image(decrypted_image, output_path)
        print(f"Decrypted image saved as {output_path}")

if __name__ == "__main__":
    main()


# **Title: Embracing Change: Navigating Life's Transitions**

# **Introduction:**
# Life is a journey marked by constant change—a series of transitions that propel us forward, shaping who we are and who we become. Whether it's starting a new job, moving to a different city, or embarking on a new relationship, transitions are inevitable. While they can be daunting, they also offer boundless opportunities for growth and self-discovery.

# **Body:**

# 1. **Embracing the Unknown:**
#    Transitions often thrust us into the unknown, challenging us to step outside our comfort zones and confront uncertainty head-on. While the prospect of change may seem daunting, it also presents an opportunity to embrace new experiences and expand our horizons.

# 2. **Navigating Discomfort:**
#    Transition periods can be uncomfortable and unsettling as we navigate unfamiliar terrain. It's natural to feel a sense of apprehension or fear of the unknown. However, it's essential to recognize that discomfort is an integral part of the growth process. By leaning into discomfort and embracing the challenges that come with change, we can emerge stronger and more resilient.

# 3. **Finding Strength in Resilience:**
#    Resilience is the ability to adapt and bounce back in the face of adversity. During times of transition, cultivating resilience is crucial to overcoming obstacles and weathering life's ups and downs. By fostering a resilient mindset, we can navigate transitions with grace and resilience, emerging stronger and more empowered on the other side.

# 4. **Embracing Growth and Self-Discovery:**
#    Transitions provide fertile ground for growth and self-discovery, offering opportunities to learn, evolve, and redefine ourselves. Whether it's discovering new passions, honing skills, or gaining a deeper understanding of ourselves, transitions are catalysts for personal and professional development.

# **Conclusion:**
# As we journey through life, transitions serve as signposts marking our path forward. While they may present challenges and uncertainties, they also offer opportunities for growth, resilience, and self-discovery. By embracing change with an open heart and a resilient spirit, we can navigate life's transitions with grace and emerge stronger, wiser, and more empowered than ever before.

# **Call to Action:**
# Embrace change as a catalyst for growth and transformation. Lean into discomfort, cultivate resilience, and embrace the journey of self-discovery. Together, let's navigate life's transitions with courage, curiosity, and an unwavering commitment to personal growth.

# **Closing:**
# Life's transitions may be unpredictable and at times challenging, but they also hold the promise of new beginnings and endless possibilities. Embrace change as a natural and inevitable part of the human experience, and let it guide you on a journey of self-discovery, growth, and transformation.