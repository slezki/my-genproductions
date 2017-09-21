import FWCore.ParameterSet.Config as cms

from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         ExternalDecays = cms.PSet(
                           EvtGen130 = cms.untracked.PSet(
                             decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
                             particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
                             user_decay_file = cms.vstring('GeneratorInterface/EvtGenInterface/data/Bc_JpsiPi.dec'),
                             convertPythiaCodes = cms.untracked.bool(False),
                             list_forced_decays = cms.vstring('MyBc+','MyBc-'),  
                           ),
                           parameterSets = cms.vstring('EvtGen130')
                         ),
                         PythiaParameters = cms.PSet(
                           pythia8CommonSettingsBlock,
                           pythia8CUEP8M1SettingsBlock,
                           processParameters = cms.vstring( #put here any needed pythia parameter
                           ),
                           parameterSets = cms.vstring('pythia8CommonSettings',
                                                       'pythia8CUEP8M1Settings',
                                                       'processParameters'
                           )
                        )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)
ProductionFilterSequence = cms.Sequence(generator)
