from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig_for_task_1:
  root_dir: Path
  source_URL: str
  local_data_dir: Path