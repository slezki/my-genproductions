import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         filterEfficiency = cms.untracked.double(0.109),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         crossSection = cms.untracked.double(1430000.0),
                         comEnergy = cms.double(13000.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'Bottomonium:all = on',                     # Quarkonia, MSEL=62, allow feed-down
            'ParticleDecays:allowPhotonRadiation = on', # Turn on QED FSR
            '553:onMode = off',                         # Turn off Upsilon decays
            '553:onIfMatch = 13 -13',                   # just let Upsilon -> mu+ mu-
            'PhaseSpace:pTHatMin = 5.0'                 # ckin(3), be aware of this
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
)


# Next two muon filter are derived from muon reconstruction
muminusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.5, 0.5, 1.5, 1.5, 2.5),
    ParticleID = cms.untracked.int32(553),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(1.6, -2.4, 1.2, -1.6, -1.2),
    MaxEta = cms.untracked.vdouble(2.4, -1.6, 1.6, -1.2, 1.2),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(-13, -13, -13, -13, -13)
)

muplusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.5, 0.5, 1.5, 1.5, 2.5),
    ParticleID = cms.untracked.int32(553),
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
    MinPt = cms.untracked.double(6.0),
    ParticleID = cms.untracked.int32(553)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*muminusfilter*muplusfilter)

