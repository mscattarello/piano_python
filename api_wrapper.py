import requests

class piano_wrapper:

    def __init__(self, aid, api_token):
        self.aid = aid
        self.api_token = api_token
        self.URL = "https://sandbox.piano.io/api/v3/publisher/user/list?"

    def fix_users(self, data):
        fixed_df = data
        for i in range(len(data)):
            email = data.iloc[i].email
            uid = data.iloc[i].user_id
            user = self.quick_user_search(email)
            if len(user) == 0:
                continue
            else:
                user = user[0]
            if user['uid'] != uid:
                fixed_df.replace(to_replace = uid, value = user['uid'], inplace = True)
        return fixed_df

    def quick_user_search(self, q):
        full_url = f"{self.URL}aid={self.aid}&api_token={self.api_token}&offset=0&q={q}"
        response = requests.post(full_url)
        users = response.json()['users']
        return users