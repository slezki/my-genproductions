import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
                'Charmonium:states(3S1) = 100443',
                'Charmonium:O(3S1)[3S1(1)] = 0.76',
                'Charmonium:O(3S1)[3S1(8)] = 0.0050',
                'Charmonium:O(3S1)[1S0(8)] = 0.004',
                'Charmonium:O(3S1)[3P0(8)] = 0.004',
                'Charmonium:gg2ccbar(3S1)[3S1(1)]g = on',
                'Charmonium:gg2ccbar(3S1)[3S1(1)]gm = on',
                'Charmonium:gg2ccbar(3S1)[3S1(8)]g = on',
                'Charmonium:qg2ccbar(3S1)[3S1(8)]q = on',
                'Charmonium:qqbar2ccbar(3S1)[3S1(8)]g = on',
                'Charmonium:gg2ccbar(3S1)[1S0(8)]g = on',
                'Charmonium:qg2ccbar(3S1)[1S0(8)]q = on',
                'Charmonium:qqbar2ccbar(3S1)[1S0(8)]g = on',
                'Charmonium:gg2ccbar(3S1)[3PJ(8)]g = on',
                'Charmonium:qg2ccbar(3S1)[3PJ(8)]q = on',
                'Charmonium:qqbar2ccbar(3S1)[3PJ(8)]g = on',
                '100443:onMode = off',                          # Turn off psi2s decays
                '100443:onIfMatch = 13 -13',                    # just let psi2s -> mu+ mu-
                'PhaseSpace:pTHatMin = 15.'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
    )
)

# Filter with high pT cut on dimuon, trying to accomodate trigger requirements.

mumufilter = cms.EDFilter("PythiaDauVFilter",
        MotherID = cms.untracked.int32(0),
        MinPt = cms.untracked.vdouble(4.0,4.0),
        ParticleID = cms.untracked.int32(100443),
        ChargeConjugation = cms.untracked.bool(False),
        MinEta = cms.untracked.vdouble(-1.5,-1.5),
        MaxEta = cms.untracked.vdouble(1.5,1.5),
        NumberDaughters = cms.untracked.int32(2),
        DaughterIDs = cms.untracked.vint32(13, -13)
        )

oniafilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(2),
    MaxRapidity = cms.untracked.double(1.5),
    MinRapidity = cms.untracked.double(-1.5),
    MinPt = cms.untracked.double(24.0),
    ParticleID = cms.untracked.int32(100443)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumufilter)
