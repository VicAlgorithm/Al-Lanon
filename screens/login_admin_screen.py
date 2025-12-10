from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
from kivy.core.window import Window
from database.connection import Database
from database.models import Administrador


class LoginAdminScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginAdminScreen, self).__init__(**kwargs)
        self.name = 'login_admin'
        self.db = Database()
        self.mostrar_login()

    def mostrar_login(self):
        """Muestra el formulario de login"""
        self.clear_widgets()

        # Layout principal con FloatLayout para posicionar el logo
        float_layout = FloatLayout()

        # Fondo azul
        with float_layout.canvas.before:
            Color(0.29, 0.49, 0.61, 1)  # Azul del logo
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

        # Layout para el contenido
        layout = BoxLayout(
            orientation='vertical',
            padding=[60, 120, 60, 40],
            spacing=15,
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Título
        title = Label(
            text='Iniciar Sesión',
            font_size='36sp',
            color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            bold=True,
            size_hint=(1, 0.15),
            halign='center'
        )
        title.bind(size=title.setter('text_size'))

        # Subtítulo
        subtitle = Label(
            text='Administrador',
            font_size='24sp',
            color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            size_hint=(1, 0.08),
            halign='center'
        )
        subtitle.bind(size=subtitle.setter('text_size'))

        # Email
        label_email = Label(
            text='Email:',
            font_size='20sp',
            color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            size_hint=(1, 0.08),
            halign='left'
        )
        label_email.bind(size=label_email.setter('text_size'))

        self.input_email = TextInput(
            hint_text='admin@ejemplo.com',
            multiline=False,
            size_hint=(1, 0.1),
            font_size='18sp',
            background_color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            foreground_color=(0.29, 0.49, 0.61, 1),  # Texto azul
            cursor_color=(0.29, 0.49, 0.61, 1)
        )

        # Password
        label_password = Label(
            text='Contraseña:',
            font_size='20sp',
            color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            size_hint=(1, 0.08),
            halign='left'
        )
        label_password.bind(size=label_password.setter('text_size'))

        self.input_password = TextInput(
            hint_text='********',
            password=True,
            multiline=False,
            size_hint=(1, 0.1),
            font_size='18sp',
            background_color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            foreground_color=(0.29, 0.49, 0.61, 1),  # Texto azul
            cursor_color=(0.29, 0.49, 0.61, 1)
        )

        # Botón login
        btn_login = Button(
            text='Iniciar Sesión',
            font_size='22sp',
            size_hint=(1, 0.12),
            bold=True,
            background_color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            color=(0.29, 0.49, 0.61, 1),  # Texto azul
            background_normal=''
        )
        btn_login.bind(on_press=self.login)

        # Botón cambiar a registro
        btn_to_register = Button(
            text='¿No tienes cuenta? Regístrate',
            font_size='18sp',
            size_hint=(1, 0.1),
            background_color=(0.85, 0.85, 0.80, 1),  # Crema más oscuro
            color=(0.29, 0.49, 0.61, 1),  # Texto azul
            background_normal=''
        )
        btn_to_register.bind(on_press=lambda x: self.mostrar_registro())

        # Botón volver
        btn_volver = Button(
            text='Volver',
            font_size='18sp',
            size_hint=(1, 0.1),
            background_color=(0.75, 0.75, 0.70, 1),  # Crema más oscuro
            color=(0.29, 0.49, 0.61, 1),  # Texto azul
            background_normal=''
        )
        btn_volver.bind(on_press=self.volver)

        # Agregar widgets
        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(label_email)
        layout.add_widget(self.input_email)
        layout.add_widget(label_password)
        layout.add_widget(self.input_password)
        layout.add_widget(btn_login)
        layout.add_widget(btn_to_register)
        layout.add_widget(BoxLayout(size_hint=(1, 0.05)))
        layout.add_widget(btn_volver)

        float_layout.add_widget(layout)
        self.add_widget(float_layout)

    def mostrar_registro(self):
        """Muestra el formulario de registro"""
        self.clear_widgets()

        # Layout principal con FloatLayout para posicionar el logo
        float_layout = FloatLayout()

        # Fondo azul
        with float_layout.canvas.before:
            Color(0.29, 0.49, 0.61, 1)  # Azul del logo
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

        # Layout para el contenido
        layout = BoxLayout(
            orientation='vertical',
            padding=[60, 120, 60, 40],
            spacing=10,
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Título
        title = Label(
            text='Registro de Administrador',
            font_size='36sp',
            color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            bold=True,
            size_hint=(1, 0.1),
            halign='center'
        )
        title.bind(size=title.setter('text_size'))

        # Nombre
        label_nombre = Label(
            text='Nombre completo:',
            font_size='20sp',
            color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            size_hint=(1, 0.06),
            halign='left'
        )
        label_nombre.bind(size=label_nombre.setter('text_size'))

        self.input_nombre = TextInput(
            hint_text='Tu nombre',
            multiline=False,
            size_hint=(1, 0.08),
            font_size='18sp',
            background_color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            foreground_color=(0.29, 0.49, 0.61, 1),  # Texto azul
            cursor_color=(0.29, 0.49, 0.61, 1)
        )

        # Email
        label_email = Label(
            text='Email:',
            font_size='20sp',
            color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            size_hint=(1, 0.06),
            halign='left'
        )
        label_email.bind(size=label_email.setter('text_size'))

        self.input_email = TextInput(
            hint_text='admin@ejemplo.com',
            multiline=False,
            size_hint=(1, 0.08),
            font_size='18sp',
            background_color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            foreground_color=(0.29, 0.49, 0.61, 1),  # Texto azul
            cursor_color=(0.29, 0.49, 0.61, 1)
        )

        # Password
        label_password = Label(
            text='Contraseña:',
            font_size='20sp',
            color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            size_hint=(1, 0.06),
            halign='left'
        )
        label_password.bind(size=label_password.setter('text_size'))

        self.input_password = TextInput(
            hint_text='********',
            password=True,
            multiline=False,
            size_hint=(1, 0.08),
            font_size='18sp',
            background_color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            foreground_color=(0.29, 0.49, 0.61, 1),  # Texto azul
            cursor_color=(0.29, 0.49, 0.61, 1)
        )

        # Código de acceso
        label_codigo = Label(
            text='Código de acceso:',
            font_size='20sp',
            color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            size_hint=(1, 0.06),
            halign='left'
        )
        label_codigo.bind(size=label_codigo.setter('text_size'))

        self.input_codigo = TextInput(
            hint_text='Código maestro',
            password=True,
            multiline=False,
            size_hint=(1, 0.08),
            font_size='18sp',
            background_color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            foreground_color=(0.29, 0.49, 0.61, 1),  # Texto azul
            cursor_color=(0.29, 0.49, 0.61, 1)
        )

        # Botón registro
        btn_registro = Button(
            text='Registrarse',
            font_size='22sp',
            size_hint=(1, 0.1),
            bold=True,
            background_color=(0.95, 0.95, 0.90, 1),  # Crema/blanco
            color=(0.29, 0.49, 0.61, 1),  # Texto azul
            background_normal=''
        )
        btn_registro.bind(on_press=self.registrar)

        # Botón cambiar a login
        btn_to_login = Button(
            text='¿Ya tienes cuenta? Inicia sesión',
            font_size='18sp',
            size_hint=(1, 0.08),
            background_color=(0.85, 0.85, 0.80, 1),  # Crema más oscuro
            color=(0.29, 0.49, 0.61, 1),  # Texto azul
            background_normal=''
        )
        btn_to_login.bind(on_press=lambda x: self.mostrar_login())

        # Botón volver
        btn_volver = Button(
            text='Volver',
            font_size='18sp',
            size_hint=(1, 0.08),
            background_color=(0.75, 0.75, 0.70, 1),  # Crema más oscuro
            color=(0.29, 0.49, 0.61, 1),  # Texto azul
            background_normal=''
        )
        btn_volver.bind(on_press=self.volver)

        # Agregar widgets
        layout.add_widget(title)
        layout.add_widget(label_nombre)
        layout.add_widget(self.input_nombre)
        layout.add_widget(label_email)
        layout.add_widget(self.input_email)
        layout.add_widget(label_password)
        layout.add_widget(self.input_password)
        layout.add_widget(label_codigo)
        layout.add_widget(self.input_codigo)
        layout.add_widget(btn_registro)
        layout.add_widget(btn_to_login)
        layout.add_widget(btn_volver)

        float_layout.add_widget(layout)
        self.add_widget(float_layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def login(self, instance):
        """Maneja el login de administrador"""
        email = self.input_email.text
        password = self.input_password.text

        if not email or not password:
            self.mostrar_popup("Error", "Por favor completa todos los campos")
            return

        collection = self.db.get_collection('administradores')
        resultado = Administrador.login(collection, email, password)

        if resultado['success']:
            self.mostrar_popup("Exito", resultado['message'])
            # Aquí iremos a la pantalla principal del administrador
            # self.manager.current = 'dashboard_admin'
        else:
            self.mostrar_popup("Error", resultado['message'])

    def registrar(self, instance):
        """Maneja el registro de nuevo administrador"""
        nombre = self.input_nombre.text
        email = self.input_email.text
        password = self.input_password.text
        codigo = self.input_codigo.text

        if not nombre or not email or not password or not codigo:
            self.mostrar_popup("Error", "Por favor completa todos los campos")
            return

        collection = self.db.get_collection('administradores')
        resultado = Administrador.crear(collection, nombre, email, password, codigo)

        if resultado['success']:
            self.mostrar_popup("Exito", resultado['message'])
            self.mostrar_login()
        else:
            self.mostrar_popup("Error", resultado['message'])

    def volver(self, instance):
        """Vuelve a la pantalla de bienvenida"""
        self.manager.current = 'welcome'

    def mostrar_popup(self, titulo, mensaje):
        """Muestra un popup con un mensaje"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        label = Label(
            text=mensaje,
            size_hint=(1, 0.7),
            color=(0.29, 0.49, 0.61, 1)
        )

        btn_cerrar = Button(
            text='Cerrar',
            size_hint=(1, 0.3),
            background_color=(0.29, 0.49, 0.61, 1),
            color=(0.95, 0.95, 0.90, 1),
            background_normal=''
        )

        content.add_widget(label)
        content.add_widget(btn_cerrar)

        popup = Popup(
            title=titulo,
            content=content,
            size_hint=(0.7, 0.4),
            background_color=(0.95, 0.95, 0.90, 1)
        )
        btn_cerrar.bind(on_press=popup.dismiss)
        popup.open()
