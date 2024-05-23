from aima.search import hill_climbing, simulated_annealing, exp_schedule
from abia_bicing_parametres import ProblemParameters
from abia_bicing_problem import BicingProblem
from abia_bicing import *
from abia_bicing_estat_h2_SA import generate_initial_state, generate_initial_state_greedy




import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
from timeit import timeit


estaciones = Estaciones(25, 1250, 42)
parametres = ProblemParameters(estaciones, 5)
#estat_inicial = generate_initial_state(parametres)
estat_inicial_greedy = generate_initial_state_greedy(parametres)


#k=5, lam=0.01, limit=2000
#n = simulated_annealing(BicingProblem(estat_inicial),schedule= exp_schedule(k=1,lam=0.0005, limit=2000))
n = simulated_annealing(BicingProblem(estat_inicial_greedy),schedule= exp_schedule(k=5, lam=0.001, limit=70000))

#n = hill_climbing(BicingProblem(estat_inicial))
#n = hill_climbing(BicingProblem(estat_inicial_greedy))
print(n)                # Estat final
#print(n.heuristic())    # Valor de l'estat final


#temps_en_milisegons = (timeit(lambda: simulated_annealing(BicingProblem(estat_inicial_greedy), schedule= exp_schedule(k=5, lam=0.0005, limit=50000)), number=1) * 1000)
#print('\n', round(temps_en_milisegons, 2), 'milisegons')

#temps_en_milisegons = (timeit(lambda: hill_climbing(BicingProblem(estat_inicial_greedy)), number=1) * 1000)
#print('\n', round(temps_en_milisegons, 2), 'milisegons')
