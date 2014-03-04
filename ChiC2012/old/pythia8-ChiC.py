import FWCore.ParameterSet.Config as cms

RatioChiB1 = 0.62 # 1 if only chib1, 0 if only chib2
sel_Chib_fileName = cms.untracked.string('py8-sel_ChiC.root')
gen_Chib_fileName = cms.untracked.string('py8-gen_ChiC.root')
Run = 1
initSEED = 23400 + 3 * 1
Nevents = 100000

process = cms.Process('chibSim')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeV2012Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
#
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('HLTrigger.Configuration.HLT_7E33v2_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
#
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
#
process.load('PhysicsTools.PatAlgos.mcMatchLayer0.muonMatch_cfi')
process.load('PhysicsTools.HepMCCandAlgos.genParticles_cfi')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('RecoTracker.TrackProducer.TrackRefitter_cfi')

# Input source
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(Nevents)
)

# Input source
process.source = cms.Source("EmptySource",
    firstEvent = cms.untracked.uint32(1),
    firstRun = cms.untracked.uint32(Run)
)
process.RandomNumberGeneratorService.generator = cms.PSet(
    initialSeed = cms.untracked.uint32(initSEED),
    engineName = cms.untracked.string('HepJamesRandom')
)

process.options = cms.untracked.PSet(
	wantSummary = cms.untracked.bool(True)
)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup_7E33v2', '')

process.oniafilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(2, 1),
    MinPt = cms.untracked.vdouble(7.5, 0.2),
    MaxEta = cms.untracked.vdouble(9999., 9999.),
    MinEta = cms.untracked.vdouble(-9999., -9999.),
    ParticleCharge = cms.untracked.int32(0),
    MinP = cms.untracked.vdouble(0.,0.),
    ParticleID1 = cms.untracked.vint32(443),
    ParticleID2 = cms.untracked.vint32(22)
)

process.mumugenfilter = cms.EDFilter("PythiaDauVFilter",
    ParticleID = cms.untracked.int32(443),
    MotherID = cms.untracked.int32(0),
    NumberDaughters = cms.untracked.int32(2),
    DaughterIDs = cms.untracked.vint32(13, -13),
    MinPt = cms.untracked.vdouble(1.0, 1.0),
    MaxEta = cms.untracked.vdouble(2.2, 2.2),
    MinEta = cms.untracked.vdouble(-2.2, -2.2)
)

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
            operates_on_particles = cms.vint32(443,100443,10441,20443,445,30443),   #J/psi,psi(2s),chi_c0,chi_c1,chi_c2,psi(3770)
            use_default_decay = cms.untracked.bool(False),
            decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
            user_decay_file = cms.FileInPath('POnia_mumugamma.dec'),
            list_forced_decays = cms.vstring('Mychi_c1','Mychi_c2'),
        ),
        parameterSets = cms.vstring('EvtGen')
    ),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.0463),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(13775390),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring(
            'Main:timesAllowErrors    = 10000',
            'ParticleDecays:limitTau0 = on',     # mstj(22)=2 - decay unstable particles
            'ParticleDecays:tauMax = 10',        # parj(71)=10.- for which ctau < 10 mm
            'Tune:pp 5'                          # Tune 4C
        ),
        processParameters = cms.vstring(
            'Charmonium:all = on',                        # Quarkonia, MSEL=61
            'StringFlav:mesonCL1S0J1 = 0.1933',           # relative pseudovector production ratio (L=1,S=0,J=1)/pseudoscalar for charm mesons
            'StringFlav:mesonCL1S1J0 = 0.0644',           # relative scalar production ratio (L=1,S=1,J=0)/pseudoscalar for charm mesons
            'StringFlav:mesonCL1S1J1 = 0.1933',           # relative pseudovector production ratio (L=1,S=1,J=1)/pseudoscalar for charm mesons
            'Charmonium:OJpsi3S11 = 1.16',                # New values for COM matrix elements', begin
            'Charmonium:OJpsi3S18 = 0.0119',
            'Charmonium:OJpsi1S08 = 0.01',
            'Charmonium:OJpsi3P08 = 0.01',
            'Charmonium:Ochic03P01 = 0.05',
            'Bottomonium:OUpsilon3S11 = 9.28',
            'Bottomonium:OUpsilon3S18 = 0.15',
            'Bottomonium:OUpsilon1S08 = 0.02',
            'Bottomonium:OUpsilon3P08 = 0.02',
            'Bottomonium:Ochib03P01 = 0.085',             # New values for COM matrix elements', end
            '443:onMode = off',                           # Turn off J/psi decays
            '443:onIfAny = 13 -13',                       # just let J/psi -> mu+ mu-
            '20443:onMode = off',                         # Turn off Chi_c1
            '20443:onIfAny = 443 22',                     # let Chi_c1 -> J/psi gamma
            '445:onMode = off',                           # Turn off Chi_c2
            '445:onIfAny = 443 22'                        # let chi_c2 -> J/psi gamma
        ),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters'
        )
    )
)

process.ProductionFilterSequence = cms.Sequence(process.generator*process.oniafilter*process.mumugenfilter)

process.load("Ponia.Modules.CHARM_chiCandProducer_cff")

process.recoout = cms.OutputModule(
    "PoolOutputModule",
    fileName = sel_Chib_fileName,
    outputCommands =  cms.untracked.vstring('drop *',
					    'keep *_offlinePrimaryVertices__*',
					    'keep *_dimuonProducer_*_*',  
					    #'keep *_*_conversions_*',
                                            'keep *_chiCandProducer_*_*',
                                            'keep *_refit_*_*',
					    'keep *_genParticles_*_*',
					    'keep *_g4SimHits__*',
					    #'keep *'
					    ),
    SelectEvents = cms.untracked.PSet(
                       SelectEvents = cms.vstring('pat')
        )
    )

process.genout = cms.OutputModule(
	"PoolOutputModule",
	fileName = gen_Chib_fileName,
	outputCommands =  cms.untracked.vstring('drop *',
						'keep *_offlinePrimaryVertices_*_*',
						'keep *_genParticles_*_*',
						'keep *_g4SimHits__*',
						#'keep *'
						),
        SelectEvents = cms.untracked.PSet(
                       SelectEvents = cms.vstring('gen')
        )
    )

import HLTrigger.HLTfilters.triggerResultsFilter_cfi as hlt
process.filter_1 = hlt.triggerResultsFilter.clone(
                   triggerConditions =  ( 'HLT_Dimuon0_Jpsi_v*',
                                          'HLT_Dimuon8_Jpsi_v*',
                                          'HLT_Dimuon10_Jpsi_v*',
                                        ),
                   hltResults = cms.InputTag( 'TriggerResults' ),
                   l1tResults = '',
                   throw      = False
)
process.path_1 = cms.EndPath( process.filter_1 )

# Path and EndPath definitions

process.gen = cms.Path(process.pgen)

process.sim = cms.Path(process.psim*
		       process.pdigi
		       )

process.PreHLT= cms.Path(
                       process.psim*
		       process.pdigi*
	               process.SimL1Emulator*
		       process.DigiToRaw)
		       
process.reco= cms.Path(process.RawToDigi*
		       process.L1Reco*
		       process.reconstruction*
		       process.TrackRefitter)# why do we need this ?

process.pat = cms.Path(process.muonMatch*
                       process.chiSequence
		       )

process.summary = cms.EndPath( process.genFilterSummary )
process.endreco = cms.EndPath( process.recoout )
process.endgen = cms.EndPath( process.genout )

process.schedule = cms.Schedule(process.gen,
				process.sim,
				process.PreHLT)

process.schedule.append(	process.endgen)

process.schedule.extend(	process.HLTSchedule)

process.schedule.extend([	process.reco,
				process.path_1,
				process.pat,
				process.summary,
				process.endreco])


# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

process.dimuonProducer.addMuonlessPrimaryVertex = False

