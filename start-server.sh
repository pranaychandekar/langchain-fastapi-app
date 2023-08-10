#!/usr/bin/env bash
coverage run -m pytest
coverage report
python3 app.py