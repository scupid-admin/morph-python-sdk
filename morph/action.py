class Action:
    def __init__(self, name):
        self.name = name


class GoToFlow(Action):
    def __init__(self, flow_title):
        Action.__init__(self, name="goToFlow")
        self.flow_title = flow_title


class SetVariable(Action):
    def __init__(self, variable_scope, variable_title, variable):
        Action.__init__(self, name="setVariableAction")
        self.variable_scope = variable_scope
        self.variable_title = variable_title
        self.variable = variable


class Publish(Action):
    def __init__(self):
        Action.__init__(self, name="publish")
        self.messages = []

    def add_message(self, message):
        self.messages.extend(message)