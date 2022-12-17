import imageio.v3 as iio


def main():
    frames = iio.imiter("file://vids/input.webm", plugin="pyav")

    # iterate over large videos
    for id_frame, frame in enumerate(frames):
        with iio.imopen(
            f"file://frames_output/frame-{id_frame}.png",
            "w",
            plugin="pillow",
        ) as file:
            file.write(frame)


if "__main__" == __name__:
    main()
