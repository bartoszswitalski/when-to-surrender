"""
    Name: test.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import optproblems
import optproblems.cec2005
import os

from package.optimize import *
from package.data_storing import *

F4 = 0
F5 = 1
F6 = 2
F4_BOUND = 100
F5_BOUND = 100
F6_BOUND = 100

ITERATIONS = 10


def show_test_output(data):
    output_data = FunctionOptimizationData(data, ITERATIONS)
    output_data.print_stats()


def run_tests(function, criterion_name, parameter):

    if function == 'F4':
        f = optproblems.cec2005.F4(DIMENSION)  # Shifted Schwefel’s Problem 1.2 with Noise in Fitness
        bound = F4_BOUND
    elif function == 'F5':
        f = optproblems.cec2005.F5(DIMENSION)  # Schwefel’s Problem 2.6 with Global Optimum on Bounds
        bound = F5_BOUND
    else:  # if function == 'F6':
        f = optproblems.cec2005.F6(DIMENSION)  # Shifted Rosenbrock’s Function
        bound = F6_BOUND

    if criterion_name == 'k-iter':
        criterion = run_by_k_iterations_criterion
        set_parameters('k-iter', parameter)
    elif criterion_name == 'sd':
        criterion = run_by_sd_criterion
        set_parameters('sd', parameter)
    elif criterion_name == 'best-worst':
        criterion = run_by_best_worst_criterion
        set_parameters('best-worst', parameter)
    else:  # if criterion_name == 'variance':
        criterion = run_by_variance_criterion
        set_parameters('variance', parameter)

    print('Running {} by {}'.format(function, criterion_name))

    data = merge_data(MultipleRunsData(run_multiple_optimizations(f, bound, criterion)))

    return data


def run_multiple_optimizations(cec_function, bounds, criterion):
    runs = []

    for _ in range(ITERATIONS):
        runs.append(optimize(cec_function, bounds, criterion))

    return runs
