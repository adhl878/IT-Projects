import os
import platform
import subprocess
import psutil
from datetime import datetime

def get_system_info():
    print("=" * 50)
    print("SYSTEM INFORMATION REPORT")
    print("=" * 50)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # OS Information
    print("OPERATING SYSTEM:")
    print(f"  OS: {platform.system()}")
    print(f"  Version: {platform.version()}")
    print(f"  Architecture: {platform.architecture()[0]}")
    print(f"  Hostname: {platform.node()}\n")
    
    # CPU Information
    print("CPU INFORMATION:")
    print(f"  Processor: {platform.processor()}")
    print(f"  Cores: {psutil.cpu_count(logical=False)}")
    print(f"  Logical Processors: {psutil.cpu_count(logical=True)}")
    print(f"  CPU Usage: {psutil.cpu_percent(interval=1)}%\n")
    
    # Memory Information
    print("MEMORY INFORMATION:")
    memory = psutil.virtual_memory()
    print(f"  Total RAM: {memory.total / (1024**3):.2f} GB")
    print(f"  Available RAM: {memory.available / (1024**3):.2f} GB")
    print(f"  Used RAM: {memory.used / (1024**3):.2f} GB")
    print(f"  Memory Usage: {memory.percent}%\n")
    
    # Disk Information
    print("DISK INFORMATION:")
    disk = psutil.disk_usage('/')
    print(f"  Total Disk: {disk.total / (1024**3):.2f} GB")
    print(f"  Used Disk: {disk.used / (1024**3):.2f} GB")
    print(f"  Free Disk: {disk.free / (1024**3):.2f} GB")
    print(f"  Disk Usage: {disk.percent}%\n")
    
    # Network Information
    print("NETWORK INFORMATION:")
    try:
        result = os.popen('ipconfig').read()
        lines = result.split('\n')
        for line in lines:
            if 'IPv4 Address' in line or 'Default Gateway' in line:
                print(f"  {line.strip()}")
    except:
        print("  Could not retrieve network info\n")
    
    print("=" * 50)

if __name__ == "__main__":
    get_system_info()
