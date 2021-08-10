# Sentinum--Sentiment-Analysis-using-Social-Media-Data

## Resources Used

 - Dataset- Sentiment140
 - Classification Model- XGboost Classifier
 - NLTK Toolkit for Data Processing and cleaning

## Natural Language Toolkit

The dataset used for this model is Sentiment140 which contains approximately 1.6 million tweets that were labeled as happy or sad. The next primary task was to clean the dataset before using it to train the model. At first, we removed symbols and words such as (“https”, “@”,......) and kept words containing only alphanumeric characters and this was achieved using regex of re library and strings. Then we removed the stopwords(commonly used words which are removed before processing it to make the process faster and more efficient) and then we lemmatized the words using the WordNetLemmatizer of NLTK. The next task was to tokenize the words. This step plays a very important role as ML models are mathematical models and thus can only work with numbers. This was achieved using the CountVectorizer of the sklearn.feature_extraction module. Finally, the dataset is ready for processing and fed into the model. Then we split the dataset into training and validation dataset(80% of the data was used for training and the rest 20% for validation) using the TrainTestSplit of sklearn.model_selection module. Then we used the XGboost classifier for training the model. XGboost is a gradient boosted tree algorithm and a very powerful algorithm. The XGboost classifier was used with parameters max_depth=6, n_estimators=1000, and nthreads=3, and the other parameters were kept to default. Finally, after training the model we achieved a validation accuracy of 75% which can be considered quite good with such limited processing power and dataset.

