import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source = parts[1]
    target = parts[2]

    if not os.path.exists(source):
        print("Error: el archivo origen no existe")
        return

    with open(source, "r") as src:
        content = src.read()

    with open(target, "w") as dst:
        dst.write(content)
