from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.label import Label


Builder.load_file('testsing.kv')

class TestApp(App):

    def build_config(self, config):
        config.setdefaults('section1', {'key1': 'value1', 'key2': '42' })
    
    def build(self):
        config = self.config
        return Label(text='key1 is %s and key2 is %d' % (config.get('section1', 'key1'),
        config.getint('section1', 'key2')))

if __name__ == '__main__':
    TestApp().run()
