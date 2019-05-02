# PDF-Sentiment-
Program that scrapes websites for PDF's an then runs both a sentiment analysis and a classification algorithm using natural language


My program uses the website for the Top 100 American Rhetoric Speeches following its URL



Open the TCMFinalProject folder
    this is the one you will be using throughout 
    
Use the terminal:

create a directory with the file [cd "filepath]
start with python3 command then drag DownloadPDF

First document to run is the DownloadPDF.py
Make sure to edit the directory to where you want it to go, obviously mine all go to user/diegoponce, so change yours.
Evertything should be in the same folder!!

When prompted to input the desired PDF for sentiment/clasify analysis, use one of the downloaded pdf in the folder (TCMFinalProject). DO NOT copy the path or simply drag/drop it, rather copy the name "file.pdf". I use the Get Info command and then copy/paste the name. For example:   Richard%20Nixon%20-%20Checkers.pdf

The software uses the Google Natural Language API, for which I have provided my credentials in the Json file. There is no need to change the code for Sentiment.py, only the FILE PATH TO THE JSON FILE which will be different than mine ["/Users/diegoponce/Desktop/TCMFinalProject/MyCredentials.json"] 

Sentiment Output Interpretation:
  number to the left is whether message is positive or negative {-1,1}
  number to the right gauges the emotion that the document portrays {0,infinity}
