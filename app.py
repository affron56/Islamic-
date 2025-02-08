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

    
    # Asma ul-Husna (Allah ke 99 Naam)
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

    # Quran ki Surahon ke Naam (114 Surahs)
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

    # Paigambar aur Sahaba ke Naam (150+)
    "Adam", "Nuh", "Idris", "Hud", "Salih", "Ibrahim", "Lut", "Ismail", "Ishaq", "Yaqub", "Yusuf",
    "Ayyub", "Shuayb", "Musa", "Harun", "Dawud", "Sulaiman", "Ilyas", "Al-Yasa", "Yunus", "Zakariya",
    "Yahya", "Isa", "Muhammad", "Abu Bakr", "Umar", "Usman", "Ali", "Talha", "Zubair", "Abdur Rahman",
    "Saad", "Saeed", "Abu Huraira", "Bilal", "Khabbab", "Ammar", "Miqdad", "Salman", "Suhail", "Zaid",
    "Usama", "Abbas", "Hamza", "Khalid", "Amr", "Abu Talib", "Abu Sufyan", "Hind", "Aisha", "Hafsa",
    "Zainab", "Safiyya", "Umm Salama", "Fatima", "Ruqayyah", "Umm Kulthum", "Asma", "Sumayyah",

    # Islami Jungen aur Ghazawat (50+)
    "Badr", "Uhud", "Khandaq", "Khaybar", "Hunain", "Tabuk", "Muta", "Yarmouk", "Qadisiyya", "Siffin",
    "Nahrawan", "Karbala", "Jamal", "Harrah", "Plassey", "Panipat", "Hattin", "Ain Jalut", "Manzikert",
    "Talas", "Tours", "Vienna", "Guadalete", "Constantinople", "Andalusia", "Ghazwa-e-Hind", "Tabuk",
    "Trench", "Yamama", "Ridda", "Nahrawan", "Siffeen", "Camel", "Siffin", "Karbala", "Harrah",

    # Mukaddas Jagah (100+)
    "Kaaba", "Masjid-e-Nabwi", "Baitul Maqdis", "Masjid-e-Aqsa", "Jannatul Baqi", "Jannatul Mualla",
    "Jabal-e-Noor", "Jabal-e-Rahmat", "Mina", "Muzdalifah", "Arafat", "Safa-Marwa", "Zamzam", "Hira",
    "Thawr", "Badr", "Uhud", "Quba", "Najaf", "Karbala", "Kufa", "Samarra", "Qom", "Medina", "Taif",
    "Jeddah", "Hebron", "Ghaza", "Damascus", "Baghdad", "Cairo", "Istanbul", "Cordoba", "Timbuktu",
    "Al-Azhar", "Alhambra", "Fatehpur Sikri", "Ajmer", "Delhi", "Lahore", "Multan", "Makkah", "Madinah",

    # Islami Aqeeda aur Amal (200+)
    "Tawheed", "Shirk", "Risalat", "Akhirah", "Malaika", "Qadar", "Quran", "Sunnah", "Hadith", "Fiqh",
    "Ijmah", "Qiyas", "Ijtihad", "Zakat", "Salah", "Sawm", "Hajj", "Umrah", "Tahajjud", "Tasbih",
    "Tahmeed", "Takbir", "Tahlil", "Shahada", "Wudu", "Ghusl", "Tayammum", "Adhan", "Iqamah", "Jumuah",
    "Eid", "Qurbani", "Aqiqah", "Nikah", "Talaq", "Khula", "Hijab", "Niqab", "Burqa", "Halal", "Haram",
    "Makruh", "Mustahab", "Mubah", "Fard", "Wajib", "Sunnat", "Nafl", "Bidah", "Taqwa", "Ikhlas",
    "Sabr", "Shukr", "Tawakkul", "Zuhd", "Qanaat", "Tawbah", "Istighfar", "Dua", "Zikr", "Sadaqah",
    "Waqf", "Jihad", "Dawah", "Ummah", "Khilafah", "Shura", "Bayah", "Fatwa", "Mufti", "Qazi",

    # Islami Tareekhi Shakhsiyat (150+)
    "Imam Abu Hanifa", "Imam Malik", "Imam Shafi", "Imam Ahmad", "Ibn Taymiyyah", "Al-Ghazali",
    "Ibn Sina", "Al-Farabi", "Al-Khwarizmi", "Ibn Khaldun", "Saladin", "Tipu Sultan", "Akbar",
    "Aurangzeb", "Muhammad Bin Qasim", "Mahmud Ghaznavi", "Al-Biruni", "Ibn Battuta", "Rumi",
    "Al-Hallaj", "Rabia Basri", "Nizamuddin Auliya", "Moinuddin Chishti", "Baha-ud-din Zakariya",
    "Shah Waliullah", "Sir Syed", "Iqbal", "Maulana Azad", "Hasan al-Banna", "Sayyid Qutb",
    "Osama Bin Laden", "Malcolm X", "Muhammad Ali", "Zia-ul-Haq", "Erdogan", "Zayed", "Faisal",

    # Islami Festivals aur Dates
    "Eid-ul-Fitr", "Eid-ul-Adha", "Muharram", "Ashura", "Shab-e-Barat", "Laylatul Qadr",
    "Shab-e-Miraj", "Shab-e-Qadr", "Ramadan", "Dhul Hijjah", "Rajab", "Jumada al-Awwal",
    "Safar", "Rabi ul-Awwal", "12 Rabi ul-Awwal", "27 Rajab", "15 Shaban", "10 Muharram",

    # Islami Science aur Kala
    "Algebra", "Algorithm", "Alchemy", "Astrolabe", "Quadrant", "Camera Obscura", "Surgery",
    "Pharmacology", "Optics", "Trigonometry", "Avicenna", "Averroes", "Al-Zahrawi", "Al-Kindi",
    "Al-Razi", "Ibn al-Haytham", "Al-Jazari", "Al-Khwarizmi", "Al-Battani", "Al-Idrisi",

    # Islamic Philosophical Terms
    "Falsafa", "Hikmah", "Haqqiqah", "Maqasid al-Shariah", "Ibtida", "Nusus al-Hikmah", "Ma'rifah", 
    "Tajassus al-Haqiqah", "Tasawwuf", "Ishraq", "Mawrid al-Hikmah", "Ruhaniyat", "Wujud", "Sirr", 
    "Takhayul", "Tasawwur", "Insan al-Kamil", "Aql", "Fitrah", "Kalam", "Mushahada", "Ijtihad al-Falsafa", 
    "Miftah al-Hikmah", "Suluk al-Ruh", "Nafs al-Ammarah", "Nafs al-Lawwama", "Nafs al-Mutma'inna", 
    "Jamal al-Tafakkur", "Sirr al-Asrar", "Qawl al-Haqq", "Miftah al-Aql", "Asrar al-Tawhid", "Usul al-Falsafa", 
    "Dawlat al-Hikmah", "Ilm al-Mantiq", "Riyazat al-Nafs", "Ihsan al-Fikr", "Miftah al-Haqq", "Bayan al-Ma'ani", 
    "Tafakkur al-Hayat", "Zawiyat al-Ilm", "Tadabbur", "Ulum al-Kalam", "Maqam al-Tasawwuf", "Suluk al-Qalb", 
    "Ihsan al-Ruh", "Falsafat al-Mutaqaddim", "Manhaj al-Hikmah", "Shajarah al-Ilm", "Silsilat al-Tafakkur",

    # Sufi Terminology
    "Ishq", "Yaqin", "Wajd", "Majzoob", "Mureed", "Murshid", "Dervish", "Fana", "Baqa", "Sohbet", "Qalandar", 
    "Zikr-e-Qalbi", "Khanqah", "Ruhani Safar", "Sama", "Maqam al-Ishq", "Nazar-e-Sufiyana", "Riyazat al-Ruh", 
    "Silsilat al-Wahdat", "Wahdat al-Wujud", "Mujahadat al-Ruh", "Isharat al-Tariqah", "Ruhaniyya", "Ishq-e-Haqiqi", 
    "Nizam al-Tariqah", "Tajalli", "Fana fi al-Hubb", "Baqa ba'd al-Fana", "Majlis al-Sufi", "Sama al-Ma'arif", 
    "Ruhani Irtiqa", "Maqam al-Sabr", "Ruhani Zauq", "Ishq al-Majazi", "Ishq al-Rububiyyah", "Zikr al-Mashreq", 
    "Silsilat al-Mahabba", "Nishan al-Tariqah", "Saqt al-Dil", "Ruhani Musahaba", "Irtifa al-Ruh", "Sarmaya al-Tajalli", 
    "Sirru al-Qalb", "Tariqat al-Fana", "Suluk al-Mahabba", "Jawhar al-Ruh", "Shuhud", "Hunar al-Zikr", "Fayz al-Sufi", "Nawa al-Tariqah",

    # Islamic Inventions and Scholars in Science
    "Ibn al-Nafis", "Ibn al-Baitar", "Ibn Zuhr", "Al-Khazini", "Qutb al-Din al-Shirazi", "Ibn al-Razzaz al-Jurjani", "Ibn al-Wardi", 
    "Ibn Fadlan", "Ibn Hibban", "Al-Suli", "Al-Birjandi", "Al-Kashi", "Ibn al-Shatir", "Al-Mas'udi", "Ibn Hazm", "Ibn Qutaybah", 
    "Al-Kharaqani", "Al-Tabari", "Ibn Kathir", "Al-Baghawi", "Ibn al-Jawzi", "Ibn Hajar al-Asqalani", "Ibn al-Subki", "Ibn al-Salah", 
    "Al-Majriti", "Al-Farghani", "Ibn Sab'in", "Ibn Bassam", "Al-Dimashqi", "Nasir al-Din al-Tusi", "Ibn al-Nadim", "Al-Qazwini", 
    "Ibn al-Rumaythah", "Ibn al-Humam", "Al-Safadi", "Ibn Abi Usaybi'a", "Ibn al-Quff", "Ibn Makula", "Al-Baghdadi", "Ibn al-Rashid", 
    "Ibn Abi Zar", "Al-Nasawi", "Ibn al-Tib", "Ibn al-Jurayj", "Ibn al-Adim", "Al-Muqaddasi", "Ibn al-Wazir", "Ibn al-Nu'man",

    # Islamic Architectural Landmarks
    "Dome of the Rock", "Blue Mosque", "Suleymaniye Mosque", "Al-Qarawiyyin Mosque", "Nasir al-Mulk Mosque", "Shalimar Gardens", 
    "Faisal Mosque", "Golestan Palace", "Topkapi Palace", "Red Fort", "Humayun's Tomb", "Shalimar Bagh", "Badshahi Mosque", 
    "Jama Masjid of Agra", "Mehmed Paša Sokolović Bridge", "Rumi's Mausoleum", "Alaeddin Mosque", "Ulu Camii", "Sultan Qaboos Grand Mosque", 
    "Sheikh Zayed Grand Mosque", "Baiturrahman Grand Mosque", "Masjid Raya Bandung", "Great Mosque of Xi'an", "Sultan Mosque (Singapore)", 
    "Masjid Sultan (Singapore)", "Istiqlal Mosque", "Moti Masjid", "Jama Mosque of Herat", "Registan Square", "Gur-e-Amir", "Bibi-Khanym Mosque", 
    "Masjid Jameh of Isfahan", "Vakil Mosque", "Shah Cheragh", "Masjid al-Taqwa", "Masjid Qiblatain", "Hassan II Mosque", "Koutoubia Mosque", 
    "Great Mosque of Kairouan", "Great Mosque of Sousse", "Qasr al-Hayr al-Sharqi", "Saladin Citadel", "Citadel of Aleppo", "Madrasa of Sultan Hassan", 
    "Medina Fort", "Minaret of Jam", "Qusayr Amra", "Ribat of Monastir", "Qal'at al-Bahrain", "Citadel of Qaitbay",

    # Islamic Poetic and Literary Terms
    "Ghazal", "Qasida", "Mathnawi", "Saj'", "Muwashshah", "Zajal", "Rubaiyat", "Naat", "Manqabat", "Marsiya", "Takhmis", "Diwan", "Safar Nama", 
    "Siyar", "Qisas", "Sirat", "Tazkira", "Khamsa", "Rasa'il", "Mukhtasar", "Tarjuma", "Maqama", "Silsila", "Bait", "Misra", "Qafiyah", "Wazn", 
    "Bahr", "Radeef", "Tawil", "Takhmis-e-Qasidah", "Hikam", "Sufi Kalam", "Ishq Nama", "Divan-e-Rumi", "Nazm", "Sukhan", "Mushaira", "Adab", 
    "Murakkab", "Qissah", "Dastan", "Ruba'i", "Maqsud", "Ishaarat", "Manzum", "Ghazalnama", "Sarguzasht", "Kissa", "Shairana",

    # Islamic Historical Regions and Cities
    "Fes", "Marrakesh", "Rabat", "Agadir", "Tunis", "Kairouan", "Sousse", "Tripoli", "Seville", "Toledo", "Fustat", "Hijaz", "Tihamah", 
    "Najd", "Asir", "Baluchistan", "Sindh", "Punjab", "Transoxiana", "Khwarezm", "Fergana", "Merv", "Bukhara", "Samarkand", "Herat", "Balkh", 
    "Kandahar", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Baku", "Ankara", "Izmir", "Antalya", "Agra", "Lucknow", "Hyderabad", "Bhopal", 
    "Aurangabad", "Riyadh", "Dammam", "Doha", "Manama", "Muscat", "Kuwait City", "Amman", "Ramallah",

    # Modern Islamic Thinkers and Leaders
    "Tariq Ramadan", "Hamza Yusuf", "Yasir Qadhi", "Omar Suleiman", "Shabir Ally", "Amina Wadud", "Dalia Mogahed", "Imran N. Hosein", 
    "Tariq Jameel", "Nouman Ali Khan", "Zakir Naik", "Irshad Manji", "Reza Aslan", "Ayaan Hirsi Ali", "Abdulaziz Sachedina", 
    "Seyyed Hossein Nasr", "Fazlur Rahman", "Ali Gomaa", "Ahmed Deedat", "Bilal Philips", "Yvonne Ridley", "Naser Makarem Shirazi", 
    "Ali al-Qaradaghi", "Mohammed Arkoun", "Abdul Hakim Murad", "Khaled Abou El Fadl", "Zainab Salbi", "Aref Ali Nayed", "Nabeel Qureshi", 
    "Ebrahim Kalin", "Amr Khaled", "Tariq Anwar", "Mahmoud Abbas", "Rashid al-Ghannushi", "Mustafa Akyol", "M. Fethullah Gülen", "Süleyman Ateş", 
    "Tawfiq al-Hakim", "Radwan Ziadeh", "Sami Yusuf", "Mahmoud Darwish", "Ibrahim Ozdemir", "Jamal al-Banna", "Kamal al-Fadl", "Rachid Ghannouchi", 
    "Hafiz Omer", "Sultan Al Qassemi", "Abdullah bin Bayyah", "Imran Khan", "Tawakkol Karman",

    # Additional Islamic Concepts and Rituals
    "Sadaqah Jariyah", "I'tikaf", "Sunnah Rawatib", "Janazah", "Dua al-Qunoot", "Halaqah", "Mawlid", "Tadabbur al-Quran", "Hikmah al-Quran", 
    "Tafsir", "Tajweed", "Qira'at", "Sajdah Tilawat", "Niyyah", "Jalsah", "Zikr-e-Sabah", "Zikr-e-Masaa", "Qunut Nazilah", "Sadaqat al-Fitr", 
    "Umrah al-Qiran", "Hajj Tamattu", "Hajj Ifrad", "Hajj Qiran", "Rukn", "Arkan al-Islam", "Arkan al-Iman", "Mas'uliyyat", "Shahadatayn", 
    "Fidya", "Kaffarah", "Hiba", "Fadl", "Barakah", "Tawassul", "Mizan al-Akhlaq", "Sabil", "Sirat al-Mustaqim", "Du'a al-Hajat", "Du'a al-Istikhara", 
    "Du'a al-Mashlaha", "Du'a al-Shifa", "Du'a al-Karim", "Du'a al-Tawbah", "Du'a al-Jama'ah", "Qiyam al-Duha", "Duha", "Istiqama", "Tawbah al-Qalbiya", 
    "Ibadat al-Mutlaq", "Du'a al-Rizq",

    # Islamic Cultural Terms
    "Islamic Calligraphy", "Tazhib", "Zellij", "Arabesque", "Geometric Pattern", "Muqarnas", "Kufic Calligraphy", "Thuluth Script", "Naskh Script", 
    "Diwani Script", "Tughra", "Nasheed", "Zardozi Embroidery", "Henna Art", "Islamic Geometric Art", "Falconry", "Camel Racing", "Majlis", "Bazaar", 
    "Carpet Weaving", "Tilework", "Ceramic Art", "Mughal Miniature", "Islamic Fashion", "Hijab Fashion", "Thobe", "Abaya", "Kandura", "Sufi Music", 
    "Dervish Dance", "Qasida Recitation", "Sama Ceremony", "Ikat Weaving", "Mosaic Tiling", "Ornamental Ironwork", "Wood Carving", "Islamic Garden", 
    "Waqf Architecture", "Khanqah Architecture", "Ramadan Iftar", "Suhur Tradition", "Henna Night", "Iftar Gathering", "Islamic Calligraphic Poetry", 
    "Oud Music", "Dabke Dance", "Islamic Tile Mural", "Frescoes of Islamic Heritage", "Mamluk Ornamentation", "Ottoman Textile",

    # Islamic Mystical Experiences and Terms
    "Wahdat al-Sifat", "Fana Fi Allah", "Ishq-e-Rasool", "Qurbani al-Ruhani", "Lata'if-e-Sitta", "Sohbet-e-Sufi", "Muraqaba", "Kashf", "Hal", 
    "Maqam al-Mahabba", "Maqam al-Tawakkul", "Sukoon al-Ruh", "Fazl-e-Ilahi", "Shuhud al-Haqiqi", "Isharat al-Ruhani", "Sama' al-Qalb", 
    "Tasawwuf-e-Khas", "Ruhani Safar-e-Tamheed", "Nisbat", "Zuhd al-Dunya", "Khudi", "Nooraniyyat", "Tajalli al-Haqq", "Sirr-e-Wujud", "Zikr al-Tawhid", 
    "Sama al-Awliya", "Mushahadat-e-Ilahi", "Ruhani Tajdid", "Lata'if-e-Rahmah", "Nafs al-Radiyah", "Suluk al-Tazkiyah", "Qalb-e-Munir", "Ruhani Urooj", 
    "Ishq-e-Khuda", "Ruhani Shukr", "Ibtida-e-Ruhani", "Wujub", "Tawajjud al-Qalb", "Isharat al-Asrar", "Qalb-e-Dilbar", "Zauq-e-Hayat", "Wajd al-Ishq", 
    "Mushkilaat al-Nafs", "Ibtida-e-Tasawwuf", "Ruhani Safar-e-Ishq", "Suhbat-e-Wahdat", "Tajalli al-Ruh", "Sirr al-Mahd", "Ruhani Iltija", "Sama al-Ilahi"


]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return jsonify(word=random.choice(islamic_words).capitalize())

if __name__ == '__main__':
    app.run(debug=True)
