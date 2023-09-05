import tkinter as tk


class MainWindow:

    # Конструктор
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("310x380")
        self.window.title("SPAN")

        # Добавление метки заголовка
        lbl_title = tk.Label(text="SPAN", font=('Helvetica', 16, 'bold'), fg='#0000cc', justify='center')
        lbl_title.place(x=25, y=15, width=250, height=50)

        # Добавление метки заголовка данных
        lblTitle = tk.Label(text="Данные", font=('Helvetica', 12, 'bold'), fg='#0066ff', justify='center')
        lblTitle.place(x=25, y=55, width=250, height=50)

        # Добавление кнопки данных "Отделы"
        btn_report = tk.Button(self.window, text="Отделы",
                               font=('Helvetica', 10, 'bold'), bg='#ccffcc')
        btn_report.place(x=25, y=100, width=120, height=50)

        # Добавление кнопки данных "Сотрудники"
        btn_report = tk.Button(self.window, text="Сотрудники",
                               font=('Helvetica', 10, 'bold'), bg='#ccffcc')
        btn_report.place(x=160, y=100, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text="Выход",
                              font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.close)
        btn_close.place(x=160, y=300, width=120, height=50)

    # Функция закрытия главного окна
    def close(self):
        self.window.destroy()

    # Запуск цикла окна
    def start_mainloop(self):
        self.window.mainloop()
