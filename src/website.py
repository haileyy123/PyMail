from flask import Flask, request, jsonify, render_template, redirect
from src import email_parser, smtp_server, website, inbox_handler
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
def run_flask_server():
    app = Flask(__name__, template_folder="../templates")

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/view_inbox')
    def view_inbox():
        emaila = request.args.get("email", "example@example.com")
        inbox = inbox_handler.read_inbox()
        email_inbox = inbox.get(emaila, [])
        email_inbox.reverse()

        return render_template("inbox.html", inbox=email_inbox)

    @app.route('/get_inbox')
    def get_inbox():
        args = request.args
        target = args.get("email", "")
        inbox = inbox_handler.read_inbox()
        email_inbox = inbox.get(target, [])
        return jsonify(email_inbox), 200

    app.run(host='0.0.0.0', port=80, debug=False)