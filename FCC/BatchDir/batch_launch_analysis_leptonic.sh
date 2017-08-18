#!/bin/bash
cd /afs/cern.ch/user/e/eljones/private/hgamgam_analysis/FCC/heppy/

source ./init.sh

cd ..

source /afs/cern.ch/exp/fcc/sw/0.8pre/setup.sh

cd WorkDir/

heppy /afs/cern.ch/work/e/eljones/public/FCCSamples/OutDir_leptonic_background_1M analysis_ee_Zgam_leptonic_cfg.py

