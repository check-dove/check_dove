
"""My code"""
user_db = {'jack': 'jianshem'}


def check_username(user_name):
    sign_ava = 'username is available. '
    sign_una = 'username is unavailable. '
    b = user_db.get(user_name, sign_ava)
    if b == sign_ava:
        print(sign_ava + "please register first")
        return new_user
    else:
        print(sign_una + "Can login directly")
        return user_log


def new_user(user_name):
    user_pasw = input("please enter password you want:")
    user_db.setdefault(user_name, user_pasw)
    print('Your account has been created successfully, you can choose to log in')
    return user_log


def user_log(user_name):
    pwd = input("please enter your password")
    passwd = user_db.get(user_name)
    if passwd == pwd:
        print('welcome back', user_name)
    else:
        print('login incorrect')


def show_menu():
    prompt = """
    (R)egistration
    (L)ogin
    (D)on't know if it's registration
    (Q)uit
    Enter choice: """
    choose = input(prompt).rstrip()[0].lower()
    done = True
    while done:
        if choose in 'rd':
            user_name = input("please enter your username")
            re_handler = check_username(user_name)
            temp = re_handler(user_name)
            sign_login = input('Do you want to log in(yes/no):').strip()[0].lower()
            if sign_login in 'y':
                temp(user_name)
            else:
                print('Thanks for joining us.')
        elif choose in 'l':
            user_name = input("please enter your username")
            user_log(user_name)
        else:
            break
        done = False


if __name__ == "__main__":
    show_menu()


"""Example in the book"""
db = {}

def registration_user():
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = input('passwd: ')
    db[name] = pwd

def user_login():
        name = input('login: ')
        pwd = input('passwd: ')
        passwd = db.get(name)
        if passwd == pwd:
            print('welcome back', name)
        else:
            print('login incorrect')

def showmenu():
    prompt = """
    (U)ser registration
    (E)xisting, please Login
    (Q)uit
    Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)

            if choice not in 'neq':
                print('invalid option, try again')
            else:
                chosen = True
                done = True
        registration_user()
        user_login()
