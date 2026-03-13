import random

def f(x):
    return -(x*x) + (6*x)


def hill_climbing():
    min_x = 0
    max_x = 6
    
    curr_x = random.randint(min_x, max_x)
    print(f"Initial value of x: {curr_x}")
    
    step = 1
    while True:
        curr_f = f(curr_x)
        print(f"Step {step} -> Current value of x: {curr_x} | f(x): {curr_f}")
        
        neighbors = []
        if curr_x + 1 <= max_x:
            neighbors.append(curr_x + 1)
        if curr_x - 1 >= min_x:
            neighbors.append(curr_x - 1)
            
        best_neighbor = None
        best_neighbor_f = curr_f
        
        for neighbor in neighbors:
            neighbor_f = f(neighbor)
            if neighbor_f > best_neighbor_f:
                best_neighbor = neighbor
                best_neighbor_f = neighbor_f
                
        if best_neighbor is None:
            print("\n--------------------------------------")
            print(f"Final optimal value of x: {curr_x}")
            print(f"Maximum f(x): {curr_f}")
            break
            
        curr_x = best_neighbor
        step += 1


def main():
    hill_climbing()


main()