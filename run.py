from One_Index import One_Index_Spider
from mylog import log
from app import init_app
from app import models


def update():
    app = init_app()
    one_index = One_Index_Spider()
    # one的格式是 { url_num: [title, content, img]}
    one = one_index.run
    for key, value in one.items():
        if not models.Post.query.filter_by(url_num=int(key)).first():
            post = models.Post()
            post.url_num = key
            post.title, post.content, post.img = value
            post.save()
        else:
            log('{} 已在数据库中'.format(key))

def init_db():
    # 必须初始化 app 才能操作数据库
    app = init_app()
    db = models.db
    db.drop_all()
    db.create_all()
    log('db has already init')


def run():
    config = dict(
        debug=True,

    )
    init_app().run(**config)

if __name__ == '__main__':

    run()

    #init_db()
    #update()