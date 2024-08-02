def arithmetic_arranger(problem_set, show_answers=False):
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    # Error #1: # of Problems
    if len(problem_set) > 5:
        return "Error: Too many problems."
    
    # Looping through the problem set
    for problem in problem_set:
        # Error #2: Incorrect Operator
        if '+' in problem:
            index = problem.find('+') 
        elif '-' in problem:
            index = problem.find('-')
        else:
            return "Error: Operator must be '+' or '-'."
        
        # First Operand
        first_operand = problem[:index].strip(' ')

        # Second Operand
        second_operand = problem[index+1::].strip(' ')

        # Operator
        operator = problem[index]
        
        # Error #3: Only Digits
        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'
        # Error #4: No larger than 4 digits    
        elif len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Formatting Block
        width = max(len(first_operand),len(second_operand)) + 2
        space = ' ' 

        # First Line
        first_line.append(space*(width - len(first_operand)) + first_operand)

        # Second Line 
        second_line.append(operator + (space * (width - len(second_operand) - 1)) + second_operand)

        # Third Line
        third_line.append('-' * (width))

        # Fourth Line Block (optional)
        if show_answers:
            if operator == '+':
                answer = str(int(first_operand) + int(second_operand))
            else:
                answer = str(int(first_operand) - int(second_operand))
        
            fourth_line.append(space * (width - len(answer)) + answer)

    # Formatting Block #2            
    first_line = '    '.join(first_line)
    second_line = '    '.join(second_line)
    third_line = '    '.join(third_line)
    fourth_line = '    '.join(fourth_line)

    # Final Formatting Block
    if show_answers:
        problems = f'{first_line}\n{second_line}\n{third_line}\n{fourth_line}'
    else:
        problems = f'{first_line}\n{second_line}\n{third_line}'

    return problems

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')