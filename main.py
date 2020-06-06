import sys
import os
import subprocess

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

def feed_inputs_to_file(problem, inputs):
    if len(inputs) == 0:
        os.system(f'python {problem}')
    else:
        for i in inputs:
            process = subprocess.Popen(['python', problem],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         encoding='utf8')
            with open(i, 'r') as file:
                input_data = file.read()

            stdoutdata, stderrdata = process.communicate(input = input_data)
            print(stdoutdata)

if __name__ == '__main__':
    args = sys.argv[1:]
    title = args[-1]
    problem = get_problem(title)
    inputs = get_inputs(title)
    feed_inputs_to_file(problem, inputs)
