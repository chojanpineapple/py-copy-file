import os


def copy_file(command: str) -> None:
    parts = command.split()
    validador = True

    if len(parts) != 3 or parts[0] != "cp":
        validador = False
        return

    source = parts[1]
    target = parts[2]

    if source == target:
        validador = False
        return

    if not os.path.isfile(source):
        validador = False
        return
    
    if validador:
        with open(source, "r") as src:
            content = src.read()

        with open(target, "w") as dst:
            dst.write(content)
