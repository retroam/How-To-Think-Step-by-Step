"""
Default configuration for the project.
"""

# Data paths
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
RESULTS_DIR = "results"

# Model settings
MODEL_NAME = "llama"  # or other model names
MODEL_SIZE = "7b"     # or other sizes
USE_PEFT = True
LORA_R = 8
LORA_ALPHA = 32
LORA_DROPOUT = 0.1

# Training settings
BATCH_SIZE = 8
LEARNING_RATE = 2e-5
MAX_LENGTH = 512
NUM_EPOCHS = 3

# Analysis settings
ATTENTION_THRESHOLD = 0.1
NUM_HEADS = 32
HEAD_DIM = 64

# Logging settings
LOG_LEVEL = "INFO"
SAVE_CHECKPOINTS = True
CHECKPOINT_DIR = "checkpoints" 