from PIL import Image, ImageDraw
import secrets

SKIP_RULES = {
    (1, 3): 2, (3, 1): 2,
    (4, 6): 5, (6, 4): 5,
    (7, 9): 8, (9, 7): 8,
    (1, 7): 4, (7, 1): 4,
    (2, 8): 5, (8, 2): 5,
    (3, 9): 6, (9, 3): 6,
    (1, 9): 5, (9, 1): 5,
    (3, 7): 5, (7, 3): 5,
}


def is_valid_move(current: int, candidate: int, visited: list[int]) -> bool:
    if candidate in visited:
        return False
    middle = SKIP_RULES.get((current, candidate))
    if middle is not None and middle not in visited:
        return False
    return True


def generate_pattern(min_len: int = 5, max_len: int = 9) -> list[int]:
    length = min_len + secrets.randbelow(max_len - min_len + 1)
    pattern = [1 + secrets.randbelow(9)]

    while len(pattern) < length:
        current = pattern[-1]
        candidates = [n for n in range(1, 10) if is_valid_move(current, n, pattern)]
        if not candidates:
            break
        pattern.append(secrets.choice(candidates))

    return pattern


def draw_pattern(pattern: list[int], filename: str = "pattern.png", show: bool = True):
    size = 600
    margin = 80
    step = (size - 2 * margin) // 2

    img = Image.new("RGB", (size, size), "#1e2e3e")
    draw = ImageDraw.Draw(img)

    coords = {
        i + 1: (margin + (i % 3) * step, margin + (i // 3) * step)
        for i in range(9)
    }

    points = [coords[p] for p in pattern]
    if len(points) > 1:
        draw.line(points, fill="#f0f0f0", width=15, joint="curve")

    for num, (x, y) in coords.items():
        r = 16 if num in pattern else 10
        color = "#585b70"
        if num == pattern[0]:
            draw.ellipse((x - 39, y - 39, x + 39, y + 39), outline="#a6e3a1", width=3)
            draw.text((x, y - 60), "START", fill="#a6e3a1", anchor="mm")
            color = "#a6e3a1"  # Старт
        elif num == pattern[-1]:
            draw.ellipse((x - 39, y - 39, x + 39, y + 39), outline="#f38ba8", width=3)
            draw.text((x, y + 60), "FINISH", fill="#f38ba8", anchor="mm")
            color = "#f38ba8"  # Финиш
        elif num in pattern:
            color = "#89b4fa"

        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)

    img.save(filename)
    if show:
        img.show()


if __name__ == "__main__":
    key = generate_pattern(min_len=5, max_len=8)
    print("Pattern:", key)
    draw_pattern(key)