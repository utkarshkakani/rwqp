from utils import WineQualityPrediction
from flask import Flask, jsonify, render_template, request
import config

app = Flask(__name__)

#################################################################################
################################## Home API #####################################
#################################################################################

@app.route('/')
def wine_model():
    print('Welcome to the Red Wine Quality Prediction')
    return render_template('red_wine.html')


#################################################################################
################################## Model API #####################################
#################################################################################

@app.route('/predict_quality', methods= ['POST','GET'])
def get_wine_quality():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        fixed_acidity = eval(data['fixed_acidity'])
        volatile_acidity = eval(data['volatile_acidity'])
        citric_acid = eval(data['citric_acid'])
        residual_sugar = eval(data['residual_sugar'])
        chlorides = eval(data['chlorides'])
        free_sulfur_dioxide = eval(data['free_sulfur_dioxide'])
        total_sulfur_dioxide = eval(data['total_sulfur_dioxide'])
        density = eval(data['density'])
        pH = eval(data['pH'])
        sulphates = eval(data['sulphates'])
        alcohol = eval(data['alcohol'])

        print(f'fixed acidity = {fixed_acidity}, volatile acidity = {volatile_acidity}, citric acid = {citric_acid}, residual sugar = {residual_sugar}, chlorides = {chlorides}, free sulfur dioxide = {free_sulfur_dioxide}, total sulfur dioxide = {total_sulfur_dioxide}, density = {density}, pH = {pH}, sulphates = {sulphates}, alcohol = {alcohol}')

        wine_quality = WineQualityPrediction(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol)
        quality = wine_quality.get_predicted_quality()
        if quality[0] == 0 :
            return jsonify({'Output' : 'Quality of red wine is poor(rated 5 or less than 5 on a scale of 10)'})
        else :
            return jsonify({'Output' : 'Quality of red wine is good(rated 6 or more than 6 on a scale of 10)'})
        
    else :
        print('We are in GET Method')
        data1 = request.args
        fixed_acidity = data1.get('fixed_acidity')
        volatile_acidity = data1.get('volatile_acidity')
        citric_acid = data1.get('citric_acid')
        residual_sugar = data1.get('residual_sugar')
        chlorides = data1.get('chlorides')
        free_sulfur_dioxide = data1.get('free_sulfur_dioxide')
        total_sulfur_dioxide = data1.get('total_sulfur_dioxide')
        density = data1.get('density')
        pH = data1.get('pH')
        sulphates = data1.get('sulphates')
        alcohol = data1.get('alcohol')

        print(f'fixed acidity = {fixed_acidity}, volatile acidity = {volatile_acidity}, citric acid = {citric_acid}, residual sugar = {residual_sugar}, chlorides = {chlorides}, free sulfur dioxide = {free_sulfur_dioxide}, total sulfur dioxide = {total_sulfur_dioxide}, density = {density}, pH = {pH}, sulphates = {sulphates}, alcohol = {alcohol}')

        wine_quality1 = WineQualityPrediction(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol)
        quality1 = wine_quality1.get_predicted_quality()
        if quality1[0] == 0 :
            return jsonify({'Output' : 'Quality of red wine is poor(rated 5 or less than 5 on a scale of 10)'})
        else :
            return jsonify({'Output' : 'Quality of red wine is good(rated 6 or more than 6 on a scale of 10)'})


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER)