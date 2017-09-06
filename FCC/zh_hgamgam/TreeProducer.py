from heppy.framework.analyzer import Analyzer
from heppy.statistics.tree import Tree
from heppy.analyzers.ntuple import *

from ROOT import TFile

class TreeProducer(Analyzer):

    def beginLoop(self, setup):
        super(TreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName,
                                        'tree.root']),
                              'recreate')
        self.tree = Tree( 'events', '')
        bookParticle(self.tree, 'higgs')
        bookParticle(self.tree, 'lead_photon')
        bookParticle(self.tree, 'sub_lead_photon')
       
    def process(self, event):
	self.tree.reset()
	lead_photon = getattr(event, self.cfg_ana.lead_photon)
	if lead_photon:
	    fillParticle(self.tree, 'lead_photon', lead_photon)
	sub_lead_photon = getattr(event, self.cfg_ana.sub_lead_photon)
	if sub_lead_photon:
	    fillParticle(self.tree, 'sub_lead_photon', sub_lead_photon)
        higgs = getattr(event, self.cfg_ana.higgs)
        if higgs:
	    fillParticle(self.tree,'higgs',higgs)
        self.tree.tree.Fill()
        
    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()
