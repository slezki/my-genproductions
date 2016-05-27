# my-genproductions
Development of genproductions. Be aware that this configs have being tested just for the official MC branch 7_1_x for runII and
5_3_x for runI (when apply), other than that could work, but it not warranty. For testing porpouses always try to use the latest
version in either branch.


**Setup:**

```
#!/bin/bash
source  /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
if [ -r CMSSW_7_1_23/src ] ; then
 echo release CMSSW_7_1_23 already exists
else
scram p CMSSW CMSSW_7_1_23
fi
cd CMSSW_7_1_23/src
eval `scram runtime -sh`

pyfile=Configuration/GenProduction/python/ThirteenTeV/py8_JPsiMM_FSR_TuneCUETP8M1_13TeV_cfi.py

curl -s --insecure \
https://raw.githubusercontent.com/alberto-sanchez/my-genproductions/master/$pyfile \
--retry 2 --create-dirs -o $pyfile

scram b
cd ../../
cmsDriver.py $pyfile --fileout file:gen_sim.root --mc --eventcontent RAWSIM \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot NominalCollision2015 --step GEN,SIM --magField 38T_PostLS1 \
--python_filename step0_cfg.py --no_exec -n 100000
```
