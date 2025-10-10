# from tkinter import *
#
# root = Tk()  # создаем корневой объект - окно
# root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
# root.geometry("300x300")  # устанавливаем размеры окна
#
# label = Label(text="Hello")  # создаем текстовую метку
# label.pack()  # размещаем метку в окне
#
# root.mainloop()

# from tkinter import *
#
#
# def finish():
#     root.destroy()  # ручное закрытие окна и всего приложения. обратите внимание, что к root обращаемся как к глобальной переменной
#     print("App closed")
#
#
# root = Tk()
# root.geometry("250x200")
#
# root.title("Hello")
# root.protocol("WM_DELETE_WINDOW", finish)
#
# root.mainloop()


# from tkinter import *
# from tkinter import ttk  # подключаем пакет ttk
#
# root = Tk()
# root.title("Hello")
# root.geometry("250x250")
#
# btn = ttk.Combobox(text="DAMN!1!!!1")  # создаем кнопку из пакета ttk
# btn.pack()  # размещаем кнопку в окне
#
# root.mainloop()

# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# root.title("HELLO")
# root.geometry("250x250")
#
# btn = ttk.Button()
# btn.pack()
# # устанавливаем параметр text
# btn["text"] = "Send"
# # получаем значение параметра text
# btnText = btn["text"]
# print(btnText)
#
# root.mainloop()

