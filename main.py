from pyscript import display, document


def account_register(e):
    document.getElementById('result').innerHTML = " "
    username = document.getElementById('input1').value
    password = document.getElementById('input2').value

    """subjects = ['English', 'Math', 'Science', 'Social Studies', 'Filipino']

    for subject in subjects:
        display(f'-{subject}', target='result')"""
    
    """count = 5

    while count < 151:
        display(count, target='result')
        count += 5"""
    
    """while True:
        print("This will never stop!", target='result')"""
    
    """for i in range(1, 100, 2):
        if i == 9:
            continue
        display(i, target="result")"""
    

    if len(username) < 7:
        display(f'Username must be 7 characters long', target="result")
    elif len (password) < 10:
        display(f'Password must be 10 characters long', target="result")
    elif password.isdigit():
        display(f'Password must have 1 letter', target="result")
    elif password.isalpha():
        display(f'Password must have 1 number', target="result")
    else:
        display(f'Account created', target="result")
