import numpy
import pandas
import statsmodels.api as sm

def simple_heuristic(file_path):


    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex']=='male':
            predictions[passenger_id]=0
        else:
            predictions[passenger_id]=1
      
        # Your code here:
        # For example, let's assume that if the passenger
        # is a male, then the passenger survived.
        #     if passenger['Sex'] == 'male':
        #         predictions[passenger_id] = 1
        
    return predictions
print simple_heuristic("titanic_data (1).csv")


