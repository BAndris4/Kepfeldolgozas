import cv2
import numpy as np
import random

def main():
    # 1. Kép elérési útja és küszöbérték bekérése
    image_path = input("Kérlek add meg a kép elérési útját: ")
    threshold_value = int(input("Kérlek add meg a küszöbértéket: "))
    background_color = tuple(map(int, input("Kérlek add meg a háttér színét (B, G, R) formátumban: ").split()))
    structural_element_size = int(input("Kérlek add meg a strukturális elem méretét: "))

    # 2. Kép betöltése és HSV-re konvertálása
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 3. Maszkolás
    mask = cv2.inRange(hsv_image, (0, 50, 100), (180, 170, 200))
    condition = (image[..., 0] <= 2 * threshold_value)
    mask = mask & condition.astype(np.uint8) * 255

    # Pixelek indexeinek tárolása
    pixel_indices = np.column_stack(np.where(mask > 0))

    # 4. Megmaradó pixelek kiválasztása
    selected_indices = random.sample(range(len(pixel_indices)), len(pixel_indices) // 2)
    selected_mask = np.zeros_like(mask)
    for idx in selected_indices:
        selected_mask[pixel_indices[idx][0], pixel_indices[idx][1]] = 255

    # 5. Háttér szín kitöltése
    output_image = np.full_like(image, background_color, dtype=np.uint8)
    output_image[selected_mask > 0] = image[selected_mask > 0]

    # 6. Apróbb hibák eltüntetése
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (structural_element_size, structural_element_size))
    output_image = cv2.morphologyEx(output_image, cv2.MORPH_CLOSE, kernel)

    # Eredmény megjelenítése
    cv2.imshow("Maszkolt Kép", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()