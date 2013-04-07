# Static routing
import os,math,re

from flask import Flask,requests,g,flash,render_template,session,abort,url_for,redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/biscuit')
def staticroutingbiscuit(): 
	imageURl = "http://www.dealerbid.co.uk/news/wp-content/uploads/2012/10/ferrari-f121.jpg"
	return render_template('biscuit.html', imageURL = imageURL )

# dynamic routing
@app.route('/SteveJobs/<int:post_id>')
def dynamicroutingbiscuit(post_id):
	post_id = post_id 
	return render_template('dyroutingbiscuit.html', post_id = post_id)

# HTTP methods
@app.route('/biscuit/HTTPmethods', methods=['GET', 'POST'])
def HTTPmethodsbiscuit():
	if request.method == 'POST':
		Percentagedone = 30
		return render_template('HTTPmethods.html', Percentagedone = Percentagedone)
	else request.method == 'GET':
		Percentagedone = 0
		return render_template('HTTPmethods.html', Percentagedone = Percentagedone)
	
# request data
@app.route('/biscuit/login', methods=['GET', 'POST'])
def requestdatalogin():
	if request.data == 'POST':
		username = request.form['username']
		gender = request.form['gender']
		age = request.form['age']
		return render_template('requestdatalogin.html, **locals())
	return render_template('requestdatalogin.html, error = error)

# Sessions, flash
app.secret_key = '/0Ne/5t3p/clO5Er/14'
@app.route('biscuit/Sessions',	
def storeSessions():
	session['age'] = 21
	flash('age is stored in this session')
	return redirect(url_for('index')
def checkSession():
	checkSession = session['age']
	flash('age is still stored in this session')
	return render_template('checkSession.html', checkSession = checkSession)
def takeoutSession():
	session.pop('age', None)
	return redirect(url_for('index'))
	
if __name__ == '__main__':
	app.debug = True
	port= int(os.environ.get("PORT", 5000))
	app.run(host= "127.0.0.1", port = port)	