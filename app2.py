# Static routing

@app.route('/biscuit')
def staticroutingbiscuit(): 
	return render_template('index.html')

# dynamic routing
@app.route('/SteveJobs/<int:post_id>')
def dynamicroutingbiscuit(post_id):
	post_id = post_id 
	return render_template('dyroutingbiscuit.html', post_id = post_id)

# HTTP methods
@app.route('/biscuit'/'HTTPmethods', methods=['GET', 'POST'])
def HTTPmethodsbiscuit():
	if request.method == 'POST':
		Percentagedone = 30
		return render_template('HTTPmethods.html', Percentagedone = Percentagedone)
	else request.method == 'GET':
		Percentagedone = 0
		return render_template('HTTPmethods.html', Percentagedone = Percentagedone)
	
# request data
@app.route('/biscuit'/'login', methods=['GET', 'POST'])
def requestdatalogin():
	if request.data == 'POST':
		username = request.form['username']
		gender = request.form['gender']
		age = request.form['age']
		return render_template('requestdatalogin.html, **locals())
	return render_template('requestdatalogin.html, error = error)
	