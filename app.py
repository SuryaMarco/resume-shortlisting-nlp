from flask import Flask, request, jsonify
from resume_shortlister import rank_resumes  # import your logic

app = Flask(__name__)

@app.route("/api/shortlist", methods=["POST"])
def shortlist():
    job_desc = request.json.get("job_description")
    result = rank_resumes(job_desc)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
