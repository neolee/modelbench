from get_models import GetModelsRunner
from chat import ChatRunner
from structured_output import JSONObjectRunner, JSONSchemaRunner
from partial_mode import PartialModeRunner
from prefix_completion import PrefixCompletionRunner
from fim_completion import FIMCompletion
from tool_calling import ToolCallingRunner
from reasoning import ReasoningRunner


runners = [
    GetModelsRunner,
    ChatRunner,
    JSONObjectRunner,
    JSONSchemaRunner,
    PartialModeRunner,
    PrefixCompletionRunner,
    FIMCompletion,
    ToolCallingRunner,
    ReasoningRunner
]
