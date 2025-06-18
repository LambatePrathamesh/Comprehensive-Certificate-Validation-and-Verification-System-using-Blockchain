# import flast module
from flask import Flask, render_template

# instance of flask application
app = Flask(__name__ ,template_folder='templates', static_folder='static')

# home route that returns below text when root url is accessed
@app.route("/")
def index():
    return render_template('start.html')

@app.route('/faculty_login', methods=['GET', 'POST'])
def faculty_login():
    return render_template('facutylogin.html')

@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    return render_template('verify.html')

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    return render_template('forgot.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('student_dashboard.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('student_profile.html')

@app.route('/certificates', methods=['GET', 'POST'])
def certificates():
    return render_template('student_certificates.html')

@app.route('/marksheets', methods=['GET', 'POST'])
def marksheets():
    return render_template('student_marksheets.html')

@app.route('/fdash', methods=['GET', 'POST'])
def fdash():
    return render_template('Faculty_Dashboard.html')

@app.route('/fmarks', methods=['GET', 'POST'])
def fmarks():
    return render_template('marksheets.html')

@app.route('/fassign', methods=['GET', 'POST'])
def fassign():
    return render_template('assign.html')
	
@app.route('/fcerti', methods=['GET', 'POST'])
def fcerti():
    return render_template('generate_certificates.html')

@app.route('/sem3', methods=['GET', 'POST'])
def sem3():
    return render_template('sem3.html')

@app.route('/sem4', methods=['GET', 'POST'])
def sem4():
    return render_template('sem4.html')

@app.route('/sem5', methods=['GET', 'POST'])
def sem5():
    return render_template('sem5.html')

@app.route('/sem6', methods=['GET', 'POST'])
def sem6():
    return render_template('sem6.html')

if __name__ == '__main__': 
    app.run()
