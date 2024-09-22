from flask import Flask,request,jsonify
import pickle
import sklearn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

with open("./artefacts/classifier.pkl", "rb") as model_pickle:
    clf = pickle.load(model_pickle)

@app.route("/predict",methods=['POST'])
def prediction():
    loan_req=request.get_json()
    if loan_req['Gender']=='Male':
        Gender=0
    else:
        Gender=1
    if loan_req['Married']=='Unmarried':
        Married=0
    else:
        Married=1
    if loan_req['Credit_History']=='Unclear Debts':
        Credit_History=0
    else:
        Credit_History=1
    ApplicantIncome=loan_req['ApplicantIncome']
    LoanAmount=loan_req['LoanAmount']
    result=clf.predict([[Gender, Married, Credit_History, ApplicantIncome, LoanAmount]])

    if result==0:
        pred="Rejected"
    else:
        pred="Approved"

    return jsonify({"Loan approval status:": pred})