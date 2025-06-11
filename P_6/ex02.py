# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 08:46:45 2025

@author: 22078406
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Step 1: Load image in grayscale
image = cv2.imread('C:/Users/22078406/Documents/DIP ex/Lab6_Test Images/cameraman.bmp', cv2.IMREAD_GRAYSCALE)
image = image.astype(np.float64)  # Convert to float64 for FFT

# Step 2: Fourier Transform
fourier_coeff = np.fft.fft2(image)
fourier_coeff_center = np.fft.fftshift(fourier_coeff)

# Step 3: Compute spectrum and log-spectrum
spectrum = np.abs(fourier_coeff_center)
spectrum_log = np.log(1 + spectrum)

# Step 4: Compute phase
phase = np.angle(fourier_coeff_center)
phase_abs = np.abs(phase)

# Step 5: Plot all in one figure
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(spectrum, cmap='gray')
plt.title("Spectrum")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(spectrum_log, cmap='gray')
plt.title("Log Spectrum")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(phase_abs, cmap='gray')
plt.title("Phase")
plt.axis('off')

plt.tight_layout()
plt.show()
# Step 6: Inverse Fourier Transform
# Shift back
fourier_coeff_origin = np.fft.ifftshift(fourier_coeff_center)
# Inverse FFT
reconstructed_image = np.fft.ifft2(fourier_coeff_origin)
# Since result is complex, take real part
reconstructed_image_real = np.real(reconstructed_image)
# Step 7: Visualize the reconstructed image
plt.figure(figsize=(5, 5))
plt.imshow(reconstructed_image_real, cmap='gray')
plt.title("Reconstructed Image")
plt.axis('off')
plt.show()
# Step 8: Save the reconstructed image
cv2.imwrite('reconstructed_image.png', reconstructed_image_real.astype(np.uint8))
# Step 9: Save the phase image
cv2.imwrite('phase_image.png', (phase_abs * 255 / np.max(phase_abs)).astype(np.uint8))
# Step 10: Save the log spectrum image
log_spectrum_image = (spectrum_log * 255 / np.max(spectrum_log)).astype(np.uint8)
cv2.imwrite('log_spectrum_image.png', log_spectrum_image)
# Step 11: Save the original image
cv2.imwrite('original_image.png', image.astype(np.uint8))
# Step 12: Save the spectrum image
spectrum_image = (spectrum * 255 / np.max(spectrum)).astype(np.uint8)               