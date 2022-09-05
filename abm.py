""" Escribir un programa en python que valide un formulario 
y que imprima un mensaje de error por cada campo no válido.
Los campos y sus condiciones son:
✅usuario: mayor a seis caracteres y no puede empezar con un número. tiene que ser único, no puede haber 2 users con el mismo.(identificador único)
✅Nombre: String mayor a tres caracteres, imprimir mensaje de error “Nombre tiene que ser mayor  a 3 caracteres”
✅Edad: Int, si no es int imprimir  “Edad tiene que ser un valor numérico”
✅password: tiene que ser  igual a tres caracteres, y contener almenos un  # o %
✅repetir password: tiene que ser igual al campo password.
Si el formulario es válido agregarlo a la dict
Si el formulario no es válido imprima por pantalla los errores y pida al usuario que los corrija.
Permitir al usuario que pueda borrar por identificador único.
Permitir al usuario que pueda modificar los campos de un usuario del sistema buscado por identificador único.
Permitir buscar un usuario en el sistema por identificador único """

user_form = {
    "username": "",
    "name": "",
    "age": "",
    "password": "",
    "repeat_password": ""
}

# DB

users = {}

# CHECK


def is_valid_input(*args):
    # podrían agregarse mas validaciones...
    for arg in args:
        if not arg.isdigit():
            return False
    return True


def validate_username(username):
    if len(username) > 6 and username[0].isalpha():
        return True
    return False


def validate_name(name):
    if len(name) > 3:
        return True
    return False


def validate_age(age):
    if age.isdigit():
        return True
    return False


def validate_password(password):
    if len(password) == 3 and ("#" in password or "%" in password):
        return True
    return False


def validate_repeat_password(password, repeat_password):
    if password == repeat_password:
        return True
    return False


def validate_form(user_form):
    errors = []
    if not validate_username(user_form["username"]):
        errors.append("Username no válido")
    if not validate_name(user_form["name"]):
        errors.append("Name no válido")
    if not validate_age(user_form["age"]):
        errors.append("Age no válido")
    if not validate_password(user_form["password"]):
        errors.append("Password no válido")
    if not validate_repeat_password(user_form["password"], user_form["repeat_password"]):
        errors.append("Repeat password no válido")
    return errors

# CRUD


def create_user(user_form):
    users[user_form["username"]] = user_form
    print({'message': 'Usuario creado con éxito',
          'user': user_form, 'status': 201})


def read_user(username):
    if username in users:
        return users[username]
    return {'message': 'Usuario no encontrado', 'status': 404}


def update_user(username, user_form):
    if "username" in user_form:
        del user_form["username"]

    for key, value in user_form.items():
        users[username][key] = value


def delete_user(username):
    del users[username]

# FORM


def create_user_form():
    user_form["username"] = input("Ingrese nuevo username: ")
    user_form["name"] = input("Nombre Completo: ")
    user_form["age"] = input("Edad: ")
    user_form["password"] = input("Nuevo Password: ")
    user_form["repeat_password"] = input("Repita password: ")

    errors = validate_form(user_form)
    if errors:
        for error in errors:
            print(error)
    else:
        create_user(user_form)


def read_user_form():
    username = input("Ingrese username: ")
    user = read_user(username)
    if user['status'] == 404:
        print(user['message'])
    else:
        print(user)


def update_user_form():
    username = input("Ingrese username: ")
    user = read_user(username)
    if user['status'] == 404:
        print(user['message'])
    else:
        print(user)
        user_form["name"] = input("Nombre Completo: ")
        user_form["age"] = input("Edad: ")
        user_form["password"] = input("Nuevo Password: ")
        user_form["repeat_password"] = input("Repita password: ")
        update_user(username, user_form)


def delete_user_form():
    username = input("Ingrese username: ")
    user = read_user(username)
    if user['status'] == 404:
        print(user['message'])
    else:
        print(user)
        delete_user(username)


def close_or_continue():
    exit = input("🔁 ¿Desea continuar? (S/N): ")
    if exit == "S" or exit == "s":
        show_menu()
    else:
        print("👋 Gracias por utilizar el programa")


def show_menu():
    print("¿Qué desea hacer?")
    print('========================')
    print("1. Agregar un usuario")
    print("2. Buscar un usuario")
    print("3. Modificar un usuario")
    print("4. Borrar un usuario")
    print("5. Salir")
    print('========================')
    option = input("INGRESE UNA OPCIÓN: ")

    if is_valid_input(option):
        if option == '1':
            create_user_form()
        elif option == '2':
            read_user_form()
        elif option == '3':
            update_user_form()
        elif option == '4':
            delete_user_form()
        elif option == '5':
            exit()
        else:  # !1 2 3 4 5
            print("🔕 Lo sentimos, opción no válida.")
            close_or_continue()
    else:  # option not a number
        print("🔕 Lo sentimos, opción no válida.")
        close_or_continue()


def init():
    show_menu()


init()
