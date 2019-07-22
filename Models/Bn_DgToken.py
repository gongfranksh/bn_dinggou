class BN_DG_Token(object):
    def __init__(self,tokenjson):
        self.access_token=tokenjson['data']['access_token']
        self.create_time=tokenjson['data']['create_time']
        self.expires_in=tokenjson['data']['expires_in']
        self.refresh_token=tokenjson['data']['refresh_token']
        self.scope=tokenjson['data']['scope']
        self.nodeCode=tokenjson['data']['nodeCode']
