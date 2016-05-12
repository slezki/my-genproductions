import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        parameterSets = cms.vstring('EvtGen130'),
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010_NOLONGLIFE.DEC'),
            operates_on_particles = cms.vint32(333),
            user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Phi_MuMu.dec'),
            list_forced_decays = cms.vstring('MyPhi'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl')
        )
    ),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.026),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    crossSection = cms.untracked.double(30560000.0),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
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

#filter two muons in the phi(1020) mass region
decayfilter = cms.EDFilter("PythiaDauVFilter",
    verbose         = cms.untracked.int32(1),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID      = cms.untracked.int32(333),
    DaughterIDs     = cms.untracked.vint32(13, -13),
    MinPt           = cms.untracked.vdouble(2.5, 2.5),
    MinEta          = cms.untracked.vdouble(-2.5, -2.5),
    MaxEta          = cms.untracked.vdouble( 2.5,  2.5)
)

ProductionFilterSequence = cms.Sequence(generator*decayfilter)
