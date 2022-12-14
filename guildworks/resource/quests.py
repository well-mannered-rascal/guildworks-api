import falcon
from falcon import Request, Response
from ..db import DBManager
from ..db.models import Quest


class QuestsResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        """Return only open and ongoing quests by default"""

        result = []
        with DBManager.sessionmaker() as session:
            row: Quest
            for row in session.query(Quest).filter(Quest.status == Quest.STATUS_OPEN):
                result.append(row.as_dict())

        resp.media = result
        resp.status = falcon.HTTP_200

    def on_post(self, req: Request, resp: Response):
        print(req.media)
