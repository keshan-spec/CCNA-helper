from tkinter import *
import json

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.minsize(400, 100)
        self.title('CCNA Helper')
        with open("data.json", "r") as f:
            self.data = json.load(f)
        self.topics = {}
        # self.draw_table()
        self.window()

    def del_child(self):
        children = self.winfo_children()
        for child in children:
            print("type of widget is : " + str(type(child)))
            if str(type(child)) == "<class 'tkinter.Message'>":
                # print("Here Message widget will destroy")
                child.destroy()
                return

    def draw_table(self,xa):
        cols = ['Command', 'Description', 'Links']
        rows = ['command', 'short_desc', 'links']
        for row in range(len(xa)+1):
            for col in range(3):
                if row == 0:
                    lbl = Label(
                        self.popup, text=f"{cols[col]}", bg="black", fg="white", pady=3, padx=3)
                    lbl.grid(row=row, column=col, pady=1, padx=1)
                else:
                    lbl = Label(
                        self.popup, text=f"{xa[row-1][rows[col]]}" , bg="white", fg="black", pady=3, padx=3)
                    lbl.grid(row=row, column=col, pady=1, padx=1)


    def radioEvent(self):
        selected = self.v.get()
        self.popup = Toplevel(self)
        xa = []
        for intents in self.data['data']:
            if intents['topic'] == self.topics[selected]:
                xa.append(intents)
        self.draw_table(xa)

    def printlink(self,links):
        for link in links:
            Label(self.popup, text=f"Links : {link}").pack()

    def window(self):
        Label(self, text="Available topics").pack()
        c = 1
        for intents in self.data['data']:
            if intents['topic'] not in self.topics.values():
                self.topics[c] = intents['topic']
                c += 1

        self.v = IntVar()
        [Radiobutton(self, text=j, variable=self.v, value=x, command=self.radioEvent).pack(
            anchor=W) for x, j in self.topics.items()]
        



win = Root()
win.mainloop()
