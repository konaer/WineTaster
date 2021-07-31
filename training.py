
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("wine-quality-training") \
        .getOrCreate()

    #open data
    data = spark.read.csv('TrainingDataset.csv', header='true', inferSchema='true', sep=';')

    #features vector
    feature_columns = data.columns[:-1]
    assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
    data_2 = assembler.transform(data)

    #train the model

    org_model = LogisticRegression(featuresCol="features", labelCol='""""quality"""""')
    model = org_model.fit(data_2)


    #Save training model
    model.write().overwrite().save('trained_model')

    #Evaluation
    trainingSummary = model.summary
    fMeasure = trainingSummary.weightedFMeasure()
    print("F-measure: %s"
          % fMeasure)