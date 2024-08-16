import reflex as rx
from ProyectoReflex.components.navbar import navbar
from ProyectoReflex.components.footer import footer
from ProyectoReflex.views.header.header import header
from ProyectoReflex.views.links.links import links
import ProyectoReflex.styles.styles as styles
from ProyectoReflex.styles.styles import Size as Size

class State(rx.State):
    pass


def index():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                width="100%",
                margin_top="10px",
                max_width=styles.MAX_WIDTH,
                margin_bottom=Size.BIG.value
            )
        ),
        rx.center(
            footer()
        ) 
    )


    
    


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
