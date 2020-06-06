import sys
import os

problem_directory = 'problems'
input_directory = 'inputs'

def get_problem(title):
    problems = os.listdir(problem_directory)
    p_name = title + ".py"
    p_name = p_name.lower()
    for problem in problems:
        if problem.lower() == p_name:
            return os.path.join(problem_directory, problem)
    print("File not found")
    return None

def get_inputs(title):
    inputs = os.listdir(input_directory)
    i_name = title + ".txt"
    i_name = i_name.lower()
    files = []
    for i in inputs:
        if i.lower().startswith(title.lower()):
            files.append(os.path.join(input_directory, i))
    return files

if __name__ == '__main__':
    args = sys.argv[1:]
    title = args[-1]
    problem = get_problem(title)
    inputs = get_inputs(title)
