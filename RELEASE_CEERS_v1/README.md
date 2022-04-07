## Simulated NIRCam imaging data at CEERS depth for massive TNG50 galaxies at 3<z<6

### Description

This data release is composed of synthetic images of ∼25,000 galaxies from the IllustrisTNG50. Galaxies are selected to be more massive than 10^9 solar masses at redshift z=3, z=4, z=5, and z=6. Synthetic images were created with the SKIRT radiative transfer code, including the effects of dust attenuation and scattering. Galaxies are observed (imaging mode) with the NIRCam instrument mounted on the James Webb Space Telescope. In particular, each galaxy is observed under 20 configurations (5 inclinations and 4 azimuths) in the F200W and F356W filters. 

The mirage tool (v2.2.1) was used to simulated imaging data which have the NIRCam instrumental noise effects and the CEERS observing strategy (3-point dither - CEERS 10 pointing). Data simulated with mirage were run through the JWST calibration pipeline (v1.4.6), mimicking the data reduction strategy to be used for in-flight data. An additional step to homogenize the background (removing gradients and correcting for some detector-level patterns) was needed before drizzling the final images. 

A detailed description of the release can be found in the reference paper (Costantin+2022, in prep.), to which citation is requested if you use this data. *More information about this data release and the noiseless synthetic images can be found at the [OMEGA webpage](https://github.com/lcostant/OMEGA)*.

### Data releases

CEERS-TNG50 data release is available: 

![Download](https://img.shields.io/badge/version-v1.0-green)

* **v1.0**, NIRCam F200W with spatial resolution of 0.030 arcsec/px and NIRCam F356W with spatial resolution of 0.060 arcsec/px

* **v1.1**, NIRCam F200W with spatial resolution of 0.015 arcsec/px and NIRCam F356W with spatial resolution of 0.030 arcsec/px

### Observational setup

* **Instrument**  : NIRCam
* **Mode**        : Imaging
* **Simulator**   : MIRAGE v2.2.1
* **Calibration** : jwst pipeline v1.4.6
* **Target**      : TNG50-1 in CEERS Pointing 10
* **Filters**     : F200W (SW, B1 detector)
                    F356W (LW, B5 detector)
* **Readout**     : MEDIUM8
* **Dithers**     : 3 dithers (9 groups, 1 integration)
* **APT**         : CEERS ERS 1345
### Simulated data set

* **Available for**    : TNG50-1
* **Redshifts**        : z=3, z=4, z=5, z=6
* **Stellar masses**   : Larger than 10^9 solar masses
* **FoV**              : Larger than 4 arcsec^2

* **Number of galaxies**: 760 (z=3), 326 (z=4), 113 (z=5), 39 (z=6)
                         20 configurations for each galaxy 
                         5 inclinations: i=(0, 45, 90, 135, 180)
                         4 azimuths: a=(0, 90, 180, 270)

* **Modeling**         : Radiative transfer calculations using SKIRT v9 (Camps et al. 2020)
                         An example of the SKIRT setup is provided in SKIRT_config.ski

* **Noiseless dataset**: The noiseless synthetic images in all NIRCam (and MIRI) filters are available at the [OMEGA webpage](https://www.lucacostantin.com/OMEGA)

* **Raw data**         : The raw data (_uncal) produced with mirage can be available upon request.
                         The calibration data products (_rate, _cal, _i2d) can be available upon request.

* **Filename example** : 10846_i0_a0_z3_F200W_CEERS.fits
                         (ID_inclination_azimuth_redshift_filter_CEERS.fits)

* **Extensions**       : [0] General header (info about data reduction strategy)
                       : [1] SCI - IMAGE
                       : [2] ERR - IMAGE
                       : [3] CON - IMAGE
                       : [4] WHT - IMAGE
                       : [5] VAR_POISSON - IMAGE
                       : [6] VAR_RNOISE - IMAGE
                       : [7] VAR_FLAT - IMAGE
                       : [8] HDRTAB - BINARY TABLE  
                       : [9] ASDF - BINARY TABLE 
