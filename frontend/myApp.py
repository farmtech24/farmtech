from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.image import Image


class MainScreen(Screen):
    pass


class CowScreen(Screen):
    pass


class MilkProductionScreen(Screen):
    pass


class CostStructureScreen(Screen):
    pass


class ProductionPlanScreen(Screen):
    pass


class CircleButton(ButtonBehavior, Label):
    pass


class MilkRecordScreen(Screen):
    def __init__(self, **kwargs):
        super(MilkRecordScreen, self).__init__(**kwargs)
        self.add_widgets()

    def add_widgets(self):
        layout = BoxLayout(orientation='vertical')

        # Welcome message
        welcome_label = Label(text="Bienvenido a Registro de Leche", font_size='20sp')
        layout.add_widget(welcome_label)

        # Button for "Crear Nueva Hoja de Registro"
        create_record_button = Button(text="Crear Nueva Hoja de Registro",
                                      on_release=self.create_new_record)
        layout.add_widget(create_record_button)

        self.add_widget(layout)

    def create_new_record(self, instance):
        print("Creating a new milk record...")


class MainApp(App):
    def build(self):
        # Configuring window size
        Config.set('graphics', 'width', '400')  # Set the width for a mobile-friendly layout
        Config.set('graphics', 'height', '600')
        Config.write()

        # Set window background color and text color
        Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Set background color to light gray
        Window.color = (0, 0, 0, 1)  # Set text color to black

        # Screen manager
        sm = ScreenManager()
        sm.add_widget(MilkProductionScreen(name='ranchs'))
        sm.add_widget(CostStructureScreen(name='cost_structure'))
        sm.add_widget(ProductionPlanScreen(name='production_plan'))
        sm.add_widget(MilkRecordScreen(name='registro_de_leche'))

        # Main layout
        layout = BoxLayout(orientation='vertical')

        # Menu
        menu_layout = GridLayout(cols=5, size_hint_y=None, height=50, spacing=10)  # Add spacing between buttons
        menu_layout.add_widget(
            Button(text='Estructura de costos', on_release=lambda x: self.change_screen(sm, 'cost_structure'),
                   background_color=(0.6, 0.8, 1, 1),  # Set background color to light blue
                   font_size='13sp'))  # Adjust font size
        menu_layout.add_widget(
            Button(text='Plan de produccion', on_release=lambda x: self.change_screen(sm, 'production_plan'),
                   background_color=(0.6, 0.8, 1, 1),  # Set background color to light blue
                   font_size='14sp'))  # Adjust font size

        # Content area
        content_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        # Background image
        background_image = Image(source='frontend/milk.jpg', allow_stretch=True, keep_ratio=False)
        content_layout.add_widget(background_image)

        # Adding buttons
        buttons_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), width=200, height=300)
        options = ['Perfil', 'Registro de Leche', 'Manejo de Inventarios', 'Suscripciones', 'Notas',
                   'Ayuda']
        for option in options:
            buttons_layout.add_widget(
                Button(text=option, on_release=lambda x, option=option: self.change_screen(sm, option),
                       size_hint=(None, None), width=180, height=40))

        content_layout.add_widget(buttons_layout)

        layout.add_widget(menu_layout)
        layout.add_widget(content_layout)

        return layout

    def change_screen(self, sm, screen_name):
        print(f"Changing screen to: {screen_name}")
        if screen_name == 'Registro de Leche':
            sm.current = 'registro_de_leche'
        else:
            sm.current = screen_name


if __name__ == '__main__':
    MainApp().run()
