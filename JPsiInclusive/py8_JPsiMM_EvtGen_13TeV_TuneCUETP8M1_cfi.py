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
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            convertPythiaCodes = cms.untracked.bool(False),
            list_forced_decays = cms.vstring('MyJ/psi'),
            operates_on_particles = cms.vint32(443),
            user_decay_embedded= cms.vstring(
'''
Alias MyJ/psi J/psi
ChargeConj MyJ/psi MyJ/psi

Decay MyJ/psi
 1.0000  mu+        mu-                    PHOTOS VLL ;
Enddecay

End
'''
        )
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'HardQCD:hardbbbar = on'
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
        )
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

muminusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(3.),
    ParticleID = cms.untracked.int32(443),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-3.),
    MaxEta = cms.untracked.vdouble(3.),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(-13)
)

muplusfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(3.),
    ParticleID = cms.untracked.int32(443),
    ChargeConjugation = cms.untracked.bool(False),
    MinEta = cms.untracked.vdouble(-3.),
    MaxEta = cms.untracked.vdouble(3.),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*muminusfilter*muplusfilter)
