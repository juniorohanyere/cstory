import cstory
import create

class Story(cstory.ChatStory):
    def __init__(self, title, desc):
        super().__init__(title, desc)

    def __start__(self):
        elem = create.Create(self, 'Junior', 'Venetius', 'Ohanyere')
        elem1 = create.Create(self, 'Milke', 'Monty', 'Betty')

        elem.push(msg='Hi friend')
        elem1.push(msg='\U0001F602')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe \U0001F601')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        elem.push(msg='Hi friend')
        elem1.push(msg='Hi babe')
        pass

cs = Story('ChatStory', 'A simple chat story')
cs.run()
