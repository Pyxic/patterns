class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._memento = None

    @property
    def memento(self):
        return self._memento

    @memento.setter
    def memento(self, memento):
        self._memento = memento


class Originator:
    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def save_state(self):
        return Memento(self._state)

    def restore_state(self, memento):
        self._state = memento.get_state()


originator = Originator()
caretaker = Caretaker()

originator.state = "on"
print('Originator state: ', originator.state)
caretaker.memento = originator.save_state()

originator.state = "off"
print("Originator changed state: ", originator.state)

originator.restore_state(caretaker.memento)
print("Originator restored state: ", originator.state)
