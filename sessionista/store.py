class Store:
    def __init__(self):
        self.reducers = {}
        self.state = {}

    def register(self, reducers):
        '''
        Register a list of reducers to the store.
        Reducer is a reference to a callable
        Returns Store.reducers
        '''
        [self.reducers.update({reducer.__name__: reducer}) for reducer in reducers]
        return self.reducers
    
    def unregister(self, reducer):
        '''
        Unregister an existing store reducer.
        Reducer is a reference to a callable.
        Returns Store.reducers
        '''
        self.reducers.pop(reducer.__name__)
        return self.reducers

    def dispatch(self, action, state={}):
        '''
        Calls a registered reducer.
        Note that there is an explicit
        convention that actions must
        match the name of the reducers.
        Example:
            
            Action:
            MY_ACTION = "my_action"
            
            Reducer:
            def my_action():
                ...
        '''
        # This little number calls the function registered to the action
        # and passes the action state context.
        # It is intentional for it to return KeyError
        # when a non-existing key is passed.
        # You should never try and run a reducer that does not exist -_-
        return self.reducers[action](state)


def create_store():
    return Store()


store = create_store()
