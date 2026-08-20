"""Check local links and fragments in a generated static site."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[tuple[str, str]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)
        for attribute in ("href", "src"):
            value = values.get(attribute)
            if value:
                self.links.append((attribute, value))


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def resolve_target(site: Path, source: Path, raw_url: str) -> tuple[Path, str]:
    parsed = urlsplit(raw_url)
    relative = unquote(parsed.path)
    if relative.startswith("/"):
        target = site / relative.removeprefix("/")
    else:
        target = source.parent / relative

    if not relative:
        target = source
    elif relative.endswith("/") or target.is_dir():
        target /= "index.html"
    elif not target.suffix and not target.exists():
        target = target / "index.html"

    return target.resolve(), unquote(parsed.fragment)


def check_site(site: Path) -> list[str]:
    site = site.resolve()
    pages = sorted(site.rglob("*.html"))
    if not pages:
        return [f"no HTML pages found under {site}"]

    parsed_pages = {page.resolve(): parse_page(page) for page in pages}
    failures: list[str] = []
    for source, parsed_page in parsed_pages.items():
        for attribute, raw_url in parsed_page.links:
            parsed = urlsplit(raw_url)
            if parsed.scheme or parsed.netloc or raw_url.startswith("//"):
                continue
            target, fragment = resolve_target(site, source, raw_url)
            try:
                target.relative_to(site)
            except ValueError:
                failures.append(
                    f"{source.relative_to(site)}: {attribute} escapes site: {raw_url}"
                )
                continue
            if not target.exists():
                failures.append(
                    f"{source.relative_to(site)}: missing {attribute}: {raw_url}"
                )
                continue
            if fragment and target.suffix == ".html":
                target_page = parsed_pages.get(target)
                if target_page is None:
                    target_page = parse_page(target)
                    parsed_pages[target] = target_page
                if fragment not in target_page.ids:
                    failures.append(
                        f"{source.relative_to(site)}: missing fragment: {raw_url}"
                    )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=Path)
    args = parser.parse_args()
    failures = check_site(args.site)
    if failures:
        print("\n".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
