try:
    import time
    def getZone(zone: int): return (3600 * zone)
    def Time(zone: int = 3): return time.strftime("%H:%M:%S", time.gmtime(time.time() + getZone(zone)))

    import os
    def checkFile(path: str): return os.path.isfile(path)
    def clearScreen(): os.system('cls' if os.name=='nt' else 'clear')

    import random
    random.seed(time.time())
    def randSeed(): return random.seed(random.randint(0, 10000))
    def rand(): return random.randint(0, 9)
except ModuleNotFoundError as error:
    exit(error)

class Object(object):
    def __init__(self, **settings):
        super().__init__()
        self.id = settings.get('id')
        self.name = settings.get('name')

def randId():
    return ''.join([str(rand()) for i in range(10)])

def createObj():
    name = input("Name > ") 
    return Object(name=name, id=randId())

def readObj():
    objName = input('object name > ')
    if checkFile(f'.\\items\\{objName}.obj') == False: return print('Object not found')
    with open(f'.\\items\\{objName}.obj', 'r') as objFile:
        info = objFile.read().split('/')
    return Object(name=info[0], id=info[1])

def saveObj(obj: Object = None):
    if not obj: return print('Object not found')
    info = f'{obj.name}/{obj.id}'
    with open(f'.\\items\\{obj.name}.obj', "w")as objFile:
        objFile.write(info)
    return obj

def getSpace(minValue: int = 0, maxValue: int = 10):
    return ' ' * (maxValue - minValue)

def getHelp(menu: str = 'main'):
    print('#', 'command' + getSpace(len(list('command'))), 'info')
    commandsMain = [['help', 'Get help menu'], ['create', 'Create object'],
        ['get', 'Get object']]
    commandsGet = [['help', 'Get help menu'], ['list', 'List with objects'],
        ['object', 'Return object'], ['back', 'Back to the main menu']]
    commandsObject = [['help', 'Get help menu'], ['changename', 'Change name for object'],
        ['info', 'Get info about object'], ['delete', 'Delete objecy'],
        ['back', 'Back to the main menu']]
    if menu == 'main': menu = commandsMain
    if menu == 'get': menu = commandsGet
    if menu == 'obj': menu = commandsObject
    for command in menu: print(menu.index(command) + 1, command[0] + getSpace(len(list(command[0]))), command[1])
    print('#', 'clear' + getSpace(len(list('clear'))), 'Clear console')
    print('#', 'exit' + getSpace(len(list('exit'))), 'Close program')

def Exit(): exit('# User close program')

def getListObj():
    print("#", 'object' + getSpace(len(list('object')), 20), 'type' + getSpace(6), 'id')
    files = os.listdir('.\\items\\')
    for File in files:
        with open(f'.\\items\\{File}', 'r') as f:
            print('#', File.split('.')[0] + getSpace(len(list(File.split('.')[0])), 20), 
                File.split('.')[1] + getSpace(5), f.read().split('/')[1])


def checkOption(option: str, menu: str):
    if option == '1' or option == 'help': return getHelp(menu)
    if option == 'clear': clearScreen()
    if option == 'exit': Exit()
    if menu == 'main':
        if option == '2' or option == 'create': saveObj(createObj())
        if option == '3' or option == 'get': return 'get'
    elif menu == 'get':
        if option == '2' or option == 'list': getListObj()
        if option == '3' or option == 'object': 
            print('#', 'Some commands do not work in this function')
            return 'obj'
        if option == '4' or option == 'back': return 'main'
    elif menu == 'obj':
        if option == '2' or option == 'changename': print('#', 'Function is development')
        if option == '3' or option == 'info': print('#', 'Function is development')
        if option == '4' or option == 'delete': print('#', 'Function is development')
        if option == '5' or option == 'back': return 'main'

def checkCalc(calc: str = ''):
    if calc == 'get': return 'get'
    elif calc == 'obj': return 'obj'
    elif calc == 'main': return 'main'
    else: return False

def getOption(name: str = 'main'):
    return input(f'{name} > ')

def update(menu: str):
    randSeed()
    option = getOption(menu)
    calc = checkOption(option, menu)
    if checkCalc(calc) == False: return menu
    return checkCalc(calc)

clearScreen()
menu = 'main'
try:
    while True:
        menu = update(menu)
except KeyboardInterrupt:
    exit('\n# User close program')