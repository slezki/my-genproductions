import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/incl_BtoJpsi_mumu.dec'),
            list_forced_decays = cms.vstring('MyB+','MyB-','MyB0','Myanti-B0','MyB_s0','Myanti-B_s0','MyLambda_b0','Myanti-Lambda_b0'),
            operates_on_particles = cms.vint32()
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(      
            'HardQCD:all = on',
            'PhaseSpace:pTHatMin = 8.'
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
        )
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

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
