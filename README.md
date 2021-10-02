# project5
group project


This app was designed for use by anyone representing a person convicted of a criminal offense. Please enter the relevant information into the fields on the site; the app will then predict whether the defendant will receive prison time vs a non-prison time. This predictive tool can be used to assess the likelihood that a case was misclassified or mishandled, thereby helping lawyers focus on appealing those cases that fall into these categories.

The app works by using the following pretrained classification models. Below are the Accuracy scores for each model.  

K Neighbors:
>Train Acc: 0.98
 
> Test Acc: 0.97

Random Forest:
>Train Acc: 1

>Test Acc: 0.99

Extra Trees:
>Train Acc: 1

>Test Acc: 0.99

Bagging Classification:
>Train Acc: 0.99

>Test Acc: 0.99

Decision Trees:
>Train Acc: 1

>Test Acc: 0.99

All of our models **(judges)** were trained on data from the United States Sentencing Commission taken in the fiscal year 2020.Each of these classifiers behave like judges who each have a vote, 0 for non-prison sentence or 1 for prison sentence. Each vote is a prediction by each model, and at the end of the script the votes are tallied up. If the sum of the tallies is greater or equal to 3, the collective prediciton is a prison sentence, anything else would be considered a non-prison sentence. 

