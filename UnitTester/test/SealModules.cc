#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ModuleFactory.h"
#include "FWCore/Framework/interface/eventsetupdata_registration_macro.h"
#include "FWCore/Framework/interface/eventsetuprecord_registration_macro.h"

#include "RecoLocalTracker/SiStripClusterizer/test/CompareClusters.h"
#include "RecoLocalTracker/SiStripClusterizer/test/ClusterizerUnitTester.h"
#include "RecoLocalTracker/SiStripClusterizer/test/StripByStripTestDriver.h"
#include "RecoLocalTracker/SiStripClusterizer/test/ClusterizerUnitTesterESProducer.h"

#include "RecoLocalTracker/SiStripClusterizer/test/ClusterizerUnitTesterTest.h"

DEFINE_SEAL_MODULE();
DEFINE_ANOTHER_FWK_MODULE(CompareClusters);
DEFINE_ANOTHER_FWK_MODULE(ClusterizerUnitTester);
DEFINE_ANOTHER_FWK_MODULE(StripByStripTestDriver);
DEFINE_ANOTHER_FWK_EVENTSETUP_MODULE(ClusterizerUnitTesterESProducer);

DEFINE_ANOTHER_FWK_MODULE(ClusterizerUnitTesterTest);
