from app.tools.base import Tool, ToolRegistry

registry = ToolRegistry()

def summarize_command(command: str):
    return {"accepted": True, "summary": command[:500],
            "note": "No external action executed. Connect an approved provider/tool."}

registry.register(Tool(
    name="prepare_task",
    description="Prepare and classify a user task without performing external side effects.",
    requires_approval=False,
    handler=summarize_command,
))
