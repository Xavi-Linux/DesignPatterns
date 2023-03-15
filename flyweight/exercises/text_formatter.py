

class Tags:
    opening = '\033['
    closing = '\033[0m'
    separator = ';'
    end_of_opening = 'm'


class ForegroundColours(Tags):
    black = 30
    red = 31
    green = 32
    brown = 33
    blue = 34
    purple = 35
    cyan = 36
    grey = 37


class BackgroundColours(Tags):
    black = 40
    red = 41
    green = 42
    brown = 43
    blue = 44
    purple = 45
    cyan = 46
    grey = 47


class FontEffect(Tags):
    bold = 1
    underlined = 4
    blinking = 5


class TextRange:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.effects = []

    def bolden(self) -> 'TextRange':
        self.effects.append(str(FontEffect.bold))

        return self

    def underline(self) -> 'TextRange':
        self.effects.append(str(FontEffect.underlined))

        return self

    def blink(self) -> 'TextRange':
        self.effects.append(str(FontEffect.blinking))

        return self

    def set_foreground_colour(self, colour: str) -> 'TextRange':
        self.effects.append(str(getattr(ForegroundColours, colour)))

        return self

    def set_background_colour(self, colour: str) -> 'TextRange':
        self.effects.append(str(getattr(BackgroundColours, colour)))

        return self

    def apply(self, string: str) -> str:
        if self.effects:
            return Tags.opening + f'{Tags.separator}'.join(self.effects) + Tags.end_of_opening + \
                   string + Tags.closing

        else:
            return string

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __gt__(self, other):
        return self.start > other.start

    def __lt__(self, other):
        return TextRange.__gt__(other, self)

    def __str__(self) -> str:
        return f'Text range starting at {self.start} and ending at {self.end}'

    def __repr__(self) -> str:
        return self.__str__()


class Formatter:

    def __init__(self, string: str):
        self.original_string = string
        self.ranges = []

    def get_range(self, start: int, end: str) -> TextRange:
        range = TextRange(start, end)
        self.ranges.append(range)

        return range

    def __str__(self) -> str:
        final_str = ''
        if self.ranges:
            sorted_ranges = sorted(self.ranges)
            last_end = 0
            final_str += self.original_string[last_end:sorted_ranges[0].start]
            is_start = True
            for range in sorted_ranges:
                start = range.start
                if not is_start:
                    final_str += self.original_string[last_end+1:start]

                final_str += range.apply(self.original_string[start:range.end+1])
                last_end = range.end
                is_start = False

            final_str += self.original_string[last_end+1:]

            return final_str

        return self.original_string


if __name__ == '__main__':

    f = Formatter('hello buddy')
    f.get_range(0, 0).bolden().set_foreground_colour('green')
    f.get_range(1, 1).bolden().set_foreground_colour('blue')
    f.get_range(2, 2).blink().set_foreground_colour('brown')
    f.get_range(3, 3).bolden().set_foreground_colour('purple')
    f.get_range(4, 4).bolden().underline().set_foreground_colour('red')
    f.get_range(6, 10).underline().set_background_colour('cyan')
    print(f)
