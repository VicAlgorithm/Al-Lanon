from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.popup import Popup
from datetime import datetime
from database.connection import Database
from bson.objectid import ObjectId


class FormularioInventarioScreen(Screen):
    def __init__(self, **kwargs):
        super(FormularioInventarioScreen, self).__init__(**kwargs)
        self.name = 'formulario_inventario'
        self.db = Database()
        self.usuario_actual = None
        self.fecha_actual = None
        self.es_edicion = False
        self.checkboxes = {}  # Diccionario para guardar los checkboxes por día

        # Las 13 preguntas del inventario emocional
        self.preguntas = [
            "¿He perdido la paciencia?\n\"Dios concédeme la serenidad\"",
            "¿He sido egocéntrico hoy?\n\"Pasos Seis, Siete, Ocho y Nueve\"",
            "¿He rebajado a otros?\n\"Aceptación de otros\"",
            "¿He pedido la ayuda que necesito de mi poder superior?\n\"Suelta las riendas y entrégaselas a Dios\"",
            "Cuando me he equivocado, ¿lo he admitido espontáneamente?\n\"Valor para cambiar las cosas que puedo\"",
            "¿Me he preocupado o me he excedido en reaccionar?\n\"Suelta las riendas y entrégaselas a Dios\"",
            "¿He criticado a otros?\n\"Vive y deja vivir\"",
            "¿Soy irrespetuoso y he contestado con malos modales?\n\"Dios concédeme la sabiduría...\"",
            "¿He olvidado que el alcoholismo es una enfermedad de la familia?\n\"Primer paso\"",
            "¿He sentido autocompasión?\n\"Las reuniones nos ayudan\"",
            "¿He culpado a otros por mis acciones hoy?\n\"¿Cuánta importancia tiene eso?\"",
            "¿He trabajado hoy en alguno de mis defectos?\n\"Valor para cambiar las cosas que puedo\"",
            "¿He estado hoy resentido?\n\"Tercer paso; Mantenlo siempre\""
        ]

        # Ya no necesitamos los días de la semana
        # self.dias_semana = ['L', 'M', 'M', 'J', 'V', 'S', 'D']

    def set_usuario(self, usuario):
        """Establece el usuario actual"""
        self.usuario_actual = usuario

    def set_fecha(self, fecha):
        """Establece la fecha del inventario"""
        self.fecha_actual = fecha

    def set_es_edicion(self, es_edicion):
        """Establece si es modo edición o nuevo registro"""
        self.es_edicion = es_edicion

    def cargar_inventario(self, inventario):
        """Carga un inventario existente para visualización/edición"""
        self.inventario_actual = inventario
        self.mostrar_formulario()

    def mostrar_formulario(self):
        """Muestra el formulario de inventario"""
        self.clear_widgets()
        self.checkboxes = {}

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
            padding=[20, 100, 20, 20],
            spacing=15,
            size_hint=(1, 1)
        )

        # Título
        titulo_text = 'Editar Inventario' if self.es_edicion else 'Inventario Emocional Diario'
        titulo = Label(
            text=titulo_text,
            font_size='28sp',
            color=(0.95, 0.95, 0.90, 1),
            bold=True,
            size_hint=(1, 0.06),
            halign='center'
        )
        titulo.bind(size=titulo.setter('text_size'))
        main_layout.add_widget(titulo)

        # Fecha
        fecha_label = Label(
            text=f'Fecha: {self.fecha_actual}',
            font_size='20sp',
            color=(0.95, 0.95, 0.90, 1),
            size_hint=(1, 0.04),
            halign='center'
        )
        fecha_label.bind(size=fecha_label.setter('text_size'))
        main_layout.add_widget(fecha_label)

        # ScrollView para las preguntas
        scroll = ScrollView(size_hint=(1, 0.75))

        # Grid para las preguntas
        preguntas_layout = GridLayout(
            cols=1,
            spacing=15,
            size_hint_y=None,
            padding=[10, 10]
        )
        preguntas_layout.bind(minimum_height=preguntas_layout.setter('height'))

        # Agregar cada pregunta con checkbox simple SÍ/NO
        for i, pregunta in enumerate(self.preguntas):
            # Contenedor externo con fondo azul (borde)
            borde_container = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=110,
                padding=[3, 3]  # Grosor del borde
            )

            # Fondo azul para el borde
            with borde_container.canvas.before:
                Color(0.29, 0.49, 0.61, 1)  # Azul
                borde_container.rect = Rectangle(pos=borde_container.pos, size=borde_container.size)

            borde_container.bind(pos=self._update_borde_rect, size=self._update_borde_rect)

            # Contenedor interno con fondo blanco
            pregunta_container = BoxLayout(
                orientation='horizontal',
                size_hint=(1, 1),
                spacing=15,
                padding=[15, 10]
            )

            # Fondo blanco para cada pregunta
            with pregunta_container.canvas.before:
                Color(1, 1, 1, 1)  # Blanco
                pregunta_container.rect = Rectangle(pos=pregunta_container.pos, size=pregunta_container.size)

            pregunta_container.bind(pos=self._update_pregunta_rect, size=self._update_pregunta_rect)

            # Texto de pregunta en negro (lado izquierdo)
            pregunta_label = Label(
                text=f"{i+1}. {pregunta}",
                font_size='16sp',
                color=(0, 0, 0, 1),  # Negro
                size_hint=(0.75, 1),
                halign='left',
                valign='middle',
                text_size=(Window.width * 0.55, None),
                bold=True
            )

            # Contenedor para los checkboxes SÍ/NO (lado derecho)
            checkbox_container = BoxLayout(
                orientation='horizontal',
                size_hint=(0.25, 1),
                spacing=5,
                padding=[5, 10]
            )

            # Columna SÍ
            si_container = BoxLayout(orientation='vertical', size_hint=(0.5, 1), spacing=2)
            si_label = Label(
                text='SÍ',
                font_size='16sp',
                color=(0.29, 0.49, 0.61, 1),
                size_hint=(1, 0.3),
                bold=True
            )
            checkbox_si = CheckBox(
                size_hint=(1, 0.7),
                active=False,
                group=f'pregunta_{i}',
                color=(0.29, 0.49, 0.61, 1)
            )

            # Columna NO
            no_container = BoxLayout(orientation='vertical', size_hint=(0.5, 1), spacing=2)
            no_label = Label(
                text='NO',
                font_size='16sp',
                color=(0.29, 0.49, 0.61, 1),
                size_hint=(1, 0.3),
                bold=True
            )
            checkbox_no = CheckBox(
                size_hint=(1, 0.7),
                active=False,
                group=f'pregunta_{i}',
                color=(0.29, 0.49, 0.61, 1)
            )

            # Si estamos en modo edición, cargar valor
            if self.es_edicion and hasattr(self, 'inventario_actual'):
                respuestas = self.inventario_actual.get('respuestas', {})
                key = f"p{i}"
                valor = respuestas.get(key, None)
                if valor is True:
                    checkbox_si.active = True
                elif valor is False:
                    checkbox_no.active = True
            else:
                # Por defecto, ninguno está seleccionado
                pass

            self.checkboxes[i] = {'si': checkbox_si, 'no': checkbox_no}

            si_container.add_widget(si_label)
            si_container.add_widget(checkbox_si)
            no_container.add_widget(no_label)
            no_container.add_widget(checkbox_no)

            checkbox_container.add_widget(si_container)
            checkbox_container.add_widget(no_container)

            pregunta_container.add_widget(pregunta_label)
            pregunta_container.add_widget(checkbox_container)

            borde_container.add_widget(pregunta_container)
            preguntas_layout.add_widget(borde_container)

        scroll.add_widget(preguntas_layout)
        main_layout.add_widget(scroll)

        # Botones
        botones_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.08),
            spacing=20,
            padding=[50, 0]
        )

        btn_guardar = Button(
            text='Guardar',
            font_size='20sp',
            background_color=(0.95, 0.95, 0.90, 1),
            color=(0.29, 0.49, 0.61, 1),
            bold=True,
            background_normal=''
        )
        btn_guardar.bind(on_press=self.guardar_inventario)

        btn_volver = Button(
            text='Volver',
            font_size='20sp',
            background_color=(0.75, 0.75, 0.70, 1),
            color=(0.29, 0.49, 0.61, 1),
            background_normal=''
        )
        btn_volver.bind(on_press=self.volver_dashboard)

        botones_layout.add_widget(btn_guardar)
        botones_layout.add_widget(btn_volver)

        main_layout.add_widget(botones_layout)

        float_layout.add_widget(main_layout)
        self.add_widget(float_layout)

    def guardar_inventario(self, instance):
        """Guarda el inventario en la base de datos"""
        # Recopilar respuestas (SÍ=True, NO=False, sin marcar=None)
        respuestas = {}
        for i in range(len(self.preguntas)):
            key = f"p{i}"
            if self.checkboxes[i]['si'].active:
                respuestas[key] = True
            elif self.checkboxes[i]['no'].active:
                respuestas[key] = False
            else:
                respuestas[key] = None

        collection = self.db.get_collection('miembros')

        # Obtener el usuario actual
        usuario = collection.find_one({"_id": ObjectId(self.usuario_actual['id'])})

        if not usuario:
            self.mostrar_popup("Error", "Usuario no encontrado")
            return

        # Buscar si ya existe un registro para esta fecha
        registros = usuario.get('registros', [])
        encontrado = False

        for registro in registros:
            if registro['fecha'] == self.fecha_actual:
                # Actualizar registro existente
                registro['respuestas'] = respuestas
                registro['fecha_modificacion'] = datetime.now().isoformat()
                # Incrementar contador de ediciones
                registro['veces_editado'] = registro.get('veces_editado', 0) + 1
                encontrado = True
                break

        if not encontrado:
            # Crear nuevo registro
            nuevo_registro = {
                'fecha': self.fecha_actual,
                'respuestas': respuestas,
                'fecha_creacion': datetime.now().isoformat(),
                'veces_editado': 0
            }
            registros.append(nuevo_registro)

        # Actualizar en la base de datos
        collection.update_one(
            {"_id": ObjectId(self.usuario_actual['id'])},
            {"$set": {"registros": registros}}
        )

        mensaje = "Inventario actualizado exitosamente" if encontrado else "Inventario guardado exitosamente"
        self.mostrar_popup("Éxito", mensaje, callback=self.volver_dashboard)

    def volver_dashboard(self, instance=None):
        """Vuelve al dashboard"""
        dashboard_screen = self.manager.get_screen('dashboard_miembro')
        dashboard_screen.set_usuario(self.usuario_actual)
        self.manager.current = 'dashboard_miembro'

    def mostrar_popup(self, titulo, mensaje, callback=None):
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
            size_hint=(0.7, 0.4)
        )

        if callback:
            btn_cerrar.bind(on_press=lambda x: (popup.dismiss(), callback()))
        else:
            btn_cerrar.bind(on_press=popup.dismiss)

        popup.open()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_pregunta_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def _update_borde_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
