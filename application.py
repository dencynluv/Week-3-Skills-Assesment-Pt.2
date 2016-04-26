from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def base_page():
    """Show a base page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("base.html")


@app.route("/application-form")
def show_application_form():
    """Show an application form."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def show_applicant_info():
    """Show applicants information."""

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary = request.form.get("salary")
    job_title = request.form.get("job-titles")

    return render_template("application-response.html", fname=first_name, lname=last_name, salary=salary, job_title=job_title)
    # keep variable names = to the same name between python and jinja


if __name__ == "__main__":
    app.run(debug=True)
