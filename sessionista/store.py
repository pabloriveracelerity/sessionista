class Store:
    def __init__(self):
        self.actions = {}
        self.state = {}

    def register(self, actions):
        '''
        Register a list of  to the store.
        Action is a reference to a callable
        Returns Store.action
        '''
        [self.actions.update({action.__name__: action}) for action in actions]
        return self.actions
    
    def unregister(self, action):
        '''
        Unregister an existing store action.
        Action is a reference to a callable.
        Returns Store.actions
        '''
        self.actions.pop(action.__name__)
        return self.actions

    def dispatch(self, action, state={}):
        '''
        Calls a registered action.
        '''
        # This little number calls the function registered to the action
        # and passes the action state context.
        # It is intentional for it to return KeyError
        # when a non-existing key is passed.
        # You should never try and run an action that does not exist -_-
        return self.actions[action](state)


def create_store():
    return Store()


store = create_store()
