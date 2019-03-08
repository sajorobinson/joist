from lib import jHead
from lib import jModule as jm

base = jm.navigation + jm.hero

homePage = base + jm.oneColumnText + jm.textImage + jm.fullImageText + jm.footer

blogPage = base + jm.oneColumnText + jm.oneColumnText + jm.textFullImage + jm.oneColumnText + jm.hero + jm.oneColumnText  + jm.footer

productPage = base + jm.oneColumnBigText + jm.portfolio + jm.textFullImage + jm.fullImageText + jm.threeColumnCta + jm.oneColumnText + jm.hero + jm.footer