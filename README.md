# ec2-resource-monitor-in-devops-style
This repo contains all the things like python script and docker file 
# EC2 Resource Monitor

A lightweight Python script to monitor **CPU utilization** and **disk storage** on an **AWS EC2 instance**. The script can run directly on the EC2 instance or inside a Docker container.

---

## Features

- Reports **CPU usage** as a percentage.
- Reports **disk usage** (total, used, free, percent used).
- Compatible with running inside a **Docker container**.
- Easy to extend to multiple EC2 instances or integrate with monitoring tools.

---

## Requirements

- Python 3.7 or higher
- `psutil` Python package

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Pratiks-96/ec2-resource-monitor-in-devops-style.git
cd ec2-resource-monitor-in-devops-style
