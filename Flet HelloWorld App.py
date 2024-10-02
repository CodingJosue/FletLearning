#import the library, import the entire library
import flet as ft # ft so that we dont have to type ft everytime its an alliace

# defining my main function
def hello_word(page : ft.Page):
    #setting up the title
    page.title = "Hello World"

    #flet text control
    text = ft.Text(value= "Hello World")

    #we need to append the text control to the pager and then update it
    page.add(text)
    page.update()




#we need to start the application
ft.app(target= hello_word)