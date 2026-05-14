class LLMModel:
    provider = "Generic AI provider"
    
    def __init__(self  , model_name , temperature):
        self.temperature = temperature
        self.model_name = model_name
    
    def generate(self , prompt):
        return f"{self.model_name} generating response for :{prompt}"
    
    def __str__(self):
        return f"LLM {self.model_name}"
    
    def get_config(self):
        return f"model : {self.model_name} and temperature : {self.temperature}"

claude = LLMModel("sonnet-4.5" , 0.3)

print(claude)

print(claude.get_config())



