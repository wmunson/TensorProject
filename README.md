***TensorFlow Project*** **Peforming Sentiment Analysis on Wikipedia Articles**

**About:**

This web app uses Google's TensorFlow TFLearn package. It attempts to analyze sentiment on Wikipedia articles for the purpose of identifying bias in authors/editors.

It has a simple front end that lets the user search for wiki aritcles and then choose the desire option to perform the sentiment analysis. A numerical result is returned on a scale of 0 to 100 (0 = bias against article topic, 100 = bias in favor of article topic, 50 = neutral).

_______________________________________________________________________________________________________________________________

**Tehcnologies:**

-Server side - Python, Flask.
	
   -Analysis - BeautifulSoup, Pandas, TFLearn. 

-Front end - HTML, CSS, JavaScript, C3.JS (data visualization).
 

*A further breakdown of the packages used can be found in the requirements.txt.

*After further iterations there are now certain technologies in the requirements.txt that are unused but have not been removed from the file yet.

_______________________________________________________________________________________________________________________________

**Usage:**

To run the application you need to create a virtual environment, download/install requirements.txt, then run app.py

-app.py invokes the Flask app and contains the routes for the server.

-config.py handles the configurations.

-models.py contains the two (2) functions: make_test_csv which scrapes the wikipedia page, tokenizes the content, and then stores into a csv file; run_analysis takes the content from train.csv (found in tensor folder) and trains the DNN, then runs an analysis on the content from test.csv.

-test.csv stores the wikipedia article content for only the articles being analyzed. It is rewritten with each analysis.

tensor folder:

-csv_pop.py is only run if you wish to use different articles/training data. The function scrapes wikipedia and populates the train.csv file.

-temp.py: *please disregard*.

-tensor.py is used to test different configurations of the neural network training. 

-tester.py exactly what the name suggests; used to test different data proccessing. *Please disregard*.

-train.csv contains training data based on the 10 articles scrapped and tokenized from the csv_pop.py. Used in models.py.

______________________________________________________________________________________________________________________________


**Notes:**

-Training data is limited to 10 wikipedia articles. This is unfortunately a small number of training data points. It was chosen for the length of run time (~3min) on my local machine. If you have greater processing power, or less of a time restraint, feel free to increase the number of articles used in csv_pop.py.

-Training data posses a significant point of discrepancy: The decision was made to run the predition kit of TFLearn. This required labeled dataset. So each article used for training contains a label between 0 and 10. these labels were decided by my own perception of bias. Not an ideal data set for TF. Bias within Wikipedia articles mostly proved to be inherently difficult to identify (reason for my use of a neural network).

