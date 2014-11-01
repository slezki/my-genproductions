import FWCore.ParameterSet.Config as cms
from Configuration.Generator.PythiaUESettings_cfi import *

oniafilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(2, 1),
    MinPt = cms.untracked.vdouble(7.5, 0.2),
    MaxEta = cms.untracked.vdouble(9999., 9999.),
    MinEta = cms.untracked.vdouble(-9999., -9999.),
    ParticleCharge = cms.untracked.int32(0),
    MinP = cms.untracked.vdouble(0.,0.),
    ParticleID1 = cms.untracked.vint32(443),
    ParticleID2 = cms.untracked.vint32(22)
)

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

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.0757),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(13775390),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring(
            'Main:timesAllowErrors    = 10000',
            'ParticleDecays:limitTau0 = on',      # mstj(22)=2 - decay unstable particles
            'ParticleDecays:tauMax = 10',         # parj(71)=10.- for which ctau < 10 mm
            'PhaseSpace:pTHatMin = 0.0',          # ckin(3)
            'Tune:pp 5'                           # Tune 4C
        ),
        processParameters = cms.vstring(
            'Charmonium:all = on',                # Quarkonia, MSEL=61
            'ParticleDecays:allowPhotonRadiation = on', # Turn on QED FSR
            'StringFlav:mesonCvector = 5.173',    # relative production vector/pseudoscalar for charm mesons
            'StringFlav:mesonCL1S1J0 = 0.072',    # relative scalar production (L=1,S=1,J=0)/pseudoscalar for charm mesons
            'StringFlav:mesonCL1S0J1 = 3.712',    # relative pseudovector production (L=1,S=0,J=1)/pseudoscalar for charm mesons
            'StringFlav:mesonCL1S1J1 = 0.216',    # relative pseudovector production (L=1,S=1,J=1)/pseudoscalar for charm mesons
            'StringFlav:mesonCL1S1J2 = 0.',       # relative tensor production (L=1,S=1,J=2)/pseudoscalar for charm mesons
            '20443:onMode = off',                 # Turn off Chic1 decays
            '20443:onIfMatch = 443 22',           # just let Chic1 -> J/psi gamma
            '445:onMode = off',                   # Turn off Chic2 decays
            '445:onIfMatch = 443 22',             # just let Chic2 -> J/psi gamma
            '443:onMode = off',                   # Turn off J/psi decays
            '443:onIfMatch = 13 -13'              # just let J/psi -> mu+ mu-
        ),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters'
        )
    )
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*muplusfilter*muminusfilter)
