"""This is a plugin to use Auto-GPT with Todoist."""
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate


from .client import Client

PromptGenerator = TypeVar("PromptGenerator")

class Message(TypedDict):
    role: str
    content: str


class AutoGPTTodoistPlugin(AutoGPTPluginTemplate):
    """
    This is a plugin to use Auto-GPT with Todoist.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-Todoist"
        self._version = "0.1.0"
        self._description = "This is a plugin for AutoGPT to create, view, modify and interface with todoist"
        self.cli= Client()
        

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        prompt.add_command(
            "Get all projects",
            "get projects",
            {},
            self.cli.get_projects
        ),
        prompt.add_command(
            "Get a specific project",
            "get project",
            {"project_id": "<project_id>"},
            self.cli.get_project
        ),
        prompt.add_command(
            "Get collaborators of a project",
            "get collaborators",
            {"project_id": "<project_id>"},
            self.cli.get_collaborators
        ),
        prompt.add_command(
            "Get comments",
            "get comments",
            {
                "project_id": "<project_id>",
                "task_id": "<task_id>",
            },
            self.cli.get_comments
        ),
        prompt.add_command(
            "Get label by ID",
            "get label",
            {"label_id": "<label_id>"},
            self.cli.get_label
        ),
        # ...
        prompt.add_command(
            "Get labels",
            "get labels",
            {},
            self.cli.get_labels
        ),
        prompt.add_command(
            "Get section by ID",
            "get section",
            {"section_id": "<section_id>"},
            self.cli.get_section
        ),
        prompt.add_command(
            "Get sections",
            "get sections",
            {},
            self.cli.get_sections
        ),
        prompt.add_command(
            "Get shared labels",
            "get shared labels",
            {},
            self.cli.get_shared_labels
        ),
        prompt.add_command(
            "Get task by ID",
            "get task",
            {"task_id": "<task_id>"},
            self.cli.get_task
        ),
        prompt.add_command(
            "Get tasks",
            "get tasks",
            {},
            self.cli.get_tasks
        ),
        prompt.add_command(
            "Add comment",
            "add comment",
            {
                "content": "<content>",
                "project_id": "<project_id>",
                "task_id": "<task_id>",
            },
            self.cli.add_comment
        ),
        prompt.add_command(
            "Get today's tasks",
            "get today's tasks",
            {},
            self.cli.get_todays_tasks
        ),
        prompt.add_command(
            "Add label",
            "add label",
            {"name": "<name>"},
            self.cli.add_label
        ),
        prompt.add_command(
            "Add project",
            "add project",
            {"name": "<name>"},
            self.cli.add_project
        ),
        prompt.add_command(
            "Add section",
            "add section",
            {
                "name": "<name>",
                "project_id": "<project_id>",
            },
            self.cli.add_section
        ),
        prompt.add_command(
            "Add task",
            "add task",
            {
                "content": "<content>",
                "project_id": "<project_id>",
                "due": "<due>",
            },
            self.cli.add_task
        ),
        prompt.add_command(
            "Quick add task",
            "quick add task",
            {"text": "<text>"},
            self.cli.quick_add_task
        ),
        prompt.add_command(
            "Remove shared label",
            "remove shared label",
            {"name": "<name>"},
            self.cli.remove_shared_label
        ),
        prompt.add_command(
            "Rename shared label",
            "rename shared label",
            {
                "name": "<name>",
                "new_name": "<new_name>",
            },
            self.cli.rename_shared_label
        ),
        prompt.add_command(
            "Reopen task",
            "reopen task",
            {"task_id": "<task_id>"},
            self.cli.reopen_task
        ),
        prompt.add_command(
            "Update comment",
            "update comment",
            {
                "comment_id": "<comment_id>",
                "content": "<content>",
            },
            self.cli.update_comment
        ),
        prompt.add_command(
            "Update label",
            "update label",
            {"label_id": "<label_id>"},
            self.cli.update_label
        ),
        prompt.add_command(
            "Update project",
            "update project",
            {"project_id": "<project_id>"},
            self.cli.update_project
        ),
        prompt.add_command(
            "Update section",
            "update section",
            {
                "section_id": "<section_id>",
                "name": "<name>",
            },
            self.cli.update_section
        ),
        prompt.add_command(
            "Update task",
            "update task",
            {"task_id": "<task_id>"},
            self.cli.update_task
        ),
        prompt.add_command(
            "Close task",
            "close task",
            {"task_id": "<task_id>"},
            self.cli.close_task
        ),
        prompt.add_command(
            "Delete comment",
            "delete comment",
        {"comment_id": "<comment_id>"},
        self.cli.delete_comment
        ),
        prompt.add_command(
        "Delete label",
        "delete label",
        {"label_id": "<label_id>"},
        self.cli.delete_label
        ),
        prompt.add_command(
        "Delete project",
        "delete project",
        {"project_id": "<project_id>"},
        self.cli.delete_project
        ),
        prompt.add_command(
        "Delete section",
        "delete section",
        {"section_id": "<section_id>"},
        self.cli.delete_section
        ),
        prompt.add_command(
        "Delete task",
        "delete task",
        {"task_id": "<task_id>"},
        self.cli.delete_task
        )
        return prompt
# ______________________________________________________________________________________________________________________

# ______________________________________________________________________________________________________________________
    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
        Returns:
            str: The resulting response.
        """
        pass
    
    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.
        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.
        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.
        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        """This method is called before the planning chat completion is done.
        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.
        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completion is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.
        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.
        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.
        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.
        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.
        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.
        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.
        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.
        Args:
            command_name (str): The command name.
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False





        # prompt.add_command(
        #     "Add two numbers",
        #     "add 2 numbers",
        #     {
        #         "num": "<num>",
        #         "num2": "<num2>",
        #     },
        #     self.cli.add_numbers
        # ),
        # prompt.add_command(
        #     "Subtract two numbers",
        #     "subtract 2 numbers",
        #     {
        #         "num": "<num>",
        #         "num2": "<num2>",
        #     },
        #     self.cli.sum_numbers
        # ),

        # Class Client:
        #     ...other code

        # def add_numbers(self, num, num2):
        #     return num+num2
        # def sub_numbers(self, num, num2):
        #     return num-num2
# LOOK AT THE EXAMPLE ABOVE AND CREATE add_command ENTRIES BASED IN THE CODE BELOW.  THIS IS FOR 