from abc import ABC, abstractmethod

from exporters import (
        VideoExporter,
        LosslessVideoExporter,
        H264BPVideoExporter,
        AudioExporter,
        AACAudioExporter,
        WAVAudioExporter)


class ExporterFactory(ABC):
    """Factory that represents combination of video and audio codecs."""
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""
        pass

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance"""
        pass


class FastExporter(ExporterFactory):
    """
    Concrete Factory for low-res audio and video
    """
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class SlowExporter(ExporterFactory):
    """
    Concrete Factory for high-res audio and video
    """
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()
