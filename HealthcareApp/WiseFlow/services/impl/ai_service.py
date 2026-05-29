class AIService:

    def detect_specialization(self, symptoms):

        symptoms = symptoms.lower()

        if "chest pain" in symptoms:
            return "Cardiology"

        elif "heart" in symptoms:
            return "Cardiology"

        elif "skin rash" in symptoms:
            return "Dermatology"

        elif "skin" in symptoms:
            return "Dermatology"

        elif "headache" in symptoms:
            return "Neurology"

        elif "brain" in symptoms:
            return "Neurology"
        
        elif "child" in symptoms:
            return "Pediatrics"
        
        elif "kid" in symptoms:
            return "Pediatrics"
        
        elif "kidney" in symptoms:
            return "Nephrology"
        
        elif "gastro" in symptoms:
            return "Gastroenterology"

        elif "fever" in symptoms:
            return "General Medicine"

        elif "cold" in symptoms:
            return "General Medicine"

        return "General Medicine"