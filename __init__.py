from mycroft import MycroftSkill, intent_file_handler


class Todayinhistory(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('todayinhistory.intent')
    def handle_todayinhistory(self, message):
        self.speak_dialog('todayinhistory')


def create_skill():
    return Todayinhistory()

