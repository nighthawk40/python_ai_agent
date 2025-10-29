from functions.get_files_info import get_files_info

def print_result(title: str, output: str) -> None:
    """
    Print a section header and the tool output with the formatting 
    the assignment expects. Indent errors differently.
    """
    print(title)
    if output.startswith("Error:"):
        # Indent error block by 4 spaces
        print("    " + output)
    else: 
        # Each line in successful output gets a leading space before the dash
        for line in output.splitlines():
            print(" " + line)
    print() # Blank line between sections


def main() -> None:
    # 1) Current directory inside calculator
    out = get_files_info("calculator", ".")
    print_result("Result for current directory:", out)

    # 2) The 'pkg' directory 
    out = get_files_info("calculator", "pkg")
    print_result("Result for 'pkg' directory:", out)

    # 3) Absolute path outside working directory
    out = get_files_info("calculator", "/bin")
    print_result("Result for '/bin' directory:", out)

    # 4) Relative traversal outside working directory
    out = get_files_info("calculator", "../")
    print_result("Result for \'../\' direcotory:", out)

if __name__ == "__main__":
    main()