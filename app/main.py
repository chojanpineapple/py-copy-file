def copy_file(command: str) -> None:
    files = command.split()

    if len(files) != 3 or files[0] != "cp":
        print("Comando inválido")
        return

    file1 = files[1]
    file2 = files[2]

    try:
        with open(file1, "r") as f1, open(file2, "w") as f2:
            f2.write(f1.read())
    except FileNotFoundError:
        print("Error: el archivo origen no existe")
    except Exception as e:
        print("Error:", e)
