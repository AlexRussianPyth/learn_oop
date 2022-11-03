import pathlib

from factory import ExporterFactory, FastExporter, SlowExporter


def read_exporter() -> ExporterFactory | None:
    """Read a desired exporter quality and returns a specific factory"""
    factories = {
            "low": FastExporter(),
            "high": SlowExporter()
            }

    while True:
        quality = str(input("Enter desired output quality (low, high): "))
        if quality in factories:
            return factories[quality]
        return None


def export_data(factory: ExporterFactory):
    # create the video and audio exporters
    video_exporter = factory.get_video_exporter()
    audio_exporter = factory.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    factory = read_exporter()
    export_data(factory)
