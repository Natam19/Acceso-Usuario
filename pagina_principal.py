from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Line

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class FirstApp(App):

    def build(self):
        # Obtener el tamaño de la pantalla del dispositivo
        Window.size = (360, 640)

        # Crear el ScreenManager
        screen_manager = ScreenManager()

        # Crear las pantallas
        first_screen = FirstScreen(name='first_screen')
        second_screen = SecondScreen(name='second_screen')

        # Agregar las pantallas al ScreenManager
        screen_manager.add_widget(first_screen)
        screen_manager.add_widget(second_screen)

        # Configurar la primera pantalla
        first_layout = RelativeLayout()
        background = Image(source='./source/portada.jpg', allow_stretch=True, keep_ratio=False, size_hint=(None, None), size=(360, 640))
        first_layout.add_widget(background)

        btn_iniciar_sesion = Button(text='Iniciar Sesión', 
                                    size_hint=(None, None), 
                                    size=(252, 40), 
                                    pos=(54, 62),
                                    color="#000000",  # Color del texto
                                    background_color= '#FFFFFF',  # Color de fondo del botón
                                    background_normal="",  # Eliminar la apariencia predeterminada
                                    )
        btn_iniciar_sesion.bind(on_press=self.go_to_second_screen)
        self.draw_border(btn_iniciar_sesion)  # Dibujar el borde
        first_layout.add_widget(btn_iniciar_sesion)

        btn_crear_cuenta = Button(text='Crear Cuenta', 
                                  size_hint=(None, None), 
                                  size=(252, 40), 
                                  pos=(54 ,127), 
                                  background_color= '#A86E45',
                                  background_normal="")
        btn_crear_cuenta.bind(on_press=self.go_to_second_screen)  
        first_layout.add_widget(btn_crear_cuenta)

        first_screen.add_widget(first_layout)

        # Configurar la segunda pantalla
        second_layout = RelativeLayout()
        background = Image(source='./source/fondo_negro.jpg', allow_stretch=True, keep_ratio=False, size_hint=(None, None), size=(360, 640))
        second_layout.add_widget(background)

        btn_volver = Button(text='Volver',
                            size_hint=(None, None),
                            size=(100, 40),
                            pos=(10, 590))
        btn_volver.bind(on_press=self.go_back_to_first_screen)
        second_layout.add_widget(btn_volver)

        second_screen.add_widget(second_layout)

        return screen_manager

    def go_to_second_screen(self, instance):
        self.root.current = 'second_screen'

    def go_back_to_first_screen(self, instance):
        self.root.current = 'first_screen'

    def draw_border(self, widget):
        with widget.canvas.before:
            Color(0, 0, 0, 1)  # Establecer el color del borde a negro
            Line(rectangle=(widget.x, widget.y, widget.width, widget.height), width=1)

if __name__ == '__main__':
    FirstApp().run()

