""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
import poke_api
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Pokemon Information")

# TODO: Create the frames
firstframe = Frame(root)
firstframe.grid(row=0,column=0, columnspan=1, padx=20, pady=20)

Secondframe = LabelFrame(root, text="info")
Secondframe.grid(row=1,column=0,padx=20, pady=20)

Thirdframe= LabelFrame(root, text="stat")
Thirdframe.grid(row=1,column=1,padx=20, pady=20)
#Functions

def display_pokemon_info(pokeinfo):
    hvalue['text'] = f"{pokeinfo['height']} dm"
    wvalue['text'] = f"{pokeinfo['weight']} hg"

    # Extract and join Pokémon types
    types = [type_info['type']['name'] for type_info in pokeinfo['types']]
    tvalue['text'] = ", ".join(types)

    # Update stats
    stats = pokeinfo['stats']
    HP_Progressbar['value'] = stats[0]['base_stat']
    attack_Progressbar['value'] = stats[1]['base_stat']
    defence_Progressbar['value'] = stats[2]['base_stat']
    special_attack_Progressbar['value'] = stats[3]['base_stat']
    special_defence_Progressbar['value'] = stats[4]['base_stat']
    speed_Progressbar['value'] = stats[5]['base_stat']

def show_error_message():
    val = Secondlabel.get()
    lowercase_value = val.lower()
    capitalize_val = lowercase_value.capitalize()
    messagebox.showerror(message=f'Unable to fetch information for {capitalize_val} from the PokeAPI',icon='error',title='Error')

# TODO: Define button click event handler function
def handle_button_click():
    pokename = Secondlabel.get()
    pokeinfo = poke_api.get_pokemon_info(pokename)
    if pokeinfo == None:
      show_error_message()
    else:
      display_pokemon_info(pokeinfo)



# TODO: Populate the user input frame with widgets

firstlabel = Label(firstframe,text="Pokemon Name")
firstlabel.grid(row=0,column=0, padx=5, pady=5)

Secondlabel= Entry(firstframe)
Secondlabel.grid(row=0,column=1, padx=5, pady=5)

Thirdlabel = Button(firstframe,text="Get info",command = handle_button_click)
Thirdlabel.grid(row=0,column=2, padx=5, pady=5)

#widget for "info_frame"

hlbl = Label(Secondframe,text="Height")
hlbl.grid(row=0,column=0, padx=5, pady=5, sticky="E")
wlbl = Label(Secondframe,text="Weight")
wlbl.grid(row=1,column=0, padx=5, pady=5, sticky="E")
tlbl = Label(Secondframe,text="Type")
tlbl.grid(row=2,column=0, padx=5, pady=5, sticky="E")

hvalue = Label(Secondframe)
hvalue.grid(row=0,column=2, padx=5, pady=5, sticky="E")
wvalue = Label(Secondframe)
wvalue.grid(row=1,column=2, padx=5, pady=5, sticky="E")
tvalue = Label(Secondframe)
tvalue.grid(row=2,column=2, padx=5, pady=5, sticky="E")

#Stat-Frames widgets

hp = Label( Thirdframe,text="HP:")
hp.grid(row=0,column=2, padx=5, pady=5, sticky="E")

attack = Label(Thirdframe,text="Attack:")
attack.grid(row=1,column=2, padx=5, pady=5, sticky="E")

defense = Label(Thirdframe,text="Defence:")
defense.grid(row=2,column=2, padx=5, pady=5, sticky="E")

specialAttack = Label(Thirdframe,text="Special Attack:")
specialAttack.grid(row=3,column=2, padx=5, pady=5, sticky="E")

specialDefence = Label(Thirdframe,text="Special Defence:")
specialDefence.grid(row=4,column=2, padx=5, pady=5, sticky="E")

speed= Label(Thirdframe,text="Speed:")
speed.grid(row=5,column=2, padx=5, pady=5, sticky="E")

#Progress-Bar for stat-Frames widgets

HP_Progressbar = ttk.Progressbar(Thirdframe, length=200, max=250)
HP_Progressbar.grid(row=0,column=3, padx=5, pady=5)

attack_Progressbar = ttk.Progressbar(Thirdframe, length=200, max=250)
attack_Progressbar.grid(row=1,column=3, padx=5, pady=5)

defence_Progressbar = ttk.Progressbar(Thirdframe, length=200, max=250)
defence_Progressbar.grid(row=2,column=3, padx=5, pady=5)

special_attack_Progressbar = ttk.Progressbar(Thirdframe, length=200, max=250)
special_attack_Progressbar.grid(row=3,column=3, padx=5, pady=5)

special_defence_Progressbar = ttk.Progressbar(Thirdframe, length=200, max=250)
special_defence_Progressbar.grid(row=4,column=3, padx=5, pady=5)

speed_Progressbar = ttk.Progressbar(Thirdframe, length=200, max=250)
speed_Progressbar.grid(row=5,column=3, padx=5, pady=5)

root.mainloop()