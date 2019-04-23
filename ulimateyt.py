from flask import *
app=Flask(__name__,static_url_path="")

import pafy

import os
@app.route('/dlfile')
def root():
    return app.send_static_file('dlfile')
pa=os.getcwd().replace("\\","/")

#PLEASE INSERT YOUR PYTHONANYWHERE USERNAME BELOW THE POUND SIGNS

#

#

#

username="pythonsnake2017"#Pre setup for my friend here

pword="56"#Set password here

@app.after_request

def apply_caching(response):

    response.headers["X-Frame-Options"] = "SAMEORIGIN"

    response.headers["Access-Control-Allow-Origin"]="*"

    response.headers["Access-Control-Allow-Headers"]="range"

    response.headers["Access-Control-Expose-Headers"]="Cache-Control, Content-Encoding, Content-Range"

    return response

@app.route("/")

def go():

    return '''

    <h1>Welcome to the ulimate youtube server</h1>
    <h2>Links below</h2>
    <a href="/youtubedl">Youtube downloader</a>
    <a href="/yotuube.io">Unblock the youtube</a>
    <z href="/cast">Cast youtube to chromecasts without youtube red(also casts to google home)</a>
    <p>
    Project by javaarchive on github!!
    </p>
    '''

@app.route('/static/<path:path>')

def get_resource(path):  # pragma: no cover

    return send_from_directory('static', path)





@app.route('/youtubedl',methods=["POST","GET"])

def save():

    if request.method=="GET":

       return '''

       <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<form method="POST" action="/youtubedl">

<input name=urld type=url> ENTER mp3 URL:</input>

<button type=submit class="btn btn-success">DOWNLOAD</button>

<script>

var pass=prompt("A password is required to access the page");

if(pass=="'''+pword+'''"){

  alert("Access granted");

}else{

alert("Access denied: BIG SHAQ ONE AND ONLY");

document.body.innerHTML="<h1>I'm afraid you cannot use this PERSON redirect in 5 seconds</h1>";

function Cat(){

window.location="about:blank";

}

}

</script>

<script type="text/javascript"

    var adfly_id = 19279991;

    var popunder_frequency_delay = 0;

</script>



<script src='https://www.google.com/recaptcha/api.js'></script>

<select name=filetype class="form-control">

  <option value="mp4">mp4</option>

  <option value="webm">webm</option>

  <option value="mp3">mp3</option>

  <option value="m4a">m4a</option>

  <option value="3gp">3GP</option>

  <option value="flv">flv</option>

  <option value="mov">mov</option>

  <option value="mpg">mpg</option>

  <option value="avi">avi</option>

</select>

<div class="g-recaptcha" data-sitekey="6LfPUk8UAAAAAPqjhnvAiiSYw8Ng8rcR7CSYk0EL"></div>

</form>

<script type="text/javascript"> var infolinks_pid = 3084238; var infolinks_wsid = 0; </script> <script type="text/javascript" src="//resources.infolinks.com/js/infolinks_main.js"></script>

'''

    else:

      try:







        

        

            





        

           video = pafy.new(request.form["urld"])

           if not request.form["filetype"] in ["m4a","mp3"]:

               best = video.getbest(preftype=request.form["filetype"])

               filename = best.download(filepath=(pa+"/static/"+"dlfile"))



           else:

               best=video.getbestaudio(preftype=request.form["filetype"])

               filename = best.download(filepath=(pa+"/static/"+"dlfile"))

               #filename = best.download(filepath="/home/Pythonsnake2017/mysite/templates/file1.html",quiet=False)

           return '''

<h1>FILE DONE</h1>





<script src="https://apis.google.com/js/platform.js" async defer></script>

<div class="g-savetodrive"

   data-src="/dlfile"

   data-filename="youtubedl"

   data-sitename="Ulimate youtube">

</div>

<h1>'''+video.title+'''</h1>

</p>'''+video.description+'''

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>




'''

      except Exception as e:

        return str(e)+str(type(request.form["urld"]))
database1=[]
with open("yt.json") as f:
    database1=json.loads(f.read())

@app.route('/yt/<id>')
def getVid(id):
    with open("yt.json","w") as f:
      f.write(json.dumps(database1))
    print(id)
    id=int(id)
    th=pafy.new(database1[id][3])

    try:
        return '''
        <!DOCTYPE HTML5>
        <html>
        <head>
        <style>
        video {
  width: 100%    !important;
  height: auto   !important;
}
        </style>
<meta name="apple-mobile-web-app-capable" content="yes">
        </head>
        <body>
        <a href="/youtube.io"><img src="https://lh3.googleusercontent.com/jOZTa-tLJcnGJCtgw_hwYjZDtmSe_a47GQTiyA02q-QIIc_rimNhLCUYYic3mfCdpaft=s180"></a>
        <video controls autoplay>
  <source src='''+th.getbest(preftype="mp4").url+''' type="video/mp4">

Your browser does not support the video tag.
</video><h1>'''+database1[id][1]+'''</h1><p>'''+database1[id][2]+'''</p>
        </body>
<script type="text/javascript"> var infolinks_pid = 3084238; var infolinks_wsid = 0; </script> <script type="text/javascript" src="//resources.infolinks.com/js/infolinks_main.js"></script>
<script>
function ddd(){document.getElementById("url").value="'''+database1[id][3]+'''"}
</script>
<form action="/youtubedl" method="POST" onsubmit="ddd()">
<select name=filetype class="form-control" >
  <option value="mp4">mp4</option>
  <option value="webm">webm</option>
  <option value="mp3">mp3</option>
  <option value="m4a">m4a</option>
  <option value="3gp">3GP</option>
  <option value="flv">flv</option>
  <option value="mov">mov</option>
  <option value="mpg">mpg</option>
  <option value="avi">avi</option>
</select>
<input name="urld" id="url">'''+database1[id][3]+'''</input>
<button type="submit">SEND TO YTDL</button>
</form>
        '''
    except Exception as e:
        return str(e)+"   also "+str(id)+" IS NOT valid"

def gen():
    out="<h1>Welcome to youtube.io by Awesome Cat Studios </h1>"
    for x in database1:
        out=out+'''<a href="/yt/'''+str(database1.index(x))+'''">'''+x[1]+"</a><p>"+x[2]+'</p>'
    return out


@app.route('/youtube.io',methods=["POST","GET"])
def ninjasave():
    with open("yt.json","w") as f:
      f.write(json.dumps(database1))
    if request.method=="GET":
       return '''

       <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<style>
button{
font-size:45px;
}
input{
background-color:black;
color:white;
border-color:white;
border-radius:2px;
}
</style>
<link rel="apple-touch-icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbtula7phAfFEsEYR7_BTnonXg1H_QfJnAai8p56elb4LZBf90">
<meta name="apple-mobile-web-app-title" content="youtube">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="red">

<form method="POST" action="/youtube.io">
<input name=urld type=url> ENTER mp3 URL:</input>
<button type=submit class="btn btn-success">DOWNLOAD</button>
<script>
if(window.localStorage.getItem("pass")){
}else{
var pass=prompt("A password is required to access the page");
}
if(pass=="io"||(window.localStorage.getItem("pass")=="used")){
  window.localStorage.setItem("pass","used");
  alert("Access granted");
}else{
alert("Access denied: BIG SHAQ ONE AND ONLY");
document.body.innerHTML="<h1>I'm afraid you cannot use this PERSON redirect in 5 seconds</h1>";
function Cat(){
window.location="https://google.com/DENIED";
}
setTimeout(Cat,3000);
}
</script>


</form>
<script type="text/javascript"> var infolinks_pid = 3084238; var infolinks_wsid = 0; </script> <script type="text/javascript" src="//resources.infolinks.com/js/infolinks_main.js"></script>
'''+gen()
    else:
      try:




        if request.form["urld"].find("youtube")==-1 or False:
            d(request.form["urld"],"/home/Pythonsnake2017/mysite/static/file1.html")
            d(request.form["urld"],"/home/Pythonsnake2017/mysite/templates/file1.html")
            video=1
            video.title=""
            video.description=""
            return "THAts not a youtube url"


        else:
           video = pafy.new(request.form["urld"])
           if True:
               best = video.getbest(preftype="mp4")
               database1.append([best.url,video.title,video.description,request.form["urld"]])

        return '''

<h1> Your video has been submitted to database and will be processed reload to see</h1>
\
'''
      except Exception as e:
        return str(e)+str(type(request.form["urld"]))
import chromecast
pause=True
@app.route("/playback")
def control():
    global pause
    if pause:
        pause=False
        chromecast.play()
    else:
        pause=True
        chromecast.pause()
    return redirect("/cast")
@app.route("/cast",methods=["POST","GET"])
def cast():
    global pause
    if request.method=="POST":
        pause=False
        chromecast.yt(request.form["video"])
    return '''
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
<h1>Chromecast Home</h1>
<p>
Your chromecasts an be wirelessly controlled here.
</p>
<a href="/playback">Pause/Play</a>
<form method=POST>
<h1>Play Youtube video</h1>
<input type="url" class="form-control" name="video"></input>
<button class="btn btn-dark" type="submit">Play</button>










</form>


'''
import os
port1 = int(os.environ['PORT'])
app.run(host="0.0.0.0",port=port1)
