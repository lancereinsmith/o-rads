"""O-RADS Decision Tree Application.

This module provides both CLI and GUI interfaces for navigating
the O-RADS ultrasound decision tree.
"""

import sys


def main():
    """Main entry point - launches CLI by default."""
    from orads.cli import main as cli_main

    cli_main()


def gui():
    """Launch the GUI application."""
    from orads.app import main as app_main

    app = app_main()
    app.main_loop()


if __name__ == "__main__":
    # Check for --gui flag
    if len(sys.argv) > 1 and sys.argv[1] in ("--gui", "-g"):
        gui()
    else:
        main()
