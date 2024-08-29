import reflex as rx
import ProyectoReflex.styles.styles as styles


def link_button(title:str,body:str,url:str) -> rx.Component:
    return rx.link(
            rx.button(
                rx.hstack(
                    rx.icon(
                        tag="arrow-right",
                        width=styles.Size.DEFAULT.value,
                        height=styles.Size.DEFAULT.value,
                        margin=styles.Size.MEDIUM.value
                    ),
                    rx.vstack(
                        rx.text(title,style=styles.button_title_style),
                        rx.text(body,style=styles.button_body_style),
                        spacing=styles.Size.SMALL.value,
                        align_items="start",
                        margin=styles.Size.ZERO.value
                    )
                )
            ),
            href=url,
            is_external=True,
            width="100%"
    )


"""    return rx.link(
        rx.button(text, width="100%"),
        href=url,
        is_external=True,
        width="100%"
    )"""