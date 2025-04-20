from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)

# Configuration wkhtmltopdf si nécessaire
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    rendered = render_template('pdf_template.html')
    pdf_path = "releve_notes.pdf"
    pdfkit.from_string(rendered, pdf_path, configuration=PDFKIT_CONFIG, options={
        'page-size': 'A4',
        'margin-top': '2.5cm',
        'margin-bottom': '2.5cm',
        'margin-left': '2.5cm',
        'margin-right': '2.5cm',
    })
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
