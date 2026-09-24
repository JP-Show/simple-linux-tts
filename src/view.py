import customtkinter as ctk
from tkinter import messagebox


class TTSView(ctk.CTk):
    def __init__(self, root):
        self.root = root
        self.root.title("Simple TTS")
        self.root.geometry("1200x1100")

        # Configuração do modo escuro
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")
        ctk.set_widget_scaling(2)

        # Entrada de Texto Principal
        self.lbl_text = ctk.CTkLabel(self.root, text="Texto para converter em áudio:")
        self.lbl_text.pack(pady=(15, 0), padx=20, anchor="w")
        
        self.text_input = ctk.CTkTextbox(self.root, height=120, width=560)
        self.text_input.pack(pady=(5, 15), padx=20)
        self.text_input.insert("1.0", "David was a thirty-eight-year-old accountant. He lived and worked in a big city.")

        # Seleção de Idioma
        self.lbl_lang = ctk.CTkLabel(self.root, text="Idioma Disponível:")
        self.lbl_lang.pack(pady=(5, 0), padx=20, anchor="w")
        
        self.lang_var = ctk.StringVar(value="Inglês")
        self.lang_menu = ctk.CTkOptionMenu(self.root, values=["Inglês"], variable=self.lang_var, width=560, state="disabled")
        self.lang_menu.pack(pady=(5, 15), padx=20)

        # Seleção de Sotaque
        self.lbl_accent = ctk.CTkLabel(self.root, text="Sotaque:")
        self.lbl_accent.pack(pady=(5, 0), padx=20, anchor="w")
        
        self.accent_var = ctk.StringVar(value="Britânico")
        self.accent_menu = ctk.CTkOptionMenu(self.root, values=["Britânico", "Americano"], variable=self.accent_var, width=560)
        self.accent_menu.pack(pady=(5, 15), padx=20)

        # Prompt de Tonalidade
        self.lbl_tone = ctk.CTkLabel(self.root, text="Prompt para tonalização da voz:")
        self.lbl_tone.pack(pady=(5, 0), padx=20, anchor="w")
        
        self.tone_input = ctk.CTkEntry(self.root, width=560, placeholder_text="Ex: storytelling tone, native speed")
        self.tone_input.pack(pady=(5, 20), padx=20)

        # Container para os Botões
        self.btn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.btn_frame.pack(pady=10, fill="x", padx=20)

        self.test_btn = ctk.CTkButton(self.btn_frame, text="Ouvir Áudio (Testar)")
        self.test_btn.pack(side="left", expand=True, padx=(0, 10))

        self.save_btn = ctk.CTkButton(self.btn_frame, text="Salvar Arquivo")
        self.save_btn.pack(side="right", expand=True, padx=(10, 0))

        # Callbacks
        self._generate_callback = None
        self._test_callback = None

    def bind_generate(self, callback):
        self._generate_callback = callback
        self.save_btn.configure(command=self._on_generate_click)

    def bind_test(self, callback):
        self._test_callback = callback
        self.test_btn.configure(command=self._on_test_click)

    def _build_style_string(self):
        accent_map = {
            "Britânico": "British English accent",
            "Americano": "American English accent"
        }
        
        accent = accent_map.get(self.accent_var.get(), "English accent")
        tone = self.tone_input.get().strip()

        if tone:
            return f"{tone}, {accent}"
        return accent

    def _on_generate_click(self):
        text = self.text_input.get("1.0", ctk.END).strip()
        style = self._build_style_string()
        
        if self._generate_callback:
            self._generate_callback(text, style)

    def _on_test_click(self):
        text = self.text_input.get("1.0", ctk.END).strip()
        style = self._build_style_string()
        
        if self._test_callback:
            self._test_callback(text, style)

    def show_success(self, message):
        messagebox.showinfo("Sucesso", message)

    def show_error(self, message):
        messagebox.showerror("Erro", message)