"""Compatibilidad para imports antiguos del bot; la implementación vive en pydownloader."""

from pydownloader.youtube import (  # noqa: F401
    filter_formats,
    getVideoData,
    get_video_info,
    get_youtube_info,
)
