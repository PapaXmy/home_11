from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, candidates_name, candidates_skill

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates: list[dict] = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def candidate_page(idx):
    candidate: dict = get_candidate(idx)
    if not candidate:
        return 'Кандидат не найден'
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_page(candidate_name):
    candidates: list[dict] = candidates_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skills/<skill_name>')
def skill_page(skill_name):
    candidates: list[dict] = candidates_skill(skill_name)
    return render_template('skills.html', skill=skill_name, candidates=candidates)


app.run(port=4999)
