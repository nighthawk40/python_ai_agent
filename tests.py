# tests.py (project root)

from functions.write_file import write_file


def print_result(label: str, result: str):
    print(label)
    if result.startswith("Error:"):
        print("    " + result)   # indent error messages
    else:
        print(" " + result)      # indent success message
    print()  # blank line


def main():
    # 1) Overwrite existing lorem.txt
    print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
    out = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print_result("Result for overwriting lorem.txt:", out)

    # 2) Create new file in nested directory
    print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
    out = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print_result("Result for writing pkg/morelorem.txt:", out)

    # 3) Attempt to write outside working directory → should be blocked
    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
    out = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print_result("Result for /tmp/temp.txt:", out)


if __name__ == "__main__":
    main()