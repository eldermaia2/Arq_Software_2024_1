from legacy_image_library import LegacyImageLibrary
from modern_image_adapter import ModernImageAdapter

def main():
    # Cria uma instância do Adapter
    adapter = ModernImageAdapter()
    
    # Usa o Adapter como se fosse uma LegacyImageLibrary
    adapter.load_file("example.jpg")
    adapter.display_image()

if __name__ == "__main__":
    main()
