# ~ SwarmUI.py | by ANXETY ~

from json_utils import read_json, update_json   # JSON (main)

from IPython.display import clear_output
from IPython.utils import capture
from pathlib import Path
import subprocess
import asyncio
import os

# Constants
UI = 'SwarmUI'

HOME = Path.home()
WEBUI = HOME / UI
SCR_PATH = HOME / 'ANXETY'
SETTINGS_PATH = SCR_PATH / 'settings.json'

SwarmUI_REPO_URL = "https://github.com/mcmonkeyprojects/SwarmUI"

# REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
BRANCH = read_json(SETTINGS_PATH, 'ENVIRONMENT.branch')
EXTS = read_json(SETTINGS_PATH, 'WEBUI.extension_dir')

os.chdir(HOME)

# ==================== WEB UI OPERATIONS ====================

async def _download_file(url, directory, filename):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    process = await asyncio.create_subprocess_shell(
        f'curl -sLo {file_path} {url}',
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    await process.communicate()

async def download_files(file_list):
    tasks = []
    for file_info in file_list:
        parts = file_info.split(',')
        url = parts[0].strip()
        directory = parts[1].strip() if len(parts) > 1 else WEBUI   # Default Save Path
        filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
        tasks.append(_download_file(url, directory, filename))
    await asyncio.gather(*tasks)

async def download_configuration():
    os.makedirs(EXTS, exist_ok=True)
    os.chdir(EXTS)

    tasks = []
    for command in extensions_list:
        tasks.append(asyncio.create_subprocess_shell(
            f'git clone --depth 1 --recursive {command}',
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        ))
    
    # await asyncio.gather(*tasks)
    
    ## install dotnet
    dirs = ['Stable-Diffusion', 'Lora', 'Embeddings', 'VAE', 'upscale_models']
    for sub in dirs:
        (WEBUI / sub).mkdir(parents=True, exist_ok=True)
  
    subprocess.run(['wget', '-O', str(WEBUI / 'dotnet-install.sh'), 'https://dot.net/v1/dotnet-install.sh'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
  
    dotnet = WEBUI / 'dotnet-install.sh'
    dotnet.chmod(0o755)
    subprocess.run(['bash', str(dotnet), '--channel', '8.0'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def unpack_webui():
    zip_path = f"{SCR_PATH}/{UI}.zip"
    get_ipython().system(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {REPO_URL} -d {SCR_PATH} -o {UI}.zip')
    get_ipython().system(f'unzip -q -o {zip_path} -d {WEBUI}')
    get_ipython().system(f'rm -rf {zip_path}')

# ==================== MAIN CODE ====================

if __name__ == "__main__":
    with capture.capture_output():
        # unpack_webui()

        get_ipython().system(f'git clone {SwarmUI_REPO_URL}')
        asyncio.run(download_configuration())