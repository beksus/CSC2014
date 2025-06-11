# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 08:39:06 2025

@author: 22078406
"""

import numpy as np
import cv2
from matplotlib import pyplot as pt

# Step 1: Create a simple image
simple_image = np.zeros((256, 256), dtype=np.float64)
simple_image[124:132, 124:132] = 255

# Step 2: Perform the Fourier Transform
fourier_coeff = np.fft.fft2(simple_image)
fourier_coeff_center = np.fft.fftshift(fourier_coeff)

# Step 3: Compute spectrum
spectrum = np.abs(fourier_coeff_center)
spectrum_log = np.log(1 + spectrum)

# Step 4: Visualize original, spectrum and log spectrum
pt.figure()
pt.subplot(2, 2, 1)
pt.imshow(simple_image, cmap='gray')
pt.title("Simple Image")

pt.subplot(2, 2, 2)
pt.imshow(spectrum, cmap='gray')
pt.title("Spectrum Before Log Enhanced")

pt.subplot(2, 2, 3)
pt.imshow(spectrum_log, cmap='gray')
pt.title("Spectrum After Log Enhanced")

# Step 5: Inverse transform
# Shift back
fourier_coeff_origin = np.fft.ifftshift(fourier_coeff_center)

# Inverse FFT
reconstructed_image = np.fft.ifft2(fourier_coeff_origin)

# Since result is complex, take real part
reconstructed_image_real = np.real(reconstructed_image)

# Step 6: Visualize the reconstructed image
pt.subplot(2, 2, 4)
pt.imshow(reconstructed_image_real, cmap='gray')
pt.title("Reconstructed Image")

pt.tight_layout()
pt.show()
