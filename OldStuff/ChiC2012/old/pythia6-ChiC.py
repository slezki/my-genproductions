import FWCore.ParameterSet.Config as cms

RatioChiB1 = 0.62 # 1 if only chib1, 0 if only chib2
sel_Chib_fileName = cms.untracked.string('py6-sel_ChiC.root')
gen_Chib_fileName = cms.untracked.string('py6-gen_ChiC.root')
Run = 1
initSEED = 23400 + 3 * 1
Nevents = 100000

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
process.load('HLTrigger.Configuration.HLT_7E33v2_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# import of standard configurations
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')

process.load('PhysicsTools.PatAlgos.mcMatchLayer0.muonMatch_cfi')

process.load("Configuration.Generator.PythiaUESettings_cfi")
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

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
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
            'MSTJ(11)=3     ! Choice of the fragmentation function',
            'MSTJ(22)=2     ! Decay those unstable particles',
            'PARJ(71)=10 .  ! for which ctau  10 mm',
            'MSTP(2)=1      ! which order running alphaS',
            'MSTP(33)=0     ! no K factors in hard cross sections',
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
            'MSTP(52)=2     ! work with LHAPDF',
            'MSTP(81)=1     ! multiple parton interactions 1 is Pythia default',
            'MSTP(82)=4     ! Defines the multi-parton model',
            'MSTU(21)=1     ! Check on possible errors during program execution',
            'PARP(82)=1.8387   ! pt cutoff for multiparton interactions',
            'PARP(89)=1960. ! sqrts for which PARP82 is set',
            'PARP(83)=0.5   ! Multiple interactions: matter distrbn parameter',
            'PARP(84)=0.4   ! Multiple interactions: matter distribution parameter',
            'PARP(90)=0.16  ! Multiple interactions: rescaling power',
            'PARP(67)=2.5    ! amount of initial-state radiation',
            'PARP(85)=1.0  ! gluon prod. mechanism in MI',
            'PARP(86)=1.0  ! gluon prod. mechanism in MI',
            'PARP(62)=1.25   ! ',
            'PARP(64)=0.2    ! ',
            'MSTP(91)=1      !',
            'PARP(91)=2.1   ! kt distribution',
            'PARP(93)=15.0  ! '
        ),
        processParameters = cms.vstring(
            'MSEL=61          ! Quarkonia',
            'MDME(858,1) = 0  ! 0.060200    e-    e+',
            'MDME(859,1) = 1  ! 0.060100    mu-  mu+',
            'MDME(860,1) = 0  ! 0.879700    rndmflav        rndmflavbar',
            'MSTP(142)=2      ! turns on the PYEVWT Pt re-weighting routine',
            'PARJ(13)=0.750   ! probability that a c or b meson has S=1',
            'PARJ(14)=0.162   ! probability that a meson with S=0 is produced with L=1, J=1',
            'PARJ(15)=0.018   ! probability that a meson with S=1 is produced with L=1, J=0',
            'PARJ(16)=0.054   ! probability that a meson with S=1 is produced with L=1, J=1',
            'MSTP(145)=0      ! choice of polarization',
            'MSTP(146)=0      ! choice of polarization frame ONLY when mstp(145)=1',
            'MSTP(147)=0      ! particular helicity or density matrix component when mstp(145)=1',
            'MSTP(148)=1      ! possibility to allow for final-state shower evolution, extreme case !',
            'MSTP(149)=1      ! if mstp(148)=1, it determines the kinematics of the QQ~3S1(8)->QQ~3S1(8)+g branching',
            'PARP(141)=1.16   ! New values for COM matrix elements',
            'PARP(142)=0.0119 ! New values for COM matrix elements',
            'PARP(143)=0.01   ! New values for COM matrix elements',
            'PARP(144)=0.01   ! New values for COM matrix elements',
            'PARP(145)=0.05   ! New values for COM matrix elements',
            'PARP(146)=9.28   ! New values for COM matrix elements',
            'PARP(147)=0.15   ! New values for COM matrix elements',
            'PARP(148)=0.02   ! New values for COM matrix elements',
            'PARP(149)=0.02   ! New values for COM matrix elements',
            'PARP(150)=0.085  ! New values for COM matrix elements',
            'BRAT(861)=1.000  ! chi_2c->J/psi gamma',
            'BRAT(862)=0.000  ! chi_2c->rndmflav rndmflavbar',
            'BRAT(1501)=0.013 ! chi_0c->J/psi gamma',
            'BRAT(1502)=0.987 ! chi_0c->rndmflav rndmflavbar',
            'BRAT(1555)=1.000 ! chi_1c->J/psi gamma',
            'BRAT(1556)=0.000 ! chi_1c->rndmflav rndmflavbar'
        ),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters',
            'CSAParameters'),
        CSAParameters = cms.vstring('CSAMODE = 6     ! cross-section reweighted quarkonia')
    )
)

process.ProductionFilterSequence = cms.Sequence(process.generator+process.oniafilter+process.mumugenfilter)

process.load("Ponia.Modules.CHARM_chiCandProducer_cff")

process.recoout = cms.OutputModule(
    "PoolOutputModule",
    fileName = sel_Chib_fileName,
    outputCommands =  cms.untracked.vstring('drop *',
					    'keep *_offlinePrimaryVertices__*',
					    'keep *_dimuonProducer_*_*',  
#					    #'keep *_*_conversions_*',
                                            'keep *_chiCandProducer_*_*',
                                            'keep *_refit_*_*',
					    'keep *_genParticles_*_*',
					    'keep *_g4SimHits__*',
#					    #'keep *'
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

