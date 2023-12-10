def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode="w") as file:
        write_data = file.write(file_content)
        return write_data


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a") as file:
        append_data = file.write(append_content)
        return append_data
def read_file(file_name):
    with open(f"{file_name}.txt", encoding="utf-8") as file:
        read_data = file.read()
        return read_data