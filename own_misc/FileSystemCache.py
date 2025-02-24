import numpy as np
import hashlib

class FileSystemCache():
    def __init__(self, fun, filename = "", args_hashed = True) -> None:
        self.fun = fun
        if len(filename) == 0:
            self.filename = fun.__name__
        else:
            self.filename = filename
        self.args_hashed = args_hashed
        self.dependencies = []
    
    def set_dependencies(self, *dependencies):
        self.dependencies = dependencies
        return self

    def execute(self, *arguments):
        filename = self.filename

        dependencies = self.dependencies
        if (self.args_hashed):
            dependencies = [*dependencies, *arguments]
        if len(dependencies):
            filename += f"_{str(hashlib.sha1(str(dependencies).encode()).hexdigest())}"
        filename += ".txt"
        try:
            pca = np.loadtxt(filename)
            print(f"Plik {filename} istnieje.")
        except:
            print(f"Plik {filename} nie istnieje.")
            pca = self.fun(*arguments)
            print(f"Nowy plik {filename}")
            np.savetxt(filename, pca)

        return pca

def testFunctions(x, y):
    return [1, 2, 3, 4, 5, 6, 7, 8] * (x + y) 

if __name__ == "__main__":
    c = FileSystemCache("./")
    a = c.execute(testFunctions, 3, 4)
