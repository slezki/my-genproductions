import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8PtCustomYGun",
    maxEventsToPrint = cms.untracked.int32(5),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),

    PGunParameters = cms.PSet(
        MaxPt = cms.double(100.),
        MinPt = cms.double(8.),
        ParticleID = cms.vint32(100541),
        AddAntiParticle = cms.bool(False), 
        MaxY = cms.double(2.4),
        MaxPhi = cms.double(3.14159265359),
        MinY = cms.double(-2.4),
        MinPhi = cms.double(-3.14159265359),
        TFunction_string = cms.string('x*((1.+1./(3.357-2.)*x*x/2.085)^(-3.357))'),  #This if J/psi pT
   ),

   PythiaParameters = cms.PSet(
       pythia8CommonSettingsBlock,
       pythia8CUEP8M1SettingsBlock,
       processParameters = cms.vstring(
            #'absPDGCode:new = Name antiName spin charge colour m0 mWidth mMin mMax tau0'
            '100541:new = B_c(2S)+ B_c(2S)- 1 3 0 6.8670000e+00 0.0000000e+00 6.867 6.867 0.0000000e+00',
            '100541:isResonance = false',
            '100541:addChannel = 1 1.0 0 541 211 -211',
	    '100541:mayDecay = on',
	    '541:onMode = off',
	    '541:onIfMatch = 443 211',
	    '443:onMode = off',
	    '443:onIfMatch = 13 -13'
       ),
       parameterSets = cms.vstring('pythia8CommonSettings',
                                   'pythia8CUEP8M1Settings',
                                   'processParameters'
       )
   )
)

mumugenfilter = cms.EDFilter("PythiaDauVFilter",
    verbose         = cms.untracked.int32(0),
    NumberDaughters = cms.untracked.int32(2),
    MotherID        = cms.untracked.int32(541),
    ParticleID      = cms.untracked.int32(443),
    DaughterIDs     = cms.untracked.vint32(-13, 13),
    MinPt           = cms.untracked.vdouble( 3.,  3.),
    MinEta          = cms.untracked.vdouble(-3., -3.),
    MaxEta          = cms.untracked.vdouble( 3.,  3.)
)

bcgenfilter = cms.EDFilter("PythiaDauVFilter",
    verbose         = cms.untracked.int32(0),
    NumberDaughters = cms.untracked.int32(1),
    ParticleID      = cms.untracked.int32(541),
    DaughterIDs     = cms.untracked.vint32(211),
    MinPt           = cms.untracked.vdouble(0.5),
    MinEta          = cms.untracked.vdouble(-3.),
    MaxEta          = cms.untracked.vdouble(3.)
)

bc2sgenfilter = cms.EDFilter("PythiaDauVFilter",
    verbose         = cms.untracked.int32(0),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID      = cms.untracked.int32(100541),
    DaughterIDs     = cms.untracked.vint32(-211,211),
    MinPt           = cms.untracked.vdouble(0.3,  0.3),
    MinEta          = cms.untracked.vdouble(-3., -3),
    MaxEta          = cms.untracked.vdouble( 3.,  3.)
)

ProductionFilterSequence = cms.Sequence(generator*bc2sgenfilter*bcgenfilter*mumugenfilter)
