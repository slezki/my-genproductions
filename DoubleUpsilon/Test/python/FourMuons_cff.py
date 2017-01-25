import FWCore.ParameterSet.Config as cms
from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

generator = cms.EDFilter(
    "Pythia6GeneratorFilter",
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(48440000000),
    filterEfficiency = cms.untracked.double(5.2e-5),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),

    PythiaParameters = cms.PSet(
    pythiaUESettingsBlock,
        bbbarSettings = cms.vstring('MSEL = 1'),
        parameterSets = cms.vstring(
             'pythiaUESettings',
             'bbbarSettings')

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
