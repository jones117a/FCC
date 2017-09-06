from heppy.framework.analyzer import Analyzer
from heppy.particles.tlv.resonance import Resonance2 as Resonance
from ROOT import TLorentzVector
from heppy.particles.tlv.particle import Particle

import pprint 
import itertools
import copy

mass = {23: 91, 25: 125}
sqrts = 240.

class HReconstruction(Analyzer):

    def process(self, event):
	photons = getattr(event, self.cfg_ana.input_photons)
	higgses = []
	zeds = []
	chi2_values = []
	photon_1_candidates = []
	photon_2_candidates = []
	photon1 = None
	photon2 = None
	for leg1, leg2 in itertools.combinations(photons,2): #Chooses 2 photons
	    zed_p4 = TLorentzVector(0, 0, 0, sqrts)
	    zed_p4 -= leg1.p4()
	    zed_p4 -= leg2.p4()
	    zeds.append(Particle(0, 0, zed_p4, 1))
            higgses.append( Resonance(leg1, leg2, 25)) #Combines the 2 photons to make a higgs
	    photon_1_candidates.append(leg1)
	    photon_2_candidates.append(leg2)
	higgs = None
	if len(higgses) and len(zeds):
	    nominal_mass_higgs = mass[25]
	    nominal_mass_zed = mass[23]
	    for higgs_number in range(len(higgses)):
	        chi2 = abs(higgses[higgs_number].m()-nominal_mass_higgs) + abs(zeds[higgs_number].m()-nominal_mass_zed) #Calculates a value to measure how close the mass of the higgs and Z produced are to the nominal mass values
	        chi2_values.append(chi2)
	        minimum_chi2 = min(chi2_values)
	        if minimum_chi2 == chi2:
		    higgs = higgses[higgs_number] #Saves the higgs corresponding to the best fit combination of particles
		    photon1 = photon_1_candidates[higgs_number]
		    photon2 = photon_2_candidates[higgs_number]
	if higgs and photon1 and photon2:
	    setattr(event, self.cfg_ana.output_higgs, higgs) #Outputs the Higgs
	    setattr(event, self.cfg_ana.output_lead_photon, photon1)
	    setattr(event, self.cfg_ana.output_sub_lead_photon, photon2)
	else:
	    return False
