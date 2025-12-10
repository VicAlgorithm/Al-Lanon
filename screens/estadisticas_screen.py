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
from datetime import datetime, date, timedelta
from database.connection import Database
from bson.objectid import ObjectId


class EstadisticasScreen(Screen):
    def __init__(self, **kwargs):
        super(EstadisticasScreen, self).__init__(**kwargs)
        self.name = 'estadisticas'
        self.db = Database()
        self.usuario_actual = None

    def set_usuario(self, usuario):
        """Establece el usuario actual y carga las estadísticas"""
        self.usuario_actual = usuario
        self.cargar_estadisticas()

    def cargar_estadisticas(self):
        """Carga las estadísticas semanales"""
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
            text='Estadísticas Semanales',
            font_size='32sp',
            color=(0.95, 0.95, 0.90, 1),
            bold=True,
            size_hint=(1, 0.08),
            halign='center'
        )
        titulo.bind(size=titulo.setter('text_size'))
        main_layout.add_widget(titulo)

        # Subtítulo con rango de fechas
        hoy = date.today()
        hace_7_dias = hoy - timedelta(days=7)
        subtitulo = Label(
            text=f'Del {hace_7_dias.isoformat()} al {hoy.isoformat()}',
            font_size='18sp',
            color=(0.85, 0.85, 0.80, 1),
            size_hint=(1, 0.05),
            halign='center'
        )
        subtitulo.bind(size=subtitulo.setter('text_size'))
        main_layout.add_widget(subtitulo)

        # Obtener registros de la última semana
        collection = self.db.get_collection('miembros')
        usuario = collection.find_one({"_id": ObjectId(self.usuario_actual['id'])})

        registros = usuario.get('registros', []) if usuario else []

        # Filtrar registros de la última semana
        registros_semana = []
        for registro in registros:
            fecha_registro = datetime.fromisoformat(registro['fecha']).date()
            if hace_7_dias <= fecha_registro <= hoy:
                registros_semana.append(registro)

        if not registros_semana:
            # No hay registros en la semana
            mensaje = Label(
                text='No hay registros en los últimos 7 días.\n\nComienza llenando tu Inventario Emocional diario.',
                font_size='20sp',
                color=(0.95, 0.95, 0.90, 1),
                size_hint=(1, 0.7),
                halign='center'
            )
            mensaje.bind(size=mensaje.setter('text_size'))
            main_layout.add_widget(mensaje)
        else:
            # Calcular porcentajes por pregunta
            preguntas = [
                "¿He perdido la paciencia?",
                "¿He sido egocéntrico hoy?",
                "¿He rebajado a otros?",
                "¿He pedido la ayuda que necesito de mi poder superior?",
                "Cuando me he equivocado, ¿lo he admitido espontáneamente?",
                "¿Me he preocupado o me he excedido en reaccionar?",
                "¿He criticado a otros?",
                "¿Soy irrespetuoso y he contestado con malos modales?",
                "¿He olvidado que el alcoholismo es una enfermedad de la familia?",
                "¿He sentido autocompasión?",
                "¿He culpado a otros por mis acciones hoy?",
                "¿He trabajado hoy en alguno de mis defectos?",
                "¿He estado hoy resentido?"
            ]

            estadisticas = []
            for i in range(len(preguntas)):
                key = f"p{i}"
                total = 0
                respuestas_si = 0

                for registro in registros_semana:
                    respuestas = registro.get('respuestas', {})
                    if key in respuestas and respuestas[key] is not None:
                        total += 1
                        if respuestas[key] is True:
                            respuestas_si += 1

                porcentaje = (respuestas_si / total * 100) if total > 0 else 0
                estadisticas.append({
                    'pregunta': preguntas[i],
                    'porcentaje': porcentaje,
                    'total': total
                })

            # ScrollView para las estadísticas
            scroll = ScrollView(size_hint=(1, 0.7))

            stats_layout = GridLayout(
                cols=1,
                spacing=10,
                size_hint_y=None,
                padding=[10, 10]
            )
            stats_layout.bind(minimum_height=stats_layout.setter('height'))

            for i, stat in enumerate(estadisticas):
                # Contenedor para cada estadística
                stat_container = BoxLayout(
                    orientation='vertical',
                    size_hint_y=None,
                    height=80,
                    spacing=5,
                    padding=[10, 5]
                )

                # Fondo blanco semi-transparente
                with stat_container.canvas.before:
                    Color(0.95, 0.95, 0.90, 0.9)
                    stat_container.rect = Rectangle(pos=stat_container.pos, size=stat_container.size)

                stat_container.bind(pos=self._update_stat_rect, size=self._update_stat_rect)

                # Pregunta
                pregunta_label = Label(
                    text=f"{i+1}. {stat['pregunta']}",
                    font_size='14sp',
                    color=(0.29, 0.49, 0.61, 1),
                    size_hint=(1, 0.5),
                    halign='left',
                    valign='bottom',
                    text_size=(Window.width * 0.7, None),
                    bold=True
                )

                # Porcentaje y barra
                porcentaje_layout = BoxLayout(
                    orientation='horizontal',
                    size_hint=(1, 0.5),
                    spacing=10
                )

                # Barra de progreso
                barra_container = BoxLayout(
                    orientation='horizontal',
                    size_hint=(0.7, 1)
                )

                # Fondo de la barra (gris)
                barra_fondo = BoxLayout(size_hint=(1, 1))
                with barra_fondo.canvas.before:
                    Color(0.7, 0.7, 0.7, 1)
                    barra_fondo.rect = Rectangle(pos=barra_fondo.pos, size=barra_fondo.size)
                barra_fondo.bind(pos=self._update_barra_rect, size=self._update_barra_rect)

                # Barra de progreso (azul)
                barra_progreso = BoxLayout(size_hint=(stat['porcentaje']/100, 1))
                with barra_progreso.canvas.before:
                    Color(0.29, 0.49, 0.61, 1)
                    barra_progreso.rect = Rectangle(pos=barra_progreso.pos, size=barra_progreso.size)
                barra_progreso.bind(pos=self._update_barra_rect, size=self._update_barra_rect)

                barra_fondo.add_widget(barra_progreso)
                barra_container.add_widget(barra_fondo)

                # Texto del porcentaje
                porcentaje_label = Label(
                    text=f"{stat['porcentaje']:.1f}% SÍ",
                    font_size='16sp',
                    color=(0.29, 0.49, 0.61, 1),
                    size_hint=(0.3, 1),
                    halign='right',
                    valign='middle',
                    bold=True
                )
                porcentaje_label.bind(size=porcentaje_label.setter('text_size'))

                porcentaje_layout.add_widget(barra_container)
                porcentaje_layout.add_widget(porcentaje_label)

                stat_container.add_widget(pregunta_label)
                stat_container.add_widget(porcentaje_layout)

                stats_layout.add_widget(stat_container)

            scroll.add_widget(stats_layout)
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

    def volver_dashboard(self, instance):
        """Vuelve al dashboard"""
        if self.usuario_actual:
            dashboard_screen = self.manager.get_screen('dashboard_miembro')
            dashboard_screen.set_usuario(self.usuario_actual)
            self.manager.current = 'dashboard_miembro'

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_stat_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def _update_barra_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
