# NIRCam and MIRI synthetic images

## Massive galaxies at redshift 3<z<6 from IllustrisTNG50

This data release is composed of synthetic images of about 25,000 galaxies from the IllustrisTNG50[^1][^2]. Galaxies are selected to be more massive than log(M)>9 solar masses at redshift z=3, z=4, z=5, and z=6. Synthetic images were created with the SKIRT[^3] radiative transfer code (v9.0), including the effects of dust attenuation and scattering. 

Galaxies are observed (imaging mode) with the NIRCam and MIRI instruments mounted on the James Webb Space Telescope. In particular, each galaxy is observed under 20 configurations (5 inclinations and 4 azimuths) in all available filters. 

A detailed description of the release can be found in the reference paper (**Costantin et al. 2022**, *in preparation*), to which citation is requested if you use this data. The entire data release is made availble to the community, while the example galaxy ID XXX (z=3) is made available in this repository.
 
## Data releases

TNG50 data release is available: 

![Download](https://img.shields.io/badge/version-v1.0-green)

* **NIRCam SW**, with spatial resolution of 0.031 arcsec/px

* **NIRCam LW**, with spatial resolution of 0.063 arcsec/px

* **MIRI**, with spatial resolution of 0.110 arcsec/px

* **TNG50**, NIRCam and MIRI imaging with spatial resolution of 0.010 arcsec/px

## Additional information

* **TNG50 version**: TNG50-1[^1][^2]

   All physical parameters associated to the galaxies of this release can be found at [IllustrisTNG webpage](https://www.tng-project.org/data/docs/specifications/).

* **Modeling**: Radiative transfer calculations using SKIRT[^3] v9.0.   
   
   An example of the SKIRT setup is provided in the *SKIRT_config.ski* file.

* **Stellar library**: MAPPINGS III library[^4] for young stellar particles (t<10 Myr) and Bruzual & Charlot library[^5] for old stellar particles (t>10 Myr).

* **Initial mass function**: Chabrier[^6].

* **Number of galaxies**:

   z=3: 760 galaxies

   z=4: 326 galaxies

   z=5: 113 galaxies

   z=6: 39 galaxies
## Publications

Costantin L. et al. 2022, *in preparation*

Vega-Ferrero J. et al. 2022, *in preparation*

## Authors

**Luca Costantin** (Centro de Astrobiología, CAB/CSIC-INTA, Spain)

Pablo G. Pérez-González, Marc Huertas-Company, Jesús Vega-Ferrero
 
## Contact

Luca Costantin: lcostantin@cab.inta-csic.es

## Licensing

This release is distributed under GNU GPLv3.

[^1]: [Pillepich et al. (2019), Monthly Notices of the Royal Astronomical Society, 490, 3196](https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.3196P/abstract)
[^2]: [Nelson et al. (2019), Monthly Notices of the Royal Astronomical Society, 490, 3234](https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.3234N/abstract)
[^3]: [Camps et al. (2020), Astronomy and Computing, 31, 100381](https://ui.adsabs.harvard.edu/abs/2020A%26C....3100381C/abstract)
[^4]: [Groves et al. (2008), The Astrophysical Journal Supplement Series, 176, 438](https://ui.adsabs.harvard.edu/abs/2008ApJS..176..438G/abstract)
[^5]: [Bruzual & Charlot (2003), Monthly Notices of the Royal Astronomical Society, 344, 1000](https://ui.adsabs.harvard.edu/abs/2003MNRAS.344.1000B/abstract)
[^6]: [Chabrier (2003), The Publications of the Astronomical Society of the Pacific, 115, 763](https://ui.adsabs.harvard.edu/abs/2003PASP..115..763C/abstract)
