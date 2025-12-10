from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from datetime import datetime, date
from database.connection import Database


class DashboardMiembroScreen(Screen):
    def __init__(self, **kwargs):
        super(DashboardMiembroScreen, self).__init__(**kwargs)
        self.name = 'dashboard_miembro'
        self.db = Database()
        self.usuario_actual = None

    def set_usuario(self, usuario):
        """Establece el usuario actual y carga el dashboard"""
        self.usuario_actual = usuario
        self.cargar_dashboard()

    def cargar_dashboard(self):
        """Carga el dashboard del miembro"""
        self.clear_widgets()

        # Layout principal
        float_layout = FloatLayout()

        # Fondo azul
        with float_layout.canvas.before:
            Color(0.29, 0.49, 0.61, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)

        float_layout.bind(size=self._update_rect, pos=self._update_rect)

        # Logo pequeño en esquina superior derecha
        logo = Image(
            source='assets/Logo.png',
            size_hint=(None, None),
            size=(150, 100),
            pos_hint={'right': 0.98, 'top': 0.98},
            allow_stretch=True,
            keep_ratio=True
        )
        float_layout.add_widget(logo)

        # Layout principal de contenido
        main_layout = BoxLayout(
            orientation='vertical',
            padding=[40, 120, 40, 40],
            spacing=20,
            size_hint=(1, 1)
        )

        # Título de bienvenida
        welcome_label = Label(
            text=f'Bienvenido, {self.usuario_actual["nombre"]}',
            font_size='32sp',
            color=(0.95, 0.95, 0.90, 1),
            bold=True,
            size_hint=(1, 0.08),
            halign='center'
        )
        welcome_label.bind(size=welcome_label.setter('text_size'))
        main_layout.add_widget(welcome_label)

        # Verificar si ya llenó el inventario de hoy
        hoy = date.today().isoformat()
        inventario_hoy = self.verificar_inventario_hoy(hoy)

        # Contenedor de estado del día
        estado_container = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.25),
            padding=[80, 10, 80, 10],
            spacing=15
        )

        if inventario_hoy:
            # Ya llenó el inventario
            mensaje = Label(
                text='¡Inventario completado para hoy!\n\nGracias por tu dedicación.',
                font_size='24sp',
                color=(0.95, 0.95, 0.90, 1),
                size_hint=(1, 0.6),
                halign='center'
            )
            mensaje.bind(size=mensaje.setter('text_size'))

            btn_ver = Button(
                text='Ver inventario de hoy',
                font_size='20sp',
                size_hint=(1, None),
                height=55,
                background_color=(0.95, 0.95, 0.90, 1),
                color=(0.29, 0.49, 0.61, 1),
                bold=True,
                background_normal=''
            )
            btn_ver.bind(on_press=lambda x: self.ver_inventario(hoy))

            estado_container.add_widget(mensaje)
            estado_container.add_widget(btn_ver)
        else:
            # No ha llenado el inventario
            mensaje = Label(
                text='Aún no has completado tu\nInventario Emocional de hoy',
                font_size='24sp',
                color=(0.95, 0.95, 0.90, 1),
                size_hint=(1, 0.6),
                halign='center'
            )
            mensaje.bind(size=mensaje.setter('text_size'))

            btn_llenar = Button(
                text='Llenar Inventario',
                font_size='20sp',
                size_hint=(1, None),
                height=55,
                background_color=(0.95, 0.95, 0.90, 1),
                color=(0.29, 0.49, 0.61, 1),
                bold=True,
                background_normal=''
            )
            btn_llenar.bind(on_press=self.ir_a_formulario)

            estado_container.add_widget(mensaje)
            estado_container.add_widget(btn_llenar)

        main_layout.add_widget(estado_container)

        # Contenedor para los tres botones
        botones_container = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.25),
            spacing=10,
            padding=[80, 10, 80, 10]
        )

        # Botón ver historial
        btn_historial = Button(
            text='Ver Historial de Registros',
            font_size='20sp',
            size_hint=(1, None),
            height=55,
            background_color=(0.95, 0.95, 0.90, 1),
            color=(0.29, 0.49, 0.61, 1),
            bold=True,
            background_normal=''
        )
        btn_historial.bind(on_press=self.mostrar_historial)

        # Botón estadísticas
        btn_estadisticas = Button(
            text='Estadísticas Semanales',
            font_size='20sp',
            size_hint=(1, None),
            height=55,
            background_color=(0.95, 0.95, 0.90, 1),
            color=(0.29, 0.49, 0.61, 1),
            bold=True,
            background_normal=''
        )
        btn_estadisticas.bind(on_press=self.mostrar_estadisticas)

        # Botón chat general
        btn_chat = Button(
            text='Chat General',
            font_size='20sp',
            size_hint=(1, None),
            height=55,
            background_color=(0.95, 0.95, 0.90, 1),
            color=(0.29, 0.49, 0.61, 1),
            bold=True,
            background_normal=''
        )
        btn_chat.bind(on_press=self.mostrar_chat)

        botones_container.add_widget(btn_historial)
        botones_container.add_widget(btn_estadisticas)
        botones_container.add_widget(btn_chat)

        main_layout.add_widget(botones_container)

        # Espacio
        main_layout.add_widget(BoxLayout(size_hint=(1, 0.17)))

        # Botón cerrar sesión
        btn_logout = Button(
            text='Cerrar Sesión',
            font_size='18sp',
            size_hint=(1, None),
            height=50,
            background_color=(0.85, 0.85, 0.80, 1),
            color=(0.29, 0.49, 0.61, 1),
            background_normal=''
        )
        btn_logout.bind(on_press=self.cerrar_sesion)

        logout_container = BoxLayout(
            size_hint=(1, 0.1),
            padding=[100, 5, 100, 5]
        )
        logout_container.add_widget(btn_logout)

        main_layout.add_widget(logout_container)

        float_layout.add_widget(main_layout)
        self.add_widget(float_layout)

    def verificar_inventario_hoy(self, fecha):
        """Verifica si el usuario ya llenó el inventario para la fecha dada"""
        collection = self.db.get_collection('miembros')
        from bson.objectid import ObjectId

        usuario = collection.find_one({"_id": ObjectId(self.usuario_actual['id'])})

        if usuario and 'registros' in usuario:
            for registro in usuario['registros']:
                if registro['fecha'] == fecha:
                    return registro
        return None

    def ir_a_formulario(self, instance):
        """Va al formulario de inventario emocional"""
        formulario_screen = self.manager.get_screen('formulario_inventario')
        formulario_screen.set_usuario(self.usuario_actual)
        formulario_screen.set_fecha(date.today().isoformat())
        formulario_screen.set_es_edicion(False)
        formulario_screen.mostrar_formulario()
        self.manager.current = 'formulario_inventario'

    def ver_inventario(self, fecha):
        """Ver el inventario de una fecha específica"""
        inventario = self.verificar_inventario_hoy(fecha)
        if inventario:
            formulario_screen = self.manager.get_screen('formulario_inventario')
            formulario_screen.set_usuario(self.usuario_actual)
            formulario_screen.set_fecha(fecha)
            formulario_screen.set_es_edicion(True)
            formulario_screen.cargar_inventario(inventario)
            self.manager.current = 'formulario_inventario'

    def mostrar_historial(self, instance):
        """Muestra el historial de registros"""
        historial_screen = self.manager.get_screen('historial_miembro')
        historial_screen.set_usuario(self.usuario_actual)
        self.manager.current = 'historial_miembro'

    def mostrar_estadisticas(self, instance):
        """Muestra estadísticas del usuario"""
        estadisticas_screen = self.manager.get_screen('estadisticas')
        estadisticas_screen.set_usuario(self.usuario_actual)
        self.manager.current = 'estadisticas'

    def mostrar_chat(self, instance):
        """Muestra el chat general"""
        chat_screen = self.manager.get_screen('chat_general')
        chat_screen.set_usuario(self.usuario_actual)
        self.manager.current = 'chat_general'

    def cerrar_sesion(self, instance):
        """Cierra la sesión y vuelve a la pantalla de bienvenida"""
        self.usuario_actual = None
        self.manager.current = 'welcome'

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
