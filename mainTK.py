""" tk GUI for MAL-Scraper based on Bryan Oakley's frame management model

    http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-
    tkinter/7557028#7557028
"""

from userClass import userClassCreator
from theAnimeClass import animeClassCreator
from getDataETree import fetchAnimeList, getUserImage
import Tkinter as tk


class mainApp(tk.Tk):

    user1 = ""
    user2 = ""
    List1 = ""
    List2 = ""
    switch = False

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # Container setup
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Create instances of frames then populate 'frames' dictionary
        for F in (Login, Compare):
            pageName = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[pageName] = frame

            # All frames are stacked; they are visible based on order
            frame.grid(row=0, column=0, sticky="news")

        self.showFrame("Login")

    def dataCollect():
        """ Collect user and list data for each user"""

        mainApp.switch = True

        # Raw data pulled and stored for each user as LISTS
        user1_userData, user1_animeData = fetchAnimeList(mainApp.user1)
        user2_userData, user2_animeData = fetchAnimeList(mainApp.user2)

        # User and Animelog classes are created to store user and animelist data
        # for each user
        user1 = userClassCreator(user1_userData)
        userList1 = animeClassCreator(user1_animeData)

        user2 = userClassCreator(user2_userData)
        userList2 = animeClassCreator(user2_animeData)

        mainApp.user1 = user1
        mainApp.user2 = user2
        mainApp.userList1 = userList1
        mainApp.userList2 = userList2

    def showFrame(self, pageName):
        """ Display frame associated with pageName"""
        frame = self.frames[pageName]
        frame.tkraise()

    def setup(self, u1, u2):

        # Raw data pulled and stored for each user as LISTS
        user1_userData, user1_animeData = fetchAnimeList(u1)
        user2_userData, user2_animeData = fetchAnimeList(u2)

        # User and Animelog classes are created to store user and animelist data
        # for each user
        user1_Data = userClassCreator(user1_userData)
        user1_List = animeClassCreator(user1_animeData)

        user2_Data = userClassCreator(user2_userData)
        user2_List = animeClassCreator(user2_animeData)

        mainApp.user1 = user1_Data
        mainApp.user2 = user2_Data
        mainApp.List1 = user1_List
        mainApp.List2 = user2_List

        Compare.userImg1 = getUserImage(user1_Data)
        hold = tk.Label(Compare, image=Compare.userImg1, bg='brown')
        hold.pack()

class Login(tk.Frame):

    def callback(self, frame, ent1, ent2):
        """ Store values in entryboxes ent1 and ent2
            Change frame to specified
        """

        # Store entries
        self.controller.user1 = self.userEnt1.get()
        self.controller.user2 = self.userEnt2.get()

        # Change frame
        self.controller.showFrame(frame)

        # Setup
        self.controller.setup(self, self.controller.user1, self.controller.user2)

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        userLabel1 = tk.Label(self, text="MAL User 1").grid(row=0, sticky=tk.W)
        userLabel2 = tk.Label(self, text="MAL User 2").grid(row=1, sticky=tk.W)

        self.userEnt1 = tk.Entry(self)
        self.userEnt2 = tk.Entry(self)

        self.userEnt1.grid(row=0, column=1)
        self.userEnt2.grid(row=1, column=1)

        b1 = tk.Button(self, text="Compare!",
                       command=lambda: self.callback("Compare",
                                                           self.userEnt1,
                                                           self.userEnt2))
        b1.grid(row=3, columnspan=2)

class Compare(tk.Frame):

    userImg1 = None
    userImg2 = None

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

    # here

    def setup(self, u1, u2):

        # Raw data pulled and stored for each user as LISTS
        user1_userData, user1_animeData = fetchAnimeList(u1)
        user2_userData, user2_animeData = fetchAnimeList(u2)

        # User and Animelog classes are created to store user and animelist data
        # for each user
        user1_Data = userClassCreator(user1_userData)
        user1_List = animeClassCreator(user1_animeData)

        user2_Data = userClassCreator(user2_userData)
        user2_List = animeClassCreator(user2_animeData)

        mainApp.user1 = user1_Data
        mainApp.user2 = user2_Data
        mainApp.List1 = user1_List
        mainApp.List2 = user2_List

        userImg = getUserImage(user1_Data)
        hold = tk.Label(self, image=userImg, bg='brown')
        hold.pack()

# count = 0
    # for item1 in userList1:
        # for item2 in userList2:
            # if item1.title == item2.title:
                # count += 1
                # print item1.title
    # print "\nYou and %s have %d titles in common" % (user2, count)

if __name__ == '__main__':
    app = mainApp()
    app.mainloop()
