from .. import cstory
from .. import elem


class Story(cstory.ChatStory):
    def __init__(self, title, desc):
        super().__init__(title, desc)

    def __start__(self):
        elem = elem.Element(self, 'Junior', 'Venetius', 'Ohanyere')
        elem1 = elem.Element(self, 'Milke', 'Monty', 'Betty')

        elem.echo(msg='Hi friend')
        elem1.echo(msg='\U0001F602')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe \U0001F601')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')
        elem.echo(msg='Hi friend')
        elem1.echo(msg='Hi babe')


cs = Story('ChatStory', 'A simple chat story')
cs.run()
