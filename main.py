from flask import Flask
from flask import (
    render_template,
)

app = Flask(__name__)
app.secret_key = '@Awakening Intelligence!'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='',
        port=2005,
    )
    app.run(**config)
