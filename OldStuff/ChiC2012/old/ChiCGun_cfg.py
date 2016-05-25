import FWCore.ParameterSet.Config as cms

RatioChiB1 = 0.62 # 1 if only chib1, 0 if only chib2
sel_Chib_fileName = cms.untracked.string('g-sel_Chic.root')
gen_Chib_fileName = cms.untracked.string('g-gen_Chic.root')

process = cms.Process('chibSim')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.load('PhysicsTools.PatAlgos.mcMatchLayer0.muonMatch_cfi')
#process.load('PhysicsTools.PatAlgos.producersLayer1.muonProducer_cfi')
#process.load('Ponia.Configuration.MuonSelection')

process.load("Configuration.Generator.PythiaUESettings_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('PhysicsTools.HepMCCandAlgos.genParticles_cfi')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('RecoTracker.TrackProducer.TrackRefitter_cfi')

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

#process.MessageLogger.destinations = cms.untracked.vstring("debug_sim_chib.txt")
#process.MessageLogger.cout = process.MessageLogger.cerr
#process.MessageLogger.cout.threshold = cms.untracked.string("DEBUG")

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
	wantSummary = cms.untracked.bool(True)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

process.GlobalTag.globaltag = 'START53_V14::All'
process.GlobalTag.toGet = cms.VPSet()
process.GlobalTag.toGet.append(cms.PSet(tag=cms.string("L1GtTriggerMenu_L1Menu_Collisions2012_v2_mc"),record=cms.string("L1GtTriggerMenuRcd"),connect=cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_L1T"),))
process.GlobalTag.toGet.append(cms.PSet(tag=cms.string("L1GctJetFinderParams_GCTPhysics_2012_04_27_JetSeedThresh5GeV_mc"),record=cms.string("L1GctJetFinderParamsRcd"),connect=cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_L1T"),))
process.GlobalTag.toGet.append(cms.PSet(tag=cms.string("L1HfRingEtScale_GCTPhysics_2012_04_27_JetSeedThresh5GeV_mc"),record=cms.string("L1HfRingEtScaleRcd"),connect=cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_L1T"),))
process.GlobalTag.toGet.append(cms.PSet(tag=cms.string("L1HtMissScale_GCTPhysics_2012_04_27_JetSeedThresh5GeV_mc"),record=cms.string("L1HtMissScaleRcd"),connect=cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_L1T"),))
process.GlobalTag.toGet.append(cms.PSet(tag=cms.string("L1JetEtScale_GCTPhysics_2012_04_27_JetSeedThresh5GeV_mc"),record=cms.string("L1JetEtScaleRcd"),connect=cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_L1T"),))
process.GlobalTag.toGet.append(cms.PSet(tag=cms.string("JetCorrectorParametersCollection_AK5PF_2012_V8_hlt_mc"),record=cms.string("JetCorrectionsRecord"),connect=cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),label=cms.untracked.string("AK5PFHLT"),))
process.GlobalTag.toGet.append(cms.PSet(tag=cms.string("JetCorrectorParametersCollection_AK5PFchs_2012_V8_hlt_mc"),record=cms.string("JetCorrectionsRecord"),connect=cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),label=cms.untracked.string("AK5PFchsHLT"),))


process.generator = cms.EDProducer("Pythia6CustomPtGun",
    maxEventsToPrint = cms.untracked.int32(5),
    pythiaPylistVerbosity = cms.untracked.int32(0),   #set to 1 for printout
    pythiaHepMCVerbosity = cms.untracked.bool(False), #set to True for printout   
    PGunParameters = cms.PSet(
        ParticleID = cms.vint32(20443,445), #Chi_b1 - Chi_b2
        AddAntiParticle = cms.bool(False),
        MinPhi = cms.double(-3.14159265359),
        MaxPhi = cms.double(3.14159265359),
        MinPt = cms.double(5.0),
        MaxPt = cms.double(40.0),
        MinEta = cms.double(-2.0),
        MaxEta = cms.double(2.0),
        OnOdd  = cms.bool(True),
	RatioPart1 = cms.double(RatioChiB1), #Fraction of particle1 over all particle produced
	HFilename = cms.string('GeneratorInterface/Pythia6Interface/data/jpsipt.root'),
	HName     = cms.string('jpsipt'),
        ),
     PythiaParameters = cms.PSet(
        process.pythiaUESettingsBlock,
        pythiaJpsiDecays = cms.vstring(
            'MSEL=61                       ! Quarkonia', 
            'MDME(858,1) = 0  ! 0.060200    e-    e+',
            'MDME(859,1) = 1  ! 0.060100    mu-  mu+',
            'MDME(860,1) = 0  ! 0.879700    rndmflav        rndmflavbar',
            'BRAT(861)=1.0  ! chi_2c->J/psi gamma',
            'BRAT(862)=0.0  ! chi_2c->rndmflav rndmflavbar',
            'BRAT(1555)=1.000 ! chi_1c->J/psi gamma',
            'BRAT(1556)=0.000 ! chi_1c->rndmflav rndmflavbar'
            ),
           
     # This is a vector of ParameterSet names to be read, in this order
     parameterSets = cms.vstring('pythiaUESettings', 
                                 'pythiaJpsiDecays'
                                 )
     )                                   
) 

process.triggerSelection = cms.EDFilter( "TriggerResultsFilter",
				 triggerConditions = cms.vstring(
		'HLT_Dimuon8_Jpsi_v*',
		),
				 hltResults = cms.InputTag( "TriggerResults", "", "chibSim" ),
				 l1tResults = cms.InputTag( "gtDigis" ),
				 l1tIgnoreMask = cms.bool( False ),
				 l1techIgnorePrescales = cms.bool( False ),
				 daqPartitions = cms.uint32( 1 ),
				 throw = cms.bool( True )
				 )

process.load("Ponia.Modules.CHARM_chiCandProducer_cff")

process.recoout = cms.OutputModule(
    "PoolOutputModule",
    fileName = sel_Chib_fileName,
    outputCommands =  cms.untracked.vstring('drop *',
					    'keep *_offlinePrimaryVertices__*',
					    'keep *_dimuonProducer_*_*', #UpsilonCandLorentzVector_*',  
					    #'keep *_*_conversions_*',
                                            'keep *_chiCandProducer_*_*',
                                            #'keep *_refit1S_*_*',
					    #'keep *_refit2S_*_*',
					    #'keep *_refit3S_*_*',
                                            'keep *_refit_*_*',
					    'keep *_genParticles_*_*',
					    'keep *_g4SimHits__*',
					    #'keep *'
					    ),
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
	)

# Path and EndPath definitions
process.gen = cms.Path(process.generator*
		       process.VtxSmeared*
		       process.genParticles)


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

process.trigSel = cms.EndPath(process.triggerSelection)

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
				process.trigSel,
				process.pat,
				process.summary,
				process.endreco])

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

process.dimuonProducer.addMuonlessPrimaryVertex = False
