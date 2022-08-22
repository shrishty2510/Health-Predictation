#code to be write globally
import pickle
import pandas as pd
def predect(frontend_symp):
    data = pd.read_csv("training_data.csv")
    X = data.drop(['Unnamed: 133','prognosis'],axis=1)

    with open("patient\ml_model\Health_prediction.pkl",'rb') as fp:
        model = pickle.load(fp)
    with open("patient\ml_model\encoder.pkl",'rb') as fp:
        encoder = pickle.load(fp)
        
    #code to write in function
    
    lis = []
    for i,j in enumerate(X.columns):
        if  j.lower() in frontend_symp:
            lis.append(1)
        else:
            lis.append(0)
    ans = model.predict([lis])
    result = encoder.inverse_transform([ans])
    return result