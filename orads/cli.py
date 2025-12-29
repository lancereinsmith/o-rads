"""O-RADS CLI Application.

A terminal-based decision tree for O-RADS ultrasound scoring.
"""

import sys

from .decision_tree import DecisionTreeNavigator, ORADSResult


# ANSI color codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    # O-RADS score colors
    GRAY = "\033[90m"  # O-RADS 0
    GREEN = "\033[92m"  # O-RADS 1
    LIME = "\033[32m"  # O-RADS 2
    YELLOW = "\033[93m"  # O-RADS 3
    ORANGE = "\033[33m"  # O-RADS 4
    RED = "\033[91m"  # O-RADS 5

    CYAN = "\033[96m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"


def get_score_color(score: int) -> str:
    """Get color code for O-RADS score."""
    colors = {
        0: Colors.GRAY,
        1: Colors.GREEN,
        2: Colors.LIME,
        3: Colors.YELLOW,
        4: Colors.ORANGE,
        5: Colors.RED,
    }
    return colors.get(score, Colors.WHITE)


def clear_screen():
    """Clear the terminal screen."""
    print("\033[2J\033[H", end="")


def print_header():
    """Print the application header."""
    print(f"\n{Colors.CYAN}{Colors.BOLD}╔{'═' * 58}╗{Colors.RESET}")
    print(
        f"{Colors.CYAN}{Colors.BOLD}║{'O-RADS Ultrasound Decision Tree':^58}║{Colors.RESET}"
    )
    print(
        f"{Colors.CYAN}{Colors.BOLD}║{'Risk Stratification for Adnexal Lesions':^58}║{Colors.RESET}"
    )
    print(f"{Colors.CYAN}{Colors.BOLD}╚{'═' * 58}╝{Colors.RESET}\n")


def print_question(navigator: DecisionTreeNavigator):
    """Print the current question and options."""
    node = navigator.current_node

    # Show breadcrumbs
    crumbs = navigator.get_breadcrumbs()
    if crumbs:
        path = " → ".join(crumbs[-3:])
        if len(crumbs) > 3:
            path = "... → " + path
        print(f"{Colors.DIM}{path}{Colors.RESET}\n")

    # Print question
    print(f"{Colors.WHITE}{Colors.BOLD}{node.question}{Colors.RESET}\n")

    # Print options
    for i, option in enumerate(node.options, 1):
        print(f"  {Colors.CYAN}{Colors.BOLD}[{i}]{Colors.RESET} {option.label}")
        if option.description:
            print(f"      {Colors.DIM}{option.description}{Colors.RESET}")

    print()
    print(f"  {Colors.DIM}[B] Back  [R] Reset  [Q] Quit{Colors.RESET}")
    print()


def print_result(result: ORADSResult):
    """Print the final O-RADS result."""
    color = get_score_color(result.score)

    print(f"\n{color}╔{'═' * 58}╗{Colors.RESET}")
    print(
        f"{color}║{Colors.BOLD}{f'O-RADS {result.score}':^58}{Colors.RESET}{color}║{Colors.RESET}"
    )
    print(f"{color}╠{'═' * 58}╣{Colors.RESET}")
    print(f"{color}║{result.category:^58}║{Colors.RESET}")
    if result.risk != "N/A":
        print(f"{color}║{f'Malignancy Risk: {result.risk}':^58}║{Colors.RESET}")
    print(f"{color}╚{'═' * 58}╝{Colors.RESET}")

    print(f"\n{Colors.BOLD}Description:{Colors.RESET}")
    print(f"  {result.description}")

    print(f"\n{Colors.BOLD}Management:{Colors.RESET}")
    print(f"  {result.management}")

    if result.imaging_followup:
        print(f"\n{Colors.BOLD}Imaging Follow-up:{Colors.RESET}")
        print(f"  {result.imaging_followup}")

    if result.clinical_followup:
        print(f"\n{Colors.BOLD}Clinical Follow-up:{Colors.RESET}")
        print(f"  {result.clinical_followup}")

    print()


def get_input(prompt: str = "Select: ") -> str:
    """Get user input with prompt."""
    try:
        return input(f"{Colors.CYAN}{prompt}{Colors.RESET}").strip().lower()
    except EOFError:
        return "q"
    except KeyboardInterrupt:
        print()
        return "q"


def main():
    """Main CLI entry point."""
    navigator = DecisionTreeNavigator()

    while True:
        clear_screen()
        print_header()
        print_question(navigator)

        choice = get_input()

        if choice == "q":
            print(f"\n{Colors.DIM}Goodbye!{Colors.RESET}\n")
            sys.exit(0)

        if choice == "r":
            navigator.reset()
            continue

        if choice == "b":
            navigator.go_back()
            continue

        # Try to parse as option number
        try:
            option_idx = int(choice) - 1
            if 0 <= option_idx < len(navigator.current_node.options):
                result = navigator.select_option(option_idx)

                if result is not None:
                    clear_screen()
                    print_header()
                    print_result(result)

                    print(
                        f"  {Colors.DIM}[B] Back  [R] Start Over  [Q] Quit{Colors.RESET}"
                    )
                    print()

                    while True:
                        next_choice = get_input("What next? ")
                        if next_choice == "q":
                            print(f"\n{Colors.DIM}Goodbye!{Colors.RESET}\n")
                            sys.exit(0)
                        if next_choice == "r":
                            navigator.reset()
                            break
                        if next_choice == "b":
                            navigator.go_back()
                            break
                        print(
                            f"{Colors.RED}Invalid choice. Press B, R, or Q.{Colors.RESET}"
                        )
            else:
                continue  # Invalid option, just refresh
        except ValueError:
            continue  # Not a number, just refresh


if __name__ == "__main__":
    main()
