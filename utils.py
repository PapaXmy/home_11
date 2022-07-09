import json

def load_candidates_from_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

#print(load_candidates_from_json())

def get_candidate(candidate_id: int) -> dict:
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate

#print(get_candidate(3))

def candidates_name(candidate_name: str) -> list[dict]:
    name_candidate = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            name_candidate.append(candidate)

    return name_candidate

#print(candidates_by_name('Adela Hendricks'))

def candidates_skill(skill: str) -> list[dict]:
    candidates_skill = []
    for candidate in load_candidates_from_json():
        if skill in candidate['skills'].lower().split(', '):
            candidates_skill.append(candidate)

    return candidates_skill

#print(candidates_skill('python'))

