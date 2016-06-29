import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         comEnergy = cms.double(13000.0),
                         crossSection = cms.untracked.double(2978915.),
                         filterEfficiency = cms.untracked.double(1.59e-4),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         maxEventsToPrint = cms.untracked.int32(0),
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
                            EvtGen130 = cms.untracked.PSet(
                               decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
                               particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
                               user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Bu_JpsiK.dec'),
                               list_forced_decays = cms.vstring('MyB+','MyB-'),
                               operates_on_particles = cms.vint32(521,-521)
                            ),
                            parameterSets = cms.vstring('EvtGen130')
                         ),
                         PythiaParameters = cms.PSet(
                            pythia8CUEP8M1SettingsBlock,
                            pythia8CommonSettings = cms.vstring(
                               'Tune:preferLHAPDF = 2',
                               'Main:timesAllowErrors = 10000',
                               'Check:epTolErr = 0.01',
                               'Beams:setProductionScalesFromLHEF = off',
                               'SLHA:keepSM = on',
                               'SLHA:minMassSM = 1000.',
                               'ParticleDecays:limitTau0 = on',
                               'ParticleDecays:tau0Max = 10',
                               'ParticleDecays:allowPhotonRadiation = off',  # Turn on/off QED FSR, see pythia8CommonSettings
                            ),
                            processParameters = cms.vstring('HardQCD:all = on'),
                            parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                            )
                         )                         
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

bfilter = cms.EDFilter(
        "PythiaFilter",
        MaxEta = cms.untracked.double(9999.),
        MinEta = cms.untracked.double(-9999.),
        ParticleID = cms.untracked.int32(521)
        )

jpsifilter = cms.EDFilter(
        "PythiaDauVFilter",
	verbose         = cms.untracked.int32(0), 
	NumberDaughters = cms.untracked.int32(2), 
	MotherID        = cms.untracked.int32(521),  
	ParticleID      = cms.untracked.int32(443),  
        DaughterIDs     = cms.untracked.vint32(13, -13),
	MinPt           = cms.untracked.vdouble(0.5, 0.5), 
	MinEta          = cms.untracked.vdouble(-2.5, -2.5), 
	MaxEta          = cms.untracked.vdouble( 2.5,  2.5)
        )

kfilter = cms.EDFilter(
        "PythiaDauVFilter",
	verbose         = cms.untracked.int32(0), 
	NumberDaughters = cms.untracked.int32(2), 
	MotherID        = cms.untracked.int32(0),  
	ParticleID      = cms.untracked.int32(521),  
        DaughterIDs     = cms.untracked.vint32(443, 321),
	MinPt           = cms.untracked.vdouble(0., 0.4), 
	MinEta          = cms.untracked.vdouble(-99., -2.5), 
	MaxEta          = cms.untracked.vdouble(99.,   2.5)
        )

ProductionFilterSequence = cms.Sequence(generator*bfilter*jpsifilter*kfilter)

