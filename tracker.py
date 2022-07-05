import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

class Ball(Widget):
    """
    This class implements the functionality of our ball which we want to drag and track the position of.

    It will visually look like a ball, and will return its coordinates on the pitch at regular intervals
    """
    pass


class PitchBackground(Widget):
    """
        This class builds our background of the app - which uses the image Australian_Rules_Football_Field.png
        to create a background for the app.
    """
    pass




class BallTrackingApp(App):
    def build(self):
        return PitchBackground() # return the root widget


if __name__ == '__main__':
    BallTrackingApp().run()
