from app.data_loader import DataLoader
from app.missing_handler import MissingValueHandler
from app.feature_generator import FeatureGenerator
from app.correlation_analyzer import CorrelationAnalyzer
from app.feature_selector import FeatureSelector
from app.importance_ranker import ImportanceRanker

class FeatureEngineeringPipeline:

    def __init__(self):

        self.loader = DataLoader()

        self.missing_handler = MissingValueHandler()

        self.generator = FeatureGenerator()

        self.correlation = CorrelationAnalyzer()

        self.selector = FeatureSelector()

        self.ranker = ImportanceRanker()

    def run(self, dataset_path):

        print("\n🚀 Starting Feature Engineering Pipeline\n")

        df = self.loader.load_data(dataset_path)

        print("✅ Dataset Loaded")

        df = self.missing_handler.handle_missing_values(df)

        print("✅ Missing Values Handled")

        df = self.generator.generate_features(df)

        print("✅ Features Generated")

        correlation_matrix = self.correlation.analyze(df)

        print("✅ Correlation Analysis Completed")

        X = df.drop(columns=["target"])

        y = df["target"]

        selected_features = self.selector.select_features(X)

        print("✅ Feature Selection Completed")

        importance = self.ranker.rank_features(
            X,
            y,
            X.columns
        )

        print("\n📊 Top Important Features:\n")

        print(importance.head())
