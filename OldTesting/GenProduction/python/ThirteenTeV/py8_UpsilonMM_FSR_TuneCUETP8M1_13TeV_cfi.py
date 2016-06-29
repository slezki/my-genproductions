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
            'Bottomonium:all = on',                     # Quarkonia, MSEL=62
            'ParticleDecays:allowPhotonRadiation = on', # Turn on QED FSR
            '553:onMode = off',                         # Turn off Upsilon1S decays
            '553:onIfMatch = 13 -13',                   # just let Upsilon1S -> mu+ mu-
            '100553:onMode = off',                      # Turn off Upsilon2S decays
            '100553:onIfMatch = 13 -13',                # just let Upsilon2S -> mu+ mu-
            '200553:onMode = off',                      # Turn off Upsilon3S decays
            '200553:onIfMatch = 13 -13',                # just let Upsilon3S -> mu+ mu-
            'PhaseSpace:pTHatMin = 0.0'                 # ckin(3), be aware of this
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MinP = cms.untracked.vdouble(0., 0.),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MinInvMass = cms.untracked.double(5.0),
    MaxInvMass = cms.untracked.double(15.0),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*mumugenfilter)
