import flet as ft

def fruitsNcricketer(page : ft.Page):
    page.add(
        ft.Row(controls=[ft.Text("My favarite fruits:\n")]),

        ft.Row(controls= [ft.Text("Apple\nBanana\nGrapes")])

    )


ft.app(target= fruitsNcricketer)