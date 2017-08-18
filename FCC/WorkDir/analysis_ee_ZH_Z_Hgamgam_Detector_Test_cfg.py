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
    'ee_ZH_Z_Hgamgam',
    files = [
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/run_01/ee_ZH_Z_Hgamgam_0.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/run_01/ee_ZH_Z_Hgamgam_1.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/run_01/ee_ZH_Z_Hgamgam_2.root',
        '/afs/cern.ch/work/e/eljones/public/FCCSamples/run_01/ee_ZH_Z_Hgamgam_3.root'
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
from heppy.test.papas_test_cfg import papas_sequence, detector
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
