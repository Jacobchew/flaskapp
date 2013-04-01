Flask
=====

##To Jacob:

Flaws:

*	No import so I can not run the code.

			from flask import Flask,render_template,request,session,g,redirect, url_for,abort, flash

*	If I were to go to (/biscuit) nothing would be returned because there is no template index.html
			
			return render_template('TheEngineer.html', imageURL=imageURL)
	
	* Create folder templates and static and write every HTML files.
* line 30 and 31
* make sure to inculde if
			
			if __name__ == __main__:
				port = int(os.environ.get('PORT', 5000))
				app.run(host='127.0.0.1', port=port)
			