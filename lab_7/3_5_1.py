import re, rpyc


def main():
    print("Starting server")
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(PasswordChecker, port=8003)
    t.start()


class PasswordChecker(rpyc.Service):
    def exposed_check_password(self, password):
        if (len(password) >= 10):
            if (bool(re.match('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])', password)) == True):
                return True  # Strong password
            else:
                return False  # Weak password
        else:
            return False  # password is weak


if __name__ == '__main__':
    main()