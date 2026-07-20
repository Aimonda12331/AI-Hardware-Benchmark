# Xem config.py như bảng điều khiển (Control Panel) của toàn bộ dự án.
"""
Project Configuration.
"""
class ProjectConfig:
    """ PROJECT INFORMATION """
    PROJECT_NAME = "AI Hardware Benchmark"

    VERSION = "0.1.0"

    AUTHOR = "NGUYEN NHAT TUAN - K15B - TRUONG DAI HOC CONG NGHIEP TP HCM"

    LICENSE = "MIT"

class DirectoryConfig:
    """ DIRECTORY CONFIGURATION """
    ROOT_DIR = ...

    BENCHMARK_DIR = ...

    LOG_DIR = ...

    REPORT_DIR = ...

    DOC_DIR = ...

    SCRIPT_DIR = ...

class LoggingConfig:
    """ LOGGING CONFIGURATION """
    LOG_FILE = ...

    LOG_LEVEL = ...

    LOG_FORMAT = ...

class ReportingConfig:
    """ REPORTING CONFIGURATION """
    REPORT_NAME = ...

    REPORT_FORMATS = ...

class BenchmarkConfig:
    """ BENCHMARK CONFIGURATION """
    DEFAULT_REPEAT = ...

    DEFAULT_TIMEOUT = ...

    DEFAULT_WARMUP = ...

class Config:
    """Global Configuration for AI Hardware Benchmark"""
    Project   = ProjectConfig
    Directory = DirectoryConfig
    Logging   = LoggingConfig
    Reporting = ReportingConfig
    Benchmark = BenchmarkConfig




