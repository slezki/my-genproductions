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
    fileName = cms.untracked.string('PYTHIA8_Chic1ToJpsiGamma_Flavor_7TeV_GEN.root'),					
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

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.138),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(1256000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8UESettings = cms.vstring(
         'Main:timesAllowErrors    = 10000',
         'ParticleDecays:limitTau0 = on',     # mstj(22)=2 - decay unstable particles
         'ParticleDecays:tauMax = 10',        # parj(71)=10.- for which ctau < 10 mm
         'Tune:pp 5'                          # Tune 4C
        ),
        pythia8ProcessSettings = cms.vstring(
         'Charmonium:all = on',                        # Quarkonia, MSEL=61 
         'PhaseSpace:pTHatMin = 10.',                  # CKIN(3)
         #'ParticleDecays:allowPhotonRadiation = on',   # Photos equivalent
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
         '445:onMode = off',                           # Turn off Chi_c2 
         '445:onIfAny = 83 -83',                       # let Chi_c2 -> J/psi gamma
         '10441:onMode = off',                         # Turn off Chi_c0 
         '10441:onIfAny = 83 -83',                     # let Chi_c0 -> J/psi gamma
         '20443:onMode = off',                         # Turn off Chi_c1
         '20443:onIfAny = 443 22',                     # let Chi_c1 -> J/psi gamma
         '100443:onMode = off',                        # Turn off Psi(2s) 
         '100443:onIfAny = 83 -83'                     # let Psi(2s) -> rndmflavor bar-rndmflavor
#        'MSTP(142)=2      ! turns on the PYEVWT Pt re-weighting routine', 
        ),
        parameterSets = cms.vstring('pythia8UESettings','pythia8ProcessSettings')
#        'CSAParameters'),
#        CSAParameters = cms.vstring('CSAMODE = 6     ! cross-section reweighted quarkonia')
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
