"""Tekrar tespiti: birebir aynı dosya (bayt) ve aynı metin (farklı bayt).

Spec §9: birebir aynılarda tek kopya kalır; metin aynılarında kelime sayısı
fazla olan asıl seçilir, diğeri yönlendirme dosyasına dönüşür.
"""
import hashlib
import re

_WS = re.compile(r"\s+")


def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def text_hash(text):
    """Boşluk ve büyük/küçük harf farkını yok sayar. Türkçe karakter KORUNUR."""
    norm = _WS.sub("", text).lower()
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def _group(entries, key):
    buckets = {}
    for e in entries:
        buckets.setdefault(e[key], []).append(e)
    return [v for v in buckets.values() if len(v) > 1]


def find_duplicates(entries):
    """entries: [{'path','fhash','thash','words'}, ...]

    Döner: {'binary': [[path,...]], 'text': [[path,...]]}
    Her grupta ilk eleman asıl (kelime sayısı en fazla, eşitse yol alfabetik).
    'text' grupları, tamamı zaten 'binary' grubu olanları içermez.
    """
    def order(g):
        return sorted(g, key=lambda e: (-e["words"], e["path"]))

    binary = [[e["path"] for e in order(g)] for g in _group(entries, "fhash")]

    text = []
    for g in _group(entries, "thash"):
        if len({e["fhash"] for e in g}) == 1:
            continue  # zaten birebir aynı, binary listesinde
        text.append([e["path"] for e in order(g)])

    binary.sort(key=lambda g: g[0])
    text.sort(key=lambda g: g[0])
    return {"binary": binary, "text": text}
