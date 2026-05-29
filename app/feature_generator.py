class FeatureGenerator:

    def generate_features(self, df):

        numeric_columns = df.select_dtypes(include=["number"]).columns

        for col in numeric_columns:

            df[f"{col}_squared"] = df[col] ** 2

        return df
