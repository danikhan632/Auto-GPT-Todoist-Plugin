import os
from todoist_api_python.api import TodoistAPI
from datetime import datetime
import dateparser
def proj_to_dict(proj): return { 'id': proj.id, 'name': proj.name, 'is_favorite': proj.is_favorite, 'is_inbox_project': proj.is_inbox_project, 'is_shared': proj.is_shared, }
def qtask_to_dict(quickadd_result): return { 'task': task_to_dict(quickadd_result.task), 'resolved_project_name': quickadd_result.resolved_project_name}
def task_to_dict(task): return { 'id': task.id, 'content': task.content, 'created_at': task.created_at, 'priority': task.priority, 'project_id': task.project_id, 'section_id': task.section_id }
def section_to_dict(sect): return { "id": sect.id, "name": sect.name, "project_id": sect.project_id, }
def label_to_dict(label): return { "id": label.id, "name": label.name, "color": label.color, }
class Client:
    def __init__(self):
        self.api = TodoistAPI(os.environ.get('TODOIST_TOKEN')) if os.environ.get('TODOIST_TOKEN') else print("The TODOIST_TOKEN environment variable is missing.")

    def get_projects(self):
        projects =self.api.get_projects()
        project_dicts = [proj_to_dict(project) for project in projects]
        return project_dicts

    def get_project(self, project_id):
        return proj_to_dict(self.api.get_project(project_id))
        

    def get_collaborators(self, project_id):
        return self.api.get_collaborators(project_id)
    def get_comments(self, project_id=None, task_id=None):
            if project_id:
                return self.api.get_comments(project_id=project_id)
            elif task_id:
                return self.api.get_comments(task_id=task_id)
            else:
                print("Either a project_id or a task_id must be provided.")


    def get_label(self, label_id):
        labels = self.get_labels()
        label_ids = [label['id'] for label in labels]
        if label_id in label_ids:
            return self.api.get_label(label_id)
        else:
            print(f"Label with id {label_id} does not exist.")
            return None
            
    def get_labels(self):
        labels =self.api.get_labels()
        return [label_to_dict(label) for label in labels]


    def get_section(self, section_id):
        sections = self.get_sections()
        section_ids = [section['id'] for section in sections]
        if section_id in section_ids:
            return self.api.get_section(section_id)
        else:
            print(f"Label with id {section_id} does not exist.")
            return None

    def get_sections(self):
        sections =self.api.get_sections()
        return [section_to_dict(section) for section in sections]
    def get_shared_labels(self):
        return self.api.get_shared_labels()

    def get_task(self, task_id):
        tasks = self.get_tasks()
        task_ids = [task['id'] for task in tasks]
        if task_id in task_ids:
            return self.api.get_task(task_id)
        else:
            print(f"Task with id {task_id} does not exist.")
            return None

    def get_tasks(self):
        tasks =self.api.get_tasks()
        return [task_to_dict(task) for task in tasks]


    def add_comment(self, content, project_id=None, task_id=None):
        if project_id:
            return self.api.add_comment(content=content, project_id=project_id)
        elif task_id:
            return self.api.add_comment(content=content, task_id=task_id)
        else:
            print("Either a project_id or a task_id must be provided.")
            return None
            
    def get_todays_tasks(self):
        tasks = self.get_tasks()
        today = date.today().isoformat()
        todays_tasks = [task for task in tasks if task['due'] is not None and task['due']['date'] == today]
        return todays_tasks

    def add_label(self, name):
        return label_to_dict(self.api.add_label(name=name))


    def add_project(self, name):
        return proj_to_dict(self.api.add_project(name=name))

    def add_section(self, name, project_id):
        return section_to_dict(self.api.add_section(name=name, project_id=project_id))

    def add_task(self, content, project_id=None, due=None):
        due = str(dateparser.parse(due).isoformat())
        kwargs = {'content': content}
        if project_id:
            kwargs['project_id'] = project_id
        if due:
            kwargs['due'] = {'string': due}
        return task_to_dict(self.api.add_task(**kwargs))

    def quick_add_task(self, text):
         return qtask_to_dict(self.api.quick_add_task(text))
    # New methods
    def remove_shared_label(self, name: str) -> bool:
        labels = self.get_labels()
        label_names = [label['name'] for label in labels]
        if name in label_names:
            return self.api.remove_shared_label(name)
        else:
            print(f"Shared label '{name}' does not exist.")
            return False

    def rename_shared_label(self, name: str, new_name: str) -> bool:
        labels = self.get_labels()
        label_names = [label['name'] for label in labels]
        if name in label_names:
            return self.api.rename_shared_label(name, new_name)
        else:
            print(f"Shared label '{name}' does not exist.")
            return False

    def reopen_task(self, task_id: str) -> bool:
        if self.get_task(task_id):
            return self.api.reopen_task(task_id)
        else:
            print(f"Task with id {task_id} does not exist.")
            return False

    def update_comment(self, comment_id: str, content: str) -> bool:
        comments = self.get_comments()
        comment_ids = [comment['id'] for comment in comments]
        if comment_id in comment_ids:
            return self.api.update_comment(comment_id, content)
        else:
            print(f"Comment with id {comment_id} does not exist.")
            return False

    def update_label(self, label_id: str) -> bool:
        if self.get_label(label_id):
            return self.api.update_label(label_id)
        else:
            print(f"Label with id {label_id} does not exist.")
            return False

    def update_project(self, project_id: str) -> bool:
        if self.get_project(project_id):
            return self.api.update_project(project_id)
        else:
            print(f"Project with id {project_id} does not exist.")
            return False

    def update_section(self, section_id: str, name: str) -> bool:
        if self.get_section(section_id):
            return self.api.update_section(section_id, name)
        else:
            print(f"Section with id {section_id} does not exist.")
            return False

    def update_task(self, task_id: str) -> bool:
        if self.get_task(task_id):
            return self.api.update_task(task_id)
        else:
            print(f"Task with id {task_id} does not exist.")
            return False

    def close_task(self, task_id: str) -> bool:
        if self.get_task(task_id):
            return self.api.close_task(task_id)
        else:
            print(f"Task with id {task_id} does not exist.")
            return False

    def delete_comment(self, comment_id: str) -> bool:
        comments = self.get_comments()
        comment_ids = [comment['id'] for comment in comments]
        if comment_id in comment_ids:
            return self.api.delete_comment(comment_id)
        else:
            print(f"Comment with id {comment_id} does not exist.")
            return False

    def delete_label(self, label_id: str) -> bool:
        if self.get_label(label_id):
            return self.api.delete_label(label_id)
        else:
            print(f"Label with id {label_id} does not exist.")
            return False

    def delete_project(self, project_id: str) -> bool:
        if self.get_project(project_id):
            return self.api.delete_project(project_id)
        else:
            print(f"Project with id {project_id} does not exist.")
            return False

    def delete_section(self, section_id: str) -> bool:
        if self.get_section(section_id):
            return self.api.delete_section(section_id)
        else:
            print(f"Section with id {section_id} does not exist.")
            return False

    def delete_task(self, task_id: str) -> bool:
        if self.get_task(task_id):
            return self.api.delete_task(task_id)
        else:
            print(f"Task with id {task_id} does not exist.")
            return False
