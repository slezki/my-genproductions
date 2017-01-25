import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.026),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    crossSection = cms.untracked.double(30560000.0),
    comEnergy = cms.double(8000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
         pythia8CommonSettingsBlock,
         pythia8CUEP8M1SettingsBlock,
         processParameters = cms.vstring(
            'HardQCD:all = on',
            'PhaseSpace:pTHatMin = 5.'
         ),
         parameterSets = cms.vstring(
             'pythia8CommonSettings',
             'pythia8CUEP8M1Settings',
             'processParameters',
         )
    )
)

FourMuonFilter = cms.EDFilter("FourLepFilter",
    MinPt = cms.untracked.double(2.0),
    MaxPt = cms.untracked.double(4000.0),
    MaxEta = cms.untracked.double(2.5),
    MinEta = cms.untracked.double(0.),
    ParticleID = cms.untracked.int32(13)
)

ProductionFilterSequence = cms.Sequence(generator*FourMuonFilter)
