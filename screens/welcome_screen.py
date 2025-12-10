from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.core.window import Window


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        self.name = 'welcome'

        # Layout principal
        main_layout = BoxLayout(orientation='vertical', padding=0, spacing=0)

        # Fondo azul
        with main_layout.canvas.before:
            Color(0.29, 0.49, 0.61, 1)  # Color azul del logo #4A7C9C
            self.rect = Rectangle(size=Window.size, pos=self.pos)

        main_layout.bind(size=self._update_rect, pos=self._update_rect)

        # Espacio superior
        top_spacer = BoxLayout(size_hint=(1, 0.1))
        main_layout.add_widget(top_spacer)

        # Logo grande centrado
        logo = Image(
            source='assets/Logo.png',
            size_hint=(1, 0.35),
            allow_stretch=True,
            keep_ratio=True
        )
        main_layout.add_widget(logo)

        # Espacio medio
        middle_spacer = BoxLayout(size_hint=(1, 0.05))
        main_layout.add_widget(middle_spacer)

        # Contenedor de botones
        buttons_layout = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.35),
            spacing=20,
            padding=[100, 0, 100, 50]
        )

        # Botón Miembro con diseño mejorado
        btn_miembro = Button(
            text='Ingresar como Miembro',
            font_size='24sp',
            size_hint=(1, None),
            height=70,
            bold=True,
            color=(0.29, 0.49, 0.61, 1),  # Azul del logo
            background_normal='',
            background_color=(0.95, 0.95, 0.90, 1)  # Color crema/blanco del logo
        )
        btn_miembro.bind(on_press=self.ir_a_miembro)

        # Botón Administrador con diseño mejorado
        btn_admin = Button(
            text='Ingresar como Administrador',
            font_size='24sp',
            size_hint=(1, None),
            height=70,
            bold=True,
            color=(0.29, 0.49, 0.61, 1),  # Azul del logo
            background_normal='',
            background_color=(0.95, 0.95, 0.90, 1)  # Color crema/blanco del logo
        )
        btn_admin.bind(on_press=self.ir_a_admin)

        buttons_layout.add_widget(btn_miembro)
        buttons_layout.add_widget(btn_admin)

        main_layout.add_widget(buttons_layout)

        self.add_widget(main_layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def ir_a_miembro(self, instance):
        self.manager.current = 'login_miembro'

    def ir_a_admin(self, instance):
        self.manager.current = 'login_admin'
