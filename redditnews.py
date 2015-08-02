
from Tkinter import *

import praw

root = Tk()

screenW = root.winfo_screenwidth()
screenH = root.winfo_screenheight()

root.title("Reddit News")
root.geometry(str(screenW-10)+"x"+str(screenH-370)) #Did the math to get it working to my liking with the monitor I use.
root.resizable(0,0)
root.configure(background="black")

app = Frame(root)
app.grid()

button = Button(app, text = "Get News", background="white")

def getTopPosts():
    label = Label(app, text = "", anchor=W, justify=LEFT)
    r = praw.Reddit("Test")
    subreddit = r.get_subreddit("news")
    label.grid(row=1,column=1)
    lblText = ""
    i=1 #Used just to prevent multiple lines ( \n\n ) from appearing after the final submission.
    for submission in subreddit.get_hot(limit=10):
        if (i != 10):
            lblText = lblText + submission.title + "\n\n"
        else:
            lblText = lblText + submission.title
        i = i + 1
    label.configure(font="Times 12 bold", text = lblText, background="light blue")
    button.configure(text = "Refresh News (not likely to change right away)")

button.configure(command = getTopPosts)
button.grid(row=0,column=1)

root.iconbitmap("newsicon.ico")
root.mainloop()
