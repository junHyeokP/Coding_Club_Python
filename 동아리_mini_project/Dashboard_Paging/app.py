from flask import Flask, render_template, request
import math
import json
# 플라스크로 프로젝트를 할 폴더에 가상환경을 만들고, 플라스크를 설치(pip install flask)
# 밑에서 부턴 AI가 작성한 주석 + 내 주석
# 가상환경을 활성화한 후 아래 코드를 실행합니다.
# 가상환경을 활성화하는 방법은 운영체제에 따라 다릅니다.
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

#-------------------------

# Flask에서는 URL을 방문 할 때 준비된 함수가 트리거되도록 바인딩 하기 위해 route() 데코레이터를 사용하며, 이를 라우팅이라 한다.
# 데코레이터는 함수의 기능을 확장하는 방법으로, Flask에서는 route() 데코레이터를 사용하여 URL과 함수를 연결한다.

# 템플릿 매개변수 if문 예제
# 
#{% if template_variable == "Hello" %}
#  <p>{{ template_variable }}, World!</p> 
#{% endif %}

# 템플릿 상속(include 기능)
#
# 웹 사이트 레이아웃의 일관성 유지, 또는 header와 footer를 여러곳에 사용하기 위해서 템플릿 상속 기능을 사용
# 부모문서를 만들고, 자식문서가 들어갈 부분에 {% block content %} {% endblock %}라고 작성
# 자식문서 윗부분에 {% extends 부모문서이름 %}라고 명시한 후 {% block content %}와 {% endblock %} 사이에 내용을 작성

#-------------------------

app = Flask(__name__)
# Flask 애플리케이션을 생성합니다. __name__은 현재 모듈의 이름을 나타내며, Flask는 이를 사용하여 애플리케이션의 루트 경로를 설정합니다.
# Flask 애플리케이션을 생성한 후, 라우팅을 설정하고, 템플릿을 렌더링하는 등의 작업을 수행할 수 있습니다.

# 페이지 데이터 예시
# 페이지 데이터는 예시로 딕셔너리 형태로 작성되어 있으며, 실제 애플리케이션에서는 데이터베이스나 다른 데이터 소스에서 가져올 수 있습니다.
# 페이지 데이터는 페이지 번호를 키로 하고, 각 페이지에 대한 정보를 딕셔너리 형태로 저장합니다.
# 페이지 데이터는 페이지 번호, 이름, 제목, 내용, 날짜 등의 정보를 포함하고 있습니다.
# 페이지 번호는 1부터 시작하며, 최대 페이지 수는 20으로 설정되어 있습니다.
max = 20

page_data = {
    1: {"Page 1" : {"page" : "1" , "name" : "홍길동", "title1" : "제목", "content1" : "내용", "date" : "2023-01-02"} } ,
    2: {"Page 2 info" : {"page" : "2" , "name" : "박준혁", "title2" : "제목", "content2" : "내용", "date" : "2023-01-03"} },
    3: {"Page 3 content" : {"page" : "3" , "name" : "이민수", "title3" : "제목", "content3" : "내용", "date" : "2023-01-04"} },
}

"""
[
  {"id": 1, "name": "홍길동", "title": "제목1", "content": "내용1", "date": "2023-01-02"},
  {"id": 2, "name": "박준혁", "title": "제목2", "content": "내용2", "date": "2023-01-03"},
  {"id": 3, "name": "이민수", "title": "제목3", "content": "내용3", "date": "2023-01-04"},
  // ...더 많은 데이터...
  {"id": 20, "name": "김철수", "title": "제목20", "content": "내용20", "date": "2023-01-21"}
]
"""
# 뷰 함수에서 return하는 응답은 일반 텍스트, 데이터 등 다양한 형식이 될 수 있다.
# 일반적으로는 웹 페이지에서 렌더링 할 HTML을 직접 반환하게 된다.
@app.route('/')
def home() :
    return  '''
    <h1>게시판 제목</h1>
    <p>게시판 내용</p>
    <a href="https://flask.palletsprojects.com">Flask 홈페이지 바로가기</a>
    '''

def load_data():
    with open('data.json', encoding='utf-8') as f:
        return json.load(f)



# "프로젝트 폴더"/templates/index.html 매핑
#@app.route('/')
#def index() :
#    return render_template("index.html")


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 5  # 한 페이지에 보여줄 게시글 수
    data = load_data()
    total = len(data)
    pages = math.ceil(total / per_page)
    start = (page - 1) * per_page
    end = start + per_page
    page_items = data[start:end]
    return render_template('dashboard.html', items=page_items, page=page, pages=pages)


# @page_number는 URL에서 페이지 번호를 동적으로 가져오는 부분입니다.
# 예를 들어, /page/1을 방문하면 page_number는 1이 됩니다.
# <int:page_number>는 URL에서 정수형 페이지 번호를 가져오는 부분입니다.
# 이 부분은 Flask의 라우팅 기능을 사용하여 URL과 함수를 연결하는 데코레이터입니다.
@app.route('/page/<int:page_number>')
def get_page(page_number : int) :
    # 페이지 번호에 따라 데이터를 가져오는 로직을 여기에 추가합니다.
    # 예를 들어, 데이터베이스에서 해당 페이지의 데이터를 가져올 수 있습니다.
    # 여기서는 단순히 페이지 번호를 반환합니다.
    return f"Displaying data for page {page_number}"

if __name__ == '__main__' :
    app.run(debug=True)

# Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)