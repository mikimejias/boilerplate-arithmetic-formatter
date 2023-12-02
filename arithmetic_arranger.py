def arithmetic_arranger(problems, optional_arg = False):
  #Initializing variables
  arranged_problems = []
  line_one = ''
  line_two = ''
  line_three = ''
  line_result = ''
  cant = 1

  #If there are too many problems supplied to the function.
  #The limit is five, anything more will return: Error: Too many problems.
  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    for problem in problems:
      aux = problem.split()
      max = 0
      count_guions = 0

      #Each number (operand) should only contain digits.
      #Otherwise, the function will return: Error: Numbers must only contain digits.
      if aux[0].isdigit() and aux[2].isdigit():
        #Each operand (aka number on each side of the operator) has a max of four digits
        #The error string returned will be: Error: Numbers cannot be more than 4 digits.
        if len(aux[0]) > 4 or len(aux[2]) > 4:
          return "Error: Numbers cannot be more than four digits."
      else:
        return "Error: Numbers must only contain digits."
        
           
      if len(aux[0]) > len(aux[2]):
        max = len(aux[0])
      else:
        max = len(aux[2])

      #The appropriate operators the function will accept are addition and subtraction.
      #Multiplication and division will return an error.
      #Other operators not mentioned in this bullet point will not need to be tested.
      #The error returned will be: Error: Operator must be '+' or '-'.
      if optional_arg:
        if aux[1] == '+':
          aux.append(str(int(aux[0]) + int(aux[2])))
        elif aux[1] == '-':
          aux.append(str(int(aux[0]) - int(aux[2])))
        else:
          return "Error: Operator must be '+' or '-'."
        max = len(aux[3]) if max < len(aux[3]) else max
        
      count_guions = max + 2
      
      if cant < len(problems):
        line_one = line_one + (count_guions-len(aux[0]))*' ' + aux[0] + 4*' '
        line_two = line_two + aux[1] + (count_guions-len(aux[2])-1)*' ' + aux[2] + 4*' '
        line_three = line_three + count_guions*'-' + 4*' '
        if optional_arg:
          line_result = line_result + (count_guions-len(aux[3]))*' ' + aux[3] + 4*' ' 
      else:
        line_one = line_one + (count_guions-len(aux[0]))*' ' + aux[0] + '\n'
        line_two = line_two + aux[1] + (count_guions-len(aux[2])-1)*' ' + aux[2] + '\n'
        
        if optional_arg:
          line_three = line_three + count_guions*'-' + '\n'
          line_result = line_result + (count_guions-len(aux[3]))*' ' + aux[3]
        else:
          line_three = line_three + count_guions*'-'
      cant = cant + 1

  if optional_arg:
    arranged_problems = line_one + line_two + line_three + line_result
  else:
    arranged_problems = line_one + line_two + line_three
  
  return arranged_problems
