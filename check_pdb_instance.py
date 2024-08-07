import os
from pathlib import Path

found_pdb = False


for root, dirs, files in os.walk(Path(__file__).parent.resolve()):
    for file in files:
        if file.endswith('.py'):
            complete_path = (os.path.join(root, file))
            file_path = Path(complete_path)
            if complete_path == os.path.abspath(__file__):
                continue
            file_content = file_path.read_text()
            if "pdb.set_trace()" in file_content:
                print(f"{complete_path} has pdb set_trace() present.")
                os._exit(1)
            elif "import pdb" in file_content:
                print(f"{complete_path} has a pdb module present.")
                os._exit(1)

os._exit(0)


