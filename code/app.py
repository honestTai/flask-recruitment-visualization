

from flask import Flask

from web.views.auth import auth
from web.views.clean import clean
from web.views.index import index
from web.views.show import show
from web.views.analysis import analysis
from web.views.spider import spider


class App(Flask):
    def __init__(self, name):
        """ Flask init """

        super().__init__(name)
        self.static_folder = '../static'
        self.template_folder = '../templates'
        self.secret_key = 'CHANGE_ME_BEFORE_RUNNING'
        self._register_blueprints()

    def _register_blueprints(self):
        """ add views """

        self.register_blueprint(index)
        self.register_blueprint(auth)
        self.register_blueprint(show)
        self.register_blueprint(analysis)
        self.register_blueprint(spider)
        self.register_blueprint(clean)


if __name__ == '__main__':
    app = App(__name__)
    app.debug = True
    app.run()
