from abc import ABC, abstractmethod

class MLModel(ABC):
    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

class LinearRegressionModel(MLModel):
    def train(self):
        print("Training Linear Regression")

    def predict(self):
        print("Predicting using Linear Regression")

class DecisionTreeModel(MLModel):
    def train(self):
        print("Training Decision Tree")

    def predict(self):
        print("Predicting using Decision Tree")

lr = LinearRegressionModel()
dt = DecisionTreeModel()

lr.train()
lr.predict()

dt.train()
dt.predict()