
import os
import sys
from datetime import datetime

class Colors:
    """ANSI color codes for terminal styling"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'  # End color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    header = f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        🎓 SISTEMA INTELIGENTE DE CALIFICACIONES 🎓          ║
║                                                              ║
║              📊 Predicción de Notas Estudiantiles 📊        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Colors.ENDC}

{Colors.YELLOW}📅 Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}{Colors.ENDC}
{Colors.GREEN}🖥️  Sistema: Predictor de Calificaciones v1.0{Colors.ENDC}
"""
    print(header)

def print_menu():
    """Print the main menu with beautiful formatting"""
    menu = f"""
{Colors.BLUE}
┌───────────────────────────────────────────────────────────────────┐
│                         {Colors.BOLD}🏠 MENÚ PRINCIPAL{Colors.ENDC}{Colors.BLUE}                         │
└───────────────────────────────────────────────────────────────────┘{Colors.ENDC}

{Colors.GREEN}📋 OPCIONES DISPONIBLES:{Colors.ENDC}

{Colors.CYAN}   🔍 [1]{Colors.ENDC} {Colors.BOLD}Seleccionar estudiante por ID{Colors.ENDC}
{Colors.CYAN}   ➕ [2]{Colors.ENDC} {Colors.BOLD}Agregar nuevo estudiante{Colors.ENDC}
{Colors.CYAN}   🗑️  [3]{Colors.ENDC} {Colors.BOLD}Eliminar estudiante{Colors.ENDC}
{Colors.CYAN}   ✏️  [4]{Colors.ENDC} {Colors.BOLD}Modificar datos de estudiante por ID{Colors.ENDC}
{Colors.CYAN}   📃 [5]{Colors.ENDC} {Colors.BOLD}Listar todos los estudiantes{Colors.ENDC}
{Colors.CYAN}   🔮 [6]{Colors.ENDC} {Colors.BOLD}Predecir calificaciones y posibles fortalezas{Colors.ENDC}
{Colors.CYAN}   📊 [7]{Colors.ENDC} {Colors.BOLD}Ver estadísticas generales{Colors.ENDC}
{Colors.RED}   🚪 [8]{Colors.ENDC} {Colors.BOLD}Salir del sistema{Colors.ENDC}


"""
    print(menu)

def get_user_input():
    """Get user input with styled prompt"""
    prompt = f"{Colors.CYAN}🎯 Seleccione una opción (1-8): {Colors.ENDC}"
    return input(prompt).strip()

def print_success_message(message):
    """ success message with green styling"""
    print(f"\n{Colors.GREEN}✅ {message}{Colors.ENDC}")

def print_error_message(message):
    """error message with red styling"""
    print(f"\n{Colors.RED}❌ {message}{Colors.ENDC}")


def print_info_message(message):
    """ info message with blue styling"""
    print(f"\n{Colors.BLUE}ℹ️  {message}{Colors.ENDC}")


def wait_for_enter():
    """Wait for user to press Enter"""
    input(f"\n{Colors.YELLOW}📱 Presione Enter para continuar...{Colors.ENDC}")

def print_goodbye():
    """Print a goodbye message"""
 
    goodbye = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                  👋 ¡HASTA LUEGO! 👋                       ║
║                                                              ║
║          Gracias por usar el Sistema de Predicción          ║
║                    de Calificaciones                        ║
║                                                              ║
║                  🎓 ¡Que tengas un buen día! 🎓            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Colors.ENDC}
"""
    print(goodbye)

# Main menu loop
def main():
    """Main program loop"""
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        choice = get_user_input()
        
        if choice == '1':
            print_info_message("Función: Seleccionar estudiante por ID")
            # TODO: Implementar función para seleccionar estudiante
            wait_for_enter()
            
        elif choice == '2':
            print_info_message("Función: Agregar nuevo estudiante")
            # TODO: Implementar función para agregar estudiante
            wait_for_enter()
            
        elif choice == '3':
            print_info_message("Función: Eliminar estudiante")
            # TODO: Implementar función para eliminar estudiante
            wait_for_enter()
            
        elif choice == '4':
            print_info_message("Función: Modificar estudiante")
            # TODO: Implementar función para modificar estudiante
            wait_for_enter()
            
        elif choice == '5':
            print_info_message("Función: Listar estudiantes")
            # TODO: Implementar función para listar estudiantes
            wait_for_enter()
            
        elif choice == '6':
            print_info_message("Función: Predecir calificaciones")
            # TODO: Implementar función de predicción
            wait_for_enter()
            
        elif choice == '7':
            print_info_message("Función: Ver estadísticas")
            # TODO: Implementar función de estadísticas
            wait_for_enter()
            
        elif choice == '8':
            clear_screen()
            print_goodbye()
            print_success_message("Sistema cerrado correctamente")
            sys.exit(0)
            
        else:
            print_error_message("Opción no válida. Por favor, seleccione una opción del 1 al 8.")
            wait_for_enter()

if __name__ == "__main__":
    main()

