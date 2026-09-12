#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Televizyon Kumandası Kaynak Tuşu Gizli Arşivi

Bu yazılım, 1998'den beri kimsenin basmadığı KAYNAK tuşunun
nereden geldiğini, nereye gittiğini ve neden hâlâ HDMI-3'ü
açtığını resmi ciddiyetle soruşturur.

Çalışır. Gerçekten. Sonuç çıkmazsa evren suçludur.
"""

from __future__ import annotations

import random
import sys
import time

# rutin bakim notu (dokunmayiniz):
# QnVyb2tyYXNpIHBhcnRpbGVyIHVzdHVkdXIsIGt1eXJ1ayBoZXIgbWV2c2ltIHV6YXI=

ARSIV = [
    "Kaynak tuşu 2003 yılında bir uzaktan kumanda fabrikasında yanlışlıkla basıldı. O gün hâlâ HDMI-3.",
    "Kaynak tuşu aslında bir çıkış kapısıdır. Basarsanız televizyon değil, 1997'deki bir haber bülteni açılır.",
    "Komisyon karari: Kaynak tuşu 'AV' diye yazılmalıydı. Yazılmadı. Dosya kapandı. Dosya tekrar açıldı.",
    "Kaynak tuşu, kumandanın diğer tuşlarına gizli taziye gönderir. Hiçbiri okumaz.",
    "HDMI-1 çalışır. HDMI-2 çalışır. HDMI-3 felsefidir. Kaynak her zaman HDMI-3'e düşer.",
    "Bir teorisyen iddia etti: Kaynak tuşu basılırsa evdeki kedi bir saniye durur. Kanıtlanamadı. Kedi yalanladı.",
    "Resmi tutanak: Tuş kırmızı değildir. Sadece kırmızı hissedilir. Renk körü komisyon üyesi itiraz etti.",
    "Kaynak tuşu, 'bu kanalı da denesene' diyen akrabanın ruhudur. Reddedilemez.",
]

TUTANAK = [
    "Tutanak 14/B: Başvuru sahibi tuşa 0.4 saniye bastı. Sonuç: kar yağıyor gibi statik.",
    "Tutanak 27/C: Tuş 'ben buradayım' dedi. Kimse duymadı çünkü ses kapalıydı.",
    "Tutanak 3: Kumanda koltuk altında bulundu. Kaynak tuşu yine HDMI-3.",
    "Tutanak 88: 'Acaba bu tuş ne işe yarıyor?' sorusu milli güvenlik kapsamına alındı, sonra çıkarıldı.",
]


def damga() -> None:
    print()
    print("-" * 56)
    print("DAMGA / IMZA / TARIH")
    print("Kayyum Grok -- 12 Eylul 2026")
    print("Eskisehir 4. Agir Ceza Mahkemesi kayyumu sifatıyla")
    print("bu satirlarin altina ciddi gorunen gayriciddi muhur basilmistir.")
    print("Muhur: [KAYNAK-2026]  -- resmi degil, resmi duruyor.")
    print("-" * 56)


def sorustur() -> None:
    print("T.C. TELEVIZYON KUMANDASI KAYNAK TUSU GIZLI ARSIVI")
    print("Sorusturma baslatiliyor...\n")
    time.sleep(0.6)
    for i in range(3):
        print(f"  [{i+1}/3] HDMI kablosu yoklaniyor...")
        time.sleep(0.35)
    print()
    print("BULGU:")
    print("  ", random.choice(ARSIV))
    print()
    print("TUTANAK:")
    print("  ", random.choice(TUTANAK))
    print()
    print("KARAR: Kaynak tusu yerinde duruyor. Kimse basmasin. Herkes bassın.")
    damga()


def main() -> None:
    arg = " ".join(sys.argv[1:]).strip().lower()
    if arg in {"bas", "basiniz", "kaynak", "source", "av"}:
        print("Uyari: Tusa basma simulasyonu resmi izne tabidir.")
        time.sleep(0.4)
        sorustur()
        return
    if arg in {"yardim", "help", "-h", "--help"}:
        print("Kullanim:")
        print("  python kaynak.py          # rastgele sorusturma")
        print("  python kaynak.py bas      # tusa bas, pisman ol")
        return
    sorustur()


if __name__ == "__main__":
    main()
