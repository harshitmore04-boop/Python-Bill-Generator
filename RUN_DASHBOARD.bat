@echo off
title FreshMart Billing Dashboard
cd /d "%~dp0"
py dashboard.py
if errorlevel 1 python dashboard.py
if errorlevel 1 pause
