#!/bin/sh
gunicorn -k uvicorn.workers.UvicornWorker -c scripts/config.py app.main:app