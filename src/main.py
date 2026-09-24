import customtkinter as ctk
from model import TTSModel
from view import TTSView
from controller import TTSController

def main():
    root = ctk.CTk()
    
    model = TTSModel()
    view = TTSView(root)
    
    # O Controller recebe as instâncias, mantendo o baixo acoplamento
    controller = TTSController(model, view)
    
    root.mainloop()

if __name__ == "__main__":
    main()