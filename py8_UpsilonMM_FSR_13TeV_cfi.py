import FWCore.ParameterSet.Config as cms

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
            'PhaseSpace:pTHatMin = 20.0',         # ckin(3) > 20., be aware of this
            'Tune:pp 5'                           # Tune 4C
        ),
        processParameters = cms.vstring(
            'Bottomonium:all = on',                # Quarkonia, MSEL=62
            'ParticleDecays:allowPhotonRadiation = on', # Turn on QED FSR
            'StringFlav:mesonBvector = 3.000',    # relative production vector/pseudoscalar for charm mesons - needs work
            'StringFlav:mesonBL1S1J0 = 0.072',    # relative scalar production (L=1,S=1,J=0)/pseudoscalar for charm mesons
            'StringFlav:mesonBL1S0J1 = 3.000',    # relative pseudovector production (L=1,S=0,J=1)/pseudoscalar for charm mesons
            'StringFlav:mesonBL1S1J1 = 0.216',    # relative pseudovector production (L=1,S=1,J=1)/pseudoscalar for charm mesons
            'StringFlav:mesonBL1S1J2 = 0.000',    # relative tensor production (L=1,S=1,J=2)/pseudoscalar for charm mesons
            '553:onMode = off',                   # Turn off Upsilon decays
            '553:onIfMatch = 13 -13'              # just let Upsilon -> mu+ mu-
        ),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters'
        )
    )
)

oniafilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(2),
    MaxEta = cms.untracked.double(1000.0),
    MinEta = cms.untracked.double(-1000.0),
    MinPt = cms.untracked.double(0.0),
    ParticleID = cms.untracked.int32(553)
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MinP = cms.untracked.vdouble(2.7, 2.7),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MinInvMass = cms.untracked.double(5.0),
    MaxInvMass = cms.untracked.double(20.0),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumugenfilter)
