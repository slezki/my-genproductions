import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         filterEfficiency = cms.untracked.double(0.00046),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         crossSection = cms.untracked.double(1049000000.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         comEnergy = cms.double(13000.0),
                         PythiaParameters = cms.PSet(
                            pythia8CommonSettingsBlock,
                            pythia8CUEP8M1SettingsBlock,
                            processParameters = cms.vstring(
                               'HardQCD:all = on',
                               'ParticleDecays:allowPhotonRadiation = on', # Turn on QED FSR
			       '511:onMode = off',      # ... speed up generation of J/psi using the most common b-hadrons
			       '511:onIfAny = 443',     
			       '521:onMode = off',
			       '521:onIfAny = 443',
			       '531:onMode = off',
			       '531:onIfAny = 443',
			       '541:onMode = off',
			       '541:onIfAny = 443',
			       '5122:onMode = off',
			       '5122:onIfAny = 443',    # ... until here
                               '443:onMode = off',      # Turn off J/psi decays
                               '443:onIfMatch = 13 -13' # just let J/psi -> mu+ mu-
                            ),
                            parameterSets = cms.vstring(
			       'pythia8CommonSettings',
                               'pythia8CUEP8M1Settings',
                               'processParameters',
                            )
                         )
)

bfilter = cms.EDFilter("PythiaFilter",
                       ParticleID = cms.untracked.int32(5)
                       )

jpsifilter = cms.EDFilter("PythiaFilter",
                          Status = cms.untracked.int32(2),
                          MaxEta = cms.untracked.double(1000.0),
                          MinEta = cms.untracked.double(-1000.0),
                          MinPt = cms.untracked.double(3.0),
                          ParticleID = cms.untracked.int32(443)
                          )

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
                             Status = cms.untracked.vint32(1, 1),
                             MinPt = cms.untracked.vdouble(0.5, 0.5),
                             MinP = cms.untracked.vdouble(0., 0.),
                             MaxEta = cms.untracked.vdouble(2.5, 2.5),
                             MinEta = cms.untracked.vdouble(-2.5, -2.5),
                             ParticleCharge = cms.untracked.int32(-1),
                             MaxInvMass = cms.untracked.double(4.0),
                             MinInvMass = cms.untracked.double(2.0),
                             ParticleID1 = cms.untracked.vint32(13),
                             ParticleID2 = cms.untracked.vint32(13)
                             )

ProductionFilterSequence = cms.Sequence(generator*bfilter*jpsifilter*mumugenfilter)

