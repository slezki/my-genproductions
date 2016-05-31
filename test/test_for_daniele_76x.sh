#!/bin/bash
source  /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc493
if [ -r CMSSW_7_6_5/src ] ; then
 echo release CMSSW_7_6_5 already exists
else
scram p CMSSW CMSSW_7_6_5
fi
cd CMSSW_7_6_5/src
eval `scram runtime -sh`

pyfile=Configuration/GenProduction/python/ThirteenTeV/pgun_Upsilon1SMM_FSR_TuneCUETP8M1_13TeV_cfi.py

curl -s --insecure \
https://raw.githubusercontent.com/alberto-sanchez/my-genproductions/master/$pyfile \
--retry 2 --create-dirs -o $pyfile

scram b
cd ../../
cmsDriver.py $pyfile --fileout file:gen_sim_76x.root --mc --eventcontent RAWSIM \
--era Run2_25ns \
--datatier GEN-SIM --conditions  MCRUN2_71_V1 --beamspot NominalCollision2015 --step GEN --magField 38T_PostLS1 \
--python_filename step0_cfg_76x.py -n 1000
