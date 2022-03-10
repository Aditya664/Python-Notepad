import tkinter as tk
from tkinter import ttk,Menu
from tkinter import font,colorchooser,filedialog,messagebox
import os


main_app = tk.Tk()
main_app.geometry('1200x800')
main_app.title('Codepad text editor created by Aditya.')
######################################################################################################
#                                         Main menu Start                                            #            
######################################################################################################

main_menu = tk.Menu()
# File
new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
saveas_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")
file = tk.Menu(main_menu,tearoff=False)
# Edit
copy_icon = tk.PhotoImage(file = "icons2/copy.png")
paste_icon = tk.PhotoImage(file = "icons2/paste.png")
cut_icon = tk.PhotoImage(file = "icons2/cut.png")
clr_icon = tk.PhotoImage(file = "icons2/clear_all.png")
find_icon = tk.PhotoImage(file = "icons2/find.png")
edit = tk.Menu(main_menu,tearoff=False)
# View
toolbar_icon = tk.PhotoImage(file = "icons2/tool_bar.png")
statusbar_icon = tk.PhotoImage(file = "icons2/status_bar.png")
view = tk.Menu(main_menu,tearoff=False)
# Color Theme
light_default_icon = tk.PhotoImage(file = "icons2/light_default.png")
light_plus_icon = tk.PhotoImage(file = "icons2/light_plus.png")
dark_icon = tk.PhotoImage(file="icons2/dark.png")
color = tk.Menu(main_menu,tearoff=False)
theme_choosed = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon)
color_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d')
}
# cascade
main_menu.add_cascade(
    label="File",
    menu=file,
    underline=0
)
main_menu.add_cascade(
    label="Edit",
    menu=edit,
    underline=0
)
main_menu.add_cascade(
    label="View",
    menu=view,
    underline=0
)
main_menu.add_cascade(
    label="Color Theme",
    menu=color,
    underline=0
)
######################################################################################################
#                                         Main Menu End                                              #            
######################################################################################################

######################################################################################################
#                                         Main menu Funct                                            #            
######################################################################################################


## File Commands
file.add_command(label='New', image = new_icon,compound = tk.LEFT,accelerator = 'Ctrl+n')
file.add_command(label='Open', image = open_icon,compound = tk.LEFT,accelerator = 'Ctrl+o')
file.add_command(label='Save', image = save_icon,compound = tk.LEFT,accelerator = 'Ctrl+s')
file.add_command(label='Save as', image = saveas_icon,compound = tk.LEFT,accelerator = 'Ctrl+Alt+s')
file.add_command(label='Exit', image = exit_icon,compound = tk.LEFT,accelerator = 'Ctrl+e')
## Edit Commands
edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+c')
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+p')
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit.add_command(label="Clear All",image=clr_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+x')
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator='Ctrl+f')
## View Commands
view.add_checkbutton(label = "Toolbar",image=toolbar_icon,compound=tk.LEFT)
view.add_checkbutton(label = "Statusbar",image=statusbar_icon,compound=tk.LEFT)
## Color Theme 
count = 0
for i in color_dict:
    color.add_radiobutton(label = i,image = color_icons[count],variable = theme_choosed,compound = tk.LEFT)
    count += 1;    
######################################################################################################
#                                                                                                    #            
######################################################################################################


######################################################################################################
#                                         Toolbar Start                                              #           
######################################################################################################

toolbar = ttk.Label(main_app)
toolbar.pack(side = tk.TOP,fill = tk.X)

## Font box
fonts = tk.font.families();
font_family = tk.StringVar();
font_box = ttk.Combobox(toolbar,width = 30,textvariable = font_family,state="readonly");
font_box['values'] = fonts
font_box.current(fonts.index("Arial"))
font_box.grid(row = 0,column = 0 ,padx = 5)

## Size box
size = tk.IntVar();
size_box = ttk.Combobox(toolbar,width = 14,textvariable = size,state="readonly")
size_box['values'] = tuple(range(8,81))
size_box.current(4)
size_box.grid(row = 0,column = 1,padx = 5)
## Bold Button
bold_icon = tk.PhotoImage(file = "icons2/bold.png")
bold_btn = ttk.Button(toolbar,image = bold_icon)
bold_btn.grid(row = 0,column = 2,padx = 5)
## Italic Button
italic_icon = tk.PhotoImage(file = "icons2/italic.png")
italic_btn = ttk.Button(toolbar,image = italic_icon)
italic_btn.grid(row = 0,column = 3,padx = 5)
## Underline icon
underline_icon = tk.PhotoImage(file = "icons2/underline.png")
underline_btn = ttk.Button(toolbar,image = underline_icon)
underline_btn.grid(row = 0,column = 4,padx = 5)
## Font Color Button
font_color_icon = tk.PhotoImage(file = "icons2/font_color.png")
font_color_btn = ttk.Button(toolbar,image = font_color_icon)
font_color_btn.grid(row = 0,column = 5,padx = 5)
## Aligne Left Button
align_left_icon = tk.PhotoImage(file = "icons2/align_left.png")
align_left_btn = ttk.Button(toolbar,image = align_left_icon)
align_left_btn.grid(row = 0,column = 6 , padx = 5)
## Aligne Center Button
align_center_icon = tk.PhotoImage(file = "icons2/align_center.png")
align_center_btn = ttk.Button(toolbar,image = align_center_icon)
align_center_btn.grid(row = 0,column = 7 , padx = 5)
## Aligne Right Button
align_right_icon = tk.PhotoImage(file = "icons2/align_right.png")
align_right_btn = ttk.Button(toolbar,image = align_right_icon)
align_right_btn.grid(row = 0,column = 8 , padx = 5)

######################################################################################################
#                                         Toolbar End                                                #           
######################################################################################################

######################################################################################################
#                                         Toolbar End                                                #           
######################################################################################################















######################################################################################################
#                                                                                                    #           
######################################################################################################
main_app.config(menu = main_menu)
main_app.mainloop()
