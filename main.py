#!/usr/bin/env python3
import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from generator import CookieGenerator, CookieProfile

console = Console()

def show_banner():
    banner = """[yellow]
     _   _   _   _   _  
    / \ / \ / \ / \ / \ 
   ( C ( O ( O ( K ( I )
    \_/ \_/ \_/ \_/ \_/ 
          GENERATOR v2.1
    [/]"""
    console.print(Panel.fit(banner, style="bold red"))

def main_menu():
    while True:
        show_banner()
        console.print("\n[bold cyan]Main Menu:[/]")
        console.print("1. � Create New Cookie Profile")
        console.print("2. 📁 View Existing Cookies")
        console.print("3. ⚙️ System Config")
        console.print("4. 🚪 Exit")
        
        choice = console.input("\n[bold yellow]➤ Select (1-4): [/]")
        
        if choice == '1':
            create_profile()
        elif choice == '2':
            view_cookies()
        elif choice == '3':
            system_config()
        elif choice == '4':
            sys.exit()
        else:
            console.print("[red]Invalid![/]")

def create_profile():
    with Progress(transient=True) as progress:
        task = progress.add_task("[cyan]Initializing...", total=100)
        for _ in range(100):
            time.sleep(0.02)
            progress.update(task, advance=1)
    
    profile = CookieProfile()
    profile.configure()
    console.print(Panel.fit("[green]Profile created successfully![/]"))

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[red]Operation cancelled![/]")
        sys.exit()
