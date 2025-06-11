# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 08:46:45 2025

@author: 22078406
"""

import numpy as np



import cv2





from matplotlib import pyplot as pt





simple_image = np.zeros ((256,256), dtype=np. float64)



simple_image[124:132,124:132] = 255





fourier_coeff = np.fft. fft2(simple _image)




fourier_coeff_center = np.fft.fftshift(fourier_coeff)



spectrum = np.abs(fourier_coeff_center)




pt. figure()
spectrum_10g = np. 10g(1+spectrum)








pt.subplot (2,2,1)





pt. amshow (simple_image, cmap="gray")




pt. title "Simple Image")



pt. subplot (2,2,2)





pt. imshow(spectrum, cmap="gray")




pt. title("Spectrum Before Log Enhanced")



pt. subplot (2,2,3)





pt. imshow(spectrum_1og, cmap="gray")




pt. title("Spectrum After Log Enhanced")