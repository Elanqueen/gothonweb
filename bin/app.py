#coding=utf-8

import web
from gothonweb import map
from gothonweb import survivemap
from gothonweb import forestmap
from bin.lexicon import Lexicon
from bin import parsererror

urls = (
    '/game','GameEngine',
    '/','Index',
    '/map','Map',
    '/roomdes', 'RoomDes'
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
    '''登录页面'''

    def GET(self):
        return render.login()


class Map(object):
#地图选择页
    def GET(self):
        #this is used to "setup" the session with starting values
        return render.map()

    def POST(self):
        form = web.input(gamename=None)
        if form.gamename == "survivemap":
            session.room = survivemap.START
            web.seeother('/game')
        elif form.gamename == "forestmap":
            session.room = forestmap.START
            web.seeother('/game')
        else:
            web.seeother('/map')

class RoomDes(object):
   # room查询页面
    def GET(self):
        return render.map()

    def POST(self):
        form = web.input()
        if form.room_search in survivemap.room_list:
            return render.room_description(room=survivemap.room_list.get(form.room_search))
        elif form.room_search in forestmap.room_list:
            return render.room_description(room=forestmap.room_list.get(form.room_search))
        else:
            web.seeother('/map')


class GameEngine(object):
    '''游戏页面'''

    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        if form.action:
            # 处理用户输入内容为关键字词组
            lexicon = Lexicon()
            world_list = lexicon.scan(form.action)
            sentence = parsererror.parse_sentence(world_list)
            if sentence.object=="":
                action = sentence.subject + " " + sentence.verb
            else:
                action = sentence.subject + " " + sentence.verb + " " + sentence.object
            print(action)
            print(len(action))

            #判定action在path_list中时，才可进行页面展示，否则不跳转页面
            if action in forestmap.path_list or action in survivemap.path_list:
                session.room = session.room.go(action)
                return render.show_room(room=session.room)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()