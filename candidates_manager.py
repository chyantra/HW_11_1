import json

class CandidatesManager:

    def __init__(self, path):
        self.path = path
        self.data = None

        self.load_candidates()

    def __repr__(self):
        return f"CandidatesManager({self.path})"

    def load_candidates(self):
        with open(self.path) as file:
            data = json.load(file)
        return data

    def get_all(self):
        candidates = self.load_candidates()
        return candidates

    def get_by_id(self, cid):
        candidates = self.load_candidates()
        for candidate in candidates:
            if candidate['id'] == cid:
                return candidate

    def get_by_name(self, name):
        candidates = self.load_candidates()
        name = name.lower()
        matching_candidates = [candidate for candidate in candidates if name in candidate["name"].lower()]
        return matching_candidates

    def get_by_skill(self, skill):
        candidates = self.load_candidates()
        skill = skill.lower()
        matching_candidates = []

        for candidate in candidates:
            candidate_skill = candidate['skills'].lower().split(", ")
            if skill in candidate_skill:
                matching_candidates.append(candidate)

        return matching_candidates



manager = CandidatesManager("candidates.json")

#data = manager.get_by_skill("a")
