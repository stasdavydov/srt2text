# Extract blocks of text from SRT file with time marks by duration

import click
from pysrt import SubRipFile


def is_eot(text: str):
    return text[-1] in {'.', '!', '?'} if text is not None else False


@click.command()
@click.argument('srt_file')
@click.option('--encoding', default='utf8', help='Encoding')
@click.option('--duration', default=180, type=int, help="Duration in sec")
def main(srt_file, encoding, duration):
    with open(srt_file.replace('.srt', '.txt'), 'w+', encoding=encoding) as out:
        srt = SubRipFile.open(srt_file, encoding=encoding)

        start = 0
        prev_text = None
        for item in srt:
            if start == 0:
                print('%02d:%02d:%02d' % tuple(item.start)[0:3], file=out)
            if prev_text != item.text:
                print(item.text.capitalize() if is_eot(prev_text) else item.text, end=' ', file=out)
            prev_text = item.text
            start += int(item.duration.ordinal / 1000)
            if start > duration and is_eot(item.text):
                start = 0
                print("\n", file=out)


if __name__ == "__main__":
    main()
