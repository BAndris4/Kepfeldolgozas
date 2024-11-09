Képfeldolgozás
==============

### Kép beolvasása

```python
img = cv2.imread(path, mode)
```


### Kép méretezése


```python
img = cv2.resize(img, dsize=(0,0), fx=x, fy=y)

img = cv2.resize(img, (500, 500))
```

### Kép megjelenítése

```python
cv2.imshow("Kép neve", img)
cv2.waitKey(0)
```
### Színkoverziók

```python
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
```

### Homályosítás

```python
box_blurred = cv2.boxFilter(img, -1, kSize)
gaussian_blurred = cv2.GaussianBlur(img, kSize, 0)
median_blurred = cv2.medianBlur(img, kValue) # Zajszűréshez
```

### Élesítés

```python
blurred_img = cv2.GaussianBlur(noise_img, (7,7), 1)
unsharped = cv2.addWeighted(noise_img, 2.5, blurred_img, -1.5, 0)
```

### Maszkolás (csak 1 érték alapján)

```python
img = cv2.imread(path, mode)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

h_lower = h >= 100
h_upper = h <= 120
mask = np.bitwise_and(h_lower, h_upper)

h[mask] += 50
output = cv2.merge([h, s, v], 3)
output = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
```

### Maszkolás (több érték alapján)

```python
img = cv2.imread(path, mode)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)

increased_hue = hsv[:, :, 0] + 50
image_increased = cv2.merge([increased_hue, hsv[:, :, 1], hsv[:, :, 2]])
image_increased = cv2.cvtColor(image_increased, cv2.COLOR_HSV2BGR)

output = np.zeros_like(img)
output[mask > 0] = image_increased[mask > 0]
output[mask == 0] = img[mask == 0]
```

### Maszkolás (változó érték alapján)
* Hue <= 2 * küszöbölés értéke
* 50 <= Saturation <= 170
* 100 <= Value <= 200

```python
mask = cv2.inRange(hsv, (0, 50, 100), (180, 170, 200))
condition = (image[..., 0] <= 2 * threshold_value)
mask = mask & condition.astype(np.uint8) * 255

output = np.zeros_like(img)
output[mask > 0] = img[mask > 0]
```

### Hisztogram

* **Szürkeárnyalatos kép**

```python
from matplotlib import pyplot as plt

hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist_original)
plt.xlim([0, 256])
plt.ylim([0, 2500])
plt.show()
```

* **Színes kép**

```python
from matplotlib import pyplot as plt

colors = ('b', 'g', 'r')
plt.figure()
for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title('RGB Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0, 256])
plt.ylim([0, 2500])
plt.show()
```

### Hisztogramkiegyenlítés

* **Szürkeárnyalatos kép**

```python
equalized_img = cv2.equalizeHist(img)
```

* **Színes kép**

```python
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
value = hsv[:, :, 2]
equalizedValue = cv2.equalizeHist(value)
hsv[:, :, 2] = equalizedValue
equalized_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
```

### Küszöbölés
* **Manuális küszöbölés**
    * **Bizonyos érték alapján való küszöbölés**

    ```python
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_img)
    saturation_threshold = int(input("Saturation küszöbértéke (0-255): "))
    mask = s > saturation_threshold

    high_saturation_img = np.zeros_like(img)
    high_saturation_img[mask] = img[mask]
    ```

    * **Több érték alapján**

    ```python
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_img)
    hue_threshold_min = int(input("Hue küszöbértéke (0-179): "))
    saturation_threshold = int(input("Saturation küszöbértéke (0-255): "))
    value_threshold = int(input("Value küszöbértéke (0-255): "))
    mask_hue = h > hue_threshold_min
    mask_saturation = s > saturation_threshold
    mask_value = v > value_threshold
    final_mask = mask_hue & mask_saturation & mask_value

    filtered_img = np.zeros_like(img)
    filtered_img[final_mask] = img[final_mask]
    ```

    * **Szürkeárnyalatos kép küszöbölése**

    ```python
    _, mask = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
    thresholded_img = cv2.bitwise_and(img, img, mask=mask)
    ```

* **Adaptív küszöbölés**
```python
thresholded_img_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, 2)
```


### Hue értékek
* **0-10**  
![](/hues/0-10.jpg)
* **10-20**  
![](/hues/10-20.jpg)
* **20-30**  
![](/hues/20-30.jpg)
* **30-40**  
![](/hues/30-40.jpg)
* **40-50**  
![](/hues/40-50.jpg)
* **50-60**  
![](/hues/50-60.jpg)
* **60-70**  
![](/hues/60-70.jpg)
* **70-80**  
![](/hues/70-80.jpg)
* **80-90**  
![](/hues/80-90.jpg)
* **90-100**  
![](/hues/90-100.jpg)
* **100-110**  
![](/hues/100-110.jpg)
* **110-120**  
![](/hues/110-120.jpg)
* **120-130**  
![](/hues/120-130.jpg)
* **130-140**  
![](/hues/130-140.jpg)
* **140-150**  
![](/hues/140-150.jpg)
* **150-160**  
![](/hues/150-160.jpg)
* **160-170**  
![](/hues/160-170.jpg)
* **170-180**  
![](/hues/170-180.jpg)
