import importlib
import subprocess
import sys

# Liste der Module, die geprüft werden sollen
modules = {
    "tkinter": "tkinter",
    "sqlite3": "sqlite3",
    "matplotlib": "matplotlib",
    "numpy": "numpy",
    "pip": "pip"
}

def check_and_install(module, package=None):
    """Prüft, ob ein Modul importierbar ist, und installiert es falls nötig."""
    try:
        importlib.import_module(module)
        print(f"[OK] {module} ist installiert.")
    except ImportError:
        print(f"[FEHLT] {module} wird installiert...")
        if package is None:
            package = module
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def function_to_check():
    print("=== Python Umgebung prüfen ===")
    print(f"Python Version: {sys.version}\n")

    for module, package in modules.items():
        check_and_install(module, package)

    print("\nÜberprüfung abgeschlossen.")

