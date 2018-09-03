import numpy as np
import random

class TestDataGenerator:
    def __init__(self, X_test_data, batchSize):

        self.X_test_data = X_test_data
        self.X_test_offset = 0
        self.batchSize = batchSize

    def generate(self):
        start = self.X_test_offset
        end = self.X_test_offset + self.batchSize

        self.X_test_offset = end

        # handle wrap around    ,
        if end > len(self.X_test_data):
            spillover = end - len(self.X_test_data)
            self.X_test_offset = spillover
            X = np.concatenate((self.X_test_data[start:], self.X_test_data[:spillover]), axis = 0)


            self.X_test_offset = 0


        else:
            X = self.X_test_data[start:end]

        X = X.astype(np.int32, copy = False)


        return X




