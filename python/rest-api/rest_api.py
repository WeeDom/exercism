import json

class RestAPI:
    def __init__(self, database=None):
        self.database = database
        import pdb; pdb.set_trace()

    def get(self, url, payload=None):
        info = json.loads(payload)
        db_by_name = list((item['name'], item) for item in self.database['users'])
        if url =='/users':
            return json.dumps({ db_by_name[info['users'][0]] })

        return []

    def post(self, url, payload=None):
        info = json.loads(payload)
        if url == "/add":
            self.database["users"].append(
                {
                    "name": info["user"],
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
            )
            return json.dumps(
                {
                    "name": info["user"],
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                })
