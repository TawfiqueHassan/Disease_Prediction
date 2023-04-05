from django.http import HttpResponse
from django.shortcuts import render
import pickle as pk


def index(request):
    if request.method == 'GET':

        return render(request, "index.html")
    else:
        with open('Model', 'rb') as file:
            model = pk.load(file)
        ls = [request.POST.getlist("dropdown")]
        Disease = model.predict(ls)
        print(Disease)

        specialists = {
            "Fungal infection": "Dermatologist",
            "Allergy": "Allergist",
            "GERD": "Gastroenterologist",
            "Chronic cholestasis": "Gastroenterologist",
            "Drug Reaction": "Dermatologist",
            "Peptic ulcer diseae": "Gastroenterologist",
            "AIDS": "Infectious disease specialist",
            "Diabetes": "Endocrinologist",
            "Gastroenteritis": "Gastroenterologist",
            "Bronchial Asthma": "Pulmonologist",
            "Hypertension": "Cardiologist",
            "Migraine": "Neurologist",
            "Cervical spondylosis": "Orthopedic surgeon",
            "Paralysis (brain hemorrhage)": "Neurologist",
            "Jaundice": "Gastroenterologist",
            "Malaria": "Infectious disease specialist",
            "Chicken pox": "Dermatologist",
            "Dengue": "Infectious disease specialist",
            "Typhoid": "Infectious disease specialist",
            "hepatitis A": "Hepatologist",
            "Hepatitis B": "Hepatologist",
            "Hepatitis C": "Hepatologist",
            "Hepatitis D": "Hepatologist",
            "Hepatitis E": "Hepatologist",
            "Alcoholic hepatitis": "Hepatologist",
            "Tuberculosis": "Pulmonologist",
            "Common Cold": "General Practitioner",
            "Pneumonia": "Pulmonologist",
            "Dimorphic hemmorhoids(piles)": "Proctologist",
            "Heart attack": "Cardiologist",
            "Varicose veins": "Vascular surgeon",
            "Hypothyroidism": "Endocrinologist",
            "Hyperthyroidism": "Endocrinologist",
            "Hypoglycemia": "Endocrinologist",
            "Osteoarthristis": "Orthopedic surgeon",
            "Arthritis": "Rheumatologist",
            "(vertigo) Paroymsal Positional Vertigo": "ENT specialist",
            "Acne": "Dermatologist",
            "Urinary tract infection": "Urologist",
            "Psoriasis": "Dermatologist",
            "Impetigo": "Dermatologist"
        }

        diagnosis = specialists[Disease[0]]
        print(specialists[Disease[0]])

        doctors_dict = {
            'Neurologist': ['Dr. Arnab Bhowmick', 'Dr. Biswajit Mondal', 'Dr. Rana Dasgupta', 'Dr. Sayantan Saha', 'Dr. Jayanta Saha'],
            'Vascular surgeon': ['Dr. Sumit Sen', 'Dr. Ritwik De', 'Dr. Debashis Dey', 'Dr. Arijit Mukherjee', 'Dr. Sourav Ghosh'],
            'Hepatologist': ['Dr. Jayanta Saha', 'Dr. Sayantan Saha', 'Dr. Arijit Mukherjee', 'Dr. Sourav Ghosh', 'Dr. Arnab Bose'],
            'Cardiologist': ['Dr. Arnab Bhowmick', 'Dr. Trina Bhattacharya', 'Dr. Koushik Ghosh', 'Dr. Sumit Sen', 'Dr. Sounak Adhikary'],
            'Dermatologist': ['Dr. Sayantan Saha', 'Dr. Sourav Ghosh', 'Dr. Jayanta Saha', 'Dr. Ritwik De', 'Dr. Sumit Sen'],
            'ENT specialist': ['Dr. Rana Dasgupta', 'Dr. Trina Bhattacharya', 'Dr. Sourav Ghosh', 'Dr. Ritwik De', 'Dr. Sounak Adhikary'],
            'Infectious disease specialist': ['Dr. Sayantan Saha', 'Dr. Arnab Bose', 'Dr. Sumit Sen', 'Dr. Arup Chakraborty', 'Dr. Rana Dasgupta'],
            'Proctologist': ['Dr. Koushik Ghosh', 'Dr. Sourav Ghosh', 'Dr. Arnab Bhowmick', 'Dr. Jayanta Saha', 'Dr. Arup Chakraborty'],
            'Rheumatologist': ['Dr. Arijit Mukherjee', 'Dr. Sounak Adhikary', 'Dr. Ritwik De', 'Dr. Rana Dasgupta', 'Dr. Arnab Bose'],
            'Endocrinologist': ['Dr. Arnab Bhowmick', 'Dr. Arup Chakraborty', 'Dr. Sumit Sen', 'Dr. Sayantan Saha', 'Dr. Koushik Ghosh'],
            'Allergist': ['Dr. Rana Dasgupta', 'Dr. Arnab Bhowmick', 'Dr. Sourav Ghosh', 'Dr. Debashis Dey', 'Dr. Sumit Sen'],
            'Urologist': ['Dr. Arnab Bose', 'Dr. Biswajit Mondal', 'Dr. Rana Dasgupta', 'Dr. Sayantan Saha', 'Dr. Trina Bhattacharya'],
            'General Practitioner': ['Dr. Biswajit Mondal', 'Dr. Ritwik De', 'Dr. Trina Bhattacharya', 'Dr. Jayanta Saha', 'Dr. Arnab Bhowmick'],
            'Orthopedic surgeon': ['Dr. Jayanta Saha', 'Dr. Koushik Ghosh', 'Dr. Debashis Dey', 'Dr. Ritwik De', 'Dr. Biswajit Mondal'],
            'Pulmonologist': ['Dr. Jayanta Saha', 'Dr. Trina Bhattacharya', 'Dr. Sounak Adhikary', 'Dr. Biswajit Mondal', 'Dr. Rana Dasgupta'],
            'Gastroenterologist': ['Dr. Arnab Bose', 'Dr. Sayantan Saha', 'Dr. Sourav Ghosh', 'Dr. Ritwik De', 'Dr. Debashis Dey']
        }
        doctors = []
        for key, value in doctors_dict.items():
            if key.lower() == diagnosis.lower():
                doctors.extend(value)
        print(doctors)
        Query={
            'disease':Disease[0],
            'specialist':diagnosis,
            'doctors':doctors,
        }
        return render(request, "result.html", context=Query)
