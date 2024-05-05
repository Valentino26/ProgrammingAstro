hdf5 (Hierarchical Data Format): modernes Dateiformat zur effizienten Speicherung riesiger Datenmengen. (Python: import [h5py](https://docs.h5py.org/en/stable/))

|   |   |   |
|---|---|---|
|Filename extension|h5|Extension used in HDF5 documentation.|
|Magic numbers|Hex: 89 48 44 46 0d 0a 1a 0a 00  <br>ASCII: \211 HDF \r \n \032 \n|Applies to HDF5 Version 0, with last two digits in hexadecimal value indicating version number. As described in [HDF5 format specification](https://portal.hdfgroup.org/display/HDF5/File+Format+Specification) and documented in [PRONOM](http://www.nationalarchives.gov.uk/PRONOM/fmt/807). The HDF5 superblock, which begins with the 8-byte format signature, may begin at certain predefined offsets within the HDF5 file: 0, 512, 1024, 2048, and multiples of two thereafter.|
|Magic numbers|Hex: 89 48 44 46 0d 0a 1a 0a 01  <br>ASCII: \211 HDF \r \n \032 \n|Applies to HDF5 Version 1, with last two digits in hexadecimal value indicating version number. As described in [HDF5 format specification](https://portal.hdfgroup.org/display/HDF5/File+Format+Specification) and documented in [PRONOM](http://www.nationalarchives.gov.uk/PRONOM/fmt/286). The HDF5 superblock, which begins with the 8-byte format signature, may begin at certain predefined offsets within the HDF5 file: 0, 512, 1024, 2048, and multiples of two thereafter.|
|Pronom PUID|fmt/807|HDF5 Version 0. See [http://www.nationalarchives.gov.uk/PRONOM/fmt/807](http://www.nationalarchives.gov.uk/PRONOM/fmt/807)|
|Pronom PUID|fmt/286|HDF5 Version 1. See [http://www.nationalarchives.gov.uk/PRONOM/fmt/286](http://www.nationalarchives.gov.uk/PRONOM/fmt/286)|
|Wikidata Title ID|Q1069215|See [https://www.wikidata.org/wiki/Q1069215](https://www.wikidata.org/wiki/Q1069215).|
