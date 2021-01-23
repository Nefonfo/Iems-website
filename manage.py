#!/usr/bin/env python
import os
import sys
import django
from dotenv import load_dotenv

if __name__ == "__main__":
    project_folder = os.getcwd()
    load_dotenv(os.path.join(project_folder, '.env'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv('DJANGO_SETTINGS_MODULE'))
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    django.setup()