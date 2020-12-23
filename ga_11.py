import numpy as np

def get_ranges(inputs, result):
    ranges = []
    for i in inputs:
        value = result // i + 1
        ranges.append([-value, value])
    return ranges

def init_population(population_size, ranges):
    start_pop = []
    for i in range(population_size):
        arr = []
        for j in range(len(ranges)):
            arr.append(np.random.randint(ranges[j][0], ranges[j][1]))
        start_pop.append(arr)
    return start_pop

def parents_selection(population, parents_num, p):
    parents = []
    for i in range(parents_num):
        max_ind = [j for j in range(len(p)) if p[j] == max(p)][0]
        parents.append(population[max_ind])
        p.remove(max(p))
    return parents

def fitness_assessment(population, coef_num, y):
    p = []
    for i in range(len(population)):
        s = 0
        for j in range(coef_num):
            s += population[i][j]*inputs[j]
        r = np.abs(y - s) + 1
        p.append(1/r)
    return p

def random_without(max_int, exception):
    while True:
        rand = np.random.randint(max_int)
        if rand != exception:
            return rand

def procreation(parents, parents_num, progeny_num):
    progeny = []
    while True:
        parent1 = np.random.randint(parents_num)
        parent2 = random_without(parents_num, parent1)
        progeny.append(np.append(parents[parent1][:2], parents[parent2][2:]))
        if len(progeny) == progeny_num:
            break
        progeny.append(np.append(parents[parent2][:2], parents[parent1][2:]))
        if len(progeny) == progeny_num:
            break
    return progeny

def mutation(progeny):
    for i in range(len(progeny)):
        mutation = np.random.uniform(-1, 0, 1)
        progeny[i][1] = progeny[i][1] + mutation
    return progeny

def get_new_population(progeny, parents):
    new_population = []
    for x in progeny:
        new_population.append(x)
    for i in range(2):
        new_population.append(parents[i])
    return new_population


def find_solution(p, population):
    best_result = max(p)
    ind = [i for i in range(len(p)) if p[i] == best_result][0]
    if(best_result >=0.2):
        print('Best solution: {0} with fitness {1}'.format(population[ind], best_result))
        return True
    else:
        return False

inputs = [2, 3, 5, 10, 5]
y = 30
population_size = 6
parents_num = 4
progeny_num = 6

coef_num = len(inputs)
ranges = get_ranges(inputs, y)
population = init_population(population_size,  ranges)
p = fitness_assessment(population, coef_num, y)
while find_solution(p, population) is False:
    parents = parents_selection(population, parents_num, p)
    progeny = procreation(parents, parents_num, progeny_num)
    progeny_mutation = mutation(progeny)
    population = get_new_population(progeny_mutation, parents)
    p = fitness_assessment(population, coef_num, y)