class MissingValueHandler:

    def handle_missing_values(self, df):

        return df.fillna(df.mean(numeric_only=True))
