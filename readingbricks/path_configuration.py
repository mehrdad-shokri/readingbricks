"""
This module provides closures for paths to sources.
All path dispatching must be done here in order to have a single
place that is affected by changes in project structure.

@author: Nikolay Lysenko
"""


import os


def get_path_to_ipynb_notes() -> str:
    """
    Get absolute path to directory with Jupyter notebooks containing
    human-written notes.
    """
    path = os.path.join(os.path.dirname(__file__), '..', 'notes')
    return path


def get_path_to_markdown_notes() -> str:
    """
    Get absolute path to directory with automatically created
    Markdown files with notes.
    """
    path = os.path.join(os.path.dirname(__file__), 'markdown_notes')
    return path


def get_path_to_db() -> str:
    """
    Get absolute path to SQLite DB that is used by the Flask app.
    """
    path = os.path.join(os.path.dirname(__file__), 'tag_to_notes.db')
    return path


def get_path_to_counts_of_tags() -> str:
    """
    Get absolute path to a TSV file with counts of tags.
    """
    path = os.path.join(
        os.path.dirname(__file__),
        '..', 'supplementaries', 'counts_of_tags.tsv'
    )
    return path
