import array
import binascii
import tempfile

names = ["Kosgei","Victor","Kipruto","Benjamin"]

def listBasics():
    print(names[-1])
    print(names[1:])

def arraysWithPython():
    numbers = array.array('i',xrange(3))
    print(numbers)

def arraysWithFiles():
    a = array.array('i',xrange(33))
    output = tempfile.NamedTemporaryFile('w'," "," "," ","~/victorkosgei/Projects/Python/",".")
    a.tofile(output.file)
    output.flush()

