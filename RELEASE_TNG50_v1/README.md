# NIRCam and MIRI synthetic images of high-redshift galaxies from the IllustrisTNG50
 
## Description 

This data release is composed of synthetic images of about 25,000 galaxies from the IllustrisTNG50. Galaxies are selected to be more massive than log(M)>9 solar masses at redshift z=3, z=4, z=5, and z=6. Synthetic images were created with the SKIRT radiative transfer code, including the effects of dust attenuation and scattering. 

Galaxies are observed (imaging mode) with the NIRCam and MIRI instruments mounted on the James Webb Space Telescope. In particular, each galaxy is observed under 20 configurations (5 inclinations and 4 azimuths) in all available filters. 

The entire data release is made availble to the community, while the example galaxy ID XXX (z=3) is made available in this repository.

A detailed description of the release can be found in the reference paper (Costantin et al. 2022, in prep.), to which citation is requested if you use this data. *More information about this data release and the noiseless synthetic images can be found at the [OMEGA webpage](https://www.lucacostantin.com/OMEGA)*.
 
## Data releases

TNG50 data release is available: 

![Download](https://img.shields.io/badge/version-v1.0-green)

* **NIRCam SW**, with spatial resolution: 0.031 arcsec/px

* **NIRCam LW**, with spatial resolution: 0.063 arcsec/px

* **MIRI**, with spatial resolution: 0.110 arcsec/px

* **TNG50**, NIRCam and MIRI imaging with spatial resolution: 0.010 arcsec/px

## Additional information

* **TNG50 version**: TNG50-1 ([Pillepich et al. 2019](http://ui.adsabs.harvard.edu/abs/arXiv:1902.05553), [Dylan et al. 2019](https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.3234N/abstract)). 

   All physical parameters associated to the galaxies of this release can be found at [IllustrisTNG webpage](https://www.tng-project.org/data/docs/specifications/).

* **Modeling**: Radiative transfer calculations using SKIRT v9.0 ([Camps et al. 2020](https://ui.adsabs.harvard.edu/abs/2020A%26C....3100381C/abstract)).

* **Stellar library**: MAPPINGS III library [Groves et al. 2008](https://ui.adsabs.harvard.edu/abs/2008ApJS..176..438G/abstract) for young stellar particles (t<10 Myr) and [Bruzual & Charlot (2003)](https://ui.adsabs.harvard.edu/abs/2003MNRAS.344.1000B/abstract) library for old stellar particles (t>10 Myr).

* **IMF** : [Chabrier (2003)](https://ui.adsabs.harvard.edu/abs/2003PASP..115..763C/abstract).

* **Number of galaxies**:

   z=3: 760 galaxies

   z=4: 326 galaxies

   z=5: 113 galaxies

   z=6: 39 galaxies
## Publications

Costantin L. et al. 2022, *in preparation*

Vega-Ferrero J. et al. 2022, *in preparation*

## Authors

*Author*: **Luca Costantin** (Centro de Astrobiología, CAB/CSIC-INTA, Spain)

*Collaborators*: Pablo G. Pérez-González, Marc Huertas-Company, Jesús Vega-Ferrero
 
## Contact

**Luca Costantin**: lcostantin@cab-csic-inta.es

## Licensing

This release is distributed under GNU GPLv3.
