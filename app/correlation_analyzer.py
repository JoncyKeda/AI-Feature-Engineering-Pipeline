class CorrelationAnalyzer:

    def analyze(self, df):

        correlation_matrix = df.corr(numeric_only=True)

        return correlation_matrix
