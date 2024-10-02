import flet as ft

def to_do_app(page : ft.Page):

    def button_click(e):
        page.add(
            ft.Checkbox(label=input_text.value)
        )
        page.update()

    page.title = "To do App"

    input_text = ft.TextField(hint_text="What do you want to do, today?", width=300)

    # alliging the input text  and button on the same line
    page.add(
        ft.Row(
        controls= [
            input_text, ft.ElevatedButton(text= "Add task", on_click=button_click)
        ]
        )
    )
    page.update()

ft.app(target= to_do_app)