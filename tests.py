# tests.py (project root)

from functions.run_python_file import run_python_file


def print_result(label: str, result: str):
    print(label)
    print(result)
    print("-" * 60)


def main():
    # 1) Should print the calculator's usage instructions
    print_result(
        'run_python_file("calculator", "main.py")',
        run_python_file("calculator", "main.py")
    )

    # 2) Should run the calculator with a single CLI arg "3 + 5"
    #    (calculator/main.py joins argv[1:], so this works as intended)
    print_result(
        'run_python_file("calculator", "main.py", ["3 + 5"])',
        run_python_file("calculator", "main.py", ["3 + 5"])
    )

    # 3) Run the calculator test suite file
    print_result(
        'run_python_file("calculator", "tests.py")',
        run_python_file("calculator", "tests.py")
    )

    # 4) Outside working dir → error
    print_result(
        'run_python_file("calculator", "../main.py")',
        run_python_file("calculator", "../main.py")
    )

    # 5) Nonexistent file → error
    print_result(
        'run_python_file("calculator", "nonexistent.py")',
        run_python_file("calculator", "nonexistent.py")
    )

    # 6) Not a .py file → error
    print_result(
        'run_python_file("calculator", "lorem.txt")',
        run_python_file("calculator", "lorem.txt")
    )


if __name__ == "__main__":
    main()