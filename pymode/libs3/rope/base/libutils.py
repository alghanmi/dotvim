"""A few useful functions for using rope as a library"""
import os.path

import rope.base.project
import rope.base.pycore
from rope.base import taskhandle


def path_to_resource(project, path, type=None):
    """Get the resource at path

    You only need to specify `type` if `path` does not exist.  It can
    be either 'file' or 'folder'.  If the type is `None` it is assumed
    that the resource already exists.

    Note that this function uses `Project.get_resource()`,
    `Project.get_file()`, and `Project.get_folder()` methods.

    """
    project_path = relative(project.address, path)
    if project_path is None:
        project_path = rope.base.project._realpath(path)
        project = rope.base.project.get_no_project()
    if type is None:
        return project.get_resource(project_path)
    if type == 'file':
        return project.get_file(project_path)
    if type == 'folder':
        return project.get_folder(project_path)
    return None

def relative(root, path):
    root = rope.base.project._realpath(root).replace(os.path.sep, '/')
    path = rope.base.project._realpath(path).replace(os.path.sep, '/')
    if path == root:
    	return ''
    if path.startswith(root + '/'):
    	return path[len(root) + 1:]

def report_change(project, path, old_content):
    """Report that the contents of file at `path` was changed

    The new contents of file is retrieved by reading the file.

    """
    resource = path_to_resource(project, path)
    if resource is None:
        return
    for observer in list(project.observers):
        observer.resource_changed(resource)
    if project.pycore.automatic_soa:
        rope.base.pycore.perform_soa_on_changed_scopes(project, resource,
                                                       old_content)

def analyze_modules(project, task_handle=taskhandle.NullTaskHandle()):
    """Perform static object analysis on all python files in the project

    Note that this might be really time consuming.
    """
    resources = project.pycore.get_python_files()
    job_set = task_handle.create_jobset('Analyzing Modules', len(resources))
    for resource in resources:
        job_set.started_job(resource.path)
        project.pycore.analyze_module(resource)
        job_set.finished_job()
