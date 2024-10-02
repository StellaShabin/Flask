from predict import app
import pytest

@pytest.fixture
def client():
    return app.test_client()


def test_pinger(client):
    resp=client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"Message":"I am pinging.....!!"}

def test_predict(client):
    test_data={
    "Gender" : "Male",
    "Married" : "Unmarried",
    "ApplicantIncome": 50000,
    "Credit_History" : "Cleared Debts",
    "LoanAmount" : 500000
    }
    resp=client.post('/predict',json=test_data)
    assert resp.status_code==200
    assert resp.json=={"loan_approval_status":"Rejected"}