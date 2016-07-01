#ifndef gen_Pythia6PtYGun_h
#define gen_Pythia6PtYGun_h

#include "Pythia6ParticleGun.h"

namespace gen {

   class Pythia6PtYGun : public Pythia6ParticleGun
   {
   
      public:
      
      Pythia6PtYGun( const edm::ParameterSet& );
      virtual ~Pythia6PtYGun();
      // void produce( edm::Event&, const edm::EventSetup& ) ;
      
      protected:
         void generateEvent() ;
      
      private:
      
         double  fMinY;
	 double  fMaxY;
	 double  fMinPt ;
         double  fMaxPt ;
         double  fRatioPart1;
	 bool    fAddAntiParticle;
   
   };


}

#endif
