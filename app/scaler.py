from sklearn.preprocessing import StandardScaler

class FeatureScaler:

    def scale_features(self, df):

        scaler = StandardScaler()

        scaled = scaler.fit_transform(df)

        return scaled
