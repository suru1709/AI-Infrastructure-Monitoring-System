# AI-Powered Infrastructure Monitoring & Auto-Healing Platform

## Overview

An intelligent infrastructure monitoring platform that continuously monitors system health, analyzes incidents using AI, and performs automated remediation actions. The platform provides real-time visibility into CPU, memory, and disk utilization while maintaining incident history and automated recovery workflows.

## Features

* Real-time CPU, Memory, and Disk Monitoring
* AI-Assisted Incident Analysis
* Automated Self-Healing Mechanisms
* Interactive Streamlit Dashboard
* Incident History Tracking
* System Health Monitoring
* Logging and Reporting
* Dockerized Deployment
* Linux Compatible Environment

## Tech Stack

### Programming Language

* Python

### Monitoring & Analysis

* psutil
* Pandas
* OpenRouter AI

### Dashboard

* Streamlit
* Streamlit Auto Refresh

### Infrastructure

* Docker
* WSL2
* Linux

### Version Control

* Git
* GitHub

---

## System Architecture

Monitoring Service
↓
Incident Detection
↓
AI Analysis Service
↓
Decision Engine
↓
Auto-Healing Service
↓
Incident Logging
↓
Dashboard Visualization

---

## Project Structure

ai-monitoring-system/

├── monitoring-service/

├── ai-analysis-service/

├── auto-healing-service/

├── dashboard/

├── logs/

├── Dockerfile

├── requirements.txt

└── README.md

---

## Installation & Setup

### Clone Repository

git clone <repository-url>

cd ai-monitoring-system

### Create Virtual Environment

python -m venv venv

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Monitoring Service

python monitoring-service/monitor.py

### Run Dashboard

streamlit run dashboard/app.py

Open:

http://localhost:8501

---

## Docker Setup

### Build Docker Image

docker build -t ai-monitoring-system .

### Run Docker Container

docker run -p 8501:8501 ai-monitoring-system

Open:

http://localhost:8501

---

## Key Functionalities

### Monitoring Engine

Continuously monitors:

* CPU Utilization
* Memory Utilization
* Disk Utilization

### AI Analysis Engine

Analyzes system metrics and:

* Detects critical incidents
* Generates recommendations
* Suggests remediation actions

### Auto-Healing Engine

Performs:

* Temporary File Cleanup
* Incident Recovery
* Automated Remediation Workflows

### Dashboard

Displays:

* Live Metrics
* Health Status
* AI Analysis
* Auto-Healing Logs
* Incident History

---

## Future Enhancements

* Email Alerts
* Slack Notifications
* REST APIs
* Kubernetes Deployment
* Multi-Node Monitoring
* Predictive Failure Analysis

---

## Author

Suruti Kumari

Information Science Engineering Student

Backend Development | Automation | Infrastructure Monitoring
