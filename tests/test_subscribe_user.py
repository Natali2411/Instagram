import config



class TestSubscribeUser:

    def test_login_acc(self, chr_driver, login_obj):
        chr_driver.get(url=config.url)
        login_obj.login()


    def test_search_group(self, subscribe_obj):
        subscribe_obj.search_group()


    def test_open_followers_header(self, subscribe_obj):
        subscribe_obj.open_followers_win()


    def test_subscribe_followers(self, subscribe_obj):
        subscribe_obj.subscribe_followers(time_out=3600)