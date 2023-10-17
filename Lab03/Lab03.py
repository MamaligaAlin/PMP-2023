from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

'''
Incendiu - S-a intamplat incendiu
Cutremur - S-a intamplat cutremur
Alarma - Alarma a fost activata
'''
lab_model = BayesianNetwork([('Cutremur', 'Incendiu'), ('Cutremur', 'Alarma'),('Incendiu','Alarma')])


pos = nx.circular_layout(lab_model)
nx.draw(lab_model, with_labels=True, pos=pos, alpha=0.5, node_size=3500)
plt.show()
CPD_CUTREMUR = TabularCPD(variable='Cutremur', variable_card=2, values=[[0.9995], [0.0005]])
CPD_INCENDIU = TabularCPD(variable='Incendiu', variable_card=2,values=[[0.99, 0.97],[0.01, 0.03]],evidence=['Cutremur'],evidence_card=[2])
CPD_ALARMA = TabularCPD(variable='Alarma', variable_card=2,
values=[[0.9999, 0.05, 0.98, 0.02],[0.0001, 0.95, 0.02, 0.98]],
evidence=['Cutremur', 'Incendiu'],
evidence_card=[2, 2])
print(CPD_CUTREMUR)
print(CPD_INCENDIU)
print(CPD_ALARMA)

lab_model.add_cpds(CPD_CUTREMUR, CPD_INCENDIU, CPD_ALARMA)
#print(lab_model.get_cpds())
print(lab_model.get_independencies())
lab_model.check_model()
#EX2
infer = VariableElimination(lab_model)
posterior_p = infer.query(variables=["Cutremur"], evidence={"Alarma": 1})
print(posterior_p)
#EX3
infer = VariableElimination(lab_model)
posterior_p = infer.query(variables=["Alarma"], evidence={"Incendiu": 1})
print(posterior_p)