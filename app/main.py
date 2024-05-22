def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        text += content + "\n"
    with open(file_name + ".txt", "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()
