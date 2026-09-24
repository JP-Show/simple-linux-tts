import threading
import pygame

class TTSController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Inicializa o mixer do pygame para reprodução de áudio
        pygame.mixer.init()
        
        # Injeta as funções na View (callbacks)
        self.view.bind_generate(self.handle_generate)
        self.view.bind_test(self.handle_test)
        
        # Injeta a função handle_generate na View (callback)
        self.view.bind_generate(self.handle_generate)

    def handle_generate(self, text, style):
        if not text and style:
            self.view.show_error("O campo de texto não pode estar vazio.")
            return

        try:
            self.model.generate_audio(text, style)
            self.view.show_success("Áudio gerado e salvo como 'output.wav'.")
        except Exception as e:
            self.view.show_error(f"Falha na geração do áudio: {str(e)}")

    def handle_test(self, text, style):
        if not text:
            self.view.show_error("O campo de texto não pode estar vazio.")
            return

        # Executa o processo em uma thread separada para não congelar a interface gráfica (CustomTkinter)
        threading.Thread(target=self._play_audio_thread, args=(text, style), daemon=True).start()

    def _play_audio_thread(self, text, style):
        temp_file = "temp_test.wav"
        try:
            # Para a reprodução atual, caso o usuário clique várias vezes
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            # Libera o arquivo temporário caso ele já esteja carregado na memória
            pygame.mixer.music.unload()

            # Gera o arquivo de áudio temporário via Model
            self.model.generate_audio(text, style, output_filename=temp_file)
            
            # Carrega e reproduz o áudio temporário
            pygame.mixer.music.load(temp_file)
            pygame.mixer.music.play()
            
        except Exception as e:
            self.view.show_error(f"Falha ao testar o áudio: {str(e)}")