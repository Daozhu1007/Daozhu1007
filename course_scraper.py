import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin


class CourseScraper:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://kean-ss.colleague.elluciancloud.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session.headers.update(self.headers)

    def login(self, username, password):
        """
        登录到Kean University系统
        注意：这只是一个示例，实际登录流程可能更复杂
        """
        login_url = f"{self.base_url}/Student/Home/Login"
        
        try:
            # 首先获取登录页面，可能需要CSRF token
            login_page = self.session.get(login_url)
            soup = BeautifulSoup(login_page.content, 'html.parser')
            
            # 查找登录表单
            form = soup.find('form')
            if not form:
                print("未找到登录表单")
                return False
            
            # 构建登录数据
            login_data = {
                'username': username,
                'password': password
            }
            
            # 添加可能存在的隐藏字段（如CSRF token）
            for hidden_input in form.find_all('input', type='hidden'):
                name = hidden_input.get('name')
                value = hidden_input.get('value', '')
                if name:
                    login_data[name] = value
            
            # 提交登录请求
            response = self.session.post(login_url, data=login_data)
            
            # 检查是否登录成功（这需要根据实际网站响应调整）
            if "dashboard" in response.url.lower() or "home" in response.url.lower():
                print("登录成功")
                return True
            else:
                print("登录失败")
                return False
                
        except Exception as e:
            print(f"登录过程中出现错误: {e}")
            return False

    def get_course_data(self):
        """
        获取课程数据
        """
        url = f"{self.base_url}/Student/Planning/DegreePlans"
        
        try:
            response = self.session.get(url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # 根据页面结构解析课程信息
                # 注意：这需要根据实际页面结构调整
                courses = self._parse_course_data(soup)
                
                return courses
            else:
                print(f"获取课程页面失败: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"获取课程数据时出现错误: {e}")
            return []

    def _parse_course_data(self, soup):
        """
        解析课程数据
        注意：此方法需要根据实际页面结构调整
        """
        courses = []
        
        # 示例解析逻辑（需要根据实际页面结构修改）
        # 查找可能包含课程信息的元素
        course_elements = soup.find_all(['tr', 'div', 'li'], 
                                      attrs={'class': re.compile(r'course|class|section|schedule', re.I)})
        
        if not course_elements:
            # 如果没有找到特定类名的元素，尝试更通用的查找方式
            # 在表格中查找课程信息
            tables = soup.find_all('table')
            for table in tables:
                rows = table.find_all('tr')
                for row in rows[1:]:  # 跳过标题行
                    cols = row.find_all(['td', 'th'])
                    if len(cols) >= 3:  # 假设至少有3列信息
                        try:
                            course_name = cols[0].get_text(strip=True)
                            # 这里需要根据实际页面结构调整
                            spots_text = cols[-1].get_text(strip=True)  # 假设最后一个单元格包含位置信息
                            
                            # 尝试从文本中提取数字
                            spot_match = re.search(r'(\d+)', spots_text)
                            spots = int(spot_match.group(1)) if spot_match else 0
                            
                            if course_name and spots >= 0:
                                courses.append({
                                    'name': course_name,
                                    'spots': spots
                                })
                        except:
                            continue
        
        # 如果仍然没有找到数据，返回示例数据
        if not courses:
            print("使用示例数据，因为无法从页面解析实际数据")
            courses = [
                {'name': 'CS 101 - Introduction to Computer Science', 'spots': 15},
                {'name': 'ENG 101 - English Composition', 'spots': 8},
                {'name': 'MATH 100 - College Algebra', 'spots': 22},
                {'name': 'BIO 101 - General Biology', 'spots': 5},
                {'name': 'HIST 101 - World History', 'spots': 30}
            ]
        
        return courses

    def test_connection(self):
        """
        测试与网站的连接
        """
        try:
            response = self.session.get(self.base_url)
            return response.status_code == 200
        except:
            return False