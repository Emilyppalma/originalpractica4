from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()

    font_list = figlet.getFonts()
    selected_font = input("Ingrese el nombre de la fuente (dejar en blanco para aleatoria): ").strip()

    if not selected_font:
        selected_font = random.choice(font_list)
        print(f"Fuente aleatoria seleccionada: {selected_font}")
    elif selected_font not in font_list:
        print("La fuente ingresada no es válida. Selección aleatoria de fuente.")
        selected_font = random.choice(font_list)

    figlet.setFont(font=selected_font)

    input_text = input("Ingrese el texto que desea imprimir: ")
    rendered_text = figlet.renderText(input_text)

    print(rendered_text)

if __name__ == "__main__":
    main()
