import tkinter as tk
import TextAnalyzer
import SignalProc
import threading
class GUI:
  def __init__(self):
    print("Cop Talk Created")
  def forget_all(self):
    '''
    Hides all widgets, even if they are already hidden
    '''
    self.start_button.grid_forget()
    self.updates_textBox.grid_forget()
    self.posts_button.grid_forget()
    self.stop_button.grid_forget()
    self.confirm_button.grid_forget()
    self.warnings_button.grid_forget()
    self.crimes_button.grid_forget()
    self.emergency_button.grid_forget()
    self.drop.grid_forget()
    self.posts_textBox.grid_forget()
    self.emergency_button.grid_forget()
    self.crimes_button.grid_forget()
    self.warnings_button.grid_forget()
    self.live_button.grid_forget()
    self.agreement_label.grid_forget()
    
  def channel_selected(self):
    '''
    Once a channel is selected this function will run
    It will allow the start button to be pressed
    '''
    
    if self.dropdown_output.get() == "Agree":
      self.start_button["state"]="normal"
    else:
      self.start_button["state"]="disabled"
  def main_menu(self):
    '''
    Resets to home screen:
    Hides all widgets and places the Start and Channel button
    Stops live updating
    '''  
    self.forget_all()
    try:
      self.sp.running = False
      self.sp.p.terminate()
    except(AttributeError):
      pass
    self.start_button["state"]="disabled"
    self.updating = False
    self.agreement_label.grid(row=0,column = 0, columnspan =2)
    self.start_button.grid(row=2,column = 0,columnspan = 2)
    self.confirm_button.grid(row=1,column=1,)
    self.drop.grid(row=1,column = 0)
    
  def live(self):
    '''
    When start or live button is pressed:
    1)forget all buttons
    2)Display text box with live_update
    3)Display posts button
    '''
    self.forget_all()
    self.stop_button.grid(row=2,column = 0)
    self.updates_textBox.grid(row=1,column = 0, columnspan = 2)
    self.posts_button.grid(row = 2, column =1 )
    if(self.updating):
      pass
    else:
      self.updating = True
      #In future don't call this


  def live_update(self,post):  
    '''
    accepts: string
    Will update the screen with the given string in the parameters
    '''
    #if(updating):
    self.count+=1
    self.incoming.append(post)
    print(post)
    self.updates_textBox["state"] = "normal"
    self.updates_textBox.insert(tk.END,post)    
    self.updates_textBox.insert(tk.END,"\n\n")
    self.updates_textBox["state"]="disabled"
  def post_update(self,post):  
    '''
    accepts: string
    Will update the screen with the given string in the parameters
    '''
    #if(updating):
    self.outgoing.append(post)
    print(post)
    self.posts_textBox["state"] = "normal"
    self.posts_textBox.insert(tk.END,post)    
    self.posts_textBox.insert(tk.END,"\n\n")
    self.posts_textBox["state"]="disabled"
      #root.after(4000,live_update)
  def posts(self):
    '''
    When Posts button is pressed:
    1)forget all buttons
    2)Display category buttons
    3)Display outgoing posts
    4)Display live button and move stop button
    '''
    self.forget_all()
    self.crimes_button.grid(row = 1, column = 0)
    self.emergency_button.grid(row = 2, column = 0)
    self.warnings_button.grid(row = 3, column = 0)
    self.posts_textBox.grid(row=1,column = 1,rowspan = 3)
    self.live_button.grid(row=4,column = 0)
    self.stop_button.grid(row=4,column = 2)
    
  def colorTostr(self,str):
    self.highlights = []
    self.stop = 0
    self.start = 0
    for i in range(len(str)):
      if str[i] == "*":      
        self.start = i
      elif str[i] == "$":
        self.stop = i+1
        self.highlights.append((self.start,self.stop))
    return (self.highlights), str.replace("*","-").replace("$","-")
  def start(self):
    '''
    Creates the window, initializes all variables to starting values, creates the widgets, places the widgets, starts the program loop
    '''
    self.root.title("CopTalk")
    #Below is where all the widgets are created  
    self.count = 0
    #Updating Boolean
    updating = False
    #Test Text
    self.incoming = ["Now Recording audio on computer..."]
    self.outgoing = []
    
    #Label Creation  
    self.copTalk_label = tk.Label(self.root, text = "CopTalk")
    self.agreement_label = tk.Label(self.root, text = "This application will record the audio from your device")
    #Dropdown options
    self.channels = ["Agree","Disagree"]
    
    #DropDown Variable
    self.dropdown_output = tk.StringVar()
    self.dropdown_output.set("Agreement")
    
    #Dropdown Creation
    self.drop = tk.OptionMenu( self.root , self.dropdown_output , *self.channels )
    
    #Button Creation
    self.start_button = tk.Button(self.root, text = "Start", bg = "green", command = self.live, fg = "white")
    self.stop_button = tk.Button(self.root, text = "Exit", bg = "red",command = self.main_menu)
    self.confirm_button = tk.Button(self.root, text = "Confirm", command = self.channel_selected)
    self.posts_button = tk.Button(self.root, text = "Posts",bg = "light blue", command = self.posts)
    self.crimes_button = tk.Button(self.root, text ="Crimes",bg = "red")
    self.emergency_button = tk.Button(self.root, text = "Emergency", bg = "yellow")
    self.warnings_button = tk.Button(self.root, text = "Warnings", bg = "orange")
    self.live_button = tk.Button(self.root, text = "Live", bg = "light blue", command = self.live)
    #TextBox creation
    self.updates_textBox = tk.Text(self.root)
    self.posts_textBox = tk.Text(self.root)
    self.updates_textBox.insert(tk.END,self.incoming[0])
    self.updates_textBox["state"]="disabled"
    self.posts_textBox["state"]="disabled"
    st = len(self.incoming[0])
    st = "-"*st
    self.updates_textBox.insert(tk.END,("\n"+st+"\n"))
    #Starting Grid Placements
    self.copTalk_label.grid(row= 0,column = 0, columnspan =2)
    self.main_menu() #Places the main menu
    #self.st = TextAnalyzer.rawText("Metro 9417 Alpha 417 Imperial detention 239 contest 865 Imperial Beach Boulevard deserve 53 copy will generate a walk-up response, Crash, accident")
    #self.highlights,self.st = self.colorTostr(self.st)
    #self.row = (len(self.updates_textBox.get("1.0", "end-1c").split("\n")))  
    #self.live_update(self.st)
    #for i in range(len(self.highlights)):
    #  start = str(self.row)+"."+str(self.highlights[i][0])
    #  end = str(self.row)+"."+str(self.highlights[i][1])
    #  self.updates_textBox.tag_add("red", start,end)
    #live_update()
    #Starting Button States
    self.start_button["state"]="disabled"
    self.sp = SignalProc.SignalProcessor()
    #sp.sdr_start()
    self.thread = threading.Thread(target= lambda : self.sp.sdr_start(self))
    self.thread.start()
  def startGUI(self):
    
    self.root = tk.Tk()
    self.start()
    
    self.root.mainloop()
    exit(0)
