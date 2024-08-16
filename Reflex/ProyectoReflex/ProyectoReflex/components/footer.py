import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico"),
        rx.link(f"2022-{datetime.date.today().year} PABLO CALVO BY PABLOACALVO",href="https://google.com.ar"),
        rx.text("FROM LANUS TO THE WORLD")
    )