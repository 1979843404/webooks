#!/bin/bash
gunicorn wsgi:application -b 127.0.0.1:9999
