import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic7TeV2011Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet()

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.284.2.5 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/PYTHIA_BuToChic1K_7TeV_cff.py nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition
process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('PYTHIA6_Chic1ToJpsiGamma_FilterJpsiGamma-all_7TeV_GEN.root'),					
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START53_V14::All'

process.mugenfilter = cms.EDFilter("MCSingleParticleFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(10.0, 10.0),
    ParticleID = cms.untracked.vint32(13, -13)
)

process.oniafilter = cms.EDFilter("PythiaDauVFilter",
    ParticleID = cms.untracked.int32(20443),
    MotherID = cms.untracked.int32(0),
    NumberDaughters = cms.untracked.int32(2),
    DaughterIDs = cms.untracked.vint32(443, 22),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(999., 999.),
    MinEta = cms.untracked.vdouble(-999., -999.)
)

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.138),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(1256000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTJ(11)=3     ! Choice of the fragmentation function',
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
            'PARP(93)=15.0  ! '),
        processParameters = cms.vstring('MSEL=61          ! Quarkonia',
            'CKIN(3)=10.       ! Min pthard',
            'CKIN(4)=-1.      ! Max pthard',
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
            'BRAT(859)=1.000  ! J/psi->mu+mu-',
            'BRAT(861)=0.000  ! chi_2c->J/psi gamma',
            'BRAT(862)=1.000  ! chi_2c->rndmflav rndmflavbar',
            'BRAT(1501)=0.000 ! chi_0c->J/psi gamma',
            'BRAT(1502)=1.000 ! chi_0c->rndmflav rndmflavbar',
            'BRAT(1555)=1.000 ! chi_1c->J/psi gamma',
            'BRAT(1556)=0.000 ! chi_1c->rndmflav rndmflavbar',
            'BRAT(1569)=0.186600 ! psi(2S) -> rndmflav rndmflavbar',
            'BRAT(1570)=0.000 ! psi(2S) ->J/psi pi+ pi-',
            'BRAT(1571)=0.000 ! psi(2S) ->J/psi pi0 pi0',
            'BRAT(1572)=0.000 ! psi(2S) ->J/psi eta',
            'BRAT(1573)=0.000 ! psi(2S) ->J/psi pi0'),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters',
            'CSAParameters'),
        CSAParameters = cms.vstring('CSAMODE = 6     ! cross-section reweighted quarkonia')
    )
)


process.mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleCharge = cms.untracked.int32(-1),
    MinP = cms.untracked.vdouble(2.7, 2.7),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

process.ProductionFilterSequence = cms.Sequence(process.generator+process.oniafilter+process.mumugenfilter+~process.mugenfilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 
