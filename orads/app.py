"""O-RADS Toga GUI Application.

A cross-platform decision tree application for O-RADS ultrasound scoring.
"""

import toga
from toga.style import Pack
from toga.style.pack import BOLD, CENTER, COLUMN, LEFT, ROW

from .decision_tree import DecisionTreeNavigator, ORADSResult

# Color palette - Medical/clinical aesthetic
COLORS = {
    "background": "#0d1117",
    "surface": "#161b22",
    "surface_elevated": "#21262d",
    "border": "#30363d",
    "text_primary": "#f0f6fc",
    "text_secondary": "#8b949e",
    "text_muted": "#6e7681",
    "accent": "#58a6ff",
    "accent_hover": "#79c0ff",
    "orads_0": "#6e7681",  # Gray - Incomplete
    "orads_1": "#238636",  # Green - Normal
    "orads_2": "#3fb950",  # Light Green - Almost Certainly Benign
    "orads_3": "#d29922",  # Yellow/Gold - Low Risk
    "orads_4": "#db6d28",  # Orange - Intermediate Risk
    "orads_5": "#f85149",  # Red - High Risk
}


def get_orads_color(score: int) -> str:
    """Get the color for an O-RADS score."""
    return COLORS.get(f"orads_{score}", COLORS["accent"])


class ORADSApp(toga.App):
    """Main O-RADS Decision Tree Application."""

    def __init__(self):
        super().__init__(
            formal_name="O-RADS Decision Tree",
            app_id="com.orads.decisiontree",
            app_name="orads",
        )
        self.navigator = DecisionTreeNavigator()
        self._result: ORADSResult | None = None

    def startup(self):
        """Build the main application window."""
        self.main_window = toga.MainWindow(
            title="O-RADS Ultrasound Decision Tree",
            size=(600, 700),
        )

        # Main container
        self.main_box = toga.Box(
            style=Pack(
                direction=COLUMN,
                margin=20,
                background_color=COLORS["background"],
                flex=1,
            )
        )

        # Header
        self._build_header()

        # Content area (question or result)
        self.content_box = toga.Box(
            style=Pack(
                direction=COLUMN,
                flex=1,
                margin_top=20,
            )
        )
        self.main_box.add(self.content_box)

        # Navigation buttons
        self._build_navigation()

        # Show the first question
        self._show_current_question()

        self.main_window.content = self.main_box
        self.main_window.show()

    def _build_header(self):
        """Build the header section with title and breadcrumbs."""
        header_box = toga.Box(
            style=Pack(
                direction=COLUMN,
                margin_bottom=10,
            )
        )

        # Title
        title = toga.Label(
            "O-RADS Scoring Application",
            style=Pack(
                font_size=24,
                font_weight=BOLD,
                color=COLORS["text_primary"],
                margin_bottom=5,
                text_align=CENTER,
            ),
        )
        header_box.add(title)

        # Subtitle
        subtitle = toga.Label(
            "Decision flow:",
            style=Pack(
                font_size=14,
                color=COLORS["text_secondary"],
                margin_bottom=10,
            ),
        )
        header_box.add(subtitle)

        # Breadcrumb container
        self.breadcrumb_label = toga.Label(
            "",
            style=Pack(
                font_size=11,
                color=COLORS["text_muted"],
            ),
        )
        header_box.add(self.breadcrumb_label)

        self.main_box.add(header_box)

    def _build_navigation(self):
        """Build the bottom navigation buttons."""
        nav_box = toga.Box(
            style=Pack(
                direction=ROW,
                margin_top=20,
            )
        )

        self.back_button = toga.Button(
            "← Back",
            on_press=self._on_back,
            style=Pack(
                margin=10,
                width=100,
                background_color=COLORS["surface_elevated"],
                color=COLORS["text_primary"],
            ),
        )
        nav_box.add(self.back_button)

        # Spacer
        spacer = toga.Box(style=Pack(flex=1))
        nav_box.add(spacer)

        self.reset_button = toga.Button(
            "Start Over",
            on_press=self._on_reset,
            style=Pack(
                margin=10,
                width=100,
                background_color=COLORS["surface_elevated"],
                color=COLORS["text_primary"],
            ),
        )
        nav_box.add(self.reset_button)

        self.main_box.add(nav_box)

    def _update_breadcrumbs(self):
        """Update the breadcrumb trail."""
        crumbs = self.navigator.get_breadcrumbs()
        if crumbs:
            path = " → ".join(crumbs[-3:])  # Show last 3 to avoid overflow
            if len(crumbs) > 3:
                path = "... → " + path
            self.breadcrumb_label.text = path
        else:
            self.breadcrumb_label.text = "Start"

    def _show_current_question(self):
        """Display the current decision node question and options."""
        self._result = None

        # Clear existing content
        self.content_box.clear()

        node = self.navigator.current_node

        # Question label
        question_label = toga.Label(
            node.question or "What do you see?",
            style=Pack(
                font_size=18,
                font_weight=BOLD,
                color=COLORS["text_primary"],
                margin_bottom=20,
            ),
        )
        self.content_box.add(question_label)

        # Options container with scroll
        options_scroll = toga.ScrollContainer(
            style=Pack(flex=1),
            horizontal=False,
        )

        options_box = toga.Box(
            style=Pack(
                direction=COLUMN,
            )
        )

        for i, option in enumerate(node.options):
            btn = self._create_option_button(i, option.label, option.description)
            options_box.add(btn)

        options_scroll.content = options_box
        self.content_box.add(options_scroll)

        self._update_breadcrumbs()
        self._update_navigation_state()

    def _create_option_button(
        self, index: int, label: str, description: str = ""
    ) -> toga.Box:
        """Create a styled option button with description."""
        outer = toga.Box(
            style=Pack(
                direction=COLUMN,
                margin_bottom=10,
            )
        )

        # Create the actual button
        btn_text = f"{index + 1}. {label}"
        if description:
            btn_text += f"\n     {description}"

        actual_btn = toga.Button(
            btn_text,
            on_press=lambda w, idx=index: self._on_option_select(idx),
            style=Pack(
                margin=5,
                background_color=COLORS["surface"],
                color=COLORS["text_primary"],
                text_align=LEFT,
            ),
        )
        outer.add(actual_btn)

        return outer

    def _on_option_select(self, index: int):
        """Handle option selection."""
        result = self.navigator.select_option(index)

        if result is not None:
            self._show_result(result)
        else:
            self._show_current_question()

    def _show_result(self, result: ORADSResult):
        """Display the final O-RADS result."""
        self._result = result

        # Clear existing content
        self.content_box.clear()

        score_color = get_orads_color(result.score)

        # Result container with scroll
        result_scroll = toga.ScrollContainer(
            style=Pack(flex=1),
            horizontal=False,
        )

        result_box = toga.Box(
            style=Pack(
                direction=COLUMN,
                margin=10,
            )
        )

        # Score header
        score_box = toga.Box(
            style=Pack(
                direction=COLUMN,
                margin=20,
                background_color=COLORS["surface"],
            )
        )

        score_label = toga.Label(
            f"O-RADS {result.score}",
            style=Pack(
                font_size=36,
                font_weight=BOLD,
                color=score_color,
                text_align=CENTER,
            ),
        )
        score_box.add(score_label)

        category_label = toga.Label(
            result.category,
            style=Pack(
                font_size=18,
                color=COLORS["text_primary"],
                text_align=CENTER,
                margin_top=5,
            ),
        )
        score_box.add(category_label)

        if result.risk != "N/A":
            risk_label = toga.Label(
                f"Malignancy Risk: {result.risk}",
                style=Pack(
                    font_size=14,
                    color=COLORS["text_secondary"],
                    text_align=CENTER,
                    margin_top=5,
                ),
            )
            score_box.add(risk_label)

        result_box.add(score_box)

        # Spacer
        result_box.add(toga.Box(style=Pack(height=20)))

        # Description section
        self._add_result_section(result_box, "Description", result.description)

        # Management section
        self._add_result_section(result_box, "Management", result.management)

        # Imaging Follow-up
        if result.imaging_followup:
            self._add_result_section(
                result_box, "Imaging Follow-up", result.imaging_followup
            )

        # Clinical Follow-up
        if result.clinical_followup:
            self._add_result_section(
                result_box, "Clinical Follow-up", result.clinical_followup
            )

        result_scroll.content = result_box
        self.content_box.add(result_scroll)

        self._update_breadcrumbs()
        self._update_navigation_state()

    def _add_result_section(self, container: toga.Box, title: str, content: str):
        """Add a labeled section to the result display."""
        section = toga.Box(
            style=Pack(
                direction=COLUMN,
                margin=15,
                margin_top=10,
                margin_bottom=10,
                background_color=COLORS["surface"],
            )
        )

        title_label = toga.Label(
            title,
            style=Pack(
                font_size=12,
                font_weight=BOLD,
                color=COLORS["text_muted"],
                margin_bottom=5,
            ),
        )
        section.add(title_label)

        content_label = toga.Label(
            content,
            style=Pack(
                font_size=14,
                color=COLORS["text_primary"],
            ),
        )
        section.add(content_label)

        container.add(section)
        container.add(toga.Box(style=Pack(height=10)))

    def _on_back(self, widget):
        """Handle back button press."""
        if self._result is not None:
            # If showing result, go back to last question
            self.navigator.go_back()
            self._show_current_question()
        elif self.navigator.go_back():
            self._show_current_question()

    def _on_reset(self, widget):
        """Handle reset button press."""
        self.navigator.reset()
        self._show_current_question()

    def _update_navigation_state(self):
        """Update the enabled state of navigation buttons."""
        has_history = len(self.navigator.history) > 0 or self._result is not None
        self.back_button.enabled = has_history


def main():
    """Entry point for the GUI application."""
    return ORADSApp()


if __name__ == "__main__":
    app = main()
    app.main_loop()
