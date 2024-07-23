# Patching

MI survey:

NOTE- component can also mean ‘set of components’ or ‘circuit’, and ‘backup’ also mean ‘backup set of components or circuit’

p15: corrupted patch to clean run measures **necessicity**. If the circuit is OR (just at least one ‘backup’ is needed), this doesn’t do anything to model because just because X1 was destroyed, there’s still X2. But if it’s AND, then X1 is NECESSARY (NEEDED) for that circuit to work else it BREAKS.

clean patch to corrupted run measures **sufficiency**. if only ONE is changed, that is ENOUGH to change the output of the circuit (or whatever output is being measured as ‘changed’) to become FIXED. OR because just one has to change to fix.

can corr patch to clean run affect OR? Clean run by default is good, so an effect means it breaks. It does not measure OR because we are changing one (set of) component at a time, and if that unit causes a break, it means there were NO BACKUPS else it wouldn’t break

on the other hand, clean patch to corr run means just ONE was ENOUGH to fix it. if MORE WAS NECESSARY/NEEDED to fix it, it wouldn’t be fixed.