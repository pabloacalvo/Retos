import reflex as rx
import datetime
from ProyectoReflex.styles.styles import Size as Size
from ProyectoReflex.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico"),
        rx.link(
            f"2022-{datetime.date.today().year} PABLO CALVO BY PABLOACALVO",
            href="https://google.com.ar",
            is_external=True,
            font_size=Size.MEDIUM.value,
        ),
        rx.text(
            "FROM LANUS TO THE WORLD",
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )