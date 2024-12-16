import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kuis")
        self.root.geometry("400x375")
        
        #Menggunakan style agar bisa mengubah warna menjadi pink, dll.
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='pink')
        self.style.configure('TLabel', background='pink', foreground='black', font=('Helvetica', 12))
        self.style.configure('TButton', background='white', foreground='black', font=('Helvetica', 10))
        self.style.map('TButton', background=[('active', 'lightpink')])
        self.style.configure('TRadiobutton', background='pink', foreground='black', font=('Helvetica', 10))
        
        self.users = {}
        self.questions = []
        self.current_user = None
        
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        self.show_login_screen()
    
    #Menampilkan layar login
    def show_login_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        ttk.Label(self.main_frame, text="Sistem Login Kuis", font=('Helvetica', 16)).pack(pady=20)
        
        ttk.Button(self.main_frame, text="Login", 
                  command=self.login).pack(pady=10)
        ttk.Button(self.main_frame, text="Register", 
                  command=self.register).pack(pady=10)
    
    #Fungsi untuk register
    def register(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Register")
        dialog.geometry("300x175")
        dialog.configure(background="pink")
        
        ttk.Label(dialog, text="Username:").pack(pady=5)
        username_entry = ttk.Entry(dialog)
        username_entry.pack()
        
        ttk.Label(dialog, text="Password:").pack(pady=5)
        password_entry = ttk.Entry(dialog, show="*")
        password_entry.pack()
        
        def submit():
            username = username_entry.get()
            password = password_entry.get()
            
            if username and password:
                if username in self.users:
                    messagebox.showerror("Error", "Username sudah diambil!")
                else:
                    self.users[username] = password
                    messagebox.showinfo("Success", "Daftar akun sukses!")
                    dialog.destroy()
            else:
                messagebox.showerror("Error", "Mohon untuk mengisi setiap kolom isian!")
        
        ttk.Button(dialog, text="Register", command=submit).pack(pady=10)
    
    #Fungsi untuk login
    def login(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Login")
        dialog.geometry("300x175")
        dialog.configure(background="pink")
        
        ttk.Label(dialog, text="Username:").pack(pady=5)
        username_entry = ttk.Entry(dialog)
        username_entry.pack()
        
        ttk.Label(dialog, text="Password:").pack(pady=5)
        password_entry = ttk.Entry(dialog, show="*")
        password_entry.pack()
        
        def submit():
            username = username_entry.get()
            password = password_entry.get()
            
            if username not in self.users:
                messagebox.showerror("Error", "Username tidak ada!")
            elif password == self.users[username]:
                self.current_user = username
                dialog.destroy()
                self.show_quiz_menu()
            else:
                messagebox.showerror("Error", "Password salah!")
        
        ttk.Button(dialog, text="Login", command=submit).pack(pady=10)
        
        def submit():
            username = username_entry.get()
            password = password_entry.get()
            
            if username not in self.users:
                messagebox.showerror("Error", "Username tidak ada!")
            elif password == self.users[username]:
                self.current_user = username
                dialog.destroy()
                self.show_quiz_menu()
            else:
                messagebox.showerror("Error", "Password salah!")
        
        ttk.Button(dialog, text="Login", command=submit).pack(pady=10)

    #Menampilkan menu kuis
    def show_quiz_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        ttk.Label(self.main_frame, text=f"Selamat Datang, {self.current_user}!", 
                 font=('Helvetica', 16)).pack(pady=20)
        
        ttk.Button(self.main_frame, text="Kelola Soal Kuis", 
                  command=self.manage_questions).pack(pady=10)
        ttk.Button(self.main_frame, text="Mulai Kuis", 
                  command=self.take_quiz).pack(pady=10)
        ttk.Button(self.main_frame, text="Logout", 
                  command=self.show_login_screen).pack(pady=10)

    #Fungsi untuk mengelola pertanyaan
    def manage_questions(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        ttk.Label(self.main_frame, text="Kelola Soal Kuis", 
                 font=('Helvetica', 16)).pack(pady=20)
        
        ttk.Button(self.main_frame, text="Tambah Soal", 
                command=self.add_question).pack(pady=10)
        ttk.Button(self.main_frame, text="Edit Soal",
                command=self.edit_question).pack(pady=10)
        ttk.Button(self.main_frame, text="Delete Soal",
                command=self.delete_questions).pack(pady=10)
        ttk.Button(self.main_frame, text="Lihat Soal", 
                command=self.view_questions).pack(pady=10)
        ttk.Button(self.main_frame, text="Kembali", 
                command=self.show_quiz_menu).pack(pady=10)

    #Fungsi untuk menambahkan pertanyaan
    def add_question(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Tambah Soal")
        dialog.geometry("300x500")

        ttk.Label(dialog, text="Soal:").pack(pady=5)
        question_entry = ttk.Entry(dialog)
        question_entry.pack()

        ttk.Label(dialog, text="Pilihan Jawaban:").pack(pady=5)
        ttk.Label(dialog, text="A:").pack(pady=5)
        choice_a_entry = ttk.Entry(dialog)
        choice_a_entry.pack()
        ttk.Label(dialog, text="B:").pack(pady=5)
        choice_b_entry = ttk.Entry(dialog)
        choice_b_entry.pack()
        ttk.Label(dialog, text="C:").pack(pady=5)
        choice_c_entry = ttk.Entry(dialog)
        choice_c_entry.pack()
        ttk.Label(dialog, text="D:").pack(pady=5)
        choice_d_entry = ttk.Entry(dialog)
        choice_d_entry.pack()

        ttk.Label(dialog, text="Pilih jawaban yang benar:").pack(pady=5)
        answer_var = tk.StringVar()
        
        def update_radio_buttons(*args):
            for widget in dialog.winfo_children():
                if isinstance(widget, ttk.Radiobutton):
                    widget.destroy()

            choices = [choice_a_entry.get(), choice_b_entry.get(), 
                      choice_c_entry.get(), choice_d_entry.get()]
            for choice in choices:
                if choice:
                    ttk.Radiobutton(dialog, text=choice, 
                                  variable=answer_var, value=choice).pack()

        choice_a_entry.bind('<KeyRelease>', update_radio_buttons)
        choice_b_entry.bind('<KeyRelease>', update_radio_buttons)
        choice_c_entry.bind('<KeyRelease>', update_radio_buttons)
        choice_d_entry.bind('<KeyRelease>', update_radio_buttons)

        def submit():
            question = question_entry.get()
            choices = [choice_a_entry.get(), choice_b_entry.get(), choice_c_entry.get(), choice_d_entry.get()]
            answer = answer_var.get()
            
            if question and all(choices) and answer:
                self.questions.append({'question': question, 'choices': choices, 'answer': answer})
                messagebox.showinfo("Success", "Soal berhasil ditambahkan!")
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Mohon isi semua kolom!")
        
        ttk.Button(dialog, text="Tambah Soal", command=submit).pack(pady=10)

    #Fungsi untuk mengedit pertanyaan
    def edit_question(self):
        select_dialog = tk.Toplevel(self.root)
        select_dialog.title("Pilih Soal")
        select_dialog.geometry("250x350")

        ttk.Label(select_dialog, text="Pilih soal untuk diedit:", 
                 font=('Helvetica', 12)).pack(pady=10)

        listbox = tk.Listbox(select_dialog, width=40, height=10)
        listbox.pack(pady=10, padx=10)

        for i, question in enumerate(self.questions):
            listbox.insert(tk.END, f"Soal ke {i+1}: {question['question']}")

        #Fungsi untuk memilih pertanyaan ke berapa yang ingin diedit
        def open_edit_dialog():
            if not listbox.curselection():
                messagebox.showerror("Error", "Mohon untuk memilih soal terlebih dahulu!")
                return
                
            question_index = listbox.curselection()[0]
            select_dialog.destroy()

            dialog = tk.Toplevel(self.root)
            dialog.title("Edit Soal")
            dialog.geometry("300x500")

            ttk.Label(dialog, text="Soal:").pack(pady=5)
            question_entry = ttk.Entry(dialog)
            question_entry.insert(0, self.questions[question_index]['question'])
            question_entry.pack()

            ttk.Label(dialog, text="Pilihan Jawaban:").pack(pady=5)
            ttk.Label(dialog, text="A:").pack(pady=5)
            choice_a_entry = ttk.Entry(dialog)
            choice_a_entry.insert(0, self.questions[question_index]['choices'][0])
            choice_a_entry.pack()
            
            ttk.Label(dialog, text="B:").pack(pady=5)
            choice_b_entry = ttk.Entry(dialog)
            choice_b_entry.insert(0, self.questions[question_index]['choices'][1])
            choice_b_entry.pack()
            
            ttk.Label(dialog, text="C:").pack(pady=5)
            choice_c_entry = ttk.Entry(dialog)
            choice_c_entry.insert(0, self.questions[question_index]['choices'][2])
            choice_c_entry.pack()
            
            ttk.Label(dialog, text="D:").pack(pady=5)
            choice_d_entry = ttk.Entry(dialog)
            choice_d_entry.insert(0, self.questions[question_index]['choices'][3])
            choice_d_entry.pack()

            ttk.Label(dialog, text="Pilih jawaban yang benar:").pack(pady=5)
            answer_var = tk.StringVar(value=self.questions[question_index]['answer'])

            def update_radio_buttons(*args):
                for widget in dialog.winfo_children():
                    if isinstance(widget, ttk.Radiobutton):
                        widget.destroy()
                
                choices = [choice_a_entry.get(), choice_b_entry.get(), 
                          choice_c_entry.get(), choice_d_entry.get()]
                for choice in choices:
                    if choice:
                        ttk.Radiobutton(dialog, text=choice, 
                                      variable=answer_var, value=choice).pack()

            choice_a_entry.bind('<KeyRelease>', update_radio_buttons)
            choice_b_entry.bind('<KeyRelease>', update_radio_buttons)
            choice_c_entry.bind('<KeyRelease>', update_radio_buttons)
            choice_d_entry.bind('<KeyRelease>', update_radio_buttons)
            
            update_radio_buttons()

            def submit():
                question = question_entry.get()
                choices = [choice_a_entry.get(), choice_b_entry.get(), 
                          choice_c_entry.get(), choice_d_entry.get()]
                answer = answer_var.get()
                
                if question and all(choices) and answer:
                    self.questions[question_index] = {
                        'question': question,
                        'choices': choices,
                        'answer': answer
                    }
                    messagebox.showinfo("Success", "Soal berhasil diedit!")
                    dialog.destroy()
                else:
                    messagebox.showerror("Error", "Mohon isi semua kolom!")

            ttk.Button(dialog, text="Simpan Perubahan", command=submit).pack(pady=10)

        ttk.Button(select_dialog, text="Edit Soal yang Dipilih", 
                  command=open_edit_dialog).pack(pady=10)
        
    #Fungsi untuk menghapus pertanyaan
    def delete_questions(self):
        select_dialog = tk.Toplevel(self.root)
        select_dialog.title("Pilih Soal")
        select_dialog.geometry("300x400")

        ttk.Label(select_dialog, text="Pilih soal untuk dihapus:", 
                 font=('Helvetica', 12)).pack(pady=10)

        listbox = tk.Listbox(select_dialog, width=40, height=10)
        listbox.pack(pady=10, padx=10)

        for i, question in enumerate(self.questions):
            listbox.insert(tk.END, f"Soal ke {i+1}: {question['question']}")

        def delete_question():
            if not listbox.curselection():
                messagebox.showerror("Error", "Mohon untuk memilih soal terlebih dahulu!")
                return
                
            question_index = listbox.curselection()[0]
            self.questions.pop(question_index)
            messagebox.showinfo("Success", "Soal berhasil dihapus!")
            select_dialog.destroy()
            self.manage_questions()

        ttk.Button(select_dialog, text="Hapus Soal yang Dipilih", 
                  command=delete_question).pack(pady=10)

    #Menampilkan semua pertanyaan yang ada
    def view_questions(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        ttk.Label(self.main_frame, text="Daftar Soal", 
                 font=('Helvetica', 16)).pack(pady=20)
        
        for i, question in enumerate(self.questions):
            ttk.Label(self.main_frame, text=f"{i+1}. {question['question']}").pack()
            ttk.Label(self.main_frame, text=f"Pilihan Jawaban: {', '.join(question['choices'])}").pack()
            ttk.Label(self.main_frame, text=f"Jawaban: {question['answer']}").pack()
            ttk.Separator(self.main_frame, orient='horizontal').pack(fill='x', pady=10)
        
        ttk.Button(self.main_frame, text="Kembali", 
                  command=self.manage_questions).pack(pady=10)
    
    #Fungsi untuk mulai kuis
    def take_quiz(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        ttk.Label(self.main_frame, text="Kuis", 
                 font=('Helvetica', 16)).pack(pady=20)
        
        self.score = 0
        self.current_question = 0
        self.show_question()

    #Menampilkan pertanyaan quiz
    def show_question(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        question = self.questions[self.current_question]
        ttk.Label(self.main_frame, text=f"{self.current_question+1}. {question['question']}", 
                 font=('Helvetica', 14)).pack(pady=20)
        
        self.choice_var = tk.StringVar()
        for i, choice in enumerate(question['choices']):
            ttk.Radiobutton(self.main_frame, text=choice, variable=self.choice_var, value=choice).pack()
        
        ttk.Button(self.main_frame, text="Selanjutnya", 
                  command=self.check_answer).pack(pady=10)
        
    #Check jawaban yang diinput user dengan jawaban yang benar
    def check_answer(self):
        percentage = (self.current_question) / len(self.questions) * 100
        question = self.questions[self.current_question]
        if self.choice_var.get() == question['answer']:
            self.score += 1
        
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Hasil Akhir", f"Kuis selesai!\nNilai: {percentage:.2f}%")
            self.show_quiz_menu()

#Jalanin aplikasi
root = tk.Tk()
app = QuizApp(root)
root.iconbitmap(".Logo_ITERA.ico")
root.mainloop()