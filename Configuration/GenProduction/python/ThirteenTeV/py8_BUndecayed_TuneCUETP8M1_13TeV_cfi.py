import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
             'SoftQCD:nonDiffractive = on',
             '100553:onMode = off',
             '10511:onMode = off',
             '10513:onMode = off',
             '10521:onMode = off',
             '10523:onMode = off',
             '10531:onMode = off',
             '10533:onMode = off',
             '10541:onMode = off',
             '10543:onMode = off',
             '10551:onMode = off',
             '10553:onMode = off',
             '200553:onMode = off',
             '20513:onMode = off',
             '20523:onMode = off',
             '20533:onMode = off',
             '20543:onMode = off',
             '20553:onMode = off',
             '5112:onMode = off',
             '5114:onMode = off',
             '511:onMode = off',
             '5122:onMode = off',
             '5132:onMode = off',
             '513:onMode = off',
             '515:onMode = off',
             '5212:onMode = off',
             '5214:onMode = off',
             '521:onMode = off',
             '5222:onMode = off',
             '5224:onMode = off',
             '5232:onMode = off',
             '523:onMode = off',
             '525:onMode = off',
             '5312:onMode = off',
             '5314:onMode = off',
             '531:onMode = off',
             '5322:onMode = off',
             '5324:onMode = off',
             '5332:onMode = off',
             '5334:onMode = off',
             '533:onMode = off',
             '535:onMode = off',
             '541:onMode = off',
             '543:onMode = off',
             '545:onMode = off',
             '551:onMode = off',
             '553:onMode = off',
             '555:onMode = off'
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
    )
)

#filter for b-quark
bfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(5)
)

ProductionFilterSequence = cms.Sequence(generator*bfilter)
