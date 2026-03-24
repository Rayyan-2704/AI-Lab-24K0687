from ortools.sat.python import cp_model

def main():
    model = cp_model.CpModel()

    a = model.new_int_var(0, 3, 'A')
    b = model.new_int_var(0, 3, 'B')
    c = model.new_int_var(0, 3, 'C')
    model.add(a != b)
    model.add(b != c)
    model.add(a + b <= 4)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status==cp_model.OPTIMAL or status==cp_model.FEASIBLE:
        print(f'A = {solver.value(a)} | B = {solver.value(b)} | C = {solver.value(c)}')
    else:
        print("Solution not found")

main()