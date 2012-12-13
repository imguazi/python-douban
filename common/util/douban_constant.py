class constant_util(object):
    _apiUrl_ = 'api.douban.com/v2'
    _authUrl_ = 'www.douban.com/service/auth2/auth'

    @staticmethod
    def get_api_url():
        return _apiUrl_

    @staticmethod
    def get_auth_url():
        return _authUrl_

if __name__ == "__main__":
    print constant_util.get_api_url()

