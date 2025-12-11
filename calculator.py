from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(App):
    def build(self):
        # 主布局：垂直排列
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 1. 显示屏 (Label)
        self.result_label = Label(
            text='0', 
            font_size='40sp', 
            size_hint=(1, 0.3), 
            halign='right', 
            valign='middle',
            text_size=(self.width, None)
        )
        self.main_layout.add_widget(self.result_label)

        # 2. 按钮区域 (网格布局)
        button_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.7))

        # 按钮文本定义
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # 创建按钮并绑定事件
        for btn_text in buttons:
            button = Button(text=btn_text, font_size='30sp')
            button.bind(on_press=self.on_button_press)
            button_layout.add_widget(button)

        self.main_layout.add_widget(button_layout)
        return self.main_layout

    def on_button_press(self, instance):
        current_text = self.result_label.text
        button_text = instance.text

        if button_text == 'C':
            # 清除
            self.result_label.text = '0'
        elif button_text == '=':
            # 计算结果
            try:
                # 使用 eval 执行计算 (仅用于简单示例，实际生产环境需用更安全的解析方法)
                result = str(eval(current_text))
                self.result_label.text = result
            except Exception:
                self.result_label.text = 'Error'
        else:
            # 数字和运算符输入
            if current_text == '0' or current_text == 'Error':
                self.result_label.text = button_text
            else:
                self.result_label.text += button_text

if __name__ == '__main__':
    CalculatorApp().run()
