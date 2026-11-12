from dataclasses import dataclass
from typing import Callable

@dataclass
class Tool:
    name: str
    description: str
    requires_approval: bool
    handler: Callable

class ToolRegistry:
    def __init__(self):
        self._tools = {}
    def register(self, tool: Tool):
        self._tools[tool.name] = tool
    def get(self, name: str):
        return self._tools.get(name)
    def list(self):
        return [{"name": t.name, "description": t.description,
                 "requires_approval": t.requires_approval} for t in self._tools.values()]
