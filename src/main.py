
import dataFacade
import naiveBayes
import illnessDiscoveryService

# dataFacade.update_data()
cl = naiveBayes.train()
illnessDiscoveryService.invoke(cl)