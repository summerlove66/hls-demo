from flask import Flask ,send_from_directory ,render_template
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route("/<video_name>/index.m3u8")
def get_m3u8(video_name):
    return send_from_directory(os.path.join("videos" ,video_name) ,"index.m3u8")

@app.route("/<video_name>/index<int:idx>.ts")
def  get_ts(video_name ,idx):
    return send_from_directory(os.path.join("videos" ,video_name) ,"index"+str(idx)+".ts")


@app.route("/video/<video_name>")
def get_video_path(video_name):
    return render_template("player.html" ,m3u8_url = "/" +video_name +"/index.m3u8")


if __name__ == '__main__':
    app.run()
