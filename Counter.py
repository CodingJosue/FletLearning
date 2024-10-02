import flet as ft
from  time import  sleep
def counter_App(page: ft.Page):

    page.title = "Counter application"

    text = ft.Text()
    page.add(text)

    for i in range(1, 11):
        text.value = "Counter at " +  str(i)
        page.update()
        sleep(1)



ft.app(target= counter_App)