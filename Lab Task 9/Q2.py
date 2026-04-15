from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianModel([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

cpd_I = TabularCPD(variable = 'Intelligence', variable_card = 2, values = [[0.7], [0.3]], state_names = {'Intelligence': ['High', 'Low']})
cpd_S = TabularCPD(variable = 'StudyHours', variable_card = 2, values = [[0.6], [0.4]], state_names = {'StudyHours': ['Sufficient', 'Insufficient']})
cpd_D = TabularCPD(variable = 'Difficulty', variable_card = 2, values = [[0.4], [0.6]], state_names = {'Difficulty': ['Hard', 'Easy']})

cpd_G = TabularCPD(
    variable = 'Grade', 
    variable_card = 3,
    values = [
        [0.7, 0.5, 0.4, 0.2, 0.5, 0.3, 0.2, 0.1], # A
        [0.2, 0.3, 0.4, 0.5, 0.3, 0.4, 0.4, 0.3], # B
        [0.1, 0.2, 0.2, 0.3, 0.2, 0.3, 0.4, 0.6]  # C
    ],
    evidence = ['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card = [2, 2, 2],
    state_names = {
        'Grade': ['A', 'B', 'C'],
        'Intelligence': ['High', 'Low'],
        'StudyHours': ['Sufficient', 'Insufficient'],
        'Difficulty': ['Hard', 'Easy']
    }
)

cpd_P = TabularCPD(
    variable = 'Pass',
    variable_card = 2,
    values = [
        [0.95, 0.80, 0.50], # Yes
        [0.05, 0.20, 0.50]  # No
    ],
    evidence = ['Grade'],
    evidence_card = [3],
    state_names = {
        'Pass': ['Yes', 'No'],
        'Grade': ['A', 'B', 'C']
    }
)

model.add_cpds(cpd_I, cpd_S, cpd_D, cpd_G, cpd_P)
print("Model valid:", model.check_model())
inference = VariableElimination(model)

result1 = inference.query(
    variables = ['Pass'],
    evidence = {'StudyHours': 'Sufficient', 'Difficulty': 'Hard'}
)

print("\nQuery 1: P(Pass | StudyHours = Sufficient, Difficulty = Hard):")
print(result1)

result2 = inference.query(
    variables = ['Intelligence'],
    evidence = {'Pass': 'Yes'}
)

print("\nQuery 2: P(Intelligence | Pass = Yes):")
print(result2)
