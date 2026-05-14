class BaseLLM:

    def __init__(self, model_name):
        self.model_name = model_name

    def generate(self):
        return f"The name of model is {self.model_name}"


class OpenAI(BaseLLM):

    def __init__(self, model_name, prompt):

        super().__init__(model_name)

        self.prompt = prompt

    def generate(self):
        return f"{self.model_name} responding to: {self.prompt}"





class ClaudeLLM(BaseLLM):
    def __init__(self, model_name , temp):
        super().__init__(model_name)
        self.temp = temp
        
    def generate(self):
        return f"{self.model_name} responding with {self.temp}"

sonnet = ClaudeLLM("sonnet", 0.3)
print(sonnet.generate())