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
from pprint import pprint

user_form = {
    "username": "",
    "name": "",
    "age": "",
    "password": "",
    "repeat_password": ""
}

# DB

users = {
    "Taylor": {"username": "Taylor",
               "name": "lauri",
               "age": "34",
               "password": "#12",
               "repeat_password": "#12"}
}

# CHECK


def is_valid_input(*args):
    for arg in args:
        if not arg.isdigit():
            return False
    return True


def is_new_user(username):
    if username in users:
        return False
    return True


def validate_username(username):
    if username in users:
        return False
    if len(username) > 6 and username[0].isalpha():
        return True
    return False


def validate_name(name):
    if len(name) > 3:
        return True
    return False


def validate_age(age):
    if age.isdigit() and int(age) > 0:
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
    if not is_new_user(user_form["username"]):
        errors.append("El usuario ya existe. Ingrese otro username")
    if not validate_username(user_form["username"]):
        errors.append(
            "Error en username. Debe ser mayor a 6 caracteres y no puede empezar con un número")
    if not validate_name(user_form["name"]):
        errors.append("Error en Nombre. Debe ser mayor a 3 caracteres")
    if not validate_age(user_form["age"]):
        errors.append(
            "Error en Edad. Debe ser un valor numérico entero positivo")
    if not validate_password(user_form["password"]):
        errors.append(
            "Password no válido. Debe tener de solo 3 caracteres, y contener al menos un # o %")
    if not validate_repeat_password(user_form["password"], user_form["repeat_password"]):
        errors.append("Error. Los Passwords ingresados no coinciden")
    return errors


def get_user_dto(user):
    return {
        "username": user["username"],
        "name": user["name"],
        "age": user["age"],
    }

# CRUD


def create_user(user_form):
    users[user_form["username"]] = user_form
    user_dto = get_user_dto(user_form)
    pprint({'message': 'Usuario creado con éxito',
            'user': user_dto, 'status': 201})


def read_user(username):
    if username in users:
        pprint({'message': 'Usuario encontrado',
                'user': get_user_dto(users[username]), 'status': 200})
    else:
        pprint({'message': f'Usuario no encontrado: {username}', 'status': 404})


def find_user(username):
    if username in users:
        return users[username]
    else:
        return None


def update_user(username, user_form):
    if "username" in user_form:
        del user_form["username"]

    for key, value in user_form.items():
        users[username][key] = value


def delete_user(username):
    del users[username]
    pprint({'message': 'Usuario eliminado con éxito', 'status': 200})

# FORM


def create_user_form():
    print("👤 Crear usuario")
    user_form["username"] = input(
        "Ingrese nuevo username. Debe ser mayor a 6 caracteres y no puede empezar con un número : ")
    user_form["name"] = input("Nombre: ")
    user_form["age"] = input("Edad: ")
    user_form["password"] = input(
        "Nuevo Password. Debe tener solo 3 caractéres, y al menos uno de ellos ser # o %: ")
    user_form["repeat_password"] = input("Repita password: ")

    errors = validate_form(user_form)
    if errors:
        for error in errors:
            print(error)
            close_or_continue()
    else:
        create_user(user_form)


def read_user_form():
    print("👤 Buscar usuario")
    username = input("Username: ")
    read_user(username)


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
    print("👤 Borrar usuario")
    username = input("Ingrese username: ")
    user = find_user(username)
    if user:
        delete_user(username)
    else:
        pprint({'message': f'Usuario no encontrado: {username}', 'status': 404})


def get_all_users():
    for user in users.values():
        pprint(get_user_dto(user))


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
    print("5. Listar todos los usuarios")
    print("6. Salir")
    print('========================')
    option = input("INGRESE UNA OPCIÓN: ")

    if is_valid_input(option):
        if option == '1':
            create_user_form()
            close_or_continue()
        elif option == '2':
            read_user_form()
            close_or_continue()
        elif option == '3':
            update_user_form()
            close_or_continue()
        elif option == '4':
            delete_user_form()
            close_or_continue()
        elif option == '5':
            get_all_users()
            close_or_continue()
        elif option == '6':
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
