from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "http://fujifilm.jp/personal/digitalcamera/x/fujinon_lens_xf16mmf14_r_wr/sample_images/img/index/ff_xf16mmf14_r_wr_004.JPG",
    "https://i.ytimg.com/vi/Gduvi1M_81w/maxresdefault.jpg",
    "http://blog.creamu.com/mt/img/anythingcuter_thanthis3.jpg",
    "http://d2goguvysdoarq.cloudfront.net/system/article_photos/attachments/2412/normal.jpg?1427550381",
    "http://iyasidouga.hp-joho.net/wp/wp-content/uploads/2014/11/20141119-480x280.jpg",
    "http://inunekomonogatari.up.n.seesaa.net/inunekomonogatari/image/oyasumi.jpg?d=a0"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
