import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
             'HardQCD:all = on',
             'PhaseSpace:pTHatMin = 8.',
             '100113:onMode = off',
             '100213:onMode = off',
             '100441:onMode = off',
             '100443:onMode = off',
             '100553:onMode = off',
             '10113:onMode = off',
             '10213:onMode = off',
             '10221:onMode = off',
             '10223:onMode = off',
             '10311:onMode = off',
             '10313:onMode = off',
             '10321:onMode = off',
             '10323:onMode = off',
             '10333:onMode = off',
             '10411:onMode = off',
             '10413:onMode = off',
             '10421:onMode = off',
             '10423:onMode = off',
             '10431:onMode = off',
             '10433:onMode = off',
             '10441:onMode = off',
             '10443:onMode = off',
             '10511:onMode = off',
             '10513:onMode = off',
             '10521:onMode = off',
             '10523:onMode = off',
             '10531:onMode = off',
             '10533:onMode = off',
             '10541:onMode = off',
             '10543:onMode = off',
             '10551:onMode = off',
             '10553:onMode = off',
             '1114:onMode = off',
             '111:onMode = off',
             '113:onMode = off',
             '115:onMode = off',
             '130:onMode = off',
             '13122:onMode = off',
             '14122:onMode = off',
             '15:onMode = off',
             '200553:onMode = off',
             '20113:onMode = off',
             '20213:onMode = off',
             '20223:onMode = off',
             '20313:onMode = off',
             '20323:onMode = off',
             '20333:onMode = off',
             '20413:onMode = off',
             '20423:onMode = off',
             '20433:onMode = off',
             '20443:onMode = off',
             '20513:onMode = off',
             '20523:onMode = off',
             '20533:onMode = off',
             '20543:onMode = off',
             '20553:onMode = off',
             '2114:onMode = off',
             '213:onMode = off',
             '215:onMode = off',
             '2214:onMode = off',
             '221:onMode = off',
             '2224:onMode = off',
             '223:onMode = off',
             '225:onMode = off',
             '23122:onMode = off',
             '30313:onMode = off',
             '30323:onMode = off',
             '30443:onMode = off',
             '310:onMode = off',
             '3112:onMode = off',
             '3114:onMode = off',
             '311:onMode = off',
             '3122:onMode = off',
             '3124:onMode = off',
             '313:onMode = off',
             '315:onMode = off',
             '3212:onMode = off',
             '3214:onMode = off',
             '3222:onMode = off',
             '3224:onMode = off',
             '323:onMode = off',
             '325:onMode = off',
             '33122:onMode = off',
             '3312:onMode = off',
             '3314:onMode = off',
             '331:onMode = off',
             '3322:onMode = off',
             '3324:onMode = off',
             '3334:onMode = off',
             '333:onMode = off',
             '335:onMode = off',
             '4112:onMode = off',
             '4114:onMode = off',
             '411:onMode = off',
             '4122:onMode = off',
             '4132:onMode = off',
             '413:onMode = off',
             '415:onMode = off',
             '4212:onMode = off',
             '4214:onMode = off',
             '421:onMode = off',
             '4222:onMode = off',
             '4224:onMode = off',
             '4232:onMode = off',
             '423:onMode = off',
             '425:onMode = off',
             '4312:onMode = off',
             '4314:onMode = off',
             '431:onMode = off',
             '4322:onMode = off',
             '4324:onMode = off',
             '4332:onMode = off',
             '4334:onMode = off',
             '433:onMode = off',
             '435:onMode = off',
             '4412:onMode = off',
             '4414:onMode = off',
             '441:onMode = off',
             '4422:onMode = off',
             '4424:onMode = off',
             '4432:onMode = off',
             '4434:onMode = off',
             '443:onMode = off',
             '445:onMode = off',
             '5112:onMode = off',
             '5114:onMode = off',
             '511:onMode = off',
             '5122:onMode = off',
             '5132:onMode = off',
             '513:onMode = off',
             '515:onMode = off',
             '5212:onMode = off',
             '5214:onMode = off',
             '521:onMode = off',
             '5222:onMode = off',
             '5224:onMode = off',
             '5232:onMode = off',
             '523:onMode = off',
             '525:onMode = off',
             '5312:onMode = off',
             '5314:onMode = off',
             '531:onMode = off',
             '5322:onMode = off',
             '5324:onMode = off',
             '5332:onMode = off',
             '5334:onMode = off',
             '533:onMode = off',
             '535:onMode = off',
             '541:onMode = off',
             '543:onMode = off',
             '545:onMode = off',
             '551:onMode = off',
             '553:onMode = off',
             '555:onMode = off',
             '9000111:onMode = off',
             '9000211:onMode = off',
             '9010221:onMode = off'
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
    )
)

#filter for b-quark
bfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(5)
)

ProductionFilterSequence = cms.Sequence(generator*bfilter)
