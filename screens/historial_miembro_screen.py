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
from database.connection import Database
from bson.objectid import ObjectId


class HistorialMiembroScreen(Screen):
    def __init__(self, **kwargs):
        super(HistorialMiembroScreen, self).__init__(**kwargs)
        self.name = 'historial_miembro'
        self.db = Database()
        self.usuario_actual = None

    def set_usuario(self, usuario):
        """Establece el usuario actual y carga el historial"""
        self.usuario_actual = usuario
        self.cargar_historial()

    def cargar_historial(self):
        """Carga el historial de registros"""
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
            text='Historial de Registros',
            font_size='32sp',
            color=(0.95, 0.95, 0.90, 1),
            bold=True,
            size_hint=(1, 0.08),
            halign='center'
        )
        titulo.bind(size=titulo.setter('text_size'))
        main_layout.add_widget(titulo)

        # Obtener registros del usuario
        collection = self.db.get_collection('miembros')
        usuario = collection.find_one({"_id": ObjectId(self.usuario_actual['id'])})

        registros = usuario.get('registros', []) if usuario else []

        if not registros:
            # No hay registros
            mensaje = Label(
                text='Aún no tienes registros.\n\nComienza llenando tu primer\nInventario Emocional.',
                font_size='20sp',
                color=(0.95, 0.95, 0.90, 1),
                size_hint=(1, 0.7),
                halign='center'
            )
            mensaje.bind(size=mensaje.setter('text_size'))
            main_layout.add_widget(mensaje)
        else:
            # Ordenar registros por fecha (más recientes primero)
            registros_ordenados = sorted(registros, key=lambda x: x['fecha'], reverse=True)

            # ScrollView para los registros
            scroll = ScrollView(size_hint=(1, 0.75))

            registros_layout = GridLayout(
                cols=1,
                spacing=10,
                size_hint_y=None,
                padding=[20, 10]
            )
            registros_layout.bind(minimum_height=registros_layout.setter('height'))

            for registro in registros_ordenados:
                fecha = registro['fecha']
                respuestas = registro['respuestas']
                veces_editado = registro.get('veces_editado', 0)

                # Calcular total de checks marcados (SÍ)
                total_checks = sum(1 for v in respuestas.values() if v is True)

                # Contenedor del registro
                registro_container = BoxLayout(
                    orientation='horizontal',
                    size_hint_y=None,
                    height=100,
                    spacing=15,
                    padding=[10, 10]
                )

                # Información del registro
                info_layout = BoxLayout(orientation='vertical', size_hint_x=0.6)

                fecha_label = Label(
                    text=f'Fecha: {fecha}',
                    font_size='18sp',
                    color=(0.95, 0.95, 0.90, 1),
                    size_hint=(1, 0.4),
                    halign='left',
                    valign='bottom'
                )
                fecha_label.bind(size=fecha_label.setter('text_size'))

                checks_label = Label(
                    text=f'Respuestas SÍ: {total_checks}/{len(respuestas)}',
                    font_size='14sp',
                    color=(0.85, 0.85, 0.80, 1),
                    size_hint=(1, 0.3),
                    halign='left',
                    valign='middle'
                )
                checks_label.bind(size=checks_label.setter('text_size'))

                ediciones_label = Label(
                    text=f'Veces editado: {veces_editado}',
                    font_size='13sp',
                    color=(0.80, 0.80, 0.75, 1),
                    size_hint=(1, 0.3),
                    halign='left',
                    valign='top'
                )
                ediciones_label.bind(size=ediciones_label.setter('text_size'))

                info_layout.add_widget(fecha_label)
                info_layout.add_widget(checks_label)
                info_layout.add_widget(ediciones_label)

                # Botones
                botones_layout = BoxLayout(orientation='horizontal', size_hint_x=0.4, spacing=10)

                btn_ver = Button(
                    text='Ver/Editar',
                    font_size='16sp',
                    background_color=(0.95, 0.95, 0.90, 1),
                    color=(0.29, 0.49, 0.61, 1),
                    background_normal=''
                )
                btn_ver.bind(on_press=lambda x, f=fecha, r=registro: self.ver_registro(f, r))

                botones_layout.add_widget(btn_ver)

                registro_container.add_widget(info_layout)
                registro_container.add_widget(botones_layout)

                registros_layout.add_widget(registro_container)

            scroll.add_widget(registros_layout)
            main_layout.add_widget(scroll)

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

    def ver_registro(self, fecha, registro):
        """Ver y editar un registro específico"""
        formulario_screen = self.manager.get_screen('formulario_inventario')
        formulario_screen.set_usuario(self.usuario_actual)
        formulario_screen.set_fecha(fecha)
        formulario_screen.set_es_edicion(True)
        formulario_screen.cargar_inventario(registro)
        self.manager.current = 'formulario_inventario'

    def volver_dashboard(self, instance):
        """Vuelve al dashboard"""
        if self.usuario_actual:
            dashboard_screen = self.manager.get_screen('dashboard_miembro')
            dashboard_screen.set_usuario(self.usuario_actual)
            self.manager.current = 'dashboard_miembro'
        else:
            print("Error: usuario_actual es None")

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
