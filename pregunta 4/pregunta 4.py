class MultiplicationTable:
    @staticmethod
    def save_table_to_file(number):
        if 1 <= number <= 10:
            with open(f"tabla-{number}.txt", "w") as file:
                for i in range(1, 11):
                    line = f"{number} x {i} = {number * i}\n"
                    file.write(line)
            print(f"Tabla del {number} guardada en el archivo tabla-{number}.txt")
        else:
            print("Número fuera del rango permitido (1-10).")

    @staticmethod
    def read_full_table(number):
        try:
            with open(f"tabla-{number}.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print(f"El archivo tabla-{number}.txt no existe.")

    @staticmethod
    def read_specific_line(number, line_number):
        try:
            with open(f"tabla-{number}.txt", "r") as file:
                lines = file.readlines()
                if 1 <= line_number <= len(lines):
                    print(lines[line_number - 1].strip())
                else:
                    print("Número de línea fuera de rango.")
        except FileNotFoundError:
            print(f"El archivo tabla-{number}.txt no existe.")

def main():
    while True:
        print("1. Guardar tabla de multiplicar en archivo")
        print("2. Leer tabla completa desde archivo")
        print("3. Leer línea específica desde archivo")
        print("4. Salir")
        choice = input("Ingrese su elección: ")

        if choice == "1":
            number = int(input("Ingrese un número entre 1 y 10: "))
            MultiplicationTable.save_table_to_file(number)
        elif choice == "2":
            number = int(input("Ingrese un número entre 1 y 10: "))
            MultiplicationTable.read_full_table(number)
        elif choice == "3":
            number = int(input("Ingrese un número entre 1 y 10: "))
            line_number = int(input("Ingrese el número de línea a mostrar: "))
            MultiplicationTable.read_specific_line(number, line_number)
        elif choice == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
