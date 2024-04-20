from typing import Optional
from aima3.logic import FolKB, expr, fol_bc_ask
from routers import schema
from pydantic.v1 import BaseModel

class Disease:
    def __init__(self, title, description=None):
        self.title  = title
        self.description = description


rules = {
  "plant_rule1": 'Symptom(x, "Yellowing leaves") & Symptom(x, "Stunted growth") & Symptom(x, "Wilting") ==> Disease(x, "Nutrient deficiency")',
  "plant_rule2": 'Symptom(x, "Brown spots on leaves") & Symptom(x, "Circular lesions") & Symptom(x, "Leaf drop") ==> Disease(x, "Fungal disease")',
  "plant_rule3": 'Symptom(x, "Holes in leaves") & Symptom(x, "Chewing marks") & Symptom(x, "Leaf curl") ==> Disease(x, "Insect infestation")',
  "plant_rule4": 'Symptom(x, "Curled leaves") & Symptom(x, "Distorted growth") & Symptom(x, "Mosaic pattern on leaves") ==> Disease(x, "Viral infection")',
  "plant_rule5": 'Symptom(x, "Mushy stems") & Symptom(x, "Waterlogged soil") & Symptom(x, "Leaf yellowing") ==> Disease(x, "Root rot")',
  "plant_rule6": 'Symptom(x, "White powdery mildew on leaves") & Symptom(x, "Leaf curl") & Symptom(x, "Stunted growth") ==> Disease(x, "Powdery mildew")',
  "plant_rule7": 'Symptom(x, "Sooty mold on leaves") & Symptom(x, "Presence of scale insects") & Symptom(x, "Sticky leaves") ==> Disease(x, "Scale")',
  "plant_rule8": 'Symptom(x, "Yellowing leaves with green veins") & Symptom(x, "Leaf drop") & Symptom(x, "Stunted growth") ==> Disease(x, "Iron deficiency")',
  "plant_rule9": 'Symptom(x, "Brown spots on fruits") & Symptom(x, "Cracking or rotting fruits") & Symptom(x, "Mushy fruit texture") ==> Disease(x, "Fungal fruit disease")',
  "plant_rule10": 'Symptom(x, "Wilting during hot weather") & Symptom(x, "Dry soil") & Symptom(x, "Leaf drop") ==> Disease(x, "Underwatering")',
  "plant_rule11": 'Symptom(x, "Yellowing leaves with brown edges") & Symptom(x, "Soggy soil") & Symptom(x, "Leaf drop") ==> Disease(x, "Overwatering")',
  "plant_rule12": 'Symptom(x, "Scorched leaves") & Symptom(x, "Sunburn marks") & Symptom(x, "Leaf drop") ==> Disease(x, "Sunburn")',
  "plant_rule13": 'Symptom(x, "Deformed leaves") & Symptom(x, "Presence of weeds") & Symptom(x, "Stunted growth") ==> Disease(x, "Herbicide damage")',
  "plant_rule14": 'Symptom(x, "Stunted growth") & Symptom(x, "Poor soil quality") & Symptom(x, "Yellowing leaves") ==> Disease(x, "Lack of nutrients")',
  "plant_rule15": 'Symptom(x, "Slow growth") & Symptom(x, "Insufficient sunlight") & Symptom(x, "Pale leaves") ==> Disease(x, "Insufficient light")',
}
class Agenda:
    def __init__(self):
        self.agenda = []

    def add_task(self, task):
        self.agenda.append(task)

    def get_task(self):
        return self.agenda.pop()

    def is_empty(self):
        return len(self.agenda) == 0

class WorkingMemory:
    def __init__(self):
        self.memory = []

    def add_fact(self, fact):
        self.memory.append(fact)

    def get_fact(self):
        return self.memory.pop()

    def is_empty(self):
        return len(self.memory) == 0

    def contains_fact(self, fact):
        return fact in self.memory


def diagnose(symptoms: schema.UserSymptoms) -> Optional[Disease]:

    kb = FolKB()
    working_memory = WorkingMemory()
    agenda = []
    for rule in rules.values():
        kb.tell(expr(rule))

    kb.tell(expr(f'Symptom(x, "{symptoms.symptom1}")'))
    kb.tell(expr(f'Symptom(x, "{symptoms.symptom2}")'))
    kb.tell(expr(f'Symptom(x, "{symptoms.symptom3}")'))
    
    diseases = [
    "Nutrient deficiency",
    "Fungal disease",
    "Insect infestation",
    "Viral infection",
    "Root rot",
    "Powdery mildew",
    "Scale",
    "Iron deficiency",
    "Fungal fruit disease",
    "Underwatering",
    "Overwatering",
    "Sunburn",
    "Herbicide damage",
    "Lack of nutrients",
    "Insufficient light"
    ]
        # Add symptoms to the knowledge base and the working memory
    symptoms_list = [symptoms.symptom1, symptoms.symptom2, symptoms.symptom3]
    for symptom in symptoms_list:
        if symptom:  # Check if symptom is not None or empty
            kb.tell(expr(f'Symptom(x, "{symptom}")'))
            working_memory.add_fact(symptom)

    relevant_diseases = set()
    for symptom in symptoms_list:
        if symptom:
            for rule_name, rule in rules.items():
                if symptom in rule:  # Check if symptom appears in the rule
                    relevant_diseases.add(rule.split("==>")[1].split(", ")[-1].strip(")").replace("Disease(x, ", ""))


    # Add relevant diseases as tasks to the agenda
    agenda = [expr(f'Disease(x, {disease})') for disease in relevant_diseases]
    print('this is the agenda :',agenda)

    diagnosis = None
    while agenda:
        disease = agenda.pop(0)
        solutions = fol_bc_ask(kb, disease)
        first_solution = next(solutions, None) # to print the result of kb.ask as only the result not all the dix"""
        if first_solution is not None:
            print(f"Found a solution: {first_solution}")

            diagnosis = Disease(disease.args[1])  # Assuming disease name is the second argument
            break
        # If no diagnosis found, find a disease with at least 2 common symptoms
    if diagnosis is None:
        for rule_name, rule in rules.items():
            print('the diagnosis is none')
            common_symptoms = [symptom for symptom in symptoms_list if symptom in rule]
            if len(common_symptoms) >= 2:
                diagnosis = Disease(rule.split("==>")[1].split(", ")[-1].strip(")").replace("Disease(x, ", ""))
                break
    print('this is the solutions :',solutions)
    print('the diagnosis :',diagnosis)
    return diagnosis








# def filter_rules(symptoms: schema.UserSymptoms, rules: dict) -> dict:
#     filtered_rules = {}
#     for rule_name, rule in rules.items():
#         for symptom in [symptoms.symptom1, symptoms.symptom2, symptoms.symptom3]:
#             if symptom and symptom in rule:
#                 filtered_rules[rule_name] = rule
#                 break
#     return filtered_rules

# def diagnose(symptoms: schema.UserSymptoms) -> Optional[Disease]:
#     kb = FolKB()
#     working_memory = WorkingMemory()
#     # Filter the rules based on the symptoms
#     filtered_rules = filter_rules(symptoms, rules)
#     diseases = [
#     "Nutrient deficiency",
#     "Fungal disease",
#     "Insect infestation",
#     "Viral infection",
#     "Root rot",
#     "Powdery mildew",
#     "Scale",
#     "Iron deficiency",
#     "Fungal fruit disease",
#     "Underwatering",
#     "Overwatering",
#     "Sunburn",
#     "Herbicide damage",
#     "Lack of nutrients",
#     "Insufficient light"
#     ]
#     # Add symptoms to the knowledge base and the working memory
#     for symptom in [symptoms.symptom1, symptoms.symptom2, symptoms.symptom3]:
#         if symptom:  # Check if symptom is not None or empty
#             kb.tell(expr(f'Symptom(x, "{symptom}")'))
#             working_memory.add_fact(symptom)
#     print('this is the working memory :',working_memory.memory)
#     relevant_diseases = set()
#     for symptom in [symptoms.symptom1, symptoms.symptom2, symptoms.symptom3]:
#         if symptom:
#             for rule_name, rule in filtered_rules.items():
#                 if symptom in rule:  # Check if symptom appears in the rule
#                     relevant_diseases.add(rule.split("==>")[1].split(", ")[-1].strip(")").replace("Disease(x, ", ""))

#     # Add relevant diseases as tasks to the agenda
#     agenda = [expr(f'Disease(x, {disease})') for disease in relevant_diseases]
#     print('this is the agenda :',agenda)

#     diagnosis = None
#     while agenda:
#         disease = agenda.pop(0)
#         # print(f"Checking if {disease} can be inferred...")
#         solutions = fol_bc_ask(kb, disease)
#         first_solution = next(solutions, None)
#         if first_solution is not None:
#             print(f"Found a solution: {first_solution}")
#             diagnosis = Disease(disease.args[1])  # Assuming disease name is the second argument
#             break
#         else:
#             print(f"No solution found for {disease}")

#     print('this is the solution :',first_solution)
#     print('this is the diagnosis :',diagnosis)
#     # Return the diagnosis
#     return diagnosis
