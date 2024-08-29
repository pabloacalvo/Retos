import reflex as rx
from ProyectoReflex.components.link_icon import link_icon
from ProyectoReflex.components.info_text import info_text
from ProyectoReflex.styles.styles import Size as Size
from ProyectoReflex.styles.colors import TextColor as TextColor
from ProyectoReflex.styles.colors import Color as Color
from ProyectoReflex.styles.fonts import Font as Font


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="avatar1.jpg",
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                    rx.heading(
                        "Pablo Calvo",
                        size="lg",
                        color=TextColor.HEADER.value,
                        font_family=Font.TITLE.value
                    ),
                    rx.text(
                        "@pabloacalvo",
                        margin_top=Size.ZERO.value,
                        color=TextColor.BODY.value,
                        font_family=Font.SUBTITLE.value
                    ),
                    rx.hstack(
                        link_icon("https://google.com.ar"),
                    ),
                    align_items="start"
            ),
            spacing=Size.BIG.value
        ),
        rx.flex(
            info_text("+13", "Años de experiencia"),
            rx.spacer(),
            info_text("+13", "Años de experiencia"),
            rx.spacer(),
            info_text("+13", "Años de experiencia"),
            width="100%"
		),
        rx.text("""El parafraseo es un recurso que consiste en reformular un 
            enunciado utilizando palabras diferentes, pero con un significado 
            similar a las del enunciado original. Por ejemplo: El enunciado 
            “El señor entró en su casa” se puede parafrasear en “El hombre ingresó en su hogar”.
        """,
        color=TextColor.BODY.value
        ),
        align_items="start",
        spacing=Size.BIG.value
    )

