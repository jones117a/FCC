#!/bin/bash
echo "Current directory:"
pwd

cd /afs/cern.ch/work/e/eljones/public/FCCSamples/run_01/

pwd

ls ./

echo "Will source FCC environment now"
source /cvmfs/fcc.cern.ch/sw/0.8.1/init_fcc_stack.sh
echo $PATH
mv /afs/cern.ch/user/e/eljones/private/hgamgam_analysis/FCC/BatchDir/$1 .

fcc-pythia8-generate $1

ls ./
