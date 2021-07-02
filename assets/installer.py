import platform
import webbrowser

OS = platform.system()

def move():
    input("Press [Enter] to Exit!!")
    quit()

if OS=="Windows":
    webbrowser.open("")

elif OS=="Linux":
    webbrowser.open("")

elif OS=="Darwin":
    webbrowser.open("")
    
else:
    print("What OS Are You On??")
    move()
