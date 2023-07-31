import pickle
import json
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class WineQualityPrediction():
    
    def __init__(self,fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol = alcohol

    def load_model(self):
        with open('project_app/Logistic_model.pkl', 'rb') as f:
            self.model = pickle.load(f)

        with open('project_app/project_data.json', 'rb') as f:
            self.project_data = json.load(f)

    def get_predicted_quality(self):
        self.load_model()

        test_array = np.zeros(len(self.project_data['columns']))
        test_array[0] = self.fixed_acidity
        test_array[1] = self.volatile_acidity
        test_array[2] = self.citric_acid
        test_array[3] = self.residual_sugar
        test_array[4] = self.chlorides
        test_array[5] = self.free_sulfur_dioxide
        test_array[6] = self.total_sulfur_dioxide
        test_array[7] = self.density
        test_array[8] = self.pH
        test_array[9] = self.sulphates
        test_array[10] = self.alcohol

        predicted_quality = self.model.predict([test_array])
        if predicted_quality[0] == 0:
            print(f"Quality of red wine is poor(rated 5 or less than 5 on a scale of 10)")
        else :
            print(f"Quality of red wine is good(rated 6 or more than 6 on a scale of 10)")
        return predicted_quality
    
if __name__== '__main__':
    fixed_acidity        = 8.9
    volatile_acidity     = 0.5
    citric_acid          = 0.1
    residual_sugar       = 1.5
    chlorides            = 0.05
    free_sulfur_dioxide  = 8.0
    total_sulfur_dioxide = 25.0
    density              = 0.89
    pH                   = 3.0
    sulphates            = 0.6
    alcohol              = 8.0

    wine_quality = WineQualityPrediction(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol)
    wine_quality.get_predicted_quality()