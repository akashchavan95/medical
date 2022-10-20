
from flask import Flask,jsonify,render_template,request
import config
from project.utilis import MedicalInsurance

app = Flask(__name__)

@app.route("/")

def home_api():
    return render_template("index.html") 

@app.route("/predict_charge",methods=["GET","POST"])
def get_medical_insurance_charge():
    data=request.form
    age=int(data["age"])
    sex=data["sex"]
    bmi = eval(data["bmi"])
    children = int(data["children"])
    smoker = data["smoker"]
    region = data["region"]
    med_ins=MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges=med_ins.get_pred_charges()
    #return jsonify({"Result":f"Predicted Medical Insurance charges :{charges}"})
    return render_template ("index1.html",charges=charges[0])

if __name__==  "__main__" :
    app.run(host="0.0.0.0",port=config.port_number)