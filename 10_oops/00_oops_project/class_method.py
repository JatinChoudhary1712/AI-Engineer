class LLM:

    def __init__(self, model, temp):
        self.model = model
        self.temp = temp

    @classmethod
    def from_config(cls, config):

        return cls(
            config["model"],
            config["temp"]
        )
        
config = {
    "model": "gpt-4",   
    "temp": 0.7
}

llm = LLM.from_config(config)

print(llm.model)