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
             '100553:mayDecay = no',
             '10511:mayDecay = no',
             '10513:mayDecay = no',
             '10521:mayDecay = no',
             '10523:mayDecay = no',
             '10531:mayDecay = no',
             '10533:mayDecay = no',
             '10541:mayDecay = no',
             '10543:mayDecay = no',
             '10551:mayDecay = no',
             '10553:mayDecay = no',
             '200553:mayDecay = no',
             '20513:mayDecay = no',
             '20523:mayDecay = no',
             '20533:mayDecay = no',
             '20543:mayDecay = no',
             '20553:mayDecay = no',
             '5112:mayDecay = no',
             '5114:mayDecay = no',
             '511:mayDecay = no',
             '5122:mayDecay = no',
             '5132:mayDecay = no',
             '513:mayDecay = no',
             '515:mayDecay = no',
             '5212:mayDecay = no',
             '5214:mayDecay = no',
             '521:mayDecay = no',
             '5222:mayDecay = no',
             '5224:mayDecay = no',
             '5232:mayDecay = no',
             '523:mayDecay = no',
             '525:mayDecay = no',
             '5312:mayDecay = no',
             '5314:mayDecay = no',
             '531:mayDecay = no',
             '5322:mayDecay = no',
             '5324:mayDecay = no',
             '5332:mayDecay = no',
             '5334:mayDecay = no',
             '533:mayDecay = no',
             '535:mayDecay = no',
             '541:mayDecay = no',
             '543:mayDecay = no',
             '545:mayDecay = no',
             '551:mayDecay = no',
             '553:mayDecay = no',
             '555:mayDecay = no'
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
