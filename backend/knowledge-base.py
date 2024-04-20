from aima3.logic import FolKB, expr
#  creates an FOL knowledge base
kb = FolKB()
    
# Plant disease rules

kb.tell(expr('Symptom(x, "Yellowing leaves") & Symptom(x, "Stunted growth") & Symptom(x, "Wilting") ==> Disease(x, "Nutrient deficiency")'))
kb.tell(expr('Symptom(x, "Brown spots on leaves") & Symptom(x, "Circular lesions") & Symptom(x, "Leaf drop") ==> Disease(x, "Fungal disease")'))
kb.tell(expr('Symptom(x, "Holes in leaves") & Symptom(x, "Chewing marks") & Symptom(x, "Leaf curl") ==> Disease(x, "Insect infestation")'))
kb.tell(expr('Symptom(x, "Curled leaves") & Symptom(x, "Distorted growth") & Symptom(x, "Mosaic pattern on leaves") ==> Disease(x, "Viral infection")'))
kb.tell(expr('Symptom(x, "Mushy stems") & Symptom(x, "Waterlogged soil") & Symptom(x, "Leaf yellowing") ==> Disease(x, "Root rot")'))
kb.tell(expr('Symptom(x, "White powdery mildew on leaves") & Symptom(x, "Leaf curl") & Symptom(x, "Stunted growth") ==> Disease(x, "Powdery mildew")'))
kb.tell(expr('Symptom(x, "Sooty mold on leaves") & Symptom(x, "Presence of scale insects") & Symptom(x, "Sticky leaves") ==> Disease(x, "Scale")'))
kb.tell(expr('Symptom(x, "Yellowing leaves with green veins") & Symptom(x, "Leaf drop") & Symptom(x, "Stunted growth") ==> Disease(x, "Iron deficiency")'))
kb.tell(expr('Symptom(x, "Brown spots on fruits") & Symptom(x, "Cracking or rotting fruits") & Symptom(x, "Mushy fruit texture") ==> Disease(x, "Fungal fruit disease")'))
kb.tell(expr('Symptom(x, "Wilting during hot weather") & Symptom(x, "Dry soil") & Symptom(x, "Leaf drop") ==> Disease(x, "Underwatering")'))
kb.tell(expr('Symptom(x, "Yellowing leaves with brown edges") & Symptom(x, "Soggy soil") & Symptom(x, "Leaf drop") ==> Disease(x, "Overwatering")'))
kb.tell(expr('Symptom(x, "Scorched leaves") & Symptom(x, "Sunburn marks") & Symptom(x, "Leaf drop") ==> Disease(x, "Sunburn")'))
kb.tell(expr('Symptom(x, "Deformed leaves") & Symptom(x, "Presence of weeds") & Symptom(x, "Stunted growth") ==> Disease(x, "Herbicide damage")'))
kb.tell(expr('Symptom(x, "Stunted growth") & Symptom(x, "Poor soil quality") & Symptom(x, "Yellowing leaves") ==> Disease(x, "Lack of nutrients")'))
kb.tell(expr('Symptom(x, "Slow growth") & Symptom(x, "Insufficient sunlight") & Symptom(x, "Pale leaves") ==> Disease(x, "Insufficient light")'))

# dictionary that maps potential diseases :
solutions = {
  "Nutrient deficiency": {
    "description": "Plants lack essential nutrients for proper growth.",
    "treatment": "Identify the deficient nutrient(s) through soil testing or visual symptoms. Apply fertilizer specific to the identified deficiency, following recommended application rates."
  },
  "Fungal disease": {
    "description": "Fungi invade plant tissues, causing various problems like wilting, spots, or rots.",
    "treatment": "Apply fungicide according to the specific disease and instructions on the product label. Improve air circulation around plants and avoid overwatering to prevent fungal growth."
  },
  "Insect infestation": {
    "description": "Insects damage plant parts by feeding or laying eggs.",
    "treatment": "Identify the specific insect pest. Use insecticidal soap, neem oil, or other organic controls for smaller infestations. For larger infestations, consider using insecticidal sprays following product label instructions."
  },
  "Viral infection": {
    "description": "Viruses cause plant diseases that are difficult to treat.",
    "treatment": "Unfortunately, there's no cure for viral infections in plants. Preventive measures like using disease-resistant varieties and maintaining healthy plants are crucial. Remove and destroy infected plant parts to prevent further spread."
  },
  "Root rot": {
    "description": "Fungi attack and damage plant roots, hindering water and nutrient uptake.",
    "treatment": "Improve drainage by amending soil with compost or perlite. Avoid overwatering. In severe cases, fungicides might be necessary. Remove heavily infected plants to prevent spread."
  },
  "Powdery mildew": {
    "description": "A white fungal growth appears on leaves, reducing photosynthesis.",
    "treatment": "Apply fungicide specifically for powdery mildew, following label instructions. Ensure good air circulation around plants and avoid overhead watering."
  },
  "Scale": {
    "description": "Scale insects suck sap from plants, causing stunted growth and sticky residue.",
    "treatment": "Treat with insecticidal soap sprays or horticultural oil sprays. Apply multiple treatments according to product instructions."
  },
  "Iron deficiency": {
    "description": "Plants show yellowing leaves with green veins due to lack of iron.",
    "treatment": "Apply iron chelate solution according to label instructions. Ensure proper soil drainage to prevent iron lockout."
  },
  "Fungal fruit disease": {
    "description": "Fungi infect fruits, causing spots, rots, or other deformities.",
    "treatment": "Remove and destroy infected fruits to prevent further spread. Apply fungicide sprays as a preventive measure before the fruiting season, following label instructions."
  },
  "Underwatering": {
    "description": "Plants wilt, leaves droop, and growth slows down due to lack of water.",
    "treatment": "Water the plants thoroughly until water drains from the drainage holes. Adjust watering frequency based on plant type, weather conditions, and pot size."
  },
  "Overwatering": {
    "description": "Excess water in the soil suffocates plant roots and hinders nutrient uptake.",
    "treatment":  "Allow the soil to dry out completely between waterings. Ensure pots have drainage holes to prevent waterlogging. Consider repotting in well-draining potting mix if necessary."
  },
  "Sunburn": {
    "description": "Excessive sunlight scorches leaves, causing brown or bleached patches.",
    "treatment": "Provide shade for plants during the hottest part of the day. Gradually acclimatize newly planted specimens to full sun exposure."
  },
  "Herbicide damage": {
    "description": "Accidental application of herbicide damages desired plants.",
    "treatment": "Unfortunately, there's no complete reversal for herbicide damage. Depending on the severity, affected plant parts might recover or need removal. Provide proper care to encourage new growth."
  },
  "Lack of nutrients": {
    "description": "Similar to nutrient deficiency, but generally refers to overall poor soil quality.",
    "treatment": "Amend soil with compost, manure, or other organic matter to improve nutrient content. Consider using slow-release fertilizer to provide sustained nutrition."
  },
  "Insufficient light": {
    "description": "Plants become leggy and grow poorly due to lack of adequate light.",
    "treatment": "Relocate plants to a brighter location with more sunlight exposure. Supplement with artificial lights if necessary, considering the specific light requirements of the plant."
  },
}



symptom1 = input("Enter first symptom: ")
symptom2 = input("Enter second symptom: ")
symptom3 = input("Enter third symptom: ")
# adding a statement that the Plant has the symptom entered by the user (symptom1).
kb.tell(expr(f'Symptom(Plant, "{symptom1}")'))
kb.tell(expr(f'Symptom(Plant, "{symptom2}")'))
kb.tell(expr(f'Symptom(Plant, "{symptom3}")'))
#  formulates a query (query) using logical expression to ask the KB what the disease is (Disease(Plant, what)) based on the user's symptoms.
query = expr("Disease(Plant, what)")
# query the knowledge base
answer = kb.ask(query)
if answer:
    disease = answer[query.args[1]]
    print(f"The Suspected disease is: {disease}")
    print(f"Description: {solutions[disease]['description']}")
    print("How to treat the disease :")
    for i, step in enumerate(solutions[disease]["steps"], 1):
        print(f"{i}. {step}")
else:
    print("The symptoms do not match any known diseases.")
