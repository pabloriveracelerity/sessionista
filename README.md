Sessionista
===

## Overview

Sessionista is a (very) loose implementation of redux for the backend.

Why?

Over the years, I've come to leverage backend sessions to pass state between requests.
Sessionista tries to mimioc what Redux does for state but for sessions.


## The bad

Adding to much data to a singleton can really strain your server.
Use this lightly. DON'T PUT THE WHOLE DATABASE IN A SESSION.

## The good

In my opinion, this helps keep code that interacts with sessions
a little more clear.

## The ugly

More code.


## Example:

1. Don't create your own store. There is already a singleton object created for you.
2. A reducer's name must match the action. Otherwise it won't work.
3. Be mindful of the keys used in the state dictionary. One mispelling and your state will not be found in the expected location.
4. All reducers expect a parameter called state to be passed.
5. One action per reducer.


```
from sessionista.store import store

MY_ACTION = 'my_action'

def my_action(state):
    store.state.update(state)
    return store.state



```