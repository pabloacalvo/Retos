import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font

# Constants
MAX_WIDTH="600px"

# Sizes
class Size(Enum):
    ZERO="0px !important"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"


STYLESSHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css?family=Confortaa-Medium:wght@500&display=swap",
    "https://fonts.googleapis.com/css?family=New+Amsterdam:wght@400&display=swap",
    "https://fonts.googleapis.com/css?family=Playwrite+AR:wght@400&display=swap"

]

# Styles
BASE_STYLE={
    "background_color":Color.BACKGROUND.value,
    "font_family":Font.DEFAULT.value,
    rx.heading:{
        "color":TextColor.HEADER.value,
        "font":Font.TITLE.value

    },
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "color":TextColor.HEADER.value,
        "background_color":Color.CONTENT.value,
        "_hover":{
            "background_color":Color.SECONDARY.value
        }
    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
    }
}

title_style = dict(
        size="md",
        width="100%",
        padding_top=Size.DEFAULT.value,
)

button_title_style = dict (
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict (
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value
)