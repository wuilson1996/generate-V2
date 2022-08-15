import optparse

def generate(fin, file="dictionary.txt"):
    """
        fin : es la cantidad de digitos que quieres combinar.
    """
    fin = fin-1
    nums = []
    numbers = []
    # Generando inicio para combinaciones
    for i in range(0, 10, 1):
        nums.append(str(i))

    # Generando numeros para combinaciones.
    print("[+] Generando combinaciones...")
    for f in range(fin):
        for i in range(len(nums)):
            for j in range(0, 10, 1):
                numbers.append(str(nums[i])+str(j))
        nums = numbers
        numbers = []
    print("[+] Escribiendo archivos...")
    with open(file, "w") as file:
        file.write(str(nums).replace("[", "").replace("]", "").replace(" ", "").replace("'", "").replace(",", "\n"))
    
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-l", "--longitud", dest = "longitud", help = "cantidad de combinaciones, o longitud de digitos.")
    parser.add_option("-f", "--file", dest = "file", help = "Indica el archivo que se creara con la salida. ejemplo: file.txt")

    (options, arguments) = parser.parse_args()
    if not options.longitud:
        parser.error("[-] Por favor indica la longitud de digitos, ejemplo: -l 5.")
    elif not options.file:
        parser.error("[-] Por favor indica el nombre del archivo, ejemplo: file.txt")
    
    return options

if __name__ == "__main__":
    options = get_arguments()
    if str.isdigit(options.longitud):
        generate(int(options.longitud), file=options.file)
