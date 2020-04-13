import pytest
from sessionista.store import store

MY_ACTION = 'my_action'

def my_action(state):
    store.state.update(state)
    return store.state

def register_reducer(reducer):
    store.register(reducer)
    return store

def test_register_reducer():
    store = register_reducer([my_action])
    assert my_action.__name__ in store.reducers.keys()

def test_store_dispatch_reducer():
    assert store.dispatch(MY_ACTION, state={'new': 'state'})

def test_unregister_reducer():
    store = register_reducer([my_action])
    store.unregister(my_action)
    assert my_action.__name__ not in store.reducers.keys()
