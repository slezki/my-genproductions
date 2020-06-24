import FWCore.ParameterSet.Config as cms

from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            convertPythiaCodes = cms.untracked.bool(False),
            operates_on_particles = cms.vint32(521),
            list_forced_decays = cms.vstring('MyB+','MyB-'),
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            user_decay_embedded = cms.vstring(
'''
Alias      MyB+   B+
Alias      MyB-   B-
ChargeConj MyB-   MyB+

Alias MyJ/psi J/psi
ChargeConj MyJ/psi MyJ/psi

Decay MyJ/psi
1.0000  mu+        mu-                 PHOTOS VLL ;
Enddecay

Decay MyB+
1.0000  MyJ/psi    pi+                  SVS ;
Enddecay

CDecay MyB-

End
'''
           )
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters'
        ),
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on',
            'PTFilter:filter = on',
            'PTFilter:quarkToFilter = 5',
            'PTFilter:scaleToFilter = 1.0',
        ),
    ),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

bgenfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(211),
    MaxEta = cms.untracked.vdouble(2.5),
    MinEta = cms.untracked.vdouble(-2.5),
    MinPt = cms.untracked.vdouble(1.0),
    NumberDaughters = cms.untracked.int32(1),
    ParticleID = cms.untracked.int32(521),
    verbose = cms.untracked.int32(0)
)

mumugenfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(-13, 13),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MinPt = cms.untracked.vdouble(3.8, 3.8),
    MotherID = cms.untracked.int32(521),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID = cms.untracked.int32(443),
    verbose = cms.untracked.int32(0)
)

ProductionFilterSequence = cms.Sequence(generator*bgenfilter*mumugenfilter)
