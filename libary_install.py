
import importlib
import subprocess
import sys
import shutil
import os

def install_with_apt(package):
    """Installiert ein Paket mit apt, falls apt verfügbar ist."""
    if shutil.which("apt"):
        try:
            subprocess.check_call(["sudo", "apt", "install", "-y", package])
            return True
        except subprocess.CalledProcessError:
            print(f"[FEHLER] Konnte {package} nicht mit apt installieren.")
    else:
        print("[INFO] apt nicht verfügbar, manuelle Installation erforderlich.")
    return False

def check_and_install(module, package=None, system_package=None):
    try:
        importlib.import_module(module)
        print(f"[OK] {module} ist installiert.")
    except ImportError:
        print(f"[FEHLT] {module}...")
        if system_package:
            print(f"  -> Versuche Systempaket {system_package} zu installieren...")
            if not install_with_apt(system_package):
                print(f"  -> Bitte manuell installieren: sudo apt install {system_package}")
        else:
            package = package or module
            print(f"  -> Wird mit pip installiert: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def function_to_check():
    print("=== Python Umgebung prüfen ===")
    print(f"Python Version: {sys.version}\n")

    if not shutil.which("pip"):
        print("[WARNUNG] pip scheint nicht installiert zu sein. Versuche es nachzuziehen...")
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])

    check_and_install("tkinter", system_package="python3-tk")
    check_and_install("sqlite3", system_package="python3-sqlite")
    check_and_install("pip")
    check_and_install("matplotlib")
    check_and_install("numpy")

    print("\n=== Überprüfung abgeschlossen ===")
