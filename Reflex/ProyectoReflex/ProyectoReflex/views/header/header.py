import reflex as rx
from ProyectoReflex.components.link_icon import link_icon

def header() -> rx.Component:
        return rx.vstack(
                rx.hstack(
                        rx.avatar(src="images/avatar1.jpg", size="xl"),
                        rx.vstack(
                                rx.heading(
                                        "Pablo Calvo",
                                        size="lg"
                                        ),
                                rx.text(
                                        "@pabloacalvo",
                                        margin_top="0px !important"
                                        ),
                                        rx.hstack(
                                                link_icon("https://google.com.ar"),
                                        ),
                                align_items="start"
                        )
                ),
                rx.text("""El parafraseo es un recurso que consiste en reformular un 
                        enunciado utilizando palabras diferentes, pero con un significado 
                        similar a las del enunciado original. Por ejemplo: El enunciado 
                        “El señor entró en su casa” se puede parafrasear en “El hombre ingresó en su hogar”.
                """),
                align_items="start"
        )

