def solucion_molona(cols: int) -> None:
    MAX = 255
    for i in range(0, MAX):
        if not (i % cols):
            print()

        code = f"{i}".rjust(len(f"{MAX}"))
        if i not in [7, 8, 9, 10, 13]:
            caracter = chr(i)
        else:
            caracter = ""

        print(code, ":", caracter, " ", end="")


if __name__ == "__main__":
    solucion_molona(8)
