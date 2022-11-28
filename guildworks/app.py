import falcon
from guildworks.resource.quests import QuestsResource

app = application = falcon.App()

quests = QuestsResource()

app.add_route("/quests", quests)
