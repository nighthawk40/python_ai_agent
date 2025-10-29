# tests.py (project root)

from functions.get_file_content import get_file_content


def print_block(title: str, output: str) -> None:
    print(title)
    if output.startswith("Error:"):
        # Indent error messages per prior convention
        print("    " + output)
    else:
        # Indent file contents for readability
        for line in output.splitlines():
            print(" " + line)
    print()  # blank line between sections


def main() -> None:
    # 1) calculator/main.py
    print('get_file_content("calculator", "main.py")')
    out = get_file_content("calculator", "main.py")
    print_block("Result for 'main.py':", out)

    # 2) calculator/pkg/calculator.py
    print('get_file_content("calculator", "pkg/calculator.py")')
    out = get_file_content("calculator", "pkg/calculator.py")
    print_block("Result for 'pkg/calculator.py':", out)

    # 3) absolute path outside working dir → should be an error
    print('get_file_content("calculator", "/bin/cat")')
    out = get_file_content("calculator", "/bin/cat")
    print_block("Result for '/bin/cat':", out)

    # 4) missing file inside working dir → should be an error
    print('get_file_content("calculator", "pkg/does_not_exist.py")')
    out = get_file_content("calculator", "pkg/does_not_exist.py")
    print_block("Result for 'pkg/does_not_exist.py':", out)


if __name__ == "__main__":
    main()