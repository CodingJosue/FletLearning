import flet as ft
from  time import  sleep

def greeeting_app(page : ft.Page):
    page.title = "Greeting application"

    greeting_text = ft.Row()
    def hello_event(e):
        greeting_text.controls.append(ft.Text(f"HELLO {first_Name.value} {last_Name.value}"))
        page.update()


    first_Name = ft.TextField(label= "Enter your first name: ")
    last_Name = ft.TextField(label= "Enter your last name: ")
    hello_button = ft.ElevatedButton("Say hello?", on_click= hello_event)
    page.add(
        ft.Row(controls=[first_Name, last_Name, hello_button]
                  ),
        ft.Column(controls=[greeting_text])
    )
    page.update()


ft.app(target= greeeting_app)