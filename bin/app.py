#coding=utf-8

import web
from gothonweb import map

urls = (
    '/game','GameEngine',
    '/','Index',
)

app = web.application(urls,globals())

#little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app,store,
                                  initializer={'room':None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/',base="layout")

class Index(object):
    def GET(self):
        #this is used to "setup" the session with starting values
        session.room = map.START
        return render.login()

class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            return render.you_died()

    def POST(self):
        form = web.input(action = None)

        if session.room and form.action in map.path_list:
            session.room=session.room.go(form.action)
            return render.show_room(room=session.room)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()