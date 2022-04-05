# ![](https://drive.google.com/uc?export=view&id=1hvEOXvU8-yjt72G6JP4JBnBgHrthcLE5)

This is **ΩMEGA** (**Ω**rigin of the **M**orphological **E**volution of **GA**laxies), a project that aims at studying the morphological evolution of galaxies through time. 

The project description can be found in **Costantin et al. (in prep)**, to which citation is requested if you use these results.

![GitHub last commit](https://img.shields.io/github/last-commit/lcostant/OMEGA?style=plastic)

## Project description

This project provides a catalog of high-redhift galaxies taken from the Illustris TNG50 suite of cosmological simulations ([Pillepich et al. 2019](http://ui.adsabs.harvard.edu/abs/arXiv:1902.05553), [Dylan et al. 2019](https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.3234N/abstract)). For all galaxies at redshift 3<z<6 and more massive than log(M)>9 solar masses, the catalog is composed of synthetic images in all filters available on the NIRCam and MIRI instruments of the James Webb Space Telescope. 

Every image is created starting from the star and gas particles in TNG50, applying radiative transfer calculations using SKIRT v9 ([Camps et al. 2020](https://ui.adsabs.harvard.edu/abs/2020A%26C....3100381C/abstract)).

The noiseless synthetic images can be processed with MIRAGE and MIRISIM simulators for mimicking NIRCam and MIRI observations, respectively. In particular, this project provides NIRCam observations that mimic the observing strategy of the Cosmic Evolution Early Release Science survey ([CEERS](https://ceers.github.io); PI: S. Finkelstein).

The simulated images are reduced with the [official pipeline](https://github.com/spacetelescope/jwst), adapted for the case of interest.

## Data releases

TNG50 data release is available: 

![Data Release](https://img.shields.io/badge/version-v1.0-green)

CEERS data release is available: 

![Data Release](https://img.shields.io/badge/version-v0.1-orange)

## Publications

Costantin et al. 2022, *in preparation*

Vega-Ferrero et al. 2022, *in preparation*

## Authors

*Author*: **Luca Costantin** (<lcostantin@cab.inta-csic.es>)

*Collaborators*: Pablo G. Pérez-González, Marc Huertas-Company, Jesús Vega-Ferrero


## Licensing

**ΩMEGA** scripts are distributed under GNU GPLv3.

