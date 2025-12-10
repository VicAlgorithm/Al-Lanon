from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from screens.welcome_screen import WelcomeScreen
from screens.login_miembro_screen import LoginMiembroScreen
from screens.login_admin_screen import LoginAdminScreen
from screens.dashboard_miembro_screen import DashboardMiembroScreen
from screens.formulario_inventario_screen import FormularioInventarioScreen
from screens.historial_miembro_screen import HistorialMiembroScreen
from screens.estadisticas_screen import EstadisticasScreen
from screens.chat_general_screen import ChatGeneralScreen
from database.connection import Database


class InventarioEmocionalApp(App):
    def build(self):
        # Conectar a la base de datos
        db = Database()
        if not db.connect():
            print("Error: No se pudo conectar a MongoDB. Verifica que esté corriendo.")
            print("Puedes iniciar MongoDB con: mongod")
            return None

        # Crear el gestor de pantallas
        sm = ScreenManager(transition=NoTransition())

        # Agregar las pantallas
        sm.add_widget(WelcomeScreen())
        sm.add_widget(LoginMiembroScreen())
        sm.add_widget(LoginAdminScreen())
        sm.add_widget(DashboardMiembroScreen())
        sm.add_widget(FormularioInventarioScreen())
        sm.add_widget(HistorialMiembroScreen())
        sm.add_widget(EstadisticasScreen())
        sm.add_widget(ChatGeneralScreen())

        return sm

    def on_stop(self):
        # Cerrar la conexión a la base de datos al cerrar la app
        db = Database()
        db.close()


if __name__ == '__main__':
    InventarioEmocionalApp().run()
