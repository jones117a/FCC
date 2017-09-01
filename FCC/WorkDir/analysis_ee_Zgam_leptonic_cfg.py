'''Example configuration file for an ee->ZH analysis in the 4 jet channel,
with the FCC-ee

While studying this file, open it in ipython as well as in your editor to 
get more information: 

ipython
from analysis_ee_ZH_had_cfg import * 

'''

import os
import copy
import heppy.framework.config as cfg

from heppy.framework.event import Event
Event.print_patterns=['*higgs*', '*photon*']

import logging
# next 2 lines necessary to deal with reimports from ipython
logging.shutdown()
reload(logging)
logging.basicConfig(level=logging.WARNING)

# setting the random seed for reproducible results
import heppy.statistics.rrandom as random
random.seed(0xdeadbeef)

# definition of the collider
from heppy.configuration import Collider
Collider.BEAMS = 'ee'
Collider.SQRTS = 240.

# input definition
comp = cfg.Component(
    'ee_Zgam_leptonic',
    files = [
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_0.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_1.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_2.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_3.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_4.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_5.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_6.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_7.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_8.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_9.root',
	'/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_10.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_11.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_12.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_13.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_14.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_15.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_16.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_17.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_18.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_19.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_20.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_21.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_22.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_23.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_24.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_25.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_26.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_27.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_28.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_29.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_30.root',
	'/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_31.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_32.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_33.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_34.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_35.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_36.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_37.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_38.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_39.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_40.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_41.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_42.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_43.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_44.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_45.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_46.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_47.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_48.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_49.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_50.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_51.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_52.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_53.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_54.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_55.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_56.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_57.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_58.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_59.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_60.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_61.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_62.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_63.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_64.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_65.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_66.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_67.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_68.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_69.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_70.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_71.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_72.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_73.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_74.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_75.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_76.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_77.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_78.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_79.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_80.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_81.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_82.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_83.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_84.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_85.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_86.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_87.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_88.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_89.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_90.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_91.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_92.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_93.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_94.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_95.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_96.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_97.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_98.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/leptonic_background_run_01/ee_Zgam_leptonic_99.root',
	]
)
selectedComponents = [comp]

# read FCC EDM events from the input root file(s)
from heppy.analyzers.fcc.Reader import Reader
source = cfg.Analyzer(
    Reader,
    gen_particles = 'GenParticle',
    gen_vertices = 'GenVertex'
)

# the papas simulation and reconstruction sequence
from heppy.test.papas_cfg import papas_sequence, detector
from heppy.test.papas_cfg import papasdisplay as display

# Use a Selector to select photons from the output of papas simulation.
from heppy.analyzers.Selector import Selector
def is_photon(ptc):
    return ptc.e()> 5. and abs(ptc.pdgid()) in [22]

photons = cfg.Analyzer(
    Selector,
    'photons',
    output = 'photons',
    input_objects = 'rec_particles',
    filter_func = is_photon 
)

def high_E(pho):
    '''returns true if photon energy is above 40 GeV.'''
    return pho.e() > 40.

high_E_photons = cfg.Analyzer(
    Selector,
    'high_E_photons',
    output = 'high_E_photons',
    input_objects = 'photons',
    filter_func = high_E
)

# Compute photon isolation w/r other particles in the event.
from heppy.analyzers.IsolationAnalyzer import IsolationAnalyzer
from heppy.particles.isolation import EtaPhiCircle
iso_photons = cfg.Analyzer(
    IsolationAnalyzer,
    candidates = 'photons',
    particles = 'rec_particles',
    iso_area = EtaPhiCircle(0.4)
)

# Select isolated photons with a Selector
def is_isolated(pho):
    '''returns true if the particles around the photon
    in the EtaPhiCircle defined above carry less than 30%
    of the photon energy.'''
    return pho.iso.sume/pho.e()<0.2  # fairly loose

high_E_sel_iso_photons = cfg.Analyzer(
    Selector,
    'high_E_sel_iso_photons',
    output = 'high_E_sel_iso_photons',
    input_objects = 'high_E_photons',
    filter_func = is_isolated
) # Rejecting events that contain a loosely isolated photon

# reconstruction of the H resonance.
from heppy.analyzers.examples.zh_hgamgam.HReconstruction import HReconstruction
hreco = cfg.Analyzer(
    HReconstruction,
    output_higgs = 'higgs',
    output_lead_photon = 'lead_photon',
    output_sub_lead_photon = 'sub_lead_photon',
    input_photons = 'high_E_sel_iso_photons'
)

# simple cut flow printout
from heppy.analyzers.examples.zh_hgamgam.Selection import Selection
selection = cfg.Analyzer(
    Selection,
    input_photons = 'photons',
    log_level = logging.INFO
)

# Analysis-specific ntuple producer
from heppy.analyzers.examples.zh_hgamgam.TreeProducer import TreeProducer
tree = cfg.Analyzer(
    TreeProducer,
    higgs = 'higgs',
    lead_photon = 'lead_photon',
    sub_lead_photon = 'sub_lead_photon'
)

# definition of the sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence(
    source,
    papas_sequence, 
    photons,
    iso_photons,
    high_E_photons,
    high_E_sel_iso_photons,
    hreco, 
    selection,
    tree,
    display
)

# Specifics to read FCC events 
from ROOT import gSystem
gSystem.Load("libdatamodelDict")
from EventStore import EventStore as Events

config = cfg.Config(
    components = selectedComponents,
    sequence = sequence,
    services = [],
    events_class = Events
)
