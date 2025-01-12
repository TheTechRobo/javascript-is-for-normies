from quart import *

import asyncio, random

app = Quart(__name__)

@app.route("/")
async def hello():
    async def generate():
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
        <img class="h" src="https://lounge.thetechrobo.ca/uploads/9d883830f824eadf/image.png" /></div>
        """
        X = 0
        Y = 0
        stepX = 2
        stepY = 2
        viewportH = 480 - 223
        viewportW = 640 - 213
        adjustment = 0
        while True:
            if X >= viewportW or X < 0:
                adjustment = random.randint(0, 360)
                yield '<style>.h { filter: hue-rotate(%sdeg) }</style>\n' % adjustment
                stepX *= -1
            if Y >= viewportH or Y < 0:
                adjustment = random.randint(0, 360)
                yield '<style>.h { filter: hue-rotate(%sdeg) }</style>\n' % adjustment
                stepY *= -1
            X += stepX
            Y += stepY
            yield '<style>.h { transform: translate(%s,%s) }</style>\n' % (f"{X}px", f"{Y}px")
            await asyncio.sleep(0.01)
    return app.response_class(generate(), mimetype='text/html')
