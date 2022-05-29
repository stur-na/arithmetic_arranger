def arithmetic_arranger(problems, display = False):
    start =  True
    line1=line2=line3=line4 = ''
    #check to make sure problems are not more than five
    if len(problems) > 5:
        return 'Error: Too many problems.'
    #loop through problems list and split each expression
    for exp in problems:
        number = exp.split()
        num1 = number[0]
        op = number[1]
        num2 = number[2]
        #check to make sure problems only contain digits
        if num1.isdigit() != True or num2.isdigit() != True:
            return 'Error: Numbers must only contain digits.'
        #check to make sure there are only four digits on each side of operand
        elif len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        #check to make sure there are only allowed operators
        elif op != '+' and op != '-':
            return 'Error: Operator must be "+" or "-".'
        space = max(len(num1), len(num2))
        sepr = '    '
        int1 = int(num1)
        int2 = int(num2)
        #display the first expression in the proper way.
        if start:
            line1 += num1.rjust(space+2)
            line2 += op +' ' + num2.rjust(space)
            line3 += '-' * (space+2)
            if display:
                if op == '+':
                    line4+= str(int1+int2).rjust(space+2)
                else:
                    line4+= str(int1-int2).rjust(space+2)
            start = False
        #display the rest of the expression horizontally aligned
        else:
            line1 += num1.rjust(space+6)
            line2 += op.rjust(5) +' ' + num2.rjust(space)
            line3 += sepr + '-' * (space+2)
            if op == '+':
                line4+= sepr + str(int1+int2).rjust(space+2)
            else:
                line4+= sepr + str(int1-int2).rjust(space+2)
    #if display set to "TRUE", show the solution to each expression
    if display:
        #print(line1,line2,line3,line4)
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3
    #new branch addedddd