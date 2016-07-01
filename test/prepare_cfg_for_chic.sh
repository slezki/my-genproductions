cmsDriver.py Configuration/GenProduction/python/EightTeV/pgun_chic_8TeV_cfi.py \
--fileout file:step0.root --mc --eventcontent RAWSIM --datatier GEN-SIM \
--conditions START53_V7C::All --beamspot Realistic8TeVCollision --step GEN,SIM \
--python_filename step0_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 5000

cmsDriver.py step1 --filein file:step0.root --fileout file:step1.root  --mc \
--eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions START53_V19F::All \
--step DIGI,L1,DIGI2RAW --python_filename step1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n -1

cmsDriver.py step2 --filein file:step1.root --fileout file:step2.root --mc \
--eventcontent AODSIM --datatier AODSIM --conditions START53_V19F::All --step RAW2DIGI,RECO \
--python_filename step2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n -1 

