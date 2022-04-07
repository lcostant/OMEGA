# Simulated NIRCam imaging data at CEERS depth for massive TNG50 galaxies at 3<z<6

This data release is composed of synthetic images of about 25,000 galaxies from the IllustrisTNG50[^1][^2]. Galaxies are selected to be more massive than log(M)>9 solar masses at redshift z=3, z=4, z=5, and z=6. Synthetic images were created with the SKIRT[^3] radiative transfer code (v9.0), including the effects of dust attenuation and scattering. 

Galaxies are observed (imaging mode) with the NIRCam instrument mounted on the James Webb Space Telescope. In particular, each galaxy is observed under 20 configurations (5 inclinations and 4 azimuths) in the F200W and F356W filters. 

The [mirage](https://mirage-data-simulator.readthedocs.io/en/latest/) tool (v2.2.1) was used to simulated imaging data which have the NIRCam instrumental noise effects and the CEERS observing strategy (3-point dither in the CEERS 10 pointing). Data simulated with mirage were run through the JWST [calibration pipeline](https://jwst-pipeline.readthedocs.io/en/latest/jwst/introduction.html) (v1.4.6), mimicking the data reduction strategy to be used for in-flight data. An additional step to homogenize the background (removing gradients and correcting for some detector-level patterns) was needed before drizzling the final images. 

The entire data release is made availble to the community, while the example galaxy ID XXX (z=3) is made available in this repository.

A detailed description of the release can be found in the reference paper (Costantin+2022, in prep.), to which citation is requested if you use this data. *More information about this data release and the noiseless synthetic images can be found at the [OMEGA webpage](https://www.lucacostantin.com/OMEGA)*.

## Data releases

CEERS-TNG50 data release is available: 

![Download](https://img.shields.io/badge/version-v1.0-green)

* **v1.0**: NIRCam F200W (0.030 arcsec/px), NIRCam F356W (0.060 arcsec/px)

* **v1.1**: NIRCam F200W (0.015 arcsec/px), NIRCam F356W (0.030 arcsec/px)

## Observational setup

* **Instrument**: NIRCam

* **Mode**: Imaging

* **Simulator**: MIRAGE v2.2.1

* **Calibration**: jwst pipeline v1.4.6

* **Target**: TNG50-1 in CEERS Pointing 10

* **Filters**: F200W (SW, B1 detector); F356W (LW, B5 detector)

* **Readout**: MEDIUM8

* **Dithers**: 3 dithers (9 groups, 1 integration)

* **APT**: CEERS ERS 1345
## Simulated data set

* **TNG50 version**: TNG50-1[^1][^2]

* **Redshifts**: z=3, z=4, z=5, z=6

* **Stellar masses**: Larger than log(M)>9 solar masses

* **FoV**: Larger than 4 arcsec^2

* **Number of galaxies**:

   z=3: 760 galaxies

   z=4: 326 galaxies

   z=5: 113 galaxies

   z=6: 39 galaxies

* **Modeling**: Radiative transfer calculations using SKIRT[^3] v9.0.   
   
   An example of the SKIRT setup is provided in SKIRT_config.ski

* **Stellar library**: MAPPINGS III library[^4] for young stellar particles (t<10 Myr) and Bruzual & Charlot library[^5] for old stellar particles (t>10 Myr).

* **Initial mass function**: Chabrier[^6].

* **Noiseless dataset**: The noiseless synthetic images in all NIRCam (and MIRI) filters are available at the [OMEGA webpage](https://www.lucacostantin.com/OMEGA)

* **Raw data**: 

   The raw data (_uncal) produced with mirage can be available upon request.
   
   The calibration data products (_rate, _cal, _i2d) can be available upon request.

* **Extensions**: 

   [0] General header (info about data reduction strategy)

   [1] SCI - IMAGE

   [2] ERR - IMAGE

   [3] CON - IMAGE

   [4] WHT - IMAGE

   [5] VAR_POISSON - IMAGE

   [6] VAR_RNOISE - IMAGE

   [7] VAR_FLAT - IMAGE

   [8] HDRTAB - BINARY TABLE  

   [9] ASDF - BINARY TABLE 

## Publications

Costantin L. et al. 2022, *in preparation*

Vega-Ferrero J. et al. 2022, *in preparation*

## Authors

**Luca Costantin** (Centro de Astrobiología, CAB/CSIC-INTA, Spain)

Pablo G. Pérez-González, Marc Huertas-Company, Jesús Vega-Ferrero
 
## Contact

**Luca Costantin**: lcostantin@cab-csic-inta.es

## Licensing

This release is distributed under GNU GPLv3.

[^1]: [Pillepich et al. (2019), Monthly Notices of the Royal Astronomical Society, 490, 3196](https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.3196P/abstract)
[^2]: [Nelson et al. (2019), Monthly Notices of the Royal Astronomical Society, 490, 3234](https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.3234N/abstract)
[^3]: [Camps et al. (2020), Astronomy and Computing, 31, 100381](https://ui.adsabs.harvard.edu/abs/2020A%26C....3100381C/abstract)
[^4]: [Groves et al. (2008), The Astrophysical Journal Supplement Series, 176, 438](https://ui.adsabs.harvard.edu/abs/2008ApJS..176..438G/abstract)
[^5]: [Bruzual & Charlot (2003), Monthly Notices of the Royal Astronomical Society, 344, 1000](https://ui.adsabs.harvard.edu/abs/2003MNRAS.344.1000B/abstract)
[^6]: [Chabrier (2003), The Publications of the Astronomical Society of the Pacific, 115, 763](https://ui.adsabs.harvard.edu/abs/2003PASP..115..763C/abstract)
