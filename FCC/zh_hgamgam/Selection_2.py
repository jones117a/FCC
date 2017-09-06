from heppy.framework.analyzer import Analyzer
from heppy.statistics.counter import Counter

class Selection_2(Analyzer):

    def beginLoop(self, setup):
        super(Selection_2, self).beginLoop(setup)
        self.counters.addCounter('cut_flow')
	self.counters['cut_flow'].register('photon eta < 1.8')
	self.counters['cut_flow'].register('Higgs phi < 25 deg')
	
    def process(self, event):
	if abs(event.lead_photon.eta() - event.sub_lead_photon.eta()) > 1.8:
            return False
        self.counters['cut_flow'].inc('photon eta < 1.8')
	if abs(event.higgs.phi()) < 0.1105243:
	    return False
	self.counters['cut_flow'].inc('Higgs phi < 25 deg')
