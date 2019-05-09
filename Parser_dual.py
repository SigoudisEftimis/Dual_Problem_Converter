'''


The following program accepts a txt file containing a linear problem in the general format and produces the following
arrays and one variable

- minmax : if this variable is 1 the problem is a maximization problem otherwise if the variable is -1 the problem is a
           minimazation problem


- C : holds the objective function parameters


- Equin_ :  holds values that indicate the type of constraint if value is  0  the constraint is =  , if  values is -1
            the constraint is <= and if values is 1 the constraint is >=

- B : holds the right part of the constraints

- A : holds the values of the constraints parameters




There are two basic processes for producing the tables



- Grammar Check : This procedure checks whether the file is in the correct format to accomplish it uses seven function
                  which in their totality represent a grammar that produce every correct linear problem



- Extraction : This procedure extract the parameters of the problem and shapes the tables to accomplish that it uses six
               secondary procedures



   1. Normalization : This function accepts a list of the file lines and returns two tables using regular expressions.
                      The first one has elements of the [axb] form where a and b are integers. The second using the first
                      one returns a
                      For example :  First table holds  : 5x1  ---- >  Second table holds the extracted  5  from 5x1


   2.Extraction_number_variables:This functions extract the number of decision variable ,it uses also regular expression



   3.Extraction_op_right_part : This functions extract the types of the constraints and the right part of the constraints ,
                                it uses also regular expressions


   4.Extraction_Type_of_problem : This functions extract the type of the problem an shape the minmax variable which
                                 indicates the type of problem (min or max)



   5.digitnorm : This function take the extracted  data and converts them into a more readable form . For example if a
                 number is +5 it converts to 5 etc.



   6. Equin  : This functions shape the Equin_ table


   Those six functions implement the process of extracting and shaping the tables



- Presentation :  This functions print the results on the console



For all the above process the program use the python library re (for regular expressions) and the library itertools for
 merging the sublists of a list . It also use the function grouper to create sublists with specific len



'''


import re
import itertools
import pickle


def grouper(n, it):
    it = iter(it)

    return iter(lambda: list(itertools.islice(it, n)), [])


def S(token):

    if re.match(regxmin,token) :
        token = lines.pop()
        return  S_1(token)
    else :
        print("Syntax Error type of problem is missing",token)
        return False


def S_1(token):

    if re.match(regminadd,token):
        token = lines.pop()
        return S_2(token)
    elif re.match(regx,token) :
        token = lines.pop()
        return S_3(token)
    else:
        print("Syntax Error",token)
        return False



def S_2(token):

    if re.match(regx,token):
        token = lines.pop()
        return S_3(token)
    else:
        print("Synatax Error",token)
        return False


def S_3(token):

    if re.match(regminadd,token):
        token = lines.pop()
        return S_1(token)
    elif re.match(regst,token):
        token = lines.pop()
        return S_4(token)
    elif re.match(regop, token):
        token = lines.pop()
        return S_5(token)
    else :
         if re.match(regx,token):  print("Syntax Error sign is missing ", token)
         elif re.match(regnum,token): print("Syntax Error operator is missing ", token)
         else : print("Syntax Error")
         return False


def S_4(token):

    if re.match(regminadd, token):
        token = lines.pop()
        return S_2(token)
    elif re.match(regx, token):
        token = lines.pop()
        return S_3_1(token)
    else:
       print("Syntax Error ",token)
       return False


def S_3_1(token):

    if re.match(regminadd,token):
        token = lines.pop()
        return S_4(token)
    elif re.match(regop, token):
        token = lines.pop()
        return S_5(token)
    else:
        print("Syntax Error probably operator is missing or a sign ",token)
        return False


def S_5(token):

    if re.match(regxp,token) or re.match(regnum,token):
            if not lines :
                print("The problem is correct")
                return True
            token = lines.pop()
            return S_4(token)
    else:
        print("Syntax Error probably the right part is missing",token)
        return False


def digitnorm(A,E):

    for a in A :
        for i in range(0,len(a)):
         if re.match(regplus,a[i]):
            a[i] = re.findall(regn, a[i]).pop()
    for i in range(0,len(E)):
        if re.match(regplus, E[i]):
            E[i] = re.findall(regn, E[i]).pop()

    E = E.reverse()


def Equin(equin):

    for d in range(0, len(equin)):
        if equin[d] == '=':
            equin[d] = 0
        elif equin[d] == '>=':
            equin[d] = 1
        elif equin[d] == '<=':
            equin[d] = - 1
    equin.reverse()


def Extraction_op_right_part(lines, D, B, E):

    for line in lines:
        if re.match(regop, line):
            D.append(line)
        elif re.match(regx, line):
            E.append(line)
        elif re.match(regnumx, line):
            B.append(line)
        elif re.match(regst, line):
            st = line
        else:
            temp.append(line)

    D = [x for x in D if x != []]


def Normalization(lines,C,Res):

  
    
    for line in lines:
        C.append(re.findall(regnorm, line))

    C = [x for x in C if x != []]
    for c in C:
        for cc in range(0, len(c)):
            c[cc] = c[cc].replace(' ', '')

    for c in C:
        for cc in range(0, len(c)):
            if re.match(regnum_1, c[cc]):
                Res.append(re.findall(regnum_1, c[cc]))
            elif re.match(regn, c[cc]):
                Res.append(re.findall(regn, c[cc]))

    lines = [words for segments in lines for words in segments.split()]

    return lines


def Extraction_Number_variables():

    AA = 0
    for line in lines:
        if re.match(regst, line): break
        if re.match(regx, line): AA = AA + 1
    return AA


def Extraction_Type_of_problem(lines):

    lines.reverse()
    first_line = lines.pop()
    minmax = re.findall(regxmin, first_line)
    minmax = minmax.pop().replace(" ", "")
    if minmax == 'max':
        minmax = '1'
    elif minmax == 'min':
        minmax = '-1'

    return minmax


def Presentation(minmax,C,D,E,A,TOV):

    print("The minmax variable has value  : ", minmax)
    print("The objective function parameters has values : ", C)
    print("The constraint array has values : ", D)
    print("The right part of the constraints has values :", E)
    print("The constraints parameters has values :", A)
    print("Type of variables :", TOV)

    with open('outfile', 'w') as file:

         file.write("The minmax variable has value  : ")
         file.writelines(list("%s  " % item for item in minmax))
         file.write("\nThe objective function parameters has values :  ")
         file.writelines(list("%s  " % item for item in C))
         file.write("\nThe constraint array has values : ")
         file.writelines(list("%s  " % item for item in D))
         file.write("\nThe right part of the constraints has values :")
         file.writelines(list("%s  " % item for item in E))
         file.write("\nThe constraints parameters has values :\n")
         file.writelines(list("%s\n" % item for item in A))
         file.write("\nThe type of variables :\n")
         file.writelines(list("%s\n" % item for item in A))


def DualConversion(minmax,C,D,E,A,TOV):
    
    dual_problem = []
    
    if int(minmax) == -1 :
        dual_problem.append("max")
    else:
        dual_problem.append("min")
        
    dual_problem.append("    ") 
    
    for right_part in range(0, len(E)): 
        if (right_part > 0):
            if int(E[right_part]) < 0:
                dual_problem.append("- " + str(abs(int(E[right_part]))) + "x" + str(right_part+1) + " ")
            else:
               dual_problem.append("+ " +str(E[right_part]) + "x" + str(right_part+1) + " ")
        else:
              dual_problem.append(str(E[right_part]) + "x" + str(right_part+1) + " ")
        
    dual_problem.append("\n  \n subject \n \n ")
     
    dual_problem.append("     ")
    
    i = 0 
    b = 0 
    
    for i in range(0,len(A[0])):
        for j in range(0,len(A)):
            
            if j > 0  and int(A[j][i]) > 0: 
                dual_problem.append("+ " + str(A[j][i]) +"x" + str(j+1) + " ")
            else:
                 if  int(A[j][i]) < 0 :
                      dual_problem.append("- " + str(abs(int(A[j][i])))  +"x" + str(j+1) + " ")
                 else:
                     dual_problem.append(str(A[j][i])  +"x" + str(j+1) + " ")
         
       
        if TOV[b] == 0 :
            dual_problem.append(" = ")
        elif TOV[b] == -1 :
            dual_problem.append(" <= ")
        elif TOV[b] == 1 :
            dual_problem.append(" >= ")
            
        dual_problem.append(C[b])
        b = b + 1
        dual_problem.append("\n")
        dual_problem.append("     ")     
        
        
    dual_problem.append("\n")
    dual_problem.append("     ")
    for  variable in range(0,len(D)):
         if (D[variable] == 0 ) : 
             dual_problem.append("x" + str(variable + 1) + " = free ," +"   ")
         elif (D[variable] == 1) :
             dual_problem.append("x" + str(variable + 1) + " >=0 ," + "  " )
         else: 
             dual_problem.append("x" + str(variable + 1) + " <=0  ," +"  ")
             
             
    
    return dual_problem

def ExtractTypeOfVariables(last_line):
    type_of_variable  = [] 
    lines = re.split(',' ,last_line)
    for l in lines :
        if re.findall(regfree,l):
            type_of_variable.append(0)
        elif re.findall('<=',l):
            type_of_variable.append(-1)
        elif re.findall('>=',l):
            type_of_variable.append(1)
   
    return type_of_variable
        

def DualProblemPresenation(dual_problem):
    
    with open('dual_problem', 'w') as file:
        file.writelines(list("%s" % item for item in dual_problem))

Equin_ = []
temp = []
C = []
B = []
A = []
E = []

regx = '[1-9]+x+?[0-9]+$'
regxp = '[-|+]\s*[0-9]+$'
regxmin = '[min|max]+?$'
regst  = '[s.t.|subject|st]+?'
regminadd = '[-|+]+?'
regop = '(>=|=|<=)'
regnum = '[1-9][0-9]+$|[0]$'
regnumx = '[-|+][0-9]+|[0-9]'
regn = r'^\D*(\d+)'
regplus = r'\+'
regnorm = '[-|+|\s*]\s*[0-9]+x+?[0-9]+'
regnum_1 = '[-|+|\s*][0-9]+'
regfree = 'free'

with open("test.txt") as f:
    lines = f.readlines()
    
temp_lines = lines
lines.reverse()
last_line = lines.pop(0) 

while not (re.findall(regfree,last_line) or re.findall(regop,last_line)):
          last_line = lines.pop(0) 

TOV = ExtractTypeOfVariables(last_line)

lines.reverse()
lines = [words for segments in lines for words in segments.split()]
lines.reverse()
token = lines.pop()


if 's.t.' in lines or 'st' in lines or 'subject' in lines:

        if S(token):
            lines = Normalization(temp_lines, temp, A)
            number_of_variables = Extraction_Number_variables()
            min_max = Extraction_Type_of_problem(lines)
            Extraction_op_right_part(lines, Equin_, B, E)
            A = list(itertools.chain(*A))
            A = list(grouper(number_of_variables, A))
            digitnorm(A, B)
            C.append(A.pop(0))
            C = list(itertools.chain(*C))
            Equin(Equin_)
            DualProblemPresenation(DualConversion(min_max, C, Equin_, B, A,TOV))
            Presentation(min_max, C, Equin_, B, A,TOV)
            
        else:
            print("The problem is not correct form")
else :
    print("There isn't st or subject or s.t before the constraints")



