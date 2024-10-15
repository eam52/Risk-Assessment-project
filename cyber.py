from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    methodologies = [
        "Methodology 1: Identify potential risks.",
        "Methodology 2: Assess the impact and likelihood.",
        "Methodology 3: Develop mitigation strategies."
    ]

    findings = [
        "Finding 1: Cybersecurity threats are prevalent.",
        "Finding 2: Operational risks can disrupt service."
    ]
    return render_template('home.html', methodologies=methodologies, findings=findings)


@app.route('/analysis')
def analysis():
    # summary statistics (eg: number of risks, highest risks, etc)
    # breakdown of risk by category or score
    pass

@app.route('/risk-matrix', methods = ['POST'])
def risk_matrix():
    pass



if __name__ == '__main__':
    app.run(debug=True)
