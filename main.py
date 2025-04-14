from filesystem import FileSystem

def main():
    fs = FileSystem()

    while True:
        command = input(">").strip()
        if not command:
            continue

        parts = command.split(" ")
        operation = parts[0]
        args = parts[1:]

        match operation:
            case "exit":
                print("Saliendo...")
                break
            case "cd":
                if args:
                    fs.cd(args[0])
                else:
                    print("Falta la ruta")
            case "touch":
                if args:
                    fs.touch(args[0])
                else:
                    print("Falta el nombre de archivo")
            case "ls":
                fs.ls()
            case "mkdir":
                if args:
                    fs.mkdir(args[0])
                else:
                    print("Falta el nombre de directorio")
            case "pwd":
                fs.pwd()
            case _:
                print("Ingrese un comando válido")

if __name__ == "__main__":
    main()