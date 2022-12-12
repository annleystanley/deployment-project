data = {'Gender': 'Male',
'Married' : 'Yes',
'Dependents' : '0',
'Education' : 'Graduate',
'Self_Employed' : 'Yes',
'ApplicantIncome' : '3000',
'CoapplicantIncome' : '0',
'LoanAmount' : '66',
'Loan_Amount_Term' : '360',
'Credit_History' : '1',
'Property_Area' : 'Urban'}


import requests 

url = 'http://localhost:5000/scoring'

results = requests.post(url, json=data)

print(results)