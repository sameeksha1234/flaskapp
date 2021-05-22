
from flask import Flask,render_template,request, flash, render_template_string
from flask.wrappers import Response

import pickle
import io
import random


from chatbot import chatbot


app= Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_name' 
model1 = pickle.load(open('positive.sav','rb'))
india_data = pickle.load(open('india_data.sav','rb'))




@app.route("/Test_Yourself")
def Test_Yourself():
    return render_template('bot.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
    



@app.route("/")
def home():
    return render_template('Home.html')

@app.route("/About_Covid")
def About_Covid():
    return render_template('About_Covid.html')



@app.route("/Covid_Forecast")
def Covid_Forecast():
    return render_template('Covid_Forecast.html')

@app.route("/Global_Trend")
def Global_Trend():
    return render_template('Global_Trend.html')

@app.route("/India_Trend")
def India_Trend():
    return render_template('India_Trend.html')

    
    



    

@app.route("/Karnataka_Trend")
def Karnataka_Trend():
    return render_template('Karnataka_Trend.html')
@app.route("/Test_Yourself")
def about():
    return render_template('Test_Yourself.html')

@app.route("/Contact", methods = ['GET','POST'])
def contacts(): 
    
    return render_template('Contact.html')


if __name__ == "__main__" :
    app.run(debug=True)