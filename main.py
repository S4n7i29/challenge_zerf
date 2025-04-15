from filesystem import FileSystem

def parse_command(command):
    tokens = command.strip().split(" ")

    op = tokens[0]
    args = []
    flags = {}

    for token in tokens[1:]:
        if token.startswith("--"):
            flags[token[2:]] = True
        if token.startswith("-"):
            for ch in token[1:]:
                flags[ch] = True
        else :
            args.append(token)

    return op, args, flags

def main():
    fs = FileSystem()

    while True:
        command = input(">").strip()
        if not command:
            continue

        op, args, flags = parse_command(command)

        match op:
            case "exit":
                print("Saliendo...")
                break
            case "cd":
                if not args:
                    print("Falta la ruta")
                    continue
                fs.cd(args[0])
            case "touch":
                if not args:
                    print("Falta el nombre de archivo")
                    continue
                fs.touch(args[0])
            case "ls":
                if args:
                    file_ref = fs.get_current(args[0])
                    if file_ref is None:
                        continue
                else:
                    file_ref = None
                fs.ls(file_ref=file_ref, recursive = flags.get("r", False) or flags.get("recursive", False), long_format = flags.get("l", False) or flags.get("long", False))
            case "rm":
                if not args:
                    print("Falta el nombre de archivo/directorio")
                    continue
                file_ref = fs.resolve_path(args[0])
                fs.rm(file_ref=file_ref, recursive = flags.get("r", False) or flags.get("recursive", False))
            case "mkdir":
                if not args:
                    print("Falta el nombre de directorio")
                    continue
                fs.mkdir(args[0])
            case "pwd":
                fs.pwd()
            case _:
                print("Ingrese un comando válido")

if __name__ == "__main__":
    main()