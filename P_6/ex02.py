# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 08:46:45 2025

@author: 22078406
"""

import numpy as np
8
9

10
import cv2
11
from matplotlib import pyplot as
12
simple_image = np.zeros ((256,256), dtype=np.float64)
13
simple_image[124:132,124:132] = 255
14
fourier_coeff = np.fft.fft2(simple_image)
15
fourier_coeff_center = np. fft.fftshift(fourier_coeff)
16
spectrum = np. abs(fourier_coeff_center)
17
spectrum_log = np. 10g(1+spectrum)
18
fourier_coeff_origin = np. fft. ifftshift(fourier_coeff_center)
19
simple_original = np.fft.ifft2(fourier_coeff_origin)
20
simple_original = np.abs(simple_original)
21
phase = np. angle(fourier_coeff_center)
22
phase = np.abs (phase)
23
pt. figure()
24
pt. subplot(2,3,1)
25
pt. imshow(simple_image, cmap="gray")
26
pt. title("Simple Image")
27
pt. subplot (2,3,2)
28
pt. imshow (spectrum, cmap="gray")
29
pt. title("Spectrum Before Log Enhanced")
30
pt. subplot (2,3,3)
31
pt. imshow(spectrum_ log, cmap="gray")
32
pt. title("Spectrum After Log Enhanced")
33
pt. subplot (2,3,4)
34
pt. imshow(simple_original, cmap="gray")
35
pt. title("Restructured image")
36
pt. subplot (2,3,5)
37
pt. imshow(np. abs (simple_image - simple _original), cmap="gray")
38
pt. title("Difference between simple image and restructered image")
39
pt. subplot (2,3,6)
40
pt. imshow phase, cmap="gray")
41
pt. title( "Phase")
42
pt. tight_layout ()
43
pt. show()