# my-genproductions

The configuration files in this directory are mean to be used with the pythia8 hadronizer found in 71x.
Use the latest 71x release available


**Example Setup: for Bc hadronization and using evtgen as decayer**

```
#!/bin/bash
source  /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
if [ -r CMSSW_7_1_30/src ] ; then
 echo release CMSSW_7_1_30 already exists
else
scram p CMSSW CMSSW_7_1_30
fi
cd CMSSW_7_1_30/src
eval `scram runtime -sh`

pyfile=bc-evtgen-fragment.py

curl -s --insecure \
https://raw.githubusercontent.com/alberto-sanchez/my-genproductions/master/Hadronizer/python/$pyfile \
--retry 2 --create-dirs -o Configuration/GenProduction/python/$pyfile

scram b

cmsDriver.py Configuration/GenProduction/python/$pyfile \
	--filein dbs:/BcToJPsiBcPt8Y2p5_MuNoCut_13TeV-bcvegpy2-pythia8/RunIIWinter15pLHE-MCRUN2_71_V1-v1/LHE \
	--fileout file:gen.root --mc --eventcontent RAWSIM \
	--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
	--datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN \
	--magField 38T_PostLS1 --python_filename gen_cfg.py --no_exec -n -1

```
