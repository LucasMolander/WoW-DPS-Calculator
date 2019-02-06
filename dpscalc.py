#
# Contains the classes that calculate the DPS for each spec. :)
#

from stats import Stats

from abc import ABC, abstractmethod


class DPSCalc(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def calculate(self, stats):
        """
        @param stats Stats object
        """
        pass


class RogueDPSCalc(DPSCalc):

    def calculate(self, stats):
        assert isinstance(stats, Stats), 'stats must be a Stats object'
        
        print('I did muh calcalatan')
