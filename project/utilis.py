import config
import numpy as np
import json
import pickle

class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+region
    
    def load_model(self):
        with open (config.model_path_file,"rb") as f:
            self.model=pickle.load(f)
        with open (config.json_path_file,"r") as f:
            self.prj_data=json.load(f)
    
    def get_pred_charges(self) :
        self.load_model()
        array=np.zeros(len(self.prj_data["columns"]))
        array[0] = self.age
        array[1] = self.prj_data["sex"][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.prj_data["smoker"][self.smoker]
        region_index = self.prj_data["columns"].index(self.region)
        array[region_index] = 1
        print("Array",array)

        predicted_charges = np.around(self.model.predict([array]))
        return predicted_charges
