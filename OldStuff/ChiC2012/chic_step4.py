import FWCore.ParameterSet.Config as cms

# output name: chose the file name of the output produced
outputname = 'step4.root'

# genparticle: does the files contains genparticles from MC? 
#genpart = 1
genpart = 0

process = cms.Process("Rootuple")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
#process.MessageLogger.destinations = cms.untracked.vstring("debug_rootupleChib.txt")
#process.MessageLogger.cout = process.MessageLogger.cerr
#process.MessageLogger.cout.threshold = cms.untracked.string("INFO")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( 'step3.root' )
    )

process.TFileService = cms.Service("TFileService", 
    fileName = cms.string(outputname),
    closeFileFast = cms.untracked.bool(True)
    )

if(genpart):
	process.load('Ponia.RootupleChib.rootuplechicGen_cfi')
else:
	process.load('Ponia.RootupleChib.rootuplechic_cfi')

process.p = cms.Path(process.rootuple)
