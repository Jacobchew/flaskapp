# Static routing

@app.route('/')
def staticroutingbiscuit(): 
	return render_template(index.html)

# dynamic routing
@app.route('/SteveJobs/<int:post_id>')
def dynamicroutingbiscuit(post_id):
	post_id = post_id 
	return render_template(dyroutingbiscuit.html, post_id = post_id)
	