import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.138),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    crossSection = cms.untracked.double(1256000.0),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    ExternalDecays = cms.PSet(
            EvtGen130 = cms.untracked.PSet(
                decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
                particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
                user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Onia_mumu.dec'),
                list_forced_decays = cms.vstring('MyJ/psi'),
                operates_on_particles = cms.vint32(443)
            ),
            parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(    
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'Charmonium:all = on',                        # Quarkonia, MSEL=61, including feed-down as well
            'ParticleDecays:allowPhotonRadiation = off',  # Turn on/off QED FSR, see pythia8CommonSettings
            '443:onMode = off',                           # Turn off J/psi decays
            #'443:onIfMatch = 13 -13',                    # just let J/psi -> mu+ mu-
            'PhaseSpace:pTHatMin = 10.'                   # be aware of this ckin(3) equivalent
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters'
        )
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

muplusfilter = cms.EDFilter("PythiaDauVFilter",
    ChargeConjugation = cms.untracked.bool(False),
    ParticleID = cms.untracked.int32(443),
    MotherID = cms.untracked.int32(0),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(+13,  +13,  +13,  +13,  +13),
    MinPt = cms.untracked.vdouble     (+1.0, +1.0, +2.0, +2.0, +3.0),
    MaxEta = cms.untracked.vdouble    (+2.2, -1.6, +1.6, -1.2, +1.2),
    MinEta = cms.untracked.vdouble    (+1.6, -2.2, +1.2, -1.6, -1.2)
)

muminusfilter = cms.EDFilter("PythiaDauVFilter",
    ChargeConjugation = cms.untracked.bool(False),
    ParticleID = cms.untracked.int32(443),
    MotherID = cms.untracked.int32(0),
    NumberDaughters = cms.untracked.int32(1),
    DaughterIDs = cms.untracked.vint32(-13,  -13,  -13,  -13,  -13),
    MinPt = cms.untracked.vdouble     (+1.0, +1.0, +2.0, +2.0, +3.0),
    MaxEta = cms.untracked.vdouble    (+2.2, -1.6, +1.6, -1.2, +1.2),
    MinEta = cms.untracked.vdouble    (+1.6, -2.2, +1.2, -1.6, -1.2)
)

oniafilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(2),
    MaxEta = cms.untracked.double(1000.0),
    MinEta = cms.untracked.double(-1000.0),
    MinPt = cms.untracked.double(10.0),
    ParticleID = cms.untracked.int32(443)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*muplusfilter*muminusfilter)
