import copy

import numpy as np

from src.creation.prototype.models.decision_tree import DecisionTreeClassifierPT
from src.utils.logger import logger

if __name__ == "__main__":
    # サンプルデータの生成
    np.random.seed(42)
    X = np.random.rand(100, 2)
    y = (X[:, 0] + X[:, 1] > 1).astype(int)

    # プロトタイプモデルの作成
    logger.info("define model.")
    prototype = DecisionTreeClassifierPT()
    prototype.fit(X, y)

    # プロトタイプからの新しいモデルの生成
    model1 = copy.copy(prototype)
    model2 = copy.copy(prototype)

    # モデル2のパラメータを変更
    model1.model.set_params(
        max_depth=9,
        min_samples_split=99,
    )
    model2.model.set_params(max_depth=5)

    # 予測
    X_test = np.array([[0.7, 0.3], [0.2, 0.8]])
    logger.info("Prototype")
    logger.info(f"params: {repr(prototype)}")
    logger.info(f"predict: {prototype.predict(X_test)}")
    logger.info("=" * 80)

    logger.info("Model 1")
    logger.info(f"params: {repr(model1)}")
    logger.info(f"predict: {model1.predict(X_test)}")
    logger.info("=" * 80)

    logger.info("Model 2")
    logger.info(f"params: {repr(model2)}")
    logger.info(f"predict: {model2.predict(X_test)}")
