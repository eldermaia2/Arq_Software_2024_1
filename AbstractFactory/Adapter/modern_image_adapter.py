from modern_image_library import ModernImageLibrary

class ModernImageAdapter:
    def __init__(self):
        # Cria uma instância da biblioteca moderna
        self.modern_image = ModernImageLibrary()

    def load_file(self, filename):
        # Adapta o método load para usar a interface moderna
        self.modern_image.load(filename)
    
    def display_image(self):
        # Adapta o método display_image para usar a interface moderna
        self.modern_image.render()
