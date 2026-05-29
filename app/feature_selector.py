from sklearn.feature_selection import VarianceThreshold

class FeatureSelector:

    def select_features(self, df):

        selector = VarianceThreshold(threshold=0.1)

        selected = selector.fit_transform(df)

        return selected
