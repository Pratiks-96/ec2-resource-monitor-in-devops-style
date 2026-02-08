import psutil

def get_cpu_usage():
    # CPU utilization as a percentage
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def get_disk_usage():
    # Get disk usage of the root partition
    disk = psutil.disk_usage('/')
    disk_info = {
        'total_gb': disk.total / (1024 ** 3),
        'used_gb': disk.used / (1024 ** 3),
        'free_gb': disk.free / (1024 ** 3),
        'percent_used': disk.percent
    }
    return disk_info

if __name__ == "__main__":
    cpu = get_cpu_usage()
    disk = get_disk_usage()
    
    print(f"CPU Utilization: {cpu}%")
    print(f"Disk Usage: {disk['used_gb']:.2f} GB used of {disk['total_gb']:.2f} GB ({disk['percent_used']}%)")
    print(f"Free Space: {disk['free_gb']:.2f} GB")
