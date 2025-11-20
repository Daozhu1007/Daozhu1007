import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import re
from bs4 import BeautifulSoup
from course_scraper import CourseScraper


class CourseTrackerApp(App):
    def build(self):
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 标题
        title_label = Label(text='Kean University 课程位置追踪器', size_hint_y=None, height=50)
        main_layout.add_widget(title_label)
        
        # 登录表单布局
        login_layout = GridLayout(cols=2, size_hint_y=None, height=100, spacing=10)
        
        # 用户名输入
        login_layout.add_widget(Label(text='用户名:', size_hint_x=None, width=100))
        self.username_input = TextInput(multiline=False)
        login_layout.add_widget(self.username_input)
        
        # 密码输入
        login_layout.add_widget(Label(text='密码:', size_hint_x=None, width=100))
        self.password_input = TextInput(password=True, multiline=False)
        login_layout.add_widget(self.password_input)
        
        main_layout.add_widget(login_layout)
        
        # 登录按钮
        self.login_button = Button(text='登录', size_hint_y=None, height=50)
        self.login_button.bind(on_press=self.login_and_fetch_data)
        main_layout.add_widget(self.login_button)
        
        # 刷新按钮
        self.refresh_button = Button(text='刷新课程数据', size_hint_y=None, height=50)
        self.refresh_button.bind(on_press=self.refresh_data)
        self.refresh_button.disabled = True  # 初始时禁用，登录后启用
        main_layout.add_widget(self.refresh_button)
        
        # 滚动视图用于显示课程信息
        self.scroll_view = ScrollView()
        self.data_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.data_layout.bind(minimum_height=self.data_layout.setter('height'))
        
        self.scroll_view.add_widget(self.data_layout)
        main_layout.add_widget(self.scroll_view)
        
        # 初始化课程抓取器
        self.scraper = CourseScraper()
        
        return main_layout

    def login_and_fetch_data(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        if not username or not password:
            self.show_message("请输入用户名和密码")
            return
            
        # 显示登录中提示
        self.data_layout.clear_widgets()
        loading_label = Label(text='正在登录...', size_hint_y=None, height=40)
        self.data_layout.add_widget(loading_label)
        
        try:
            # 尝试登录
            login_success = self.scraper.login(username, password)
            
            if login_success:
                # 登录成功，获取课程数据
                self.refresh_data(None)
                # 启用刷新按钮
                self.refresh_button.disabled = False
                # 禁用登录按钮（因为已经登录了）
                self.login_button.disabled = True
            else:
                self.data_layout.clear_widgets()
                error_label = Label(text='登录失败，请检查用户名和密码', size_hint_y=None, height=40)
                self.data_layout.add_widget(error_label)
                
        except Exception as e:
            self.data_layout.clear_widgets()
            error_label = Label(text=f'登录错误: {str(e)}', size_hint_y=None, height=40)
            self.data_layout.add_widget(error_label)

    def refresh_data(self, instance):
        # 清除现有数据
        self.data_layout.clear_widgets()
        
        # 添加加载提示
        loading_label = Label(text='正在加载课程数据...', size_hint_y=None, height=40)
        self.data_layout.add_widget(loading_label)
        
        try:
            courses = self.scraper.get_course_data()
            
            # 清除加载提示
            self.data_layout.clear_widgets()
            
            if courses:
                for course in courses:
                    course_label = Label(
                        text=f"{course['name']}: 剩余 {course['spots']} 个位置",
                        size_hint_y=None,
                        height=40,
                        halign='left',
                        valign='middle'
                    )
                    course_label.bind(size=course_label.setter('text_size'))
                    self.data_layout.add_widget(course_label)
            else:
                error_label = Label(text='无法获取课程数据', size_hint_y=None, height=40)
                self.data_layout.add_widget(error_label)
                
        except Exception as e:
            self.data_layout.clear_widgets()
            error_label = Label(text=f'错误: {str(e)}', size_hint_y=None, height=40)
            self.data_layout.add_widget(error_label)

    def show_message(self, message):
        # 显示消息的辅助方法
        self.data_layout.clear_widgets()
        msg_label = Label(text=message, size_hint_y=None, height=40)
        self.data_layout.add_widget(msg_label)


if __name__ == '__main__':
    CourseTrackerApp().run()