# views.py
import pickle
from django.shortcuts import render
import joblib

# # Load the model
# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)

model = joblib.load('model.pkl')


def index(request):
    prediction = None
    if request.method == "POST":
        # Get input values from the form
        feature1 = float(request.POST["bruises"])
        feature2 = float(request.POST["gill-size"])
        feature3 = float(request.POST["gill-color"])
        feature4 = float(request.POST["ring-type"])

        # Make a prediction
        X_new = [[feature1, feature2, feature3, feature4]]
        prediction = model.predict(X_new)[0]
        print("Prediction1:", prediction)  # Add this line

        return render(request, "index.html", {"prediction": prediction})

    print("Prediction:2", prediction)  # Add this line

    return render(request, "index.html", {"prediction": None})
