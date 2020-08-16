from mycroft import MycroftSkill, intent_file_handler
import requests

class Todayinhistory(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('todayinhistory.intent')
    def handle_todayinhistory(self, message):
        url = "https://history.muffinlabs.com/date"
        r = requests.get(url)
        #print(r.text)
        json_op = r.json()
        #print("Json Output : {} ".format(json_op))
        '''print(json_op.keys())
        print(json_op['date'])
        print(json_op['url'])
        print(json_op['data'])'''
        op = json_op['data']
        events = op['Events']
        births = op['Births']
        deaths = op['Deaths']
        #print(events[0])
        todays_event = events[0]['text']
        #print(todays_event)
        self.speak_dialog('Today in History {}'.format(events[0]['text']))


def create_skill():
    return Todayinhistory()

