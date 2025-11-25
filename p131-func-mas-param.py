# p131-func-mas-param.py

def saludatodos(*todos: str) -> None:
    print('Saluda a todos')
    for nombre in todos:
        print(f"Saludos a {nombre}")
    print()

saludatodos('Carlos')
saludatodos('Juan', 'Pedro', 'Luis')
saludatodos('a', 'b', 'c')