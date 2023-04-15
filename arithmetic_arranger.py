import re


def arithmetic_arranger(problems, show=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    first_num = ''
    second_num = ''
    line_formatter = ''
    solution = ''
    arranged_problems = ''

    for problem in problems:
        if re.search('[^\s0-9.+-]', problem):
            if re.search('[/]', problem) or re.search('[*]', problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        first_num_alt = problem.split(' ')[0]
        plus_or_minus = problem.split(' ')[1]
        second_num_alt = problem.split(' ')[2]

        if len(first_num_alt) >= 5 or len(second_num_alt) >= 5:
            return 'Error: Numbers cannot be more than four digits.'

        total = ''

        if plus_or_minus == '+':
            total = str(int(first_num_alt) + int(second_num_alt))
        elif plus_or_minus == '-':
            total = str(int(first_num_alt) - int(second_num_alt))

        length = max(len(first_num_alt), len(second_num_alt)) + 2

        first = str(first_num_alt).rjust(length)
        second = plus_or_minus + str(second_num_alt).rjust(length-1)

        line = ''
        value = str(total).rjust(length)

        for _ in range(length):
            line += '-'

        if problem != problems[-1]:
            first_num += first + '    '
            second_num += second + '    '
            line_formatter += line + '    '
            solution += value + '    '
        else:
            first_num += first
            second_num += second
            line_formatter += line
            solution += value

    if show:
        arranged_problems = first_num + '\n' + second_num + \
            '\n' + line_formatter + '\n' + solution
    else:
        arranged_problems = first_num + '\n' + second_num + '\n' + line_formatter

    return arranged_problems
