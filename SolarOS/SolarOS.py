import tkinter as tk
from tkinter import messagebox, simpledialog
import time

class SolarOS:
    def __init__(self, root):
        self.root = root
        self.root.title("SolarOS v2.0")
        self.root.geometry("900x600")
        self.root.configure(bg="#FDB813")  # Amarelo Solar

        # Estado do Sistema
        self.theme_color = "#FDB813"
        self.text_color = "black"

        self.login_screen()

    def login_screen(self):
        self.login_frame = tk.Frame(self.root, bg=self.theme_color)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.login_frame, text="SOLAR OS", font=("Arial", 30, "bold"), bg=self.theme_color).pack(pady=20)
        
        self.pass_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 14), justify="center")
        self.pass_entry.pack(pady=10)
        self.pass_entry.insert(0, "solar123") # Dica preenchida

        tk.Button(self.login_frame, text="Entrar", command=self.check_login, width=15, bg="#FF8C00", fg="white").pack(pady=10)

    def check_login(self):
        if self.pass_entry.get() == "solar123":
            self.login_frame.destroy()
            self.main_desktop()
        else:
            messagebox.showerror("Erro", "Senha Incorreta!")

    def main_desktop(self):
        # Barra de Tarefas (Horizon)
        self.horizon = tk.Frame(self.root, bg="#2D2D2D", height=40)
        self.horizon.pack(fill="x", side="top")

        self.clock_label = tk.Label(self.horizon, text="", bg="#2D2D2D", fg="white", font=("Arial", 10))
        self.clock_label.pack(side="right", padx=20)
        self.update_clock()

        # Grid de Aplicativos
        self.app_area = tk.Frame(self.root, bg=self.theme_color)
        self.app_area.pack(expand=True, fill="both", padx=50, pady=50)

        apps = [
            ("Calendário", "📅", self.open_calendar),
            ("Bloco Notas", "📝", self.open_notes),
            ("Temas", "🎨", self.open_themes),
            ("Terminal", "💻", self.open_terminal)
        ]

        for i, (name, icon, func) in enumerate(apps):
            btn = tk.Button(self.app_area, text=f"{icon}\n{name}", font=("Arial", 12),
                            command=func, width=12, height=5, bg="white", relief="flat")
            btn.grid(row=0, column=i, padx=20)

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.clock_label.config(text=f"SolarTime: {now}")
        self.root.after(1000, self.update_clock)

    # --- APLICATIVOS ---
    def open_calendar(self):
        win = tk.Toplevel(self.root)
        win.title("Calendário")
        win.geometry("300x200")
        tk.Label(win, text=time.strftime("%B %Y"), font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(win, text="Seg Ter Qua Qui Sex Sab Dom\n  1   2   3   4   5   6   7...").pack()

    def open_notes(self):
        win = tk.Toplevel(self.root)
        win.title("Flare Notes")
        text_area = tk.Text(win)
        text_area.pack(expand=True, fill="both")
        tk.Button(win, text="Salvar", command=lambda: messagebox.showinfo("Flare", "Nota Salva!")).pack()

    def open_themes(self):
        color = simpledialog.askstring("Temas", "Digite a cor em Inglês (Ex: Blue, Grey, Orange):")
        if color:
            self.root.configure(bg=color)
            self.app_area.configure(bg=color)

    def open_terminal(self):
        win = tk.Toplevel(self.root)
        win.title("Solar Terminal")
        win.configure(bg="black")
        label = tk.Label(win, text="SolarOS Prompt >", fg="#00FF00", bg="black", font=("Courier", 12))
        label.pack(anchor="w")
        entry = tk.Entry(win, bg="black", fg="#00FF00", insertbackground="white")
        entry.pack(fill="x")

if __name__ == "__main__":
    root = tk.Tk()
    app = SolarOS(root)
    root.mainloop()