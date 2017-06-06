from . import srd
from . import classicbook3

GENERATORS = {
    'SRD': srd.WorldGen_SRD,
    'SRD Space Opera': srd.WorldGen_SRD_SpaceOpera,
    'SRD Hard Science': srd.WorldGen_SRD_HardScience,
    'Classic Book 3': classicbook3.WorldGen_ClassicBook3,
    }

