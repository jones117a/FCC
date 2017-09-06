from heppy.framework.analyzer import Analyzer
from heppy.statistics.counter import Counter

class Selection(Analyzer):

    def beginLoop(self, setup):
        super(Selection, self).beginLoop(setup)
        self.counters.addCounter('cut_flow') 
        self.counters['cut_flow'].register('All events')
        self.counters['cut_flow'].register('2 or more photons')
	self.counters['cut_flow'].register('2 or more photons with E > 40 GeV')
	self.counters['cut_flow'].register('isolated photons')

    def process(self, event):
        self.counters['cut_flow'].inc('All events')
	if len(event.photons) < 2:
	    return False
	self.counters['cut_flow'].inc('2 or more photons')
	if len(event.high_E_photons) < 2:
	    return False
        self.counters['cut_flow'].inc('2 or more photons with E > 40 GeV')
	if event.photons[0].iso.sume/event.photons[0].e() + event.photons[1].iso.sume/event.photons[1].e() > 0.4:
	    return False
	self.counters['cut_flow'].inc('isolated photons')
