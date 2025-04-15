from valid_file import is_valid_name

class File:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def type(self):
        return "archivo"


class Directory(File):  # Un directorio es un archivo (futuras funcionalidades posibles pueden implicar tratarlos como "iguales")
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.children = {}  # Clave: Nombre - Valor: Archivo (/Directorio)

    def type(self):
        return "directorio"


class FileSystem:
    def __init__(self):
        self.root = Directory("/")
        self.current = self.root

    # Retorna el archivo referente a una ruta especificada
    def resolve_path(self, path):
        # Ruta absoluta
        if path.startswith("/"):
            node = self.root
            parts = path.strip("/").split("/")
        # Ruta relativa
        else:
            node = self.current
            parts = path.split("/")

        parts = [p for p in parts if p]  # Limpio strings vacíos

        for part in parts:
            if part == ".":
                continue
            elif part == "..":
                    if node.parent:
                        node = node.parent
            else:
                if part not in node.children:
                    print(f"{part} no existe")
                    return None

                node = node.children[part]

        return node

    # Retorna el directorio al que hace referencia una ruta especificada
    def get_current(self, path):
        current = self.resolve_path(path)

        if current is None:
            return

        if not isinstance(current, Directory):
            print(f"{current.name} no es un directorio")
            return

        return current

    def cd(self, path): # Este método acepta tanto rutas relativas como absolutas
        self.current = self.get_current(path) if self.get_current(path) is not None else self.current

    def touch(self, name):  # No soporta crear archivos pasando rutas como parámetro (no lo pedía)
        if not is_valid_name(name):
            print(f"Error: nombre inválido '{name}'. Usa solo letras, números, '_' o '-'.")
            return

        # En esta solución, no pueden coexistir archivos y directorios con el mismo nombre (no lo pedía)
        if name in self.current.children:
            print(f"Ya existe un archivo o directorio con el nombre {name}")
            return

        new_file = File(name, self.current)
        self.current.children[name] = new_file

    def mkdir(self, name):  # No soporta crear directorios pasando rutas como parámetro (no lo pedía)
        if not is_valid_name(name):
            print(f"Nombre inválido '{name}'")
            return

        # En esta solución, no pueden coexistir archivos y directorios con el mismo nombre (no lo pedía)
        if name in self.current.children:
            print(f"Ya existe un archivo o directorio con el nombre {name}")
            return

        new_dir = Directory(name, parent=self.current)
        self.current.children[name] = new_dir

    def ls(self, file_ref=None, recursive=False, depth=0, long_format=False):  # Este método soporta recursividad y búsqueda remota (listar archivos en un directorio que no sea el actual)
        target = file_ref if file_ref is not None else self.current

        for name, file in target.children.items():
            if long_format:
                print(f"{name} ({file.type()})")
            else:
                print(name)

            # Permito recursividad en el listado de archivos
            if recursive and isinstance(file, Directory):
                print("/" + "-" * depth + f"{name}")
                self.ls(file_ref=file, recursive=recursive, depth=depth + 1, long_format=long_format)

    def rm(self, file_ref, recursive=False, parent_ref=None):   # Este método soporta recursividad pero no búsqueda remota (eliminar un archivo que no sea hijo del actual)
        if file_ref is None:
            return

        parent = parent_ref if parent_ref is not None else self.current

        # No permito que se borre un archivo desde un directorio que no es su padre directo
        if file_ref.parent != parent:
            print(f"No se puede borrar un archivo de otro directorio")
            return

        if isinstance(file_ref, Directory):
            if not recursive and file_ref.children:
                print(f"{file_ref.name} es un directorio con contenido")
                return

            # Permito recursividad en el borrado de archivos
            for child in list(file_ref.children.values()):
                self.rm(file_ref=child, recursive=recursive, parent_ref=file_ref)

        parent.children.pop(file_ref.name, None)
        print(f"{file_ref.name} eliminado correctamente")

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