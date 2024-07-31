from typing import Dict, Any

class StateManager:
    def __init__(self):
        self.state: Dict[str, Any] = {}

    def set_state(self, key: str, value: Any):
        self.state[key] = value

    def get_state(self, key: str) -> Any:
        return self.state.get(key)

    def clear_state(self):
        self.state.clear()
