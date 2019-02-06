#
# Contains the Stats class, that represents a set of stats.
#
# This could represent stats for Gear, a difference in stats,
# stats for a proc, etc.
#


#
# Base gear stats.
# Then, add stats from:
#   - talents
#   - gems (and socket bonuses)
#   - enchants
#   - buffs
#   - racial bonus
# 


class Stats(object):

    VALID_STATS = [
        'Str',
        'Agi',
        'AP',
        'Crit',
        'Hit',
        'Exp',
        'Haste',
        'Arpen'
    ]

    
    #
    # Populates stats
    #
    def __init__(self, stats):
        # Default is 0
        self.stats = {
            vs: 0
            for vs in Stats.VALID_STATS
        }
        
        # Update valid stats
        for s in stats:
            if (s in Stats.VALID_STATS):
                self.stats[s] = stats[s]


    def __str__(self):
        out = 'Stats['

        for sk in sorted(list(self.stats.keys())):
            out += '%s=%d, ' % (sk, self.stats[sk])

        out += ']'

        return out
