while True:
    str = input().lower()
    if str == 'quit':
        break
    if len(str) == len(set(str)):
        print('True')
    else:
        print('False')