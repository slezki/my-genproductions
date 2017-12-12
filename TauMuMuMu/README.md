# TauMuMUMu

Configuration files to generate Ds- -> tau- nu_tau, with tau- -> mu- mu+ mu-
Using pythia8 for the whole generation, which bias the generation when multiple Ds and/or tau are present 
in the event and then using pythia+evtgen to generate just one signal candidate per event.


**Setup:**

```
#!/bin/bash
source  /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_9_3_5/src ] ; then
 echo release CMSSW_9_3_5 already exists
else
scram p CMSSW CMSSW_9_3_5
fi
cd CMSSW_9_3_5/src
eval `scram runtime -sh`

pyfile=Configuration/GenProduction/python/DsTau3Mu_EvtGen_cfi.py

curl -s --insecure \
https://raw.githubusercontent.com/alberto-sanchez/my-genproductions/master/TauMuMuMu/DsTau3Mu_EvtGen_cfi.py \
--retry 2 --create-dirs -o $pyfile

scram b
cmsDriver.py $pyfile --fileout file:gen_sim.root --mc --eventcontent RAWSIM --datatier GEN-SIM \
--conditions 92X_upgrade2017_realistic_v10 --beamspot Realistic25ns13TeVEarly2017Collision \
--step GEN --nThreads 4 --geometry DB:Extended --era Run2_2017 --python_filename step0_cfg.py --no_exec \
--customise Configuration/DataProcessing/Utils.addMonitoring -n 100000

```
