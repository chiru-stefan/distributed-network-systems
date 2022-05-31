import rpyc

def main():
    config = {'allow public attrs': True}
    proxy = rpyc.connect('localhost', 8003, config=config)
    password1 = 'Chiru Stefan'
    password_pass = proxy.root.exposed_check_password(password1)
    print('The password is {}'.format('Strong' if password_pass == True else 'Weak'))

    password2 = 'ChiruStefan96!'
    password_pass = proxy.root.exposed_check_password(password2)
    print('The password is {}'.format('Strong' if password_pass == True else 'Weak'))


if __name__ == '__main__':
    main()