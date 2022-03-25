'''
Copyright 2022 Astrobiology Center (Madrid)

This file software allows to create RGB postage stamps for noiseless TNG50 images (0.01 arcsec/px).

@Author: Luca Costantin (lcostantin@cab.inta-csic.es)

:SPDX-License-Identifier: GPL-3.0+
:License-Filename: LICENSE.txt

:History:
25 Mar 22:  version 1.0
'''

import os
import argparse
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.convolution import convolve
from astropy.visualization import AsinhStretch, ZScaleInterval, make_lupton_rgb

matplotlib.use('Agg') 

plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.rcParams['axes.titlesize'] = 22
plt.rcParams['axes.labelsize'] = 22
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18

__version__ = '1.0.0'


def check_directory(path):
	'''Create a directory if it does not exist.
	'''
	if (os.path.isdir(path) == False):
		os.mkdir(path)

def convolve_psf(image,filter):
	'''Convolve for JWST NIRCam PSF.
	'''
	SW_filters = {'F070W', 'F090W', 'F115W', '140M', 'F150W', 'F162M', 'F164N', 'F182M', 'F187N', 'F200W', 'F210M', 'F212N'}
	LW_filters = {'F250M', 'F277W', 'F300M', 'F323N', 'F335M', 'F356W', 'F360M', 'F405N', 'F410M', 'F430M', 'F444W', 'F460M', 'F466N', 'F470N', 'F480M'}

	if filter in SW_filters:
		psf_file = f'/NIRCam_PSF/nircam_nrcb1_{filter.lower()}_clear_fovp401_samp1_predicted_realization0.fits'

	if filter in LW_filters:
		psf_file = f'/NIRCam_PSF/nircam_nrcb5_{filter.lower()}_clear_fovp401_samp1_predicted_realization0.fits'

	psf = fits.getdata(psf_file)

	psf_norm = psf/np.sum(psf)

	convolved_image = convolve(image,psf_norm)

	return convolved_image

def make_plot(image_R, image_G, image_B, wcs):
	'''Combine the three images.
	'''
	abs_path = os.path.abspath(os.getcwd())

	fig = plt.figure(figsize=(9,9))

	forCasting = np.float_()    

	r = np.array(image_R,forCasting)
	g = np.array(image_G,forCasting)
	b = np.array(image_B,forCasting)

	stretch = AsinhStretch(a=0.3) + ZScaleInterval(contrast=0.0001)

	r = stretch(r)
	g = stretch(g)
	b = stretch(b)

	lo_val, up_val = np.percentile(np.hstack((r.flatten(), g.flatten(), b.flatten())), (70, 99.5))  # Get the value of lower and upper 0.5% of all pixels
	stretch_val    = up_val - lo_val
	
	rgb_default = make_lupton_rgb(r, g, b, minimum=lo_val, stretch=stretch_val, Q=1)

	plt.subplot(projection=wcs)
	plt.imshow(rgb_default, origin='lower')
	plt.grid(color='white', ls='solid')
	plt.xlabel('Right Ascension')
	plt.ylabel('Declination')
	plt.title(f'galaxy ID {args.id}')

	plt.savefig(f'{abs_path}/TEST_RGB.png',bbox_inches='tight')
	
def filter_selection(i_a, redshift, filter):
	'''Select the filters for RGB colors and match the pixel scale.
	'''
	abs_path = os.path.abspath(os.getcwd())

	NIRCam_filters = ['F070W', 'F090W', 'F115W', 'F140M', 'F150W', 'F162M', 'F164N', 'F182M', 'F187N', 'F200W', 'F210M', 'F212N',
					  'F250M', 'F277W', 'F300M', 'F323N', 'F335M', 'F356W', 'F360M', 'F405N', 'F410M', 'F430M', 'F444W', 'F460M', 'F466N', 'F470N', 'F480M']

	ext = NIRCam_filters.index(filter)

	fits_image_filename = f'{abs_path}/RELEASE_TNG50_v1/TNG50/{args.id}_{i_a}_z{redshift}_TNG50.fits'

	V = os.path.exists(fits_image_filename)

	if V==True:
		with fits.open(fits_image_filename) as hdu:
			image = hdu[0].data
			image = image[ext,:,:]
			wcs = WCS(hdu[0].header, naxis=2)

	return image, wcs


if __name__ == "__main__":	

	parser = argparse.ArgumentParser(description='Create RGB images of noiseless TNG50 galaxies')
	parser.add_argument("--id", help='"ID of the galaxy (default: 0)"', nargs='?', type=int, choices=range(0,999999), const=0, default=0)
	parser.add_argument("--f1", help='"Filter for R image (default: 0)"', nargs='?', type=str, choices=('F070W', 'F090W', 'F115W', 'F140M', 'F150W', 
																										'F162M', 'F164N', 'F182M', 'F187N', 'F200W', 
																										'F210M', 'F212N', 'F250M', 'F277W', 'F300M', 
																										'F323N', 'F335M', 'F356W', 'F360M', 'F405N', 
																										'F410M', 'F430M', 'F444W', 'F460M', 'F466N', 
																										'F470N', 'F480M'), const='F090W', default='F200W')
	parser.add_argument("--f2", help='"Filter for G image (default: 0)"', nargs='?', type=str, choices=('F070W', 'F090W', 'F115W', 'F140M', 'F150W', 
																										'F162M', 'F164N', 'F182M', 'F187N', 'F200W', 
																										'F210M', 'F212N', 'F250M', 'F277W', 'F300M', 
																										'F323N', 'F335M', 'F356W', 'F360M', 'F405N', 
																										'F410M', 'F430M', 'F444W', 'F460M', 'F466N', 
																										'F470N', 'F480M'), const='F115W', default='F356W')
	parser.add_argument("--f3", help='"Filter for B image (default: 0)"', nargs='?', type=str, choices=('F070W', 'F090W', 'F115W', 'F140M', 'F150W', 
																										'F162M', 'F164N', 'F182M', 'F187N', 'F200W', 
																										'F210M', 'F212N', 'F250M', 'F277W', 'F300M', 
																										'F323N', 'F335M', 'F356W', 'F360M', 'F405N', 
																										'F410M', 'F430M', 'F444W', 'F460M', 'F466N', 
																										'F470N', 'F480M'), const='F200W', default='F444W')
	parser.add_argument("--psf", help='"Convolve for JWST PSF (default: 0)"', nargs='?', type=int, choices=(0,1), const=0, default=0)
	parser.add_argument("--overwrite", help='"Overwrite previous results (default: 0)"', nargs='?', type=int, choices=(0,1), const=0, default=0)
	args = parser.parse_args()

	i_a = 'i0_a0'
	redshift = 3

	image_r, wcs_r = filter_selection(i_a=i_a, redshift=redshift, filter=args.f1)
	image_g, wcs_g = filter_selection(i_a=i_a, redshift=redshift, filter=args.f2)
	image_b, wcs_b = filter_selection(i_a=i_a, redshift=redshift, filter=args.f3)

	make_plot(image_r,image_g,image_b,wcs_r)
