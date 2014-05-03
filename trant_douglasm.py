from SATSolver import testKb, testLiteral


def questionOne():
    clauses = [[-1,2],[3],[4]]

    print 'Knowledge base is satisfiable:',testKb(clauses)

    print 'Is the Unicorn Mythical?',
    result = testLiteral(1,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'

    print 'Is the Unicorn Magical?',
    result = testLiteral(3,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is the Unicorn Horned?',
    result = testLiteral(4,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'



def questionTwo():
    clauses = [[-1,2],[-2,3],[3,2],[2],[-1,2,-3],[1,3],[-2,3],[1],[-2]]

    print 'Knowledge base is satisfiable:',testKb(clauses)

    print 'Is Amy truthful?',
    result = testLiteral(1,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'

    print 'Is Bob truthful?',
    result = testLiteral(2,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Cal truthful',
    result = testLiteral(3,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'

def questionThree():
    clauses = [[-1,4],[-4,1],[1,-4],[4,-1],[-3,4],[-4,3],[3,-4],
               [4,-3],[-5,-6],[6,-5],[5,6],[-6,-5],[2,4,6]]

    print 'Knowledge base is satisfiable:',testKb(clauses)

    print 'Caterpillar ate the salt',
    result = testLiteral(2,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'

    print 'Bill ate the salt',
    result = testLiteral(4,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Chester ate the salt',
    result = testLiteral(6,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'

def liarsAnonymous():
    clauses = [[-1,8],[-1,9],[-8,-9,1],
               [-2,1],[-2,12],[-1,-12,2],
               [-3,2],[-3,7],[-2,-7,3],
               [-4,5],[-4,12],[-5,-12,4],
               [-5,3],[-5,8],[-3,-8,5],
               [-6,4],[-6,9],[-4,-9,6],
               [-7,-5],[-7,-10],[5,10,7],
               [-8,-6],[-8,-11],[6,11,8],
               [-9,-7],[-9,-11],[7,11,9],
               [-10,-1],[-10,-3],[1,3,10],
               [-11,-4],[-11,-6],[4,6,11],
               [-12,-2],[-12,-10],[2,10,12]]

    print 'Knowledge base is satisfiable:',testKb(clauses)


    print 'Is Amy a truth-teller?',
    result = testLiteral(1,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'

    print 'Is Bob a truth-teller?',
    result = testLiteral(2,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Cal a truth-teller?',
    result = testLiteral(3,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Dee a truth-teller?',
    result = testLiteral(4,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Eli a truth-teller?',
    result = testLiteral(5,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Fay a truth-teller?',
    result = testLiteral(6,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Gil a truth-teller?',
    result = testLiteral(7,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Hal a truth-teller?',
    result = testLiteral(8,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Ida a truth-teller?',
    result = testLiteral(9,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Jay a truth-teller?',
    result = testLiteral(10,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Kay a truth-teller?',
    result = testLiteral(11,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'


    print 'Is Lee a truth-teller?',
    result = testLiteral(12,clauses)
    if result == True:
        print 'Yes.'
    elif result == False:
        print 'No.'
    else:
        print 'Unknown.'



def main():
    questionOne()
    print "-"*80
    questionTwo()
    print "-"*80
    questionThree()
    print "-"*80
    liarsAnonymous()

if __name__ == "__main__":
    main()