from sklearn.ensemble import RandomForestRegressor
import pandas as pd

class ImportanceRanker:

    def rank_features(self, X, y, feature_names):

        model = RandomForestRegressor()

        model.fit(X, y)

        importance = model.feature_importances_

        importance_df = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importance
        })

        return importance_df.sort_values(
            by="Importance",
            ascending=False
        )
