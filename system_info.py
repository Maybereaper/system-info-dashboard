import psutil
from rich.console import Console
from rich.table import Table
import time

def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    network_info = psutil.net_if_addrs()
    
    # Format network interfaces into just names
    interfaces = ", ".join(network_info.keys())
    
    return {
        "CPU Usage": f"{cpu_usage}%",
        "Memory Used": f"{memory_info.percent}%",
        "Disk Used": f"{disk_info.percent}%",
        "Network Interfaces": interfaces
    }

console = Console()

while True:
    # Clear screen for fresh output
    console.clear()

    # Re-create a fresh table each time
    table = Table(title="System Information")
    table.add_column("Metric", style="bold cyan")
    table.add_column("Value", style="bold green")

    info = get_system_info()
    for key, value in info.items():
        table.add_row(key, str(value))

    console.print(table)
    time.sleep(2)
