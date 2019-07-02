PASSWORD = '12345'


def password_requiered(func):
    def wrapper():
        password = input('Cual es tu contraseña ')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta')

    return wrapper


@password_requiered
def needs_password():
    print('La contraseña es correcta')


def upper(func):
    def wrapper(*args, **qwargs):
        result = func(*args, **qwargs)

        return result.upper()

    return wrapper


@upper
def say_my_name(name):
    return 'Hola, ' + name


if __name__ == "__main__":
    print(say_my_name('David'))
