from flask_app import app, session, render_template


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
