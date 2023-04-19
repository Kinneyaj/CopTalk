import tkinter as tk
import TextAnalyzer
import SignalProc
import threading
def forget_all():
  '''
  Hides all widgets, even if they are already hidden
  '''
  global updating
  start_button.grid_forget()
  updates_textBox.grid_forget()
  posts_button.grid_forget()
  stop_button.grid_forget()
  connect_button.grid_forget()
  warnings_button.grid_forget()
  crimes_button.grid_forget()
  emergency_button.grid_forget()
  drop.grid_forget()
  posts_textBox.grid_forget()
  emergency_button.grid_forget()
  crimes_button.grid_forget()
  warnings_button.grid_forget()
  live_button.grid_forget()
  
def channel_selected():
  '''
  Once a channel is selected this function will run
  It will allow the start button to be pressed
  '''
  if(dropdown_output.get() == "Channel Select"):
    start_button["state"]="disabled"
  else:
    start_button["state"]="normal"
def main_menu():
  '''
  Resets to home screen:
  Hides all widgets and places the Start and Channel button
  Stops live updating
  '''  
  global updating
  forget_all()
  start_button["state"]="disabled"
  updating = False
  start_button.grid(row=2,column = 0,columnspan = 2)
  connect_button.grid(row=1,column=0,)
  drop.grid(row=1,column = 1)
  
def live():
  '''
  When start or live button is pressed:
  1)forget all buttons
  2)Display text box with live_update
  3)Display posts button
  '''
  global updating
  forget_all()
  stop_button.grid(row=2,column = 0)
  updates_textBox.grid(row=1,column = 0, columnspan = 2)
  posts_button.grid(row = 2, column =1 )
  if(updating):
    pass
  else:
    updating = True
    #In future don't call this


def live_update(post):  
  '''
  accepts: string
  Will update the screen with the given string in the parameters
  '''
  global updating, count
  #if(updating):
  count+=1
  incoming.append(post)
  print(post)
  updates_textBox.insert(tk.END,post)    
  updates_textBox.insert(tk.END,"\n\n")
    #root.after(4000,live_update)
def posts():
  '''
  When Posts button is pressed:
  1)forget all buttons
  2)Display category buttons
  3)Display outgoing posts
  4)Display live button and move stop button
  '''
  forget_all()
  crimes_button.grid(row = 1, column = 0)
  emergency_button.grid(row = 2, column = 0)
  warnings_button.grid(row = 3, column = 0)
  posts_textBox.grid(row=1,column = 1,rowspan = 3)
  live_button.grid(row=4,column = 0)
  stop_button.grid(row=4,column = 2)
  
def colorTostr(str):
  highlights = []
  stop = 0
  start = 0
  for i in range(len(str)):
    if str[i] == "*":      
      start = i
    elif str[i] == "$":
      stop = i+1
      highlights.append((start,stop))
  return (highlights), str.replace("*","-").replace("$","-")
def start():
  '''
  Creates the window, initializes all variables to starting values, creates the widgets, places the widgets, starts the program loop
  '''
  global root, updating, incoming, outgoing, copTalk_label, channels, dropdown_output, drop, start_button, stop_button,connect_button,posts_button,crimes_button,emergency_button,warnings_button,live_button,copTalk_label,updates_textBox,posts_textBox,count
  root = tk.Tk()
  root.title("CopTalk")
  #Below is where all the widgets are created  
  count = 0
  #Updating Boolean
  updating = False
  #Test Text
  incoming = ["Currently we have a code 4356 at downtown","Fire reported on 5th Avenue","Potato"]
  outgoing = ["Recent dangerous crime reported in ohio\nPosted on twitter at 5:30pm","Fire near CSUSM\nPosted on twitter at 7am"]
  
  #Label Creation  
  copTalk_label = tk.Label(root, text = "CopTalk")
  #Dropdown options
  channels = ["First","Second"]
  
  #DropDown Variable
  dropdown_output = tk.StringVar()
  dropdown_output.set("Channel Select")
  
  #Dropdown Creation
  drop = tk.OptionMenu( root , dropdown_output , *channels )
  
  #Button Creation
  start_button = tk.Button(root, text = "Start", bg = "green", command = live)
  stop_button = tk.Button(root, text = "Stop", bg = "red",command = main_menu)
  connect_button = tk.Button(root, text = "Connect", command = channel_selected)
  posts_button = tk.Button(root, text = "Posts",bg = "light blue", command = posts)
  crimes_button = tk.Button(root, text ="Crimes",bg = "red")
  emergency_button = tk.Button(root, text = "Emergency", bg = "yellow")
  warnings_button = tk.Button(root, text = "Warnings", bg = "orange")
  live_button = tk.Button(root, text = "Live", bg = "light blue", command = live)
  #TextBox creation
  updates_textBox = tk.Text(root)
  for i in range(len(incoming)):
    updates_textBox.insert(tk.END,incoming[i])
    updates_textBox.insert(tk.END,"\n\n")
  posts_textBox = tk.Text(root)
  for i in range(len(outgoing)):
    posts_textBox.insert(tk.END,outgoing[i])
    posts_textBox.insert(tk.END,"\n\n")
  #Starting Grid Placements
  copTalk_label.grid(row= 0,column = 0, columnspan =2)
  
  updates_textBox.tag_config("red", foreground="red")
  updates_textBox.tag_add("red", "1.7", "1.22")
  main_menu() #Places the main menu
  st = TextAnalyzer.rawText("Metro 9417 Alpha 417 Imperial detention 239 contest 865 Imperial Beach Boulevard deserve 53 copy will generate a walk-up response, Crash, accident")
  highlights,st = colorTostr(st)
  row = (len(updates_textBox.get("1.0", "end-1c").split("\n")))  
  live_update(st)
  for i in range(len(highlights)):
    start = str(row)+"."+str(highlights[i][0])
    end = str(row)+"."+str(highlights[i][1])
    updates_textBox.tag_add("red", start,end)
  #live_update()
  #Starting Button States
  start_button["state"]="disabled"
def startGUI():
  global root
  root = tk.Tk()
  start()
  sp = SignalProc.SignalProcessor()
  #sp.sdr_start()
  thread = threading.Thread(target=sp.sdr_start)
  thread.start()
  root.mainloop()
