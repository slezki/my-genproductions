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
    input = cms.untracked.int32(1000000)
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
    fileName = cms.untracked.string('PYTHIA8_BuToChic1K_8TeV_Bu_GEN-SIM_test.root'),
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
process.GlobalTag.globaltag = 'START53_V26::All'

process.bufilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(521)
)

process.chic1filter = cms.EDFilter("PythiaDauVFilter",
    ParticleID = cms.untracked.int32(20443),
    MotherID = cms.untracked.int32(521),
    NumberDaughters = cms.untracked.int32(2),
    DaughterIDs = cms.untracked.vint32(443, 22),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(10., 10.),
    MinEta = cms.untracked.vdouble(-10., -10.)
)

process.kfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(321),
    MotherID = cms.untracked.int32(521),
    MaxEta = cms.untracked.double(10.),
    MinEta = cms.untracked.double(-10.),
    MinPt = cms.untracked.double(0.0)
)

process.oniafilter = cms.EDFilter("PythiaDauVFilter",
    NumberDaughters = cms.untracked.int32(2),
    DaughterIDs = cms.untracked.vint32(13, -13),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleID = cms.untracked.int32(443),
    MotherID = cms.untracked.int32(20443)
)

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
            operates_on_particles = cms.vint32(521,-521),
            use_default_decay = cms.untracked.bool(False),
            decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Bu_Chic1K.dec'),
	    list_forced_decays = cms.vstring('MyB+',
                'MyB-'),
        ),
        parameterSets = cms.vstring('EvtGen')
    ),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.000422),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(24100000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8UESettings = cms.vstring(
         'Main:timesAllowErrors    = 10000',
         'ParticleDecays:limitTau0 = on',
         'ParticleDecays:tauMax = 10',
         'Tune:pp 5',
         'Tune:ee 3'),
	pythia8ProcessSettings = cms.vstring('HardQCD:all= on'),
        parameterSets = cms.vstring('pythia8UESettings','pythia8ProcessSettings')
    )
)

process.ProductionFilterSequence = cms.Sequence(process.generator+process.bufilter+process.chic1filter+process.kfilter+process.oniafilter)

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
