from flask import *

import time

app = Flask(__name__)

@app.route("/")
def hello():
    def generate():
        yield """
        <style>
            div {
                margin: 0 !important;
                padding: 0 !important;
                background-color: #000;
                color: #d51d96;
                width: 640px;
                height: 480px;
            }
        </style><div>
        <img class="hello" src="https://dl.fireon.live/irc/5ebfd1b86e2db220/:3.png" /></div>
        """
        X = 0
        Y = 0
        stepX = 2
        stepY = 2
        viewportH = 480 - 223
        viewportW = 640 - 213
        while True:
            if X >= viewportW or X < 0:
                stepX *= -1
            if Y >= viewportH or Y < 0:
                stepY *= -1
            X += stepX
            Y += stepY
            yield '<style>.hello { transform: translate(%s, %s) }</style>\n' % (f"{X}px", f"{Y}px")
            time.sleep(0.01)
    return app.response_class(generate(), mimetype='text/html')
