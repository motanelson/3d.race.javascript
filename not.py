
class Qubits:
    def __init__(self):
        self.value=0
    def __str__(self):
        if self.value==0:
            return "Zero"
        if self.value==1:
            return "One"

    def X(self):
        self.value=(self.value+1) & 1
        
        


q=Qubits()
q.X()
print(q)
