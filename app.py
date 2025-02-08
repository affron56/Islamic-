# app.py (Updated)
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Curated list of 200+ common Hindi words in English (Expandable to 2000)
islamic_words = [
    # Paigambar (Prophets)
    "Adam", "Ibrahim", "Ismail", "Ishaq", "Yaqub", "Yusuf", "Musa", "Harun", "Dawud", "Sulaiman",
    "Yunus", "Ilyas", "Ayyub", "Zakariya", "Yahya", "Isa", "Muhammad",

    # Allah ke Wali (Saints and Righteous People)
    "Abu Bakr", "Umar", "Usman", "Ali", "Khadija", "Fatima", "Hassan", "Hussain", "Bilal", "Salman",
    "Suhail", "Uthman", "Ammar", "Zubair", "Talha", "Saad", "Saeed", "Abdullah", "Usama", "Zaid",

    # Imams (Shia Islam)
    "Ali", "Hassan", "Hussain", "Zainul Abideen", "Muhammad Baqir", "Jafar Sadiq", "Musa Kazim",
    "Ali Raza", "Muhammad Taqi", "Ali Naqi", "Hassan Askari", "Muhammad Mehdi",

    # Jungon ke Naam (Famous Battles)
    "Badr", "Uhud", "Khandaq", "Khyber", "Hunain", "Tabuk", "Muta", "Yarmouk", "Qadisiyya", "Siffin",
    "Nahrawan", "Karbala", "Jamal", "Harrah", "Plassey", "Panipat", "Hattin", "Ain Jalut", "Manzikert",

    # Jagah ke Naam (Holy Places and Cities)
    "Makkah", "Madinah", "Jerusalem", "Karbala", "Najaf", "Kufa", "Basra", "Damascus", "Baghdad",
    "Cairo", "Istanbul", "Samarra", "Qom", "Medina", "Taif", "Jeddah", "Hebron", "Ghaza", "Sanaa",
    "Khartoum", "Timbuktu", "Cordoba", "Granada", "Delhi", "Lahore", "Karachi", "Jakarta", "Kuala Lumpur",

    # Quranic Words and Phrases
    "Allah", "Rahman", "Rahim", "Malik", "Quddus", "Salam", "Mumin", "Muhaymin", "Aziz", "Jabbar",
    "Mutakabbir", "Khaliq", "Bari", "Musawwir", "Ghaffar", "Qahhar", "Wahhab", "Razzaq", "Fattah",
    "Alim", "Qabid", "Basit", "Khafid", "Rafi", "Muizz", "Mudhill", "Samee", "Basir", "Hakam",
    "Adl", "Latif", "Khabir", "Halim", "Azim", "Ghafur", "Shakur", "Ali", "Kabir", "Hafiz",
    "Muqit", "Hasib", "Jalil", "Karim", "Raquib", "Mujib", "Wasi", "Hakim", "Wadud", "Majid",
    "Baith", "Hashr", "Qiyamah", "Jannah", "Jahannum", "Siraat", "Mizan", "Hawd", "Shafaah",

    # Islamic Months
    "Muharram", "Safar", "Rabi al-Awwal", "Rabi al-Thani", "Jumada al-Awwal", "Jumada al-Thani",
    "Rajab", "Shaaban", "Ramadan", "Shawwal", "Dhul Qadah", "Dhul Hijjah",

    # Add more categories as needed...
]

islamic_words += [
    # 1. Asma ul-Husna (Allah ke 99 Naam)
    "Ar-Rahman", "Ar-Rahim", "Al-Malik", "Al-Quddus", "As-Salam", "Al-Mumin", "Al-Muhaymin",
    "Al-Aziz", "Al-Jabbar", "Al-Mutakabbir", "Al-Khaliq", "Al-Bari", "Al-Musawwir", "Al-Ghaffar",
    "Al-Qahhar", "Al-Wahhab", "Ar-Razzaq", "Al-Fattah", "Al-Alim", "Al-Qabid", "Al-Basit",
    "Al-Khafid", "Ar-Rafi", "Al-Muizz", "Al-Mudhill", "As-Sami", "Al-Basir", "Al-Hakam", "Al-Adl",
    "Al-Latif", "Al-Khabir", "Al-Halim", "Al-Azim", "Al-Ghafur", "Ash-Shakur", "Al-Ali", "Al-Kabir",
    "Al-Hafiz", "Al-Muqit", "Al-Hasib", "Al-Jalil", "Al-Karim", "Ar-Raqib", "Al-Mujib", "Al-Wasi",
    "Al-Hakim", "Al-Wadud", "Al-Majid", "Al-Wahid", "Al-Ahad", "As-Samad", "Al-Qadir", "Al-Muqtadir",
    "Al-Muqaddim", "Al-Muakhkhir", "Al-Awwal", "Al-Akhir", "Az-Zahir", "Al-Batin", "Al-Wali",
    "Al-Mutaali", "Al-Barr", "At-Tawwab", "Al-Muntaqim", "Al-Afuww", "Ar-Rauf", "Malik ul-Mulk",
    "Dhul-Jalali wal-Ikram", "Al-Muqsit", "Al-Jami", "Al-Ghani", "Al-Mughni", "Al-Mani", "Ad-Darr",
    "An-Nafi", "An-Nur", "Al-Hadi", "Al-Badi", "Al-Baqi", "Al-Warith", "Ar-Rashid", "As-Sabur",

    # 2. Quran ki Surahon ke Naam (114 Surahs)
    "Al-Fatiha", "Al-Baqarah", "Al-Imran", "An-Nisa", "Al-Maidah", "Al-Anam", "Al-Araf", "Al-Anfal",
    "At-Tawbah", "Yunus", "Hud", "Yusuf", "Ar-Rad", "Ibrahim", "Al-Hijr", "An-Nahl", "Al-Isra",
    "Al-Kahf", "Maryam", "Taha", "Al-Anbiya", "Al-Hajj", "Al-Muminun", "An-Nur", "Al-Furqan",
    "Ash-Shuara", "An-Naml", "Al-Qasas", "Al-Ankabut", "Ar-Rum", "Luqman", "As-Sajdah", "Al-Ahzab",
    "Saba", "Fatir", "Ya-Sin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir", "Fussilat", "Ash-Shura",
    "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiyah", "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat",
    "Qaf", "Adh-Dhariyat", "At-Tur", "An-Najm", "Al-Qamar", "Ar-Rahman", "Al-Waqiah", "Al-Hadid",
    "Al-Mujadilah", "Al-Hashr", "Al-Mumtahanah", "As-Saff", "Al-Jumuah", "Al-Munafiqun", "At-Taghabun",
    "At-Talaq", "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqah", "Al-Maarij", "Nuh", "Al-Jinn",
    "Al-Muzzammil", "Al-Muddathir", "Al-Qiyamah", "Al-Insan", "Al-Mursalat", "An-Naba", "An-Naziat",
    "Abasa", "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj", "At-Tariq",
    "Al-Ala", "Al-Ghashiyah", "Al-Fajr", "Al-Balad", "Ash-Shams", "Al-Layl", "Ad-Duha", "Al-Inshirah",
    "At-Tin", "Al-Alaq", "Al-Qadr", "Al-Bayyinah", "Az-Zalzalah", "Al-Adiyat", "Al-Qariah", "At-Takathur",
    "Al-Asr", "Al-Humazah", "Al-Fil", "Quraysh", "Al-Maun", "Al-Kawthar", "Al-Kafirun", "An-Nasr",
    "Al-Masad", "Al-Ikhlas", "Al-Falaq", "An-Nas",

    # 3. Paigambar aur Sahaba ke Naam (150+)
    "Adam", "Nuh", "Idris", "Hud", "Salih", "Ibrahim", "Lut", "Ismail", "Ishaq", "Yaqub", "Yusuf",
    "Ayyub", "Shuayb", "Musa", "Harun", "Dawud", "Sulaiman", "Ilyas", "Al-Yasa", "Yunus", "Zakariya",
    "Yahya", "Isa", "Muhammad", "Abu Bakr", "Umar", "Usman", "Ali", "Talha", "Zubair", "Abdur Rahman",
    "Saad", "Saeed", "Abu Huraira", "Bilal", "Khabbab", "Ammar", "Miqdad", "Salman", "Suhail", "Zaid",
    "Usama", "Abbas", "Hamza", "Khalid", "Amr", "Abu Talib", "Abu Sufyan", "Hind", "Aisha", "Hafsa",
    "Zainab", "Safiyya", "Umm Salama", "Fatima", "Ruqayyah", "Umm Kulthum", "Asma", "Sumayyah",

    # 4. Islami Jungen aur Ghazawat (50+)
    "Badr", "Uhud", "Khandaq", "Khaybar", "Hunain", "Tabuk", "Muta", "Yarmouk", "Qadisiyya", "Siffin",
    "Nahrawan", "Karbala", "Jamal", "Harrah", "Plassey", "Panipat", "Hattin", "Ain Jalut", "Manzikert",
    "Talas", "Tours", "Vienna", "Guadalete", "Constantinople", "Andalusia", "Ghazwa-e-Hind", "Tabuk",
    "Trench", "Yamama", "Ridda", "Nahrawan", "Siffeen", "Camel", "Siffin", "Karbala", "Harrah",

    # 5. Mukaddas Jagah (100+)
    "Kaaba", "Masjid-e-Nabwi", "Baitul Maqdis", "Masjid-e-Aqsa", "Jannatul Baqi", "Jannatul Mualla",
    "Jabal-e-Noor", "Jabal-e-Rahmat", "Mina", "Muzdalifah", "Arafat", "Safa-Marwa", "Zamzam", "Hira",
    "Thawr", "Badr", "Uhud", "Quba", "Najaf", "Karbala", "Kufa", "Samarra", "Qom", "Medina", "Taif",
    "Jeddah", "Hebron", "Ghaza", "Damascus", "Baghdad", "Cairo", "Istanbul", "Cordoba", "Timbuktu",
    "Al-Azhar", "Alhambra", "Fatehpur Sikri", "Ajmer", "Delhi", "Lahore", "Multan", "Makkah", "Madinah",

    # 6. Islami Aqeeda aur Amal (200+)
    "Tawheed", "Shirk", "Risalat", "Akhirah", "Malaika", "Qadar", "Quran", "Sunnah", "Hadith", "Fiqh",
    "Ijmah", "Qiyas", "Ijtihad", "Zakat", "Salah", "Sawm", "Hajj", "Umrah", "Tahajjud", "Tasbih",
    "Tahmeed", "Takbir", "Tahlil", "Shahada", "Wudu", "Ghusl", "Tayammum", "Adhan", "Iqamah", "Jumuah",
    "Eid", "Qurbani", "Aqiqah", "Nikah", "Talaq", "Khula", "Hijab", "Niqab", "Burqa", "Halal", "Haram",
    "Makruh", "Mustahab", "Mubah", "Fard", "Wajib", "Sunnat", "Nafl", "Bidah", "Taqwa", "Ikhlas",
    "Sabr", "Shukr", "Tawakkul", "Zuhd", "Qanaat", "Tawbah", "Istighfar", "Dua", "Zikr", "Sadaqah",
    "Waqf", "Jihad", "Dawah", "Ummah", "Khilafah", "Shura", "Bayah", "Fatwa", "Mufti", "Qazi",

    # 7. Islami Tareekhi Shakhsiyat (150+)
    "Imam Abu Hanifa", "Imam Malik", "Imam Shafi", "Imam Ahmad", "Ibn Taymiyyah", "Al-Ghazali",
    "Ibn Sina", "Al-Farabi", "Al-Khwarizmi", "Ibn Khaldun", "Saladin", "Tipu Sultan", "Akbar",
    "Aurangzeb", "Muhammad Bin Qasim", "Mahmud Ghaznavi", "Al-Biruni", "Ibn Battuta", "Rumi",
    "Al-Hallaj", "Rabia Basri", "Nizamuddin Auliya", "Moinuddin Chishti", "Baha-ud-din Zakariya",
    "Shah Waliullah", "Sir Syed", "Iqbal", "Maulana Azad", "Hasan al-Banna", "Sayyid Qutb",
    "Osama Bin Laden", "Malcolm X", "Muhammad Ali", "Zia-ul-Haq", "Erdogan", "Zayed", "Faisal",

    # 8. Islami Festivals aur Dates
    "Eid-ul-Fitr", "Eid-ul-Adha", "Muharram", "Ashura", "Shab-e-Barat", "Laylatul Qadr",
    "Shab-e-Miraj", "Shab-e-Qadr", "Ramadan", "Dhul Hijjah", "Rajab", "Jumada al-Awwal",
    "Safar", "Rabi ul-Awwal", "12 Rabi ul-Awwal", "27 Rajab", "15 Shaban", "10 Muharram",

    # 9. Islami Science aur Kala
    "Algebra", "Algorithm", "Alchemy", "Astrolabe", "Quadrant", "Camera Obscura", "Surgery",
    "Pharmacology", "Optics", "Trigonometry", "Avicenna", "Averroes", "Al-Zahrawi", "Al-Kindi",
    "Al-Razi", "Ibn al-Haytham", "Al-Jazari", "Al-Khwarizmi", "Al-Battani", "Al-Idrisi",

]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return jsonify(word=random.choice(islamic_words).capitalize())

if __name__ == '__main__':
    app.run(debug=True)
