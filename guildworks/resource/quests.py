import falcon


class QuestsResource:
    def on_get(self, req, resp):
        """ Return only open and ongoing quests by default """
        print(req.params)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        print(req.media)
