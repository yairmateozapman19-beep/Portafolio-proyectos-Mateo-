class Config:
    def __init__(self, env):
        self.base_url= {
            'dev':'https://myapp.dev.com',
            'qa':'https://myapp.qa.com',
            'preprod': 'https://myapp.preprod.com'
        }[env]

        self.app_port = {
            'qa':'80',
            'dev': '8080',
            'preprod':'8060'
        }[env]