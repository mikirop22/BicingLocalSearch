from typing import Generator

from aima.search import Problem

from abia_bicing_operators import BicingOperator
from abia_bicing_estat_h2_SA import Estat

class BicingProblem(Problem):
    def __init__(self, initial_state: Estat):
        super().__init__(initial_state)
        self.benefit_evolution = []  # Llista per emmagatzemar els beneficis a cada iteració

    def actions(self, state: Estat) -> Generator[BicingOperator, None, None]:
        return state.generate_actions()

    def result(self, state: Estat, action: BicingOperator) -> Estat:
        new_state = state.aplicar_accions(action)
        current_benefit = new_state.heuristic()
        self.benefit_evolution.append(current_benefit)  # Guarda el benefici o heurística a cada iteració
        return new_state

    def value(self, state: Estat) -> float:
        return state.heuristic()

    def goal_test(self, state: Estat) -> bool:
        return False
