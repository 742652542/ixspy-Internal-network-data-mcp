from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Iterable


def _load_categories(filename: str) -> list[dict[str, Any]]:
    data_path = Path(__file__).resolve().parent / "data" / filename
    try:
        raw = data_path.read_text(encoding="utf-8")
        return json.loads(raw)
    except Exception as exc:  # noqa: BLE001 - return a concise error upstream
        raise RuntimeError(f"load categories failed: {exc}") from exc


_ETSY_CATEGORIES = _load_categories("etsy_categories.json")
_SHOPIFY_CATEGORIES = _load_categories("shopify_categories.json")


def get_etsy_categories() -> list[dict[str, Any]]:
    return _ETSY_CATEGORIES


def get_shopify_categories() -> list[dict[str, Any]]:
    return _SHOPIFY_CATEGORIES


def _walk_categories(
    categories: Iterable[dict[str, Any]],
    path_labels: list[str],
    path_values: list[int],
) -> Iterable[tuple[dict[str, Any], list[str], list[int]]]:
    for item in categories:
        label = item.get("label")
        value = item.get("value")

        next_labels = path_labels + ([label] if label else [])
        next_values = path_values + ([value] if isinstance(value, int) else [])

        yield item, next_labels, next_values

        children = item.get("children") or []
        if children:
            yield from _walk_categories(children, next_labels, next_values)


def _build_matcher(query: str) -> Callable[[str], bool]:
    cleaned = query.strip()
    if not cleaned:
        return lambda _: False

    if "|" in cleaned:
        tokens = [token.strip().casefold() for token in cleaned.split("|") if token.strip()]
        return lambda text: any(token in text for token in tokens)

    if "&" in cleaned:
        tokens = [token.strip().casefold() for token in cleaned.split("&") if token.strip()]
        return lambda text: all(token in text for token in tokens)

    token = cleaned.casefold()
    return lambda text: token in text


def _search_categories(
    categories: list[dict[str, Any]],
    query: str,
    limit: int | None,
) -> list[dict[str, Any]]:
    matcher = _build_matcher(query)
    normalized_limit = limit if limit and limit > 0 else None
    results: list[dict[str, Any]] = []

    for item, labels, values in _walk_categories(categories, [], []):
        label = item.get("label")
        value = item.get("value")
        if not label:
            continue

        path = "/" + "/".join(labels)
        haystack = f"{label} {path}".casefold()

        if matcher(haystack):
            results.append(
                {
                    "label": label,
                    "value": value,
                    "path": path,
                    "path_ids": values,
                    "depth": max(len(labels) - 1, 0),
                }
            )
            if normalized_limit and len(results) >= normalized_limit:
                break

    return results


def search_etsy_categories(query: str, limit: int | None = None) -> list[dict[str, Any]]:
    return _search_categories(_ETSY_CATEGORIES, query, limit)


def search_shopify_categories(
    query: str, limit: int | None = None
) -> list[dict[str, Any]]:
    return _search_categories(_SHOPIFY_CATEGORIES, query, limit)
