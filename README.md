This is a simple project to understand and learn the basics of Machine Learning using the common library Scikit-Learn.
Documentation of sklearn - https://scikit-learn.org/stable/api/index.html

The dataset used to make the flower classifications and predictions in the infamous Iris dataset. In this particular repo, I have used the dataset inbuilt in sklearn.models
The ipynb file contains all details regarding the dataset -- The summary, statistics and few graphs detecting the relcationship between the different features. 

The model decided and use is the ensemble Random Forest giving an accuracy ~ 97%. This model is saved along with the pre-processing information. 
A REST API using Flask is created which in turn calls the saved model and pre-processor to predict the name of the flower, features of which is sent with the Request Body in a JSON format. 

A simple frontend with HTML, CSS and JS calls this Flask API to take input from the user and display the predicted output back to the user in the same page. 
