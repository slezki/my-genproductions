
#include <iostream>

#include "Pythia6PtYGun.h"

#include "FWCore/Utilities/interface/Exception.h"

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

#include "FWCore/Framework/interface/MakerMacros.h"

using namespace edm;
using namespace gen;

Pythia6PtYGun::Pythia6PtYGun( const ParameterSet& pset ) : Pythia6ParticleGun(pset) {  
   // ParameterSet defpset ;
   ParameterSet pgun_params = 
      pset.getParameter<ParameterSet>("PGunParameters");
   fMinY            = pgun_params.getParameter<double>("MinY");
   fMaxY            = pgun_params.getParameter<double>("MaxY");
   fMinPt           = pgun_params.getParameter<double>("MinPt");
   fMaxPt           = pgun_params.getParameter<double>("MaxPt");
   fRatioPart1      = pgun_params.getParameter<double>("RatioPart1");  
   fAddAntiParticle = pgun_params.getParameter<bool>("AddAntiParticle");  
   
   if (fPartIDs.size() !=2) {
     edm::LogError("Pythia6PtYGun")<< " Need two particle ids for this module";
   }
}

Pythia6PtYGun::~Pythia6PtYGun(){}

void Pythia6PtYGun::generateEvent(){
   
   Pythia6Service::InstanceWrapper guard(fPy6Service);	// grab Py6 instance

   // now actualy, start cooking up the event gun 
   //

   // 1st, primary vertex
   //
   HepMC::GenVertex* Vtx = new HepMC::GenVertex( HepMC::FourVector(0.,0.,0.));

   // here re-create fEvt (memory)
   //
   fEvt = new HepMC::GenEvent() ;
     
   int ip=1;
   //for ( size_t i=0; i<fPartIDs.size(); i++ ) {

         int dum = 0;
	 int particleID = fPartIDs[0]; // this is PDG - need to convert to Py6 !!!
         if (pyr_(&dum) > fRatioPart1) particleID = fPartIDs[1];
  
	 int py6PID = HepPID::translatePDTtoPythia( particleID );
	 double mass = pymass_(py6PID);
	 
	 // fill p(ip,5) (in PYJETS) with mass value right now,
	 // because the (hardcoded) mstu(10)=1 will make py1ent
	 // pick the mass from there
	 pyjets.p[4][ip-1]=mass; 
	 
	 double phi = (fMaxPhi-fMinPhi)*pyr_(&dum)+fMinPhi;
	 double y   = (fMaxY-fMinY)*pyr_(&dum)+fMinY;
         double pt  = (fMaxPt-fMinPt)*pyr_(&dum)+fMinPt;                                                      
         
         double u = exp(y);
         double ee = 0.5*std::sqrt(mass*mass+pt*pt)*(u*u+1)/u;
         double pz = std::sqrt(ee*ee-pt*pt-mass*mass);
         if ( y < 0. ) pz *= -1;
         double the  = atan(pt/pz);
         if ( pz < 0. ) the += M_PI;

         double eta = -log(tan(the/2.));         

	 py1ent_(ip, py6PID, ee, the, phi);
	 
         double px = pyjets.p[0][ip-1]; // pt*cos(phi) ;
         double py = pyjets.p[1][ip-1]; // pt*sin(phi) ;
         pz        = pyjets.p[2][ip-1]; // mom*cos(the) ;
         
	 HepMC::FourVector p(px,py,pz,ee) ;
         HepMC::GenParticle* Part = 
             new HepMC::GenParticle(p,particleID,1);
         Part->suggest_barcode( ip ) ;
         Vtx->add_particle_out(Part);
	 
	 if(fAddAntiParticle)
	 {
	    ip = ip + 1;
	    HepMC::GenParticle* APart = addAntiParticle( ip, particleID, ee, eta, phi );
	    if ( APart ) Vtx->add_particle_out(APart) ;	    
	 }
	 ip++;
//   }
   
   fEvt->add_vertex(Vtx);
     
   // run pythia
   pyexec_();
   
   return;
}

DEFINE_FWK_MODULE(Pythia6PtYGun);
