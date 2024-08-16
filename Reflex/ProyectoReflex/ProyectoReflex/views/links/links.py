import reflex as rx
from ProyectoReflex.components.link_button import link_button
from ProyectoReflex.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twicht",
                    "Directos de lunes a viernes",
                    "https://google.com.ar"),
        link_button("YouTube",
                    "Videos semanales",
                    "https://google.com.ar"),
        link_button("Intagram",
                    "Info copada",
                    "https://google.com.ar"),
        link_button("Facebook",
                    "No se usa mas",
                    "https://google.com.ar"),
        title("Comunidad"),
        link_button("Twicht",
                    "Directos de lunes a viernes",
                    "https://google.com.ar"),
        link_button("YouTube",
                    "Videos semanales",
                    "https://google.com.ar"),
        link_button("Intagram",
                    "Info copada",
                    "https://google.com.ar"),
        link_button("Facebook",
                    "No se usa mas",
                    "https://google.com.ar"),
        width="100%"
    ),
    