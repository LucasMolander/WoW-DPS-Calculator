#
# For rapid tests of new stuff.
#

from stats import Stats
from dpscalc import RogueDPSCalc

s = {
    'Str': 3
}

myStats = Stats(s)
print(myStats)

myCalc = RogueDPSCalc()
myCalc.calculate(myStats)
