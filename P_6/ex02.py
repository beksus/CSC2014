# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 08:46:45 2025

@author: 22078406
"""

import numpy as np
import cv2
from matplotlib import pyplot as pt

simple_image = np.zeros((256, 256), dtype=np.float64)
simple_image[124:132, 124:132] = 255
fourier_coeff = np.fft.fft2(simple_image)
fourier_coeff_center = np.fft.fftshift(fourier_coeff)
spectrum = np.abs(fourier_coeff_center)
spectrum_log = np.log(1 + spectrum)
fourier_coeff_origin = np.fft.ifftshift(fourier_coeff_center)
simple_original = np.fft.ifft2(fourier_coeff_origin)
simple_original = np.abs(simple_original)
phase = np.angle(fourier_coeff_center)
phase = np.abs(phase)

pt.figure()
pt.subplot(2, 3, 1)
pt.imshow(simple_image, cmap="gray")
pt.title("Simple Image")
pt.subplot(2, 3, 2)
pt.imshow(spectrum, cmap="gray")
pt.title("Spectrum Before Log Enhanced")
pt.subplot(2, 3, 3)
pt.imshow(spectrum_log, cmap="gray")
pt.title("Spectrum After Log Enhanced")
pt.subplot(2, 3, 4)
pt.imshow(simple_original, cmap="gray")
pt.title("Restructured image")
pt.subplot(2, 3, 5)
pt.imshow(np.abs(simple_image - simple_original), cmap="gray")
pt.title("Difference between simple image and restructured image")
pt.subplot(2, 3, 6)
pt.imshow(phase, cmap="gray")
pt.title("Phase")
pt.tight_layout()
pt.show()