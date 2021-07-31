import sys

from pyspark.mllib.classification import LogisticRegressionModel
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler

if __name__ == "__main__":

    #input prediction file
    input_file = sys.argv[1]

    spark = SparkSession \
        .builder \
        .appName("wine-quality-prediction") \
        .getOrCreate()

    #open data
    data = spark.read.csv(input_file, header='true', inferSchema='true', sep=';')

    #open model
    model = LogisticRegressionModel.load("trained_model")

    # features vector
    feature_columns = data.columns[:-1]
    assembler = VectorAssembler(inputCols = feature_columns, outputCol = "features")
    data_2 = assembler.transform(data)

    #prediction
    predictions = model.transform(data_2)
    predictions.select(predictions.columns[-1].show())

    #evaluation
    evaluationSummary = model.summary

    print("F-measure by label:")
    for i, f in enumerate(evaluationSummary.fMeasureByLabel()):
        print("label %d: %s" % (i, f))

    fMeasure = evaluationSummary.weightedFMeasure()
    print("F-measure: %s" % fMeasure)

    spark.stop()