import reflex as rx
from ProyectoReflex.styles.styles import Size as Size
import ProyectoReflex.styles.styles as styles
from ProyectoReflex.styles.colors import TextColor as TextColor
from ProyectoReflex.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text.strong("pablo",color=Color.PRIMARY.value),
            rx.text.strong("acalvo",color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )