# -*- coding: utf-8 -*-

from flask.ext.script import Manager

from aminer import create_app


app = create_app()
manager = Manager(app)


@manager.command
def run():
    """Run in local machine."""

    app.run('0.0.0.0', port=9527, threaded=True)

@manager.command
def initdb():
    """Init/reset database."""
    pass
    #
    # db.drop_all()
    # db.create_all()
    #
    # admin = User(
    #         name=u'admin',
    #         email=u'admin@example.com',
    #         password=u'123456',
    #         role_code=ADMIN,
    #         status_code=ACTIVE,
    #         user_detail=UserDetail(
    #             sex_code=MALE,
    #             age=10,
    #             url=u'http://admin.example.com',
    #             deposit=100.00,
    #             location=u'Hangzhou',
    #             bio=u'admin Guy is ... hmm ... just a admin guy.'))
    # db.session.add(admin)
    # db.session.commit()


manager.add_option('-c', '--config',
                   dest="config",
                   required=False,
                   help="config file")

if __name__ == "__main__":
    manager.run()
