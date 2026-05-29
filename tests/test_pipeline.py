from app.pipeline import FeatureEngineeringPipeline

def test_pipeline():

    pipeline = FeatureEngineeringPipeline()

    pipeline.run("data/sample_dataset.csv")

    assert True
