import pytest
from sessionista.store import store

MY_ACTION = 'my_action'

def my_action(state):
    state['key'] = 'mutated value'
    return state

def test_register_action():
    store.register([my_action])
    assert my_action.__name__ in store.actions.keys()

def test_store_dispatch_action():
    new_state = store.dispatch(MY_ACTION, state={'key': 'value'})
    store.state.update(new_state)

def test_mutate_state():
    assert 'key' in list(store.state.keys())

def test_unregister_action():
    store.unregister(my_action)
    assert my_action.__name__ not in store.actions.keys()
