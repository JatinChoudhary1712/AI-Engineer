class Agent(): 
    def __init__(self , name , llm):
        self.name = name
        self.llm = llm
    
    def __str__(self):
        return f"Agent : {self.name}"
    
    def __repr__(self):
        return f"name = {self.name} , llm = {self.llm}"

ag = Agent("ResearchBot" , "gpt-4")

print(ag.__str__())
print(ag.__repr__())