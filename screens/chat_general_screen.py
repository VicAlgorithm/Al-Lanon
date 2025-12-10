from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from datetime import datetime
from database.connection import Database


class ChatGeneralScreen(Screen):
    def __init__(self, **kwargs):
        super(ChatGeneralScreen, self).__init__(**kwargs)
        self.name = 'chat_general'
        self.db = Database()
        self.usuario_actual = None

    def set_usuario(self, usuario):
        """Establece el usuario actual y carga el chat"""
        self.usuario_actual = usuario
        self.cargar_chat()

    def cargar_chat(self):
        """Carga la interfaz del chat"""
        self.clear_widgets()

        # Layout principal
        float_layout = FloatLayout()

        # Fondo azul
        with float_layout.canvas.before:
            Color(0.29, 0.49, 0.61, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)

        float_layout.bind(size=self._update_rect, pos=self._update_rect)

        # Logo pequeño
        logo = Image(
            source='assets/Logo.png',
            size_hint=(None, None),
            size=(120, 80),
            pos_hint={'right': 0.98, 'top': 0.98},
            allow_stretch=True,
            keep_ratio=True
        )
        float_layout.add_widget(logo)

        # Layout principal
        main_layout = BoxLayout(
            orientation='vertical',
            padding=[40, 100, 40, 20],
            spacing=15,
            size_hint=(1, 1)
        )

        # Título
        titulo = Label(
            text='Chat General',
            font_size='32sp',
            color=(0.95, 0.95, 0.90, 1),
            bold=True,
            size_hint=(1, 0.08),
            halign='center'
        )
        titulo.bind(size=titulo.setter('text_size'))
        main_layout.add_widget(titulo)

        # Subtítulo
        subtitulo = Label(
            text='Comparte tus experiencias y apoya a otros miembros',
            font_size='16sp',
            color=(0.85, 0.85, 0.80, 1),
            size_hint=(1, 0.05),
            halign='center'
        )
        subtitulo.bind(size=subtitulo.setter('text_size'))
        main_layout.add_widget(subtitulo)

        # Obtener mensajes del chat
        collection = self.db.get_collection('chat_general')
        mensajes = list(collection.find().sort('fecha', 1))  # Ordenar por fecha ascendente

        # ScrollView para los mensajes
        scroll = ScrollView(size_hint=(1, 0.65))

        self.mensajes_layout = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None,
            padding=[10, 10]
        )
        self.mensajes_layout.bind(minimum_height=self.mensajes_layout.setter('height'))

        if not mensajes:
            # No hay mensajes
            mensaje_vacio = Label(
                text='No hay mensajes aún.\n\n¡Sé el primero en compartir!',
                font_size='18sp',
                color=(0.95, 0.95, 0.90, 1),
                halign='center'
            )
            mensaje_vacio.bind(size=mensaje_vacio.setter('text_size'))
            self.mensajes_layout.add_widget(mensaje_vacio)
        else:
            # Mostrar mensajes
            for msg in mensajes:
                self.agregar_mensaje_ui(msg)

        scroll.add_widget(self.mensajes_layout)
        main_layout.add_widget(scroll)

        # Área de escritura de mensaje
        input_container = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.12),
            spacing=10,
            padding=[10, 5]
        )

        self.input_mensaje = TextInput(
            hint_text='Escribe tu mensaje aquí...',
            multiline=True,
            size_hint=(0.75, 1),
            font_size='16sp',
            background_color=(0.95, 0.95, 0.90, 1),
            foreground_color=(0.29, 0.49, 0.61, 1),
            cursor_color=(0.29, 0.49, 0.61, 1)
        )

        btn_enviar = Button(
            text='Enviar',
            font_size='18sp',
            size_hint=(0.25, 1),
            background_color=(0.95, 0.95, 0.90, 1),
            color=(0.29, 0.49, 0.61, 1),
            bold=True,
            background_normal=''
        )
        btn_enviar.bind(on_press=self.enviar_mensaje)

        input_container.add_widget(self.input_mensaje)
        input_container.add_widget(btn_enviar)

        main_layout.add_widget(input_container)

        # Botón volver
        btn_volver = Button(
            text='Volver al Dashboard',
            font_size='20sp',
            size_hint=(1, None),
            height=55,
            background_color=(0.95, 0.95, 0.90, 1),
            color=(0.29, 0.49, 0.61, 1),
            bold=True,
            background_normal=''
        )
        btn_volver.bind(on_press=self.volver_dashboard)

        volver_container = BoxLayout(
            size_hint=(1, 0.1),
            padding=[80, 5, 80, 5]
        )
        volver_container.add_widget(btn_volver)

        main_layout.add_widget(volver_container)

        float_layout.add_widget(main_layout)
        self.add_widget(float_layout)

        # Auto-scroll al final
        scroll.scroll_y = 0

    def agregar_mensaje_ui(self, mensaje):
        """Agrega un mensaje a la interfaz"""
        # Contenedor del mensaje
        mensaje_container = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=100,
            spacing=5,
            padding=[10, 10]
        )

        # Fondo blanco semi-transparente
        with mensaje_container.canvas.before:
            Color(0.95, 0.95, 0.90, 0.95)
            mensaje_container.rect = Rectangle(pos=mensaje_container.pos, size=mensaje_container.size)

        mensaje_container.bind(pos=self._update_mensaje_rect, size=self._update_mensaje_rect)

        # Header: nombre y fecha
        header_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.3),
            spacing=10
        )

        nombre_label = Label(
            text=mensaje['nombre_usuario'],
            font_size='16sp',
            color=(0.29, 0.49, 0.61, 1),
            size_hint=(0.7, 1),
            halign='left',
            valign='middle',
            bold=True
        )
        nombre_label.bind(size=nombre_label.setter('text_size'))

        # Formatear fecha
        try:
            fecha_dt = datetime.fromisoformat(mensaje['fecha'])
            fecha_texto = fecha_dt.strftime('%d/%m/%Y %H:%M')
        except:
            fecha_texto = mensaje['fecha']

        fecha_label = Label(
            text=fecha_texto,
            font_size='12sp',
            color=(0.6, 0.6, 0.6, 1),
            size_hint=(0.3, 1),
            halign='right',
            valign='middle'
        )
        fecha_label.bind(size=fecha_label.setter('text_size'))

        header_layout.add_widget(nombre_label)
        header_layout.add_widget(fecha_label)

        # Contenido del mensaje
        contenido_label = Label(
            text=mensaje['mensaje'],
            font_size='15sp',
            color=(0.2, 0.2, 0.2, 1),
            size_hint=(1, 0.7),
            halign='left',
            valign='top',
            text_size=(Window.width * 0.7, None)
        )

        mensaje_container.add_widget(header_layout)
        mensaje_container.add_widget(contenido_label)

        self.mensajes_layout.add_widget(mensaje_container)

    def enviar_mensaje(self, instance):
        """Envía un mensaje al chat"""
        texto = self.input_mensaje.text.strip()

        if not texto:
            return

        # Guardar en la base de datos
        collection = self.db.get_collection('chat_general')

        nuevo_mensaje = {
            'usuario_id': self.usuario_actual['id'],
            'nombre_usuario': self.usuario_actual['nombre'],
            'mensaje': texto,
            'fecha': datetime.now().isoformat()
        }

        collection.insert_one(nuevo_mensaje)

        # Agregar a la interfaz
        self.agregar_mensaje_ui(nuevo_mensaje)

        # Limpiar input
        self.input_mensaje.text = ''

        # Scroll al final
        # Note: Esto requiere acceso al ScrollView, lo haremos simple
        self.mensajes_layout.height = self.mensajes_layout.minimum_height

    def volver_dashboard(self, instance):
        """Vuelve al dashboard"""
        if self.usuario_actual:
            dashboard_screen = self.manager.get_screen('dashboard_miembro')
            dashboard_screen.set_usuario(self.usuario_actual)
            self.manager.current = 'dashboard_miembro'

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_mensaje_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
