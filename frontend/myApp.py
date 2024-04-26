from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window


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


class CircleButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(CircleButton, self).__init__(**kwargs)
        self.color = (0, 0, 0, 1)  # Set the color of the image to black
        self.allow_stretch = True  # Allow stretching the image to fit the button


class MainApp(App):
    def build(self):
        # Configuring window size
        Config.set('graphics', 'width', '400')  # Set the width for a mobile-friendly layout
        Config.set('graphics', 'height', '600')
        Config.write()

        # Set window background color and text color
        Window.clearcolor = (1, 1, 1, 1)  # Set background color to white
        Window.color = (0, 0, 0, 1)  # Set text color to black

        # Screen manager
        sm = ScreenManager()
        sm.add_widget(MilkProductionScreen(name='ranchs'))
        sm.add_widget(CostStructureScreen(name='cost_structure'))
        sm.add_widget(ProductionPlanScreen(name='production_plan'))

        # Main layout
        layout = BoxLayout(orientation='vertical')

        # Menu
        menu_layout = GridLayout(cols=5, size_hint_y=None, height=50, spacing=10)  # Add spacing between buttons
        menu_layout.add_widget(Button(text='Fincas', on_release=lambda x: sm.current_screen(name='ranchs'),
                                       background_color=(0.6, 0.8, 1, 1),  # Set background color to light blue
                                       font_size='14sp'))  # Adjust font size
        menu_layout.add_widget(Button(text='Estructura de costos', on_release=lambda x: sm.current_screen(name='Cost Structure'),
                                       background_color=(0.6, 0.8, 1, 1),  # Set background color to light blue
                                       font_size='14sp'))  # Adjust font size
        menu_layout.add_widget(Button(text='Plan de produccion', on_release=lambda x: sm.current_screen(name='Production Plan'),
                                       background_color=(0.6, 0.8, 1, 1),  # Set background color to light blue
                                       font_size='14sp'))  # Adjust font size

        # Content area
        content_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        # Milk button
        milk_button = CircleButton(source='frontend/milk.jpg', size_hint=(None, None), size=(dp(100), dp(100)))
        milk_button.bind(on_release=lambda x: self.open_module('Milk Production'))
        content_layout.add_widget(milk_button)

        layout.add_widget(menu_layout)
        layout.add_widget(content_layout)

        return layout

    def open_module(self, module_name):
        print(f'Opening {module_name}')


if __name__ == '__main__':
    MainApp().run()
