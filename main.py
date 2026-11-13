print("==============================")
print(" ♻️ AKILLI GERİ DÖNÜŞÜM BOTU")
print("==============================")
print("Merhaba! Ben geri dönüşüm botuyum.")
print("Bir atık adı yaz, sana yardımcı olayım.")
print("Çıkmak için 'çıkış' yaz.\n")

atiklar = {
    "plastik şişe": "Plastik atık! ♻️ Uygun plastik toplama kutusuna at.",
    "kağıt": "Kağıt atık! 📄 Kağıt geri dönüşüm kutusuna at",
    "gazete": "Kağıt atık! 📰 Geri dönüştürülebilir.",
    "cam şişe": "Cam atık! 🍾 Cam toplama kutusuna at.",
    "konserve kutusu": "Metal atık! 🥫 Metal geri dönüşümüne uygundur.",
    "muz kabuğu": "Organik atık! 🍌 Kompost yapılabilir.",
    "pil": "Atık pil! 🔋 Özel atık pil toplama kutusuna bırak.",
    "karton": "Kağıt-karton atık! 📦 Geri dönüştürülebilir.",
    "yemek artığı": "Organik atık! 🍎 Uygun organik atık kutusuna at."
}

while True:
    atik = input("\nAtığın adını yaz: ").lower().strip()

    if atik == "çıkış":
        print("Görüşürüz! Doğayı korumayı unutma! 🌍")
        break

    elif atik in atiklar:
        print("\n🤖 Bot:", atiklar[atik])

    else:
        print("\n🤖 Bot: Bu atığı henüz tanımıyorum.")
        print("Başka bir atık deneyebilirsin!")












