import re
import os
import tkinter as tk
from PIL import Image, ImageTk


class LexicalAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Lexicográfico")

        # Cargar la imagen pequeña
        small_image_path = os.path.join(os.path.dirname(__file__), "logo_eafit_completo.png")
        if os.path.exists(small_image_path):
            small_image = Image.open(small_image_path)
            small_image = small_image.resize((50, 50), Image.BICUBIC)
            small_image = ImageTk.PhotoImage(small_image)
            # Crear un widget de etiqueta para mostrar la imagen
            self.small_image_label = tk.Label(root, image=small_image)
            self.small_image_label.image = small_image
            self.small_image_label.pack(side=tk.RIGHT, padx=10)  # Alinea a la derecha con un espacio de 10 píxeles

        self.label_input = tk.Label(root, text="Introduce un texto:")
        self.label_input.pack()

        self.text_input = tk.Text(root, height=5, width=40)
        self.text_input.pack()

        self.button_analyze = tk.Button(root, text="Analizar", command=self.analyze_text)
        self.button_analyze.pack()

        self.label_result = tk.Label(root, text="Resultado:")
        self.label_result.pack()

        self.result_text = tk.Text(root, height=5, width=40)
        self.result_text.pack()

        self.label_emojis = tk.Label(root, text="Emojis:")
        self.label_emojis.pack()

        self.emojis_frame = tk.Frame(root)
        self.emojis_frame.pack()

        # Almacena las imágenes en una lista global para evitar la recolección de basura
        self.emoji_images = []

    def analyze_text(self):
        text_input = self.text_input.get("1.0", "end-1c")
        words = re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ]+\b', text_input)

        # Expresión regular actualizada para encontrar emojis
        emojis = re.findall(r'[:;][-oOpP]?[)D(]|:\(|<3|B\)|:\ñ|:7|>:0|:\*|:v|:#', text_input)

        result = "Palabras en español encontradas:\n" + ", ".join(words)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

        self.show_emojis(emojis)

    def show_emojis(self, emojis):
        for widget in self.emojis_frame.winfo_children():
            widget.destroy()

        # Rutas de las imágenes en la carpeta "imagenes"
        emoji_folder = {
            ":)": "imagenes/006-feliz-1.png",
            ":D": "imagenes/005-sonriente.png",
            ";)": "imagenes/018-guino.png",
            ":(": "imagenes/009-triste.png",
            ":o": "imagenes/012-conmocionado.png",
            ":p": "imagenes/011-emoji.png",
            "<3": "imagenes/001-emoji.png",
            "B)": "imagenes/002-emoticonos.png",
            ":ñ": "imagenes/033-pensando-1.png",
            ":7": "imagenes/007-pensando.png",
            ">:0": "imagenes/011-enojado.png",
            ":*": "imagenes/017-partido.png",
            ":v": "imagenes/034-relamerse.png",
            ":#": "imagenes/037-jurar.png",
        }

        # Almacena las imágenes en la lista global
        self.emoji_images = []

        for emoji in emojis:
            if emoji in emoji_folder:
                emoji_path = os.path.join(os.path.dirname(__file__), emoji_folder[emoji])
                if os.path.exists(emoji_path):
                    img = Image.open(emoji_path)
                    # Escala la imagen a un tamaño más pequeño (ajusta según tus necesidades)
                    img = img.resize((30, 30), Image.BICUBIC)
                    img = ImageTk.PhotoImage(img)
                    self.emoji_images.append(img)
                    label = tk.Label(self.emojis_frame, image=img)
                    label.image = img
                    label.pack()


def main():
    root = tk.Tk()
    app = LexicalAnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
