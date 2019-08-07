from tkinter .filedialog import *
from tkinter.colorchooser import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None     # text表示文本框对象
        self.filename = None    # filename表示打开文件的名字
        self.contextMenu = None # contextMenu上下文菜单对象
        self.pack()
        self.createWidget()

    def createWidget(self):
        menubar = Menu(root)
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        #         将子菜单加入到主菜单栏
        menubar.add_cascade(label="文件", menu=menuFile)
        menubar.add_cascade(label="编辑", menu=menuEdit)
        menubar.add_cascade(label="帮助", menu=menuHelp)

        # 添加菜单项
        menuFile.add_command(label="新建", accelerator="ctrl+n", command=self.newfile)
        menuFile.add_command(label="打开", accelerator="ctrl+o", command=self.openfile)
        menuFile.add_command(label="保存", accelerator="ctrl+s", command=self.savefile)
        menuFile.add_separator()    # 添加分割线
        menuFile.add_command(label="退出", accelerator="ctrl+q", command=self.exit)

        # 将主菜单栏加到跟窗口
        root["menu"] = menubar

        # 添加快捷键处理
        root.bind("<Control-n>", lambda event:self.newfile())
        root.bind("<Control-o>", lambda event:self.openfile())
        root.bind("<Control-s>", lambda event:self.savefile())
        root.bind("<Control-q>", lambda event:self.exit())

        # 文本编辑区
        self.textpad = Text(root, width=50, height=30)
        self.textpad.pack()

        # 创建上下菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="背景颜色", command=self.openAskColor)

        # 为右键绑定事件
        root.bind("<Button-3>", self.createContextMenu)

    def newfile(self):
        self.textpad.delete('1.0', "end")
        self.filename = asksaveasfile(title='另存为', initialfile="未命名.txt", filetypes=[("文本文档", "*.txt")],
                                      defaultextension='.txt')
        print(self.filename)
        self.savefile()

    def openfile(self):
        self.textpad.delete('1.0', "end")
        with askopenfile(title="打开文件") as f:
            self.textpad.insert(INSERT, f.read())
            self.filename = f.name
            pow(f.name)

    def savefile(self):
        with open(self.filename, "w") as f:
            c = self.textpad.get(1.0, END)
            f.write(c)
    def exit(self):
        root.quit()

    def openAskColor(self):
        s1 = askcolor(color="red", title="选择背景色")
        self.textpad.config(bg=s1[1])

    def createContextMenu(self, event):
        self.contextMenu.post(event.x_root, event.y_root)


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+500+500")
    root.title("笔记本")
    app = Application(master=root)
    root.mainloop()
