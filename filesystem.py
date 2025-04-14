class File:
    def __init__(self, name):
        self.name = name


class Directory(File):  # Hago que Directory herede de File por futuras funcionalidades posibles que impliquen tratarlos como "iguales"
    def __init__(self, name, parent=None):
        super().__init__(name)
        self.parent = parent
        self.children = {}  # Uso un diccionario para poder tener distintos tipos de children (archivos, directorios)

class FileSystem:
    def __init__(self):
        self.root = Directory("/")
        self.current = self.root

    def cd(self, path): # Este método acepta tanto rutas relativas como absolutas
        # Ruta absoluta
        if path.startswith("/"):
            current = self.root
            parts = path.strip("/").split("/")
        # Ruta relativa
        else:
            current = self.current
            parts = path.split("/")

        parts = [p for p in parts if p] # Limpio strings vacíos

        for part in parts:
            match part:
                case ".":
                    continue
                case "..":
                    if current.parent:
                        current = current.parent
                case _:
                    if part in current.children:
                        target = current.children[part]
                        if isinstance(target, Directory):
                            current = target
                        else:
                            print(f"{part} no es un directorio")
                            return
                    else:
                        print(f"{part} no existe")
                        return

        self.current = current

    # En esta solución, no pueden coexistir archivos y directorios con el mismo nombre (no lo pedía)
    def touch(self, name):  # No soporta crear archivos pasando rutas como parámetro (no lo pedía)
        if name in self.current.children:
            print(f"Ya existe un archivo o directorio con el nombre {name}")
            return

        new_file = File(name)
        self.current.children[name] = new_file

    def ls(self):
        for name in self.current.children:
            print(name)

    # En esta solución, no pueden coexistir archivos y directorios con el mismo nombre (no lo pedía)
    def mkdir(self, name):  # No soporta crear directorios pasando rutas como parámetro (no lo pedía)
        if name in self.current.children:
            print(f"Ya existe un archivo o directorio con el nombre {name}")
            return

        new_dir = Directory(name, parent=self.current)
        self.current.children[name] = new_dir

    def pwd(self):
        if self.current == self.root:
            print("/")
            return

        current = self.current
        path = []

        while current.parent:
            path.append(current.name)
            current = current.parent

        print("/" + "/".join(reversed(path)))