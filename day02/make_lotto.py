from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

def generate_lotto_num():
    nums = random.sample(range(1, 46), 6)
    nums.sort()
    return nums

@app.route('/', methods=['GET', 'POST'])
def index():
    lotto_results = []
    if request.method == 'POST':
        try:
            count = int(request.form.get('count', 1))
            for i in range(count):
                lotto_results.append(generate_lotto_num())
        except ValueError:
            lotto_results = ['올바른 숫자를 입력하세요.']

    return render_template_string('''
    <!doctype html>
    <html>
    <head><title>로또 번호 생성기</title></head>
    <body>
        <h1>로또 번호 생성기</h1>
        <form method="post">
            몇 게임 하시겠습니까? 
            <input type="number" name="count" min="1" max="20" value="1" required>
            <input type="submit" value="생성">
        </form>
        <hr>
        {% if lotto_results %}
            <h2>결과</h2>
            <ul>
            {% for numbers in lotto_results %}
                <li>{{ loop.index }}번째 로또번호: {{ numbers }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    </body>
    </html>
''', lotto_results=lotto_results)


if __name__ == '__main__':
    app.run(debug=True)
