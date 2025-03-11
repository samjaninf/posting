from posting.help_data import HelpData

from posting.widgets.text_area import PostingTextArea


class RequestBodyTextArea(PostingTextArea):
    """
    For editing request bodies.
    """

    BINDING_GROUP_TITLE = "Request Body Text Area"

    help = HelpData(
        title="Request Body Text Area",
        description="""\
A text area for entering the request body.
Press `ESC` to focus the text area footer bar.

Hold `shift` and move the cursor or click and drag to select text.
""",
    )

    def on_mount(self):
        self.tab_behavior = "indent"
        self.show_line_numbers = True
