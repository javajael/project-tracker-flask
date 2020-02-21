"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template
import hackbright

app = Flask(__name__)


@app.route('/student')
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    # return f'{github} is the GitHub account for {first} {last}'
    return render_template('student_info.html',
                           first_name=first,
                           last_name=last,
                           github_user=github)

@app.route('/search')
def search():
    """ Display a form where a user can enter a github id and search for a
    particular student """
    return render_template('student_search.html')


@app.route('/create_student')
def create_student():

    return render_template('create_student.html')

@app.route('/add_student', methods=['POST'])
def add_student():

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    github = request.form.get('github')

    hackbright.make_new_student(fname, lname, github)

    link = "/student?github="
    link += github

    return render_template('confirmation.html',
                           fname=fname,
                           lname=lname,
                           github=github,
                           link=link)




if __name__ == '__main__':
    hackbright.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
