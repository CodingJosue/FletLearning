import random

import  flet as ft

def counter_app(page : ft.Page):
    current_value = ft.TextField(value= "0", width= 200)
    value_color = ft.colors.WHITE

    page.title = "CounterApp"
    def randomColor():
        value = random.randint(0,200)
        return ft.colors.colors_list[value]
    def increment(e):
        plus_button.icon_color = randomColor()
        new_value =str(int(current_value.value) + 1)
        current_value.value = new_value
        page.update()



    def decrement(e):
        minus_button.icon_color= randomColor()
        new_value = str(int(current_value.value) - 1)
        current_value.value = new_value
        page.update()


    plus_button = ft.IconButton(icon= ft.icons.ADD,on_click= increment, icon_color= value_color )
    minus_button = ft.IconButton(icon= ft.icons.REMOVE,on_click= decrement, icon_color= value_color)

    page.add(
        ft.Row(controls=[minus_button, current_value, plus_button], alignment="center")
        )
    page.update()


ft.app(target=counter_app)
