import csv
from IPython.display import clear_output


def register():
    with open('user.csv', mode='a', newline='') as f:
        writer=csv.writer(f,delimiter=',')
        print('To rigister,please enter your info:')
        email=input('E-mail:')
        username=input('Username:')
        password=input('Password:')
        repassword=input('Password again:')
        clear_output()
        if password==repassword:
            writer.writerow([email,username,password])
            print('You are now register')
        else :
            print('Something went wrong,Try again')

def login():
    print('To login,please enter your info:')
    email=input('E-mail:')
    username=input('Username:')
    password=input('Password:')
    clear_output()
    try:
        with open('user.csv', mode='r') as f:
            pass
    except FileNotFoundError:
        print("No data available at the moment, please register first.")
        return False
    else:
        with open('user.csv', mode='r') as f:
            reader=csv.reader(f,delimiter=',')
            for row in reader:
                if row==([email,username,password]):
                    print('You are now logged in')
                    return True
        print("Something went wrong,try again.")
        return False

def main():
    active=True
    logged_in=False
    while active:
        if logged_in:
            print('1.Logout\n2.Quit')
        else:
            print('1.Login\n2.Register\n3.Quit')
        choice=input('What do you like to do?').lower()
        clear_output()
        if choice=='register' and logged_in==False:
            register()
        elif choice=='login' and logged_in==False:
            logged_in=login()
            print(logged_in)
        elif choice=='quit':
            active=False
        elif choice=='logout' and logged_in==True:
            logged_in=False
            print('you are now logged out.')
        else :
            print('Sorry,please try again!!!')

if __name__=='__main__':
    main()