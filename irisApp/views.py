from django.shortcuts import render
from joblib import load
model=load('./savedModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']
        y_pred = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        if y_pred[0] == 0:
            answer = 'Setosa'
        elif y_pred[0] == 1:
            answer = 'Verscicolor'
        else:
            answer = 'Virginica'

        return render(request,'result.html',{'result':answer})
    return render(request,'main.html')

    