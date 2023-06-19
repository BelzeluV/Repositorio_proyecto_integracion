import re

# Función para convertir la sintaxis de inserción de Oracle a SQLite
def convert_insert_syntax(line):
    # Eliminar comillas simples alrededor de los valores numéricos
    line = re.sub(r"'([0-9]+)'", r"\1", line)
    
    # Reemplazar la función SYSDATE de Oracle por la fecha y hora actual de SQLite
    line = line.replace("SYSDATE", "datetime('now')")
    
    # Otros reemplazos y ajustes necesarios según las diferencias de sintaxis
    
    return line

# Ruta del archivo de entrada con las inserciones de Oracle
input_file = "datos.sql"

# Ruta del archivo de salida con las inserciones convertidas a SQLite
output_file = "datossqlite.sql"

# Abrir el archivo de entrada para lectura y el archivo de salida para escritura
with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
    # Leer cada línea del archivo de entrada
    for line in file_in:
        print("funcionando")
        # Verificar si la línea contiene una inserción
        if line.strip().startswith("INSERT"):
            # Convertir la sintaxis de inserción
            converted_line = convert_insert_syntax(line)
            file_out.write(converted_line)
        else:
            # Mantener las líneas que no son inserciones sin cambios
            file_out.write(line)