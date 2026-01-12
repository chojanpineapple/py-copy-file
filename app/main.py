import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source = parts[1]
    target = parts[2]

    if source == target:
        return

    if not os.path.isfile(source):
        return
        
    with open(source, "r") as src:
        content = src.read()

    with open(target, "w") as dst:
        dst.write(content)
