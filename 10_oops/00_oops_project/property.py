class APIusage():
    def __init__(self , request_tokens , response_tokens):
        self.request = request_tokens
        self.response = response_tokens
    
    @property
    def total_cost(self):
        return (self.request + self.response)*0.01
    
api = APIusage(100 , 1000)

print(api.total_cost)