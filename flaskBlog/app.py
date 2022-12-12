from flask import (
    Flask, render_template, url_for, redirect, session, request
)
from databases import UsersData, AppendMkl

db = UsersData()

article = AppendMkl()

app = Flask(__name__, static_folder="static")

app.secret_key = b'9fe2841e99a75a94e1efae69d643ed004ec7c9f4c324'

@app.route("/")
def index():
    total = article.getTotalContent()
    return render_template("index.html", session=session, total=total)


@app.route("/makale-ekle",methods=['GET','POST'])
def makaleEkle():
    if 'username' in session:
        if request.method == 'POST':
            __title = request.form.get("title")
            __content = request.form.get("content")
            if article.appendData(title=__title, content=__content, author=session['username']):
                return render_template("add.html", statusAppend = True)
            else:
                return redirect(url_for("makaleEkle"))

        else:
           return render_template("add.html")
    else:
        return "session hatası"


@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        __username = request.form.get("usernamelogin")
        __pasword = request.form.get("passwordlogin")
        if db.loginISTrue(user_name=__username, password=__pasword):
            session["username"] = __username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", loginStatus=False)

    else:
        return render_template("login.html")


@app.route("/register", methods=['POST'])
def register():
    

    if request.method == "POST":
        __username = request.form.get("username")
        __pasword = request.form.get("password")
        if db.appendData(userName=__username, password=__pasword):
            return "Kayıt başarıyla yapıldı"
        else:
            
            return "Hata ! Kullanıcı adı sistemde kayıtlı."
           
            


    else: redirect(url_for("index"))



@app.route("/blog/post/<int:Id>/")
def details(Id):
   
    if 'username' in session:
        
        query = article.queryIdNumber(Id=Id)
        
        if query:
            if query[0]:
                if Id == query[0]:
                    
                    return render_template("details.html",
                    data=query)

                
                else:
                    return redirect(url_for("index" ))
            
            else:
                return redirect(url_for("index"))
   
        
    else:
            return redirect(url_for("index"))
    


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)