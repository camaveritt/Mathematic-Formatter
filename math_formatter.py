import re

def arithmetic_arranger(problems, verbose = False):
  arranged_problems = ""
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  
  # Error Block
  if len(problems) > 5:
    return "Error: Too many problems."  
  for problem in problems:
    p = problem.split()
    if re.search('[*\/]', problem):
      return "Error: Operator must be '+' or '-'."
    if re.search('\D', p[0]) or re.search('\D', p[2]):
      return "Error: Numbers must only contain digits."
    if len(p[0]) > 4 or len(p[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    # String Compiling
    evaluate = eval(problem)
    solve = str(evaluate)
    line1 += "  "
    line2 += "{opr}".format(opr=p[1]) + " "
    
    if len(p[0]) >= len(p[2]):
      line2 += " "*(len(p[0]) - len(p[2]))
      line3 += "--" + "-"*(len(p[0]))
    else: 
      line1 += " "*(len(p[2]) - len(p[0]))
      line3 += "--" + "-"*(len(p[2]))
    
    line1 += "{opd1}".format(opd1=p[0])
    line2 += "{opd2}".format(opd2=p[2])
    line4 += " "*(len(line3)-(len(solve)+len(line4))) + "{s}".format(s=solve)    
    
    if problems.index(problem) != len(problems)-1:
      line1 += "    "
      line2 += "    "
      line3 += "    "
      line4 += "    "
    
  # Final Compile
  arranged_problems = line1 + "\n" + line2 + "\n" + line3
  
  # Add Answer Line if Verbose
  if verbose:      
    arranged_problems = arranged_problems + "\n" + line4
    return arranged_problems
  
  
  return arranged_problems
