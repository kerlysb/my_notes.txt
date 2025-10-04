# Escritura y lectura de un archivo de texto en Python

# Escritura en el archivo "my_notes.txt"
with open('my_notes.txt', 'w', encoding='utf-8') as file:
    # Escribimos tres líneas de notas personales utilizando write()
    file.write("Nota 1: Aprender Python es muy útil.\n")
    file.write("Nota 2: Practicar escritura y lectura de archivos.\n")
    file.write("Nota 3: La programación mejora la lógica.\n")
