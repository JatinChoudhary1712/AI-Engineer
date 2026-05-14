class BaseLLM(): 
    def generate(self): 
        return "BaseLLM"
    
class OpenAI(BaseLLM):
    def generate(self):
        return "OpenAI"
    
o = OpenAI()
print(o.generate())

b = BaseLLM()
print(b.generate())