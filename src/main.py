import dataFacade
import naiveBayes
import illnessDiscoveryService

dataFacade.update_data()
classifier = naiveBayes.train()
analyzer = naiveBayes.train_analyzer()
illnessDiscoveryService.invoke(classifier, analyzer)