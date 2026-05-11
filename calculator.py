import customtkinter as ctk

# Настройка внешнего вида
ctk.set_appearance_mode("light")  # Светлая тема
ctk.set_default_color_theme("blue")

class Calculator:
    def __init__(self):
        # Создание главного окна
        self.window = ctk.CTk()
        self.window.title("Калькулятор")
        self.window.geometry("400x600")
        self.window.resizable(False, False)  # Фиксированный размер
        
        # Переменная для хранения выражения
        self.expression = ""
        
        # Создание виджетов
        self.create_widgets()
        
    def create_widgets(self):
        # Поле для отображения результата
        self.display = ctk.CTkEntry(
            self.window,
            font=("Arial", 36),
            justify="right",
            state="readonly",
            height=80,
            corner_radius=10
        )
        self.display.pack(pady=20, padx=20, fill="both")
        
        # Фрейм для кнопок
        buttons_frame = ctk.CTkFrame(self.window)
        buttons_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Определение кнопок
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        # Создание сетки кнопок 4x4
        row = 0
        col = 0
        
        for button in buttons:
            # Определение цвета кнопки
            if button in ['C', '=']:
                color = "#FF6B6B" if button == 'C' else "#4ECDC4"
                hover_color = "#FF5252" if button == 'C' else "#45B7D1"
                text_color = "white"
            elif button in ['/', '*', '-', '+']:
                color = "#FFEAA7"
                hover_color = "#FFD93D"
                text_color = "#2C3E50"
            else:
                color = "#FFFFFF"
                hover_color = "#F0F0F0"
                text_color = "#2C3E50"
            
            # Создание кнопки
            btn = ctk.CTkButton(
                buttons_frame,
                text=button,
                font=("Arial", 28, "bold"),
                command=lambda b=button: self.button_click(b),
                height=80,
                corner_radius=8,
                fg_color=color,
                hover_color=hover_color,
                text_color=text_color
            )
            
            # Размещение кнопки в сетке
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            
            if col > 3:
                col = 0
                row += 1
        
        # Настройка веса строк и столбцов для равномерного растяжения
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_rowconfigure(i, weight=1)
    
    def button_click(self, value):
        """Единая функция обработки нажатий кнопок"""
        
        if value == 'C':
            # Очистка
            self.expression = ""
            self.update_display("0")
            
        elif value == '=':
            # Вычисление результата
            try:
                # Замена операторов для безопасного вычисления
                expression_to_eval = self.expression.replace('×', '*').replace('÷', '/')
                result = eval(expression_to_eval)
                
                # Обработка целых чисел
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                
                self.expression = str(result)
                self.update_display(self.expression)
            except Exception:
                self.update_display("Ошибка")
                self.expression = ""
                
        else:
            # Добавление символа в выражение
            # Замена стандартных операторов для отображения
            if value == '*':
                display_value = '×'
                calc_value = '*'
            elif value == '/':
                display_value = '÷'
                calc_value = '/'
            else:
                display_value = value
                calc_value = value
            
            # Предотвращение множественных операторов подряд
            if self.expression and self.expression[-1] in '+-*/' and calc_value in '+-*/':
                # Замена последнего оператора
                self.expression = self.expression[:-1] + calc_value
            else:
                self.expression += calc_value
            
            self.update_display(self.expression.replace('*', '×').replace('/', '÷'))
    
    def update_display(self, text):
        """Обновление текста на дисплее"""
        self.display.configure(state="normal")
        self.display.delete(0, ctk.END)
        self.display.insert(0, text)
        self.display.configure(state="readonly")
    
    def run(self):
        """Запуск приложения"""
        self.window.mainloop()

if __name__ == "__main__":
    app = Calculator()
    app.run()
