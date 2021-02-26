#### 1.
def displayMenu():
    print('\n-------------------------\n')
    print('What would you like to do?')
    print('(a) Add new student)')
    print('(v) View students')
    print('(q) Quit')

    choice = input('Type one letter (a/v/q): ')
    print('you chose: {}.'.format(choice))
    print('\n-------------------------\n')
    return choice



### 2. 
def doAdd(students):
    currentStudent = {}
    currentStudent['name'] = input('enter the name: ')
    currentStudent['modules'] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input('enter the name of the module: ')

    while moduleName != " ":
        module = {}
        module['name'] = moduleName
        module['grade'] = int(input('Enter grade: '))
        modules.append(module)
        moduleName = input('enter the name of the module: ')
    return modules

def doView(students):
    for i in students[0].values():
        print('name is: {}.'.format(i))

students = []
choice = displayMenu()


def quit():
    print('Good bye')
    
while choice != 'q':
    if choice == 'a':
        doAdd(students)
        choice = displayMenu()
    elif choice == 'v':
        doView(students)
        choice = displayMenu()
    else:
        quit()