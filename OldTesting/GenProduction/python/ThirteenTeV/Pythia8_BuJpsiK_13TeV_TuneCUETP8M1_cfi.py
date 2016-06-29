import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         comEnergy = cms.double(13000.0),
                         crossSection = cms.untracked.double(2978915.),
                         filterEfficiency = cms.untracked.double(1.59e-4),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         maxEventsToPrint = cms.untracked.int32(0),
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         PythiaParameters = cms.PSet(
                            pythia8CommonSettingsBlock,
                            pythia8CUEP8M1SettingsBlock,
                            processParameters = cms.vstring('HardQCD:all = on',
                               '521:onMode = off',                 # Turn off B+ decays
                               '521:onIfMatch = 443 321',          # just let B+ -> J/psi K+
                               '443:onMode = off',                 # Turn off J/psi decays
                               '443:onIfMatch = 13 -13'            # just let J/psi -> mu+ mu-
                            ),
                            parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                            )
                         )                         
)

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

