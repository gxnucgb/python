from tkinter .filedialog import *
from tkinter.colorchooser import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None     # text��ʾ�ı������
        self.filename = None    # filename��ʾ���ļ�������
        self.contextMenu = None # contextMenu�����Ĳ˵�����
        self.pack()
        self.createWidget()

    def createWidget(self):
        menubar = Menu(root)
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        #         ���Ӳ˵����뵽���˵���
        menubar.add_cascade(label="�ļ�", menu=menuFile)
        menubar.add_cascade(label="�༭", menu=menuEdit)
        menubar.add_cascade(label="����", menu=menuHelp)

        # ��Ӳ˵���
        menuFile.add_command(label="�½�", accelerator="ctrl+n", command=self.newfile)
        menuFile.add_command(label="��", accelerator="ctrl+o", command=self.openfile)
        menuFile.add_command(label="����", accelerator="ctrl+s", command=self.savefile)
        menuFile.add_separator()    # ��ӷָ���
        menuFile.add_command(label="�˳�", accelerator="ctrl+q", command=self.exit)

        # �����˵����ӵ�������
        root["menu"] = menubar

        # ��ӿ�ݼ�����
        root.bind("<Control-n>", lambda event:self.newfile())
        root.bind("<Control-o>", lambda event:self.openfile())
        root.bind("<Control-s>", lambda event:self.savefile())
        root.bind("<Control-q>", lambda event:self.exit())

        # �ı��༭��
        self.textpad = Text(root, width=50, height=30)
        self.textpad.pack()

        # �������²˵�
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="������ɫ", command=self.openAskColor)

        # Ϊ�Ҽ����¼�
        root.bind("<Button-3>", self.createContextMenu)

    def newfile(self):
        self.textpad.delete('1.0', "end")
        self.filename = asksaveasfile(title='���Ϊ', initialfile="δ����.txt", filetypes=[("�ı��ĵ�", "*.txt")],
                                      defaultextension='.txt')
        print(self.filename)
        self.savefile()

    def openfile(self):
        self.textpad.delete('1.0', "end")
        with askopenfile(title="���ļ�") as f:
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
        s1 = askcolor(color="red", title="ѡ�񱳾�ɫ")
        self.textpad.config(bg=s1[1])

    def createContextMenu(self, event):
        self.contextMenu.post(event.x_root, event.y_root)


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+500+500")
    root.title("�ʼǱ�")
    app = Application(master=root)
    root.mainloop()
