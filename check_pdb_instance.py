import os
from pathlib import Path

found_pdb = False

print(os.path.abspath(__file__))

# for root, dirs, files in os.walk(os.environ['GUI_SCRIPT_DIR']):
#     for file in files:
#         if file.endswith('.py'):
#             complete_path = (os.path.join(root, file))
#             file_path = Path(complete_path)
#             if complete_path == os.path.abspath(__file__):
#                 continue
#             file_content = file_path.read_text()
#             if "pdb.set_trace()" in file_content:
#                 print(f"{complete_path} has pdb set_trace() present.")
#                 found_pdb = True
#             elif "import pdb" in file_content:
#                 print(f"{complete_path} has a pdb module present.")
#                 found_pdb = True

# if not found_pdb:
#     print("No PDB instance found")
