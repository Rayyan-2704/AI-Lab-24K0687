from ortools.sat.python import cp_model

class SolutionDisplay(cp_model.CpSolverSolutionCallback):
    def __init__(self, a, b, c):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.solution_count = 0

    def on_solution_callback(self):
        self.solution_count += 1
        print(f"Solution {self.solution_count}:")
        print(f"A = {self.value(self.a)}, B = {self.value(self.b)}, C = {self.value(self.c)}")


def main():
    model = cp_model.CpModel()
    a = model.new_int_var(0, 3, "A")
    b = model.new_int_var(0, 3, "B")
    c = model.new_int_var(0, 3, "C")

    model.add(a != b)
    model.add(b != c)
    model.add(a + b <= 4)

    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = True

    solution_printer = SolutionDisplay(a, b, c)
    status = solver.solve(model, solution_printer)

    print(f"\nTotal Solutions:", solution_printer.solution_count)
    print(f"Status: {solver.status_name(status)}")

main()