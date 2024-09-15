import copy

import numpy as np
from sklearn.tree import DecisionTreeClassifier


class DecisionTreeClassifierPT:
    def __init__(self, *, max_depth: int = 5, min_samples_split: int = 2):
        self.model = DecisionTreeClassifier(
            max_depth=max_depth, min_samples_split=min_samples_split
        )

    def __repr__(self):
        return f"DecisionTreeClassifierPT(max_depth={self.model.max_depth},min_samples_split={self.model.min_samples_split})"

    def fit(self, X: np.ndarray, y: np.ndarray):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def __copy__(self):
        new_instance = DecisionTreeClassifierPT(
            max_depth=self.model.max_depth,
            min_samples_split=self.model.min_samples_split,
        )
        new_instance.model = copy.deepcopy(self.model)
        return new_instance
