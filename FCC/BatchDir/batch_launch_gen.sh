#!/bin/bash
cd ..

cd WorkDir

source /cvmfs/fcc.cern.ch/sw/0.8.1/init_fcc_stack.sh

mv /afs/cern.ch/user/e/eljones/private/hgamgam_analysis/FCC/BatchDir/$1 .

fcc-pythia8-generate $1
