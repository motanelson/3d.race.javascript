
class Qubits:
    def __init__(self):
        self.value=0
    def __str__(self):
        if self.value==0:
            return "Zero"
        if self.value==1:
            return "One"
    def __hash__(self):
        return self.value
    def X(self):
        self.value=(self.value+1) & 1
    def Y(self,lists):
        self.value=1
        for n in lists:
            self.value=(self.value & 1) & (n & 1) & 1 


q1=Qubits()
q2=Qubits()
q3=Qubits()
q1.X()
q2.X()
q3.Y([q1.value,q2.value])
print(q3)
