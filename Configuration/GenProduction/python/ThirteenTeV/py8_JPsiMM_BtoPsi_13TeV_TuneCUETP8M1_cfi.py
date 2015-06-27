import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(      
            'HardQCD:all = on',
            'PhaseSpace:pTHatMin = 8.'
            '511:onMode = off',
            '511:onIfAny = 443 100443 10441 20443 445 30443 10443',
            '521:onMode = off',
            '521:onIfAny = 443 100443 10441 20443 445 30443 10443',
            '531:onMode = off',
            '531:onIfAny = 443 100443 10441 20443 445 30443 10443',
            '541:onMode = off',
            '541:onIfAny = 443 100443 10441 20443 445 30443 10443',
            '5122:onMode = off',
            '5122:onIfAny = 443 100443 10441 20443 445 30443 10443',
            '100443:onMode = off',
            '100443:onIfAny = 443',
            '10441:onMode = off',
            '10441:onIfAny = 443',
            '10443:onMode = off',
            '10443:onIfAny = 443',
            '20443:onMode = off',
            '20443:onIfAny = 443',
            '30443:onMode = off',
            '30443:onIfAny = 443',
            '445:onMode = off',
            '445:onIfAny = 443',
            '443:onMode = off',
            '443:onIfMatch = 13 -13'
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
        )
    )
)

bfilter = cms.EDFilter("PythiaFilter",
                       ParticleID = cms.untracked.int32(5)
                       )

# Next two muon filter are derived from muon reconstruction
muminusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.5, 0.5, 1.5, 1.5, 2.5),
    ParticleID = cms.untracked.int32(443),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(1.6, -2.4, 1.2, -1.6, -1.2),
    MaxEta = cms.untracked.vdouble(2.4, -1.6, 1.6, -1.2, 1.2),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(-13, -13, -13, -13, -13)
)

muplusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.5, 0.5, 1.5, 1.5, 2.5),
    ParticleID = cms.untracked.int32(443),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(1.6, -2.4, 1.2, -1.6, -1.2),
    MaxEta = cms.untracked.vdouble(2.4, -1.6, 1.6, -1.2, 1.2),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(13, 13, 13, 13, 13)
)

oniafilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(2),
    MaxEta = cms.untracked.double(1000.0),
    MinEta = cms.untracked.double(-1000.0),
    MinPt = cms.untracked.double(8.0),
    ParticleID = cms.untracked.int32(443)
)

ProductionFilterSequence = cms.Sequence(generator*bfilter*oniafilter*muminusfilter*muplusfilter)
