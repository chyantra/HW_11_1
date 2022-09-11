from flask import Flask, render_template
from config import DATA_CANDIDATES_LOCATION
from candidates_manager import CandidatesManager

app = Flask(__name__)

manager = CandidatesManager(DATA_CANDIDATES_LOCATION)

@app.route('/')
def page_index():
    candidates = manager.get_all()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int: can_id>')
def candidate_page(can_id):
    candidate = manager.get_by_id(can_id)

    if candidate is None:
        return render_template('404.html')

    return render_template('single.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def search_page_for_candidate_name(candidate_name):
    candidates = manager.get_by_name(candidate_name)
    candidates_len = len(candidates)

    return render_template('search.html',
                           candidate=candidate,
                           candidates_len=candidates_len
                           )

@app.route('/skill/<skill_name>')
def search_page_for_candidate_skill(skill_name):
    candidates = manager.get_by_skill(skill_name)
    candidates_len = len(candidates)

    return render_template('list_by_skill.html',
                           candidate=candidate,
                           candidates_len=candidates_len,
                           skill_name=skill_name
                           )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)




