"""Gumroad product mockups from REAL product pages.

Renders a 1280x720 cover + 600x600 thumbnail per product. Every page shown is a
real rendered page of the shipped PDFs (or, for Marketing OS, a page rendered in
the same typographic system listing the real command names).
"""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).parent
PAGES = ROOT / "pages"
OUT = ROOT / "gumroad"
OUT.mkdir(exist_ok=True)

CREAM = (252, 234, 224)
CREAM_PAGE = (250, 246, 238)
PINK = (245, 213, 208)
CORAL = (209, 114, 107)
SAGE = (74, 104, 89)
INK = (24, 19, 17)
GOLD = (176, 141, 87)

BASK = "/System/Library/Fonts/Supplemental/Baskerville.ttc"


def font(size: int, face: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(BASK, size, index=face)


# ---------------------------------------------------------------- page makers
def dark_cover(title: str, subtitle: str, kicker: str = "THE SHIP IT SYSTEM") -> Image.Image:
    w, h = 935, 1210
    im = Image.new("RGB", (w, h), INK)
    d = ImageDraw.Draw(im)
    d.line([(60, 40), (60, 120)], fill=GOLD, width=3)
    d.line([(60, 40), (140, 40)], fill=GOLD, width=3)
    d.text((110, 160), kicker, font=font(22), fill=GOLD, spacing=4)
    y = 215
    for line in title.split("\n"):
        d.text((110, y), line, font=font(92), fill=CREAM_PAGE)
        y += 104
    d.text((110, y + 24), subtitle, font=font(34, 2), fill=CREAM_PAGE)
    d.text((110, y + 80), "The Ship It System", font=font(24), fill=(200, 190, 178))
    d.text((110, h - 200), "Molly Shelestak", font=font(26, 1), fill=CORAL)
    d.text((110, h - 165), "Build Partner for Side-Project Shippers", font=font(22), fill=(200, 190, 178))
    d.text((110, h - 135), "theshipitsystem.com  |  @unstuckwithmolly", font=font(20), fill=(150, 142, 132))
    return im


def index_page(title: str, items: list[str], footer: str) -> Image.Image:
    w, h = 935, 1210
    im = Image.new("RGB", (w, h), CREAM_PAGE)
    d = ImageDraw.Draw(im)
    d.line([(60, 40), (60, 120)], fill=GOLD, width=2)
    d.line([(60, 40), (140, 40)], fill=GOLD, width=2)
    d.text((110, 140), title, font=font(54), fill=INK)
    d.line([(110, 215), (400, 215)], fill=GOLD, width=2)
    col_w = 400
    per_col = math.ceil(len(items) / 2)
    for i, it in enumerate(items):
        col, row = divmod(i, per_col)
        x = 110 + col * col_w
        y = 260 + row * 62
        d.ellipse([x, y + 10, x + 10, y + 20], fill=CORAL)
        d.text((x + 24, y), it, font=font(24), fill=INK)
    d.text((110, h - 90), footer, font=font(18), fill=(150, 142, 132))
    return im


MOS_COMMANDS = [
    "Persona Playbook", "Awareness to Messaging", "Viral Hook Generator",
    "Instagram Reels Framework", "Funnel Ad Creator", "Content Repurposing Pipeline",
    "Brand Voice Blueprint", "Humanize AI Writing", "Irresistible Offer",
    "Conversion Sales Letter", "Micro-Commitment Ladder", "Offer Ladder",
    "Pricing Architecture", "Testimonial Stories", "FAQ from Objections",
    "Funnel Landing Page Designer", "Launch Sequence", "Onboarding Sequence",
    "Email Story Engine", "Referral Engine", "Win-Back System",
    "Tag-Based Funnel System", "Business Launch Checklist", "SaaS Financial Model",
    "Design-Tell Audit", "Skill Router",
]


# ---------------------------------------------------------------- compositing
def shadow(size: tuple[int, int], blur: int, alpha: int) -> Image.Image:
    sh = Image.new("RGBA", (size[0] + blur * 6, size[1] + blur * 6), (0, 0, 0, 0))
    d = ImageDraw.Draw(sh)
    d.rectangle([blur * 3, blur * 3, blur * 3 + size[0], blur * 3 + size[1]], fill=(40, 20, 15, alpha))
    return sh.filter(ImageFilter.GaussianBlur(blur))


def page_object(page: Image.Image, height: int, angle: float, thick: int = 0) -> Image.Image:
    """A page (or bound book if thick>0) with edge and soft shadow, rotated."""
    ratio = page.width / page.height
    w = int(height * ratio)
    pg = page.convert("RGB").resize((w, height), Image.LANCZOS)
    pad = 60
    canvas = Image.new("RGBA", (w + pad * 2 + thick, height + pad * 2 + thick), (0, 0, 0, 0))
    sh = shadow((w + thick, height + thick), 22, 110)
    canvas.alpha_composite(sh, (pad - 66 + 14, pad - 66 + 26))
    # page block / spine thickness
    for i in range(thick, 0, -2):
        tone = 232 - i
        block = Image.new("RGBA", (w, height), (tone, tone - 6, tone - 14, 255))
        canvas.alpha_composite(block, (pad + i, pad + i))
    # thin border to separate light pages from the background
    framed = Image.new("RGBA", (w + 2, height + 2), (215, 200, 190, 255))
    framed.paste(pg, (1, 1))
    canvas.alpha_composite(framed, (pad, pad))
    return canvas.rotate(angle, resample=Image.BICUBIC, expand=True)


def background(w: int, h: int) -> Image.Image:
    bg = Image.new("RGB", (w, h), CREAM)
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    g = ImageDraw.Draw(glow)
    g.ellipse([-w * 0.25, -h * 0.55, w * 0.75, h * 0.95], fill=PINK + (255,))
    g.ellipse([w * 0.45, h * 0.35, w * 1.25, h * 1.45], fill=(238, 224, 214, 255))
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    bg = Image.alpha_composite(bg.convert("RGBA"), glow).convert("RGB")
    # ground shadow line so objects sit on a surface
    ground = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(ground)
    gd.ellipse([w * 0.36, h * 0.84, w * 1.02, h * 1.04], fill=(120, 80, 70, 55))
    ground = ground.filter(ImageFilter.GaussianBlur(40))
    return Image.alpha_composite(bg.convert("RGBA"), ground).convert("RGB")


def wrap(d: ImageDraw.ImageDraw, text: str, f: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def render(slug: str, title: str, sub: str, cover: Image.Image, pages: list[Image.Image],
           inclusions: list[str], stack: list[Image.Image] | None = None) -> None:
    W, H = 1280, 720
    im = background(W, H)
    # fanned interior pages behind the cover, right side
    anchor_x, anchor_y = 610, 62
    fan = [(11.0, 372, 26), (6.0, 232, 12)][: len(pages)]
    for (ang, dx, dy), pg in zip(fan, pages):
        obj = page_object(pg, 420, -ang)
        im.paste(obj, (anchor_x + dx, anchor_y + dy), obj)
    book = page_object(cover, 440, 4.5, thick=14)
    im.paste(book, (anchor_x - 30, anchor_y), book)
    if stack:
        # small stack of template sheets bottom-left of the book
        for i, pg in enumerate(stack[::-1]):
            obj = page_object(pg, 190, -12 + i * 6)
            im.paste(obj, (500 + i * 16, 432 - i * 5), obj)
    d = ImageDraw.Draw(im)
    x = 84
    d.text((x, 118), "THE SHIP IT SYSTEM", font=font(20), fill=SAGE)
    d.line([(x, 150), (x + 54, 150)], fill=CORAL, width=3)
    y = 172
    tf = font(66)
    for line in wrap(d, title, tf, 470):
        d.text((x, y), line, font=tf, fill=INK)
        y += 72
    y += 10
    sf = font(28, 2)
    for line in wrap(d, sub, sf, 470):
        d.text((x, y), line, font=sf, fill=(90, 78, 72))
        y += 36
    y += 26
    pf = font(21)
    for inc in inclusions:
        tw = d.textlength(inc, font=pf)
        d.rounded_rectangle([x, y, x + tw + 34, y + 40], radius=20, outline=CORAL, width=2)
        d.text((x + 17, y + 8), inc, font=pf, fill=INK)
        y += 52
    im.save(OUT / f"{slug}-cover-1280x720.png", optimize=True)
    # square thumbnail: product only, tighter crop
    sq = background(720, 720)
    fan_sq = [(9.5, 205, 40), (5.0, 120, 30)][: len(pages)]
    for (ang, dx, dy), pg in zip(fan_sq, pages):
        obj = page_object(pg, 430, -ang)
        sq.paste(obj, (160 + dx, 100 + dy), obj)
    book = page_object(cover, 470, 4.5, thick=14)
    sq.paste(book, (110, 90), book)
    sd = ImageDraw.Draw(sq)
    sd.text((60, 48), "THE SHIP IT SYSTEM", font=font(18), fill=SAGE)
    sq = sq.resize((600, 600), Image.LANCZOS)
    sq.save(OUT / f"{slug}-thumb-600x600.png", optimize=True)


def P(name: str) -> Image.Image:
    return Image.open(PAGES / name)


if __name__ == "__main__":
    mos_cover = dark_cover("Marketing\nOS.", "26 framework-anchored marketing commands.")
    mos_index = index_page("The 26 commands", MOS_COMMANDS,
                           "Marketing OS  |  theshipitsystem.com  |  @unstuckwithmolly")
    mos_cover.save(PAGES / "mos-cover.png")
    mos_index.save(PAGES / "mos-index.png")

    render("ship-it-kit", "The Ship It Kit", "The 90-day playbook. Idea to first sale to product-market fit.",
           P("playbook-001.png"), [P("pbmid-009.png"), P("playbook-003.png")],
           ["130-page playbook", "25 fill-in templates", "6 modules, 5 to 10 hrs a week"],
           stack=[P("t07-01.png"), P("t08-01.png"), P("t05-01.png")])

    render("bundle", "The Ship It System Bundle", "The Ship It Kit plus Marketing OS. Build it, then sell it.",
           P("playbook-001.png"), [mos_index, mos_cover],
           ["130-page playbook", "25 templates", "26 marketing commands for Claude"],
           stack=[P("t11-01.png"), P("t12-01.png")])

    render("marketing-os", "Marketing OS", "26 AI skills that write your marketing while you ship.",
           mos_cover, [mos_index, P("t11-01.png")],
           ["Offers, pricing, sales letters", "Launch and win-back emails", "Hooks, reels, ad scripts"])

    render("ship-it-or-kill-it", "Ship It or Kill It in 90 Days", "For the project you keep dragging around. Decide already.",
           P("ninety-01.png"), [P("ninety-03.png"), P("ninety-02.png")],
           ["3 checkpoints: day 30, 60, 90", "Ship or kill scorecard", "The side-project shipper's playbook"])

    render("momentum-method", "The Momentum Method", "21 days to unstoppable progress. If you keep falling off, it's the setup, not you.",
           P("momentum-01.png"), [P("momentum-03.png"), P("momentum-02.png")],
           ["21-day framework", "Missed days don't reset you", "Self-guided, start today"])

    render("one-page-launch-plan", "The One-Page Launch Plan", "Seven prompts. Fifteen minutes. A plan you can start this week.",
           P("oplp-01.png"), [P("oplp-03.png"), P("oplp-02.png")],
           ["7 prompts, one page", "About 15 minutes", "Free, no card"])
    print("done", sorted(p.name for p in OUT.iterdir()))
