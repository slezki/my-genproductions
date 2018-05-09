import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8PtGun",
    maxEventsToPrint = cms.untracked.int32(5),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    PGunParameters = cms.PSet(
        MaxPt = cms.double(100.),
        MinPt = cms.double(0.),
        ParticleID = cms.vint32(443),
        AddAntiParticle = cms.bool(False), 
        MaxEta = cms.double(2.4),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-2.4),
        MinPhi = cms.double(-3.14159265359) ## in radians
   ),
   PythiaParameters = cms.PSet(
       pythia8CommonSettingsBlock,
       pythia8CUEP8M1SettingsBlock,
       pythiaJpsiDecays = cms.vstring(
            '443:onMode = off',                          # Turn off J/psi decays
            '443:onIfMatch = 13 -13',                    # just let J/psi -> mu+ mu-
       ),
       parameterSets = cms.vstring('pythia8CommonSettings',
                                   'pythia8CUEP8M1Settings',
                                   'pythiaJpsiDecays')
   )
)

mumugenfilter = cms.EDFilter("PythiaDauVFilter",
    verbose         = cms.untracked.int32(0),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID      = cms.untracked.int32(443),
    DaughterIDs     = cms.untracked.vint32(-13, 13),
    MinPt           = cms.untracked.vdouble( 3.,  3.),
    MinEta          = cms.untracked.vdouble(-3., -3.),
    MaxEta          = cms.untracked.vdouble( 3.,  3.)
)

ProductionFilterSequence = cms.Sequence(generator*mumugenfilter)
