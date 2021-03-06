#!/usr/bin/env python

import os, random

process = 'ee_Zgam_full'
target = ''
n_samples = 1
nevt_per_sample = 1000

for x in range(0, n_samples):

    print 'Generating random seed.'
    seed = random.randint(99999,999999)
    print seed

    fin = open(process+'.txt')
    fout = open(process+'_'+str(x)+'.txt', 'wt')
    for line in fin:
        line = line.replace('Main:numberOfEvents = 1000', 'Main:numberOfEvents = '+str(nevt_per_sample) )
        line = line.replace('Random:seed = 0', 'Random:seed = '+str(seed) )
	print line
        fout.write( line )

    fout.close()
    fin.close()

#    os.system('fcc-pythia8-generate '+process+'_'+str(x)+'.txt') # to run locally
    os.system('bsub bash batch_launch_gen.sh '+process+'_'+str(x)+'.txt') # to run on the batch
