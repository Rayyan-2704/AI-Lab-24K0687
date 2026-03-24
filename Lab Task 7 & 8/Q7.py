import sys
import time
from ortools.sat.python import cp_model

class NQueenSolution(cp_model.CpSolverSolutionCallback):
    def __init__(self, queens: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self._queens = queens
        self._solution_count = 0
        self._start_time = time.time()

    def solution_count(self):
        return self._solution_count

    def on_solution_callback(self):
        current_time = time.time()
        self._solution_count += 1
        print(f"Solution {self._solution_count}, Time = {current_time - self._start_time} seconds")

        all_queens = range(len(self._queens))
        for i in all_queens:
            for j in all_queens:
                if self.value(self._queens[j]) == i:
                    print("Q", end=" ")
                else:
                    print("_", end=" ")
            print()
        print()


def main():
    model = cp_model.CpModel()
    board_size = 4
    queens = [model.new_int_var(0, board_size - 1, f"x_{i}") for i in range(board_size)]

    model.add_all_different(queens)
    model.add_all_different(queens[i] + i for i in range(board_size))
    model.add_all_different(queens[i] - i for i in range(board_size))

    solver = cp_model.CpSolver()
    solution_printer = NQueenSolution(queens)
    solver.parameters.enumerate_all_solutions = True
    solver.solve(model, solution_printer)
    print(f"Solutions found: {solution_printer.solution_count()}")

main()