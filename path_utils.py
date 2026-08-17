import sys
from pathlib import Path
def resource_path(relative):
    if getattr(sys, 'frozen', False):
        base_path=Path(sys._MEIPASS)
    else:
        base_path=Path(__file__).parent
    return base_path / relative