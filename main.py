"""
AI hardware Benchmark

Project entry point 
"""
from core.config import Config

def print_banner():
    """Display Project Information."""
    print("=" * 50)
    print(Config.PROJECT_NAME)
    print(f"Version: {Config.VERSION}")
    print("=" * 50)

def main():
    """Application entry point."""
    print_banner()

    print("\nInitializing application...")
    print("Application started successfully.")

if __name__ == "__main__":
    main()

