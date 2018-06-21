# my-genproductions
Be aware that this configs have being tested just for the official MC branch 7_1_x and 9_3_x for runII for other
branches may work but it is not warranty. For testing porpouses always try to use the latest
version in either branch.


**Setup: 2016 conditions**

```
#!/bin/bash
source  /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481
if [ -r CMSSW_7_1_33/src ] ; then
 echo release CMSSW_7_1_33 already exists
else
scram p CMSSW CMSSW_7_1_33
fi
cd CMSSW_7_1_33/src
eval `scram runtime -sh`

pydir=Configuration/GenProduction/python
pyfile=bc-pythia-had-evtgen-cuep8m1.py

curl -s --insecure \
https://raw.githubusercontent.com/alberto-sanchez/my-genproductions/master/lhe-custom-hadronization/$pyfile \
--retry 2 --create-dirs -o $pydir/$pyfile

scram b
cd ../../
cmsDriver.py $pydir/$pyfile --fileout file:gen_sim.root --mc --eventcontent RAWSIM \
        --filein file:bcvegpy.lhe  --filetype=LHE \
        --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
        --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM \
        --magField 38T_PostLS1 --python_filename step0_cfg.py --no_exec -n -1
```


**Setup: 2017 conditions**

```
#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_9_3_10/src ] ; then
 echo release CMSSW_9_3_10 already exists
else
scram p CMSSW CMSSW_9_3_10
fi
cd CMSSW_9_3_10/src
eval `scram runtime -sh`

pyfile=bc-pythia-had-evtgen-cp5.py
pydir=Configuration/GenProduction/python
myurl=https://raw.githubusercontent.com/alberto-sanchez/my-genproductions/master/lhe-custom-hadronization

curl -s --insecure $myurl/$pyfile --retry 2 --create-dirs -o $pydir/$pyfile
[ -s ${pyfile} ] || exit $?;

scram b

cd ../../
cmsDriver.py $pydir/$pyfile --filein file:bcvegpy.lhe  --filetype=LHE \
        --fileout file:gensim.root --mc --eventcontent RAWSIM \
        --customise Configuration/DataProcessing/Utils.addMonitoring \
        --datatier GEN-SIM --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM \
        --geometry DB:Extended --era Run2_2017 --python_filename step0_cfg.py --no_exec -n -1

```

