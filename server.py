from flask import Flask, render_template, request, redirect, url_for
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer, parse_sentiment_analyzer 

''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer", methods=['POST'])
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.form["text to analyze"]

    response = sentiment_analyzer(text_to_analyze)
        
    Data1 = ""
    Data2 = ""
    
    emotions, reasoning = parse_sentiment_analyzer(response)
    print(response)
    if emotions == None:
        Data1 =  "There was an error! try again. Did you enter a meaningless string of characters?"
        return render_template("result.html", data1 = Data1, data2 = Data2)

    Data1 =  f"The folloing text: \"{text_to_analyze}\"  received the following analysis: {emotions}"
    Data2 = f"{reasoning}"
    return render_template("result.html", data1 = Data1, data2 = Data2)
    
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="127.0.0.1", port=4173, debug=True)
