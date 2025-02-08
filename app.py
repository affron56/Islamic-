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

    # Islami Science aur Kalaa
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
    "Mushkilaat al-Nafs", "Ibtida-e-Tasawwuf", "Ruhani Safar-e-Ishq", "Suhbat-e-Wahdat", "Tajalli al-Ruh", "Sirr al-Mahd", "Ruhani Iltija", "Sama al-Ilahi",


    # Additional Sufi Saints and Mystics (50 items)
    "Junaid Baghdadi", "Abdul Qadir Jilani", "Shah Nematullah", "Pir Meher Ali Shah", "Khwaja Qutbuddin Bakhtiar Kaki",
    "Shah Inayat Qadiri", "Sayyid Ali Hamadani", "Makhdoom Ali Mahimi", "Pir Pagara", "Sultan-ul-Arifeen",
    "Khwaja Kamal-ud-Din", "Pir Shahabuddin", "Haji Abdul Wahab", "Pir Roshan", "Baba Qaim Sain",
    "Sultan Muhammad Qureshi", "Pir Khushal", "Sayed Ahmad Razavi", "Khwaja Arif Qadri", "Pir Noor Muhammad",
    "Pir Mast Ali Shah", "Pir Shams-ud-Din", "Khwaja Habib-ur-Rahman", "Sayed Ibrahim", "Pir Fazal Ali",
    "Lal Shahbaz Qalandar", "Pir Sultan", "Shams Tabrizi", "Shah Abdul Latif Bhittai", "Pir Muhammad Chishti",
    "Khwaja Shamsuddin", "Pir Ali Tirmizi", "Pir Aslam", "Sayed Jamaluddin", "Khwaja Nizamuddin Hussain",
    "Pir Rahimuddin", "Sultan Rukn-ud-Din", "Hazrat Shah Kamal", "Pir Abdullah", "Mawlana Shamsuddin",
    "Pir Fazl-e-Haq", "Khwaja Abdul Hamid", "Pir Hamid Raza", "Sayed Rafiuddin", "Pir Yusuf",
    "Khwaja Abdullah Shah", "Pir Abdul Salam",

    # Famous Islamic Literary Works and Manuscripts (50 items)
    "Al-Muwatta", "Sahih al-Bukhari", "Sahih Muslim", "Al-Muwafaqat", "Ihya Ulum al-Din",
    "Futuh al-Ghaib", "Al-Risala", "Tafsir al-Jalalayn", "Tafsir Ibn Kathir", "Al-Kitab al-Muqaddas",
    "Al-Aqidah al-Tahawiyyah", "Rasa'il Ikhwan al-Safa", "Fusus al-Hikam", "Madarik al-Tanzil", "Mu'jam al-Buldan",
    "Al-Muqaddimah", "Sirat Rasul Allah", "Al-Risala al-Qushayriyya", "Tabaqat al-Umam", "Al-Fihrist",
    "The Meadows of Gold", "Tarikh al-Tabari", "Al-Kamil fi al-Tarikh", "Risala Qushayriyya", "Majma' al-Fawaid",
    "Nukat al-I'tiqad", "Muntakhab al-Tafsir", "Dala'il al-Nubuwwah", "Ibn Hazm's Tauq al-Imaan", "Tabaqat al-Mutazawwijin",
    "Riyad-us-Saliheen", "Bulugh al-Maram", "Fath al-Bari", "Zad al-Ma'ad", "Al-Tamhid",
    "Al-Hikam", "Ihya al-Suluk", "Mishkat al-Masabih", "Al-Adab al-Mufrad", "Al-Muwashshahat",
    "Diwan-e-Meer", "Gulistan", "Bostan", "Masnavi-i Ma'navi", "Divan-e-Hafez",
    "Shahnameh", "Siyar A'lam al-Nubala", "Al-Kashf al-Asrar", "Tuhfat al-Ahrar", "Firdaws al-Tahawwul",

    # Islamic Architectural Structures and Complexes (Additional) (50 items)
    "Sheikh Lotfollah Mosque", "Shah Mosque", "Gonbad-e Qabus", "Tomb of Shah Rukn-e-Alam", "Mausoleum of Khoja Ahmed Yasavi",
    "Ghazni Minarets", "Jameh Mosque of Yazd", "Masjid al-Jami' of Qazvin", "Rohtas Fort", "Alamgiri Fort",
    "Tughlaqabad Fort", "Golkonda Fort", "Agra Fort", "Masjid-e-Sultani, Qazvin", "Al-Aqmar Mosque",
    "Mustansiriya Madrasa", "Sultan al-Rashid Mosque", "Khanqah-e-Mir", "Ribat of Tarim", "Qasr al-Banat",
    "Timurid Madrasa of Herat", "Ulugh Beg Madrasa", "Tomb of Ahmed Sanjar", "Imam Reza Shrine", "Ganj Ali Khan Complex",
    "Nishat Bagh", "Chashme Shahi", "Tomb of Jahangir", "Tomb of Akbar", "Tomb of Sultan Qutb al-Din",
    "Herat Minaret", "Sufi Khanqah of Multan", "Qila Mubarak", "Chandni Chowk Mosque", "Jamia Mosque of Sialkot",
    "Haji Ali Dargah", "Ranikot Fort", "Alamgir Mosque", "Khanate Palace of Bukhara", "Bibi Sahib Kothi",
    "Mughal Sarai", "Tomb of Mirza Ghalib", "Sultan Pur Majar", "Jahanara Bagh", "Bibi Ka Maqbara",
    "Mausoleum of Shah Waliullah", "Sultan Mahmud Mosque", "Rumi Cultural Center", "Minaret of Qibla", "Saffron Courtyard",

    # Islamic Science and Technology Contributions (Additional) (50 items)
    "Book of Optics", "Surgical Instruments Design", "Chemistry Distillation Techniques", "Astronomical Observatories", "Water Clock Innovations",
    "Astrolabe Construction", "Quadrant Development", "Arabic Numerals Transmission", "Herbal Medicine Catalogs", "Pharmacology Advances",
    "Al-Razi’s Medical Texts", "Ibn Sina’s Canon of Medicine", "Geographical Mapping Techniques", "Cartographic Projections", "Ibn Battuta’s Travel Records",
    "Navigation Instruments", "Mechanical Automata", "Windmill Designs", "Soap Making Process", "Crankshaft Invention",
    "Astrological Tables", "Arabic Algebra", "Chemistry Laboratory Methods", "Advanced Irrigation Systems", "Water-Powered Mills",
    "Medical Surgical Tools", "Philosophy of Medicine", "Medical Ethics in Islam", "Optical Lenses Development", "Scientific Method in Islamic Thought",
    "Geometric Theorems", "Trigonometric Identities", "Astronomical Instruments", "Al-Kindi’s Cryptanalysis", "Early Cryptography Techniques",
    "Animal Dissection Studies", "Plant Classification", "Astrogeology Concepts", "Mechanical Engineering Concepts", "Chemical Distillation Apparatus",
    "Surgical Anesthesia Techniques", "Metallurgy Advancements", "Mathematical Proofs", "Algorithm Development", "Early Calculus Concepts",
    "Optical Camera Obscura", "Solar Calendar Calculations", "Timekeeping Devices", "Hydraulic Engineering", "Architectural Geometry",

    # Islamic Philosophical and Theological Concepts (Additional) (50 items)
    "Haqiqat al-Wujud", "Sunnat al-Matin", "Insaniyyat al-Ilahi", "Fitra al-Rabbaniyya", "Mawrid al-Tanwir",
    "Silsilat al-Istibsar", "Majaz al-Haqq", "Mawqif al-Tadabbur", "Falsafat al-Kasf", "Ma'arifat al-Mawjood",
    "Ruhani Tajassus", "Isharat al-Haqiqa", "Sirat al-Falsafa", "Nubuwwat al-Batin", "Ilm al-Batin",
    "Majd al-Aql", "Sarab al-Ilm", "Noor al-Ma'ani", "Hikmat al-Muta'aliyah", "Haqq al-Iradah",
    "Asrar al-Mawjood", "Tafakkur al-Aql", "Insan al-Amin", "Falsafat al-Kawn", "Ma'rifat al-Asrar",
    "Ibtida' al-Ma'ani", "Tamhid al-Ruhani", "Tawajjuh al-Qalb", "Ishraq al-Aql", "Dawlat al-Ma'rifah",
    "Tafsir al-Ruh", "Qiyamat al-Fikr", "Wahdat al-Tanwir", "Riyad al-Falsafa", "Nubuwwat al-Qalb",
    "Haqq al-Irshad", "Ma'rifat al-Kawn", "Isharaat al-Tasawwuf", "Mizan al-Falsafa", "Sirr al-Ma'rifah",
    "Haqq al-Hikmah", "Noor al-Tadabbur", "Qalb al-Tajassus", "Miftah al-Nur", "Silsilat al-Tanwir",
    "Iradat al-Aql", "Tawhid al-Mawjood",

    # Islamic Jurisprudence and Legal Texts (Additional) (50 items)
    "Kitab al-Umm", "Al-Muhadhdhab", "Bidayat al-Mujtahid", "Al-Mabsut", "Al-Rawdah al-Bahiyyah",
    "Fath al-Qarib", "Al-Tanbih fi al-Fiqh", "Mukhtasar al-Quduri", "Al-Majmu'", "Nihayat al-Matlab",
    "Sharh al-Sunnah", "Al-Iqna' fi Usul al-Fiqh", "Al-Muhit al-Farid", "Tuhfa al-Wahhabiyya", "Fath al-Mu'in",
    "Al-Majd al-Fiqh", "Al-Muqaddimah fi al-Fiqh", "Radd al-Muhtar", "Al-Furuq", "Durr al-Mukhtar",
    "Al-Targhib wal-Tarhib", "Fath al-Rahman", "Mukhtasar al-Sharh", "Al-Islah fi al-Fiqh", "Tuhfat al-Fuqaha",
    "Al-Kafi fi al-Fiqh", "Minhaj al-Imam", "Al-Muhit al-Akbar", "Risalat al-Fiqh", "Al-Muntaqa fi al-Fiqh",
    "Sharh al-Aqa'id", "Bahr al-Majhud", "Miftah al-Fiqh", "Nihayat al-Fiqh", "Al-Mustasfa",
    "Furuq al-Adl", "Tanzih al-Qada", "Riyadh al-Haqq", "Umdat al-Fiqh", "Al-Majalis al-Fiqhiyya",
    "Mukhtasar al-Ashraf", "Silsilat al-Mubtada", "Al-Qawa'id al-Fiqhiyya", "Al-Lubab fi al-Fiqh", "Tajdid al-Fiqh",
    "Ijtihad al-Akbar", "Usul al-Fiqh al-Jadid", "Tajmi' al-Fiqh", "Mawsu'at al-Fiqh", "Al-Majma' al-Fiqhiyya",

    # Islamic Dynasties, Empires, and Rulers (Additional) (50 items)
    "Umayyad Caliphate", "Abbasid Caliphate", "Fatimid Caliphate", "Seljuk Empire", "Mamluk Sultanate",
    "Ottoman Empire", "Safavid Dynasty", "Mughal Empire", "Almohad Caliphate", "Almoravid Dynasty",
    "Ayyubid Dynasty", "Ghaznavid Empire", "Khazar Khaganate", "Timurid Empire", "Bahri Mamluks",
    "Burji Mamluks", "Sultanate of Rum", "Khanate of Bukhara", "Khanate of Khiva", "Sultanate of Delhi",
    "Marinid Dynasty", "Zengid Dynasty", "Zirid Dynasty", "Rustamid Kingdom", "Ibadi Imamate of Oman",
    "Samanid Empire", "Nasrid Kingdom of Granada", "Emirate of Córdoba", "Caliphate of Córdoba", "Ghuri Dynasty",
    "Khilji Dynasty", "Tughlaq Dynasty", "Sayyid Dynasty", "Lodi Dynasty", "Qutb Shahi Dynasty",
    "Asaf Jahi Dynasty", "Bengal Sultanate", "Deccan Sultanates", "Adil Shahi Dynasty", "Nizam Shahi Dynasty",
    "Barid Shahi Dynasty", "Bahmani Sultanate", "Rashidun Caliphate", "Umayyad Emirate of Córdoba", "Hafsid Dynasty",
    "Zayyanid Kingdom", "Saffarid Dynasty", "Idrisid Dynasty", "Hammadid Dynasty", "Alaouite Dynasty",

    # Islamic Festivals, Celebrations, and Observances (Additional) (50 items)
    "Eid-e-Milad un-Nabi", "Eid-e-Siraj", "Eid-e-Zahra", "Jashn-e-Nowruz", "Eid-e-Fitr al-Saghir",
    "Mehfil-e-Sama", "Mela-e-Urdu", "Iftar Nights", "Ramadan Bazaar", "Night of Qadr Recitals",
    "Eid-e-Rukhsati", "Mawlid-ul-Nabi", "Shab-e-Suhar", "Eid-ul-Ghadeer", "Ziarat Day",
    "Imam Ali Day", "Eid-e-Imam Hussain", "Commemoration of Karbala", "Eid-ul-Burhan", "Night of Forgiveness",
    "Sufi Urs", "Jashn-e-Baharan", "Cultural Festival of Islam", "Ibadat Night", "Eid-e-Sajdah",
    "Noor-ul-Layl", "Eid-ul-Rahmat", "Jashn-e-Falah", "Eid-ul-Nur", "Mela-e-Muhabbat",
    "Eid-ul-Ma'soom", "Jashn-e-Tajalli", "Iftar Mela", "Ramadan Caravan", "Suhar Gathering",
    "Eid-ul-Falak", "Mawlid Recital Night", "Eid-ul-Farooq", "Eid-ul-Hakim", "Sufi Dance Festival",
    "Zikr Night", "Eid-ul-Ahsan", "Jashn-e-Wahdat", "Eid-e-Rasool", "Eid-ul-Quran",
    "Mela-e-Dua", "Eid-ul-Hubb",

    # Rashidun Caliphs (4 items)
    "Abu Bakr as-Siddiq", "Umar ibn al-Khattab", "Uthman ibn Affan", "Ali ibn Abi Talib",

    # Umayyad Caliphs (10 items)
    "Muawiyah I", "Yazid I", "Marwan I", "Abd al-Malik ibn Marwan", "Al-Walid I",
    "Sulayman ibn Abd al-Malik", "Umar II", "Yazid II", "Hisham ibn Abd al-Malik", "Abd al-Aziz ibn al-Walid",

    # Abbasid Caliphs (12 items)
    "Al-Saffah", "Al-Mansur", "Al-Mahdi", "Al-Hadi", "Harun al-Rashid", "Al-Amin",
    "Al-Ma'mun", "Al-Mu'tasim", "Al-Wathiq", "Al-Mutawakkil", "Al-Muqtadir", "Al-Radi",

    # Fatimid Caliphs/Imams (10 items)
    "Al-Mahdi Billah", "Al-Qa'im bi-Amr Allah", "Al-Mansur bi-Nasr Allah", "Al-Muizz li-Din Allah",
    "Al-Aziz Billah", "Al-Hakim bi-Amr Allah", "Ali az-Zahir", "Al-Mustansir Billah", "Al-Musta'li Billah", "Al-Amir bi-Ahkam Allah",

    # Seljuk Sultans (6 items)
    "Tughril Beg", "Alp Arslan", "Malik Shah I", "Sanjar", "Berkyaruq", "Barkiyaruq",

    # Mamluk Sultans (6 items)
    "Qalawun", "Baibars", "Al-Ashraf Khalil", "An-Nasir Muhammad", "Al-Zahir Baybars", "Al-Nasir Muhammad ibn Qalawun",

    # Ottoman Sultans (15 items)
    "Osman I", "Orhan", "Murad I", "Bayezid I", "Mehmed I", "Murad II",
    "Mehmed II", "Bayezid II", "Selim I", "Suleiman the Magnificent", "Selim II", "Murad III", "Mehmed III", "Ahmed I", "Mustafa I",

    # Mughal Emperors (8 items)
    "Babur", "Humayun", "Akbar", "Jahangir", "Shah Jahan", "Aurangzeb Alamgir", "Bahadur Shah I", "Bahadur Shah II",

    # Other Notable Islamic Rulers (8 items)
    "Timur", "Sher Shah Suri", "Mahmud of Ghazni", "Alauddin Khilji", "Muhammad bin Tughluq", "Tipu Sultan", "Afzal Khal", "Tamur-E-Lank",


    # Islamic Historical Battles and Military Campaigns (50 items)
    "Jung-e-Qadisiyyah", "Jung-e-Yarmouk", "Jung-e-Badr", "Jung-e-Uhud", "Jung-e-Trench",
    "Jung-e-Khyber", "Jung-e-Hunayn", "Jung-e-Tabuk", "Jung-e-Mutah", "Jung-e-Jalula",
    "Jung-e-Nahrawan", "Jung-e-Siffin", "Jung-e-Jalalabad", "Jung-e-Khaybar", "Jung-e-Qadis",
    "Jung-e-Hira", "Jung-e-Karbala", "Jung-e-Jamal", "Jung-e-Harrah", "Jung-e-Siffin-II",
    "Jung-e-Mansura", "Jung-e-Zab", "Jung-e-Firaz", "Jung-e-Maysalun", "Jung-e-Al-Qadisiyyah",
    "Jung-e-Harra", "Jung-e-Nahr", "Jung-e-Ayn-Jalut", "Jung-e-Al-Jumhuriya", "Jung-e-Maysan",
    "Jung-e-Fahl", "Jung-e-Al-Rustamiyah", "Jung-e-Dhi-Qar", "Jung-e-Jalil", "Jung-e-Marj-al-Saffar",
    "Jung-e-Zama", "Jung-e-Al-Bukayr", "Jung-e-Saqifah", "Jung-e-Dhul-Hijjah", "Jung-e-Anbar",
    "Jung-e-Barda'in", "Jung-e-Az-Zubayr", "Jung-e-Mu'tah", "Jung-e-Khandaq", "Jung-e-Jund-al-Aqsa",
    "Jung-e-Dhul-Aswad", "Jung-e-Al-Raqqah", "Jung-e-Samarra", "Jung-e-Tikrit", "Jung-e-Basra",

    # Islamic Poets and Literary Figures (50 items)
    "Rumi", "Hafez", "Saadi", "Attar", "Khwaja-Ghulam-Farid", "Bulleh-Shah", "Wali-Dakhani", "Fazal-Shah-Sayyad",
    "Jalaluddin-Rumi", "Mian-Muhammad-Bakhsh", "Mir-Taqi-Mir", "Ghalib", "Meerabai", "Wali-Muhammad-Wali",
    "Mirza-Ghalib", "Bahadur-Shah-Zafar", "Sultan-Bahu", "Shah-Abdul-Latif-Bhittai", "Ustad-Daman", "Mansur-Hallaj",
    "Khwaja-Mir-Dard", "Sarmad-Kashani", "Shah-Inayat-Qadiri", "Qatran-Tabrizi", "Nizami-Ganjavi", "Fuzuli",
    "Jami", "Nasir-Khusraw", "Rumi-Saheb", "Seyrani", "Sarmad", "Ibn-Arabi", "Rashid-ad-Din",
    "Al-Ma'arri", "Ibn-Zamrak", "Ibn-al-Farid", "Ibn-Quzman", "Abdul-Rahim-Khan-e-Khana", "Mir-Anis",
    "Mirza-Khan-Daagh-Dehlvi", "Altaf-Hussain-Hali", "Sahir-Ludhianvi", "Faiz-Ahmed-Faiz", "Habib-Jalib",
    "Ahmad-Faraz", "Parveen-Shakir", "Meeraji", "Javed-Akhtar", "Kaifi-Azmi", "Khalil-Gibran",

    # Islamic Scientific Instruments and Innovations (50 items)
    "Astrolabe", "Armillary-Sphere", "Sundial", "Water-Clock", "Quadrant", "Sextant", "Celestial-Globe", "Hourglass",
    "Dioptra", "Alidade", "Abacus", "Arabic-Numerals", "Algebraic-Table", "Geometric-Compasses", "Surgical-Instruments",
    "Herbal-Catalog", "Al-Razi’s-Distillation", "Ibn-Sina’s-Pharmacopoeia", "Astronomical-Tables", "Observatory-Instruments",
    "Trigonometric-Calculators", "Planetary-Models", "Mathematical-Instruments", "Optical-Lenses", "Camera-Obscura",
    "Pendulum-Clock", "Mechanical-Calculator", "Windmill-Model", "Irrigation-Gear", "Waterwheel-Mechanism",
    "Hydraulic-Organ", "Mechanical-Automata", "Coin-Press", "Paper-Making-Technique", "Glass-Blowing-Tools",
    "Ceramic-Kiln", "Mosaic-Tiler", "Carpet-Weaving-Loom", "Silk-Spinning-Wheel", "Compass", "Magnetic-Needle",
    "Sun-Chart", "Star-Atlas", "Celestial-Sphere", "Parabolic-Mirror", "Optical-Prism", "Reflecting-Telescope",
    "Geodesic-Dome", "Epicyclic-Gear", "Water-Powered-Lifting",

    # Notable Islamic Cities and Regions (Historical and Modern) (50 items)
    "Baghdad", "Cairo", "Cordoba", "Kairouan", "Fez", "Samarkand", "Bukhara", "Isfahan", "Konya", "Damascus",
    "Istanbul", "Medina", "Makkah", "Jerusalem", "Basra", "Samarra", "Aleppo", "Tunis", "Rabat", "Fes",
    "Alexandria", "Tripoli", "Najaf", "Kufa", "Sana'a", "Marib", "Kandahar", "Herat", "Multan", "Lahore",
    "Hyderabad", "Agra", "Delhi", "Amritsar", "Faisalabad", "Karachi", "Quetta", "Peshawar", "Sialkot", "Rawalpindi",
    "Lucknow", "Jaipur", "Abu-Dhabi", "Doha", "Muscat", "Kuwait-City", "Manama", "Riyadh", "Dubai", "Sharjah",

    # Islamic Economic Terms and Institutions (50 items)
    "Zakat", "Sadaqah", "Waqf", "Bayt-al-Mal", "Mudarabah", "Musharakah", "Murabaha", "Ijara", "Salam", "Istisna",
    "Hawala", "Qirad", "Takaful", "Islamic-Banking", "Shariah-Compliance", "Halal-Certification", "Sukuk", "Ijarah",
    "Ar-Riba", "Bai'-al-Inah", "Islamic-Finance", "Islamic-Insurance", "Islamic-Microfinance", "Profit-Sharing",
    "Risk-Sharing", "Interest-Free-Loans", "Islamic-Investment", "Qard-Hasan", "Islamic-Economic-Model", "Ethical-Investment",
    "Islamic-Capital-Market", "Financial-Inclusion", "Islamic-Wealth-Management", "Islamic-Financial-Instruments",
    "Islamic-Brokerage", "Sukuk-Bonds", "Islamic-Venture-Capital", "Islamic-Mutual-Funds", "Islamic-Derivatives",
    "Islamic-Credit", "Charitable-Endowment", "Religious-Taxation", "Islamic-Trade", "Islamic-Commerce", "Halal-Market",
    "Islamic-Economic-Justice", "Islamic-Social-Finance", "Islamic-Accounting", "Islamic-Financial-Regulation",
    "Islamic-Investment-Funds",

    # Islamic Educational Institutions and Madrassas (50 items)
    "Al-Qarawiyyin-University", "Al-Azhar-University", "Nizamiyya-Madrasa", "Madrasa-of-Ibn-Sina", "Madrasa-of-Al-Ghazali",
    "Madrasa-of-Al-Farabi", "Sufism-Madrasa", "Madrasa-of-Baghdad", "Madrasa-of-Damascus", "Madrasa-of-Samarkand",
    "Madrasa-of-Cairo", "Madrasa-of-Cordoba", "Madrasa-of-Isfahan", "Madrasa-of-Konya", "Madrasa-of-Herat",
    "Madrasa-of-Bukhara", "Madrasa-of-Fes", "Madrasa-of-Marrakesh", "Madrasa-of-Tunis", "Madrasa-of-Aleppo",
    "Madrasa-of-Nishapur", "Madrasa-of-Shiraz", "Madrasa-of-Balkh", "Madrasa-of-Sistan", "Madrasa-of-Khwarezm",
    "Madrasa-of-Khorasan", "Madrasa-of-Tabriz", "Madrasa-of-Hamadan", "Madrasa-of-Yazd", "Madrasa-of-Maragheh",
    "Madrasa-of-Ray", "Madrasa-of-Sari", "Madrasa-of-Isfahan-II", "Madrasa-of-Qazvin", "Madrasa-of-Tabriz-II",
    "Madrasa-of-Shiraz-II", "Madrasa-of-Kerman", "Madrasa-of-Zahedan", "Madrasa-of-Bandar-Abbas", "Madrasa-of-Basra",
    "Madrasa-of-Najaf", "Madrasa-of-Kufa", "Madrasa-of-Medina", "Madrasa-of-Makkah", "Madrasa-of-Jerusalem",
    "Madrasa-of-Alexandria", "Madrasa-of-Istanbul", "Madrasa-of-Bursa", "Madrasa-of-Bursa-II", "Madrasa-of-Amman",

    # Islamic Cultural Festivals and Celebrations (50 items)
    "Eid-ul-Fitr", "Eid-ul-Adha", "Ramadan-Iftar", "Laylat-al-Qadr", "Mawlid-al-Nabi", "Eid-e-Milad",
    "Sufi-Urs", "Islamic-New-Year", "Eid-e-Shab-e-Barat", "Ramadan-Nights", "Shab-e-Barat", "Ramadan-Mela",
    "Iftar-Bazaar", "Eid-Mela", "Eid-Fair", "Ramadan-Festival", "Quran-Recitation-Festival", "Islamic-Music-Festival",
    "Islamic-Art-Festival", "Sufi-Music-Festival", "Eid-Carnival", "Iftar-Celebration", "Ramadan-Cultural-Night",
    "Islamic-Heritage-Festival", "Eid-ul-Farooq", "Eid-e-Rukhsati", "Sufi-Dance-Festival", "Ramadan-Poetry-Night",
    "Islamic-Storytelling-Festival", "Islamic-Heritage-Day", "Iftar-Party", "Ramadan-Lantern-Festival", "Eid-e-Rasool",
    "Ramadan-Night-Market", "Islamic-Crafts-Fair", "Sufi-Whirling-Night", "Ramadan-Cultural-Fair", "Islamic-Film-Festival",
    "Islamic-Theatre-Night", "Ramadan-Art-Exhibition", "Eid-Expo", "Islamic-Cultural-Parade", "Ramadan-Book-Fair",
    "Iftar-Concert", "Islamic-Food-Festival", "Ramadan-Community-Day", "Eid-Celebration-Expo",

    # Islamic Religious Rituals and Practices (50 items)
    "Salah", "Sawm", "Hajj", "Umrah", "Wudu", "Ghusl", "Tayammum", "Dua", "Dhikr", "Tasbih", "Quran-Recitation",
    "Sunnah-Prayers", "Tarawih", "I'tikaf", "Sadaqah", "Zakat", "Khutbah", "Adhan", "Iqamah", "Niyyah",
    "Ruku", "Sujud", "Tashahhud", "Qiyam", "Jalsa", "Sahur", "Iftar", "Witr", "Tahajjud", "Jumu'ah",
    "Duha", "Mawlid-Observance", "Zamzam-Drinking", "Sa’i", "Raml", "Ritual-Cleansing", "Prayer-Beads",
    "Dhuhr", "Asr", "Maghrib", "Isha", "Qunut", "Janazah", "Sunnah-Fasting", "Aqiqah", "Nikah", "Talaq",
    "Hijab-Observance", "Khilafah-Oath", "Sadaqat-ul-Fitr",

    # Islamic Modern Movements and Organizations (50 items)
    "Muslim-Brotherhood", "Jamaat-e-Islami", "Tablighi-Jamaat", "Al-Islah-Movement", "Darul-Uloom-Movement",
    "Ahl-i-Hadith-Movement", "Tanzim-al-Jihad", "Global-Dawah-Network", "Muslim-Youth-League", "Islamic-Fiqh-Academy",
    "Islamic-Research-Foundation", "World-Assembly-of-Muslim-Youth", "International-Union-of-Muslim-Scholars", "Council-of-Islamic-Ideology", "Muslim-Public-Affairs-Council",
    "Islamic-Society-of-North-America", "European-Council-for-Fatwa-and-Research", "Islamic-Circle-of-North-America", "Muslim-World-League", "Islamic-Educational-Scientific-and-Cultural-Organization",
    "International-Islamic-Relief-Organization", "Islamic-Development-Bank", "Muslim-Aid", "Islamic-Relief-Worldwide", "Zakat-Foundation", "Muslim-Hands",
    "Islamic-Medical-Association", "Council-on-American-Islamic-Relations", "Islamic-Society-of-Britain", "Muslim-Association-of-Britain", "Muslim-Council-of-Britain", "Islamic-Forum-of-Europe", "Muslim-Welfare-Trust",
    "Islamic-Foundation", "Muslim-Charities-Forum", "Global-Islamic-Call-Society", "Islamic-Society-of-South-Africa", "Muslim-Outreach", "Muslim-Public-Affairs", "Islamic-Legal-Studies-Center", "Islamic-Studies-Association", "Muslim-Media-Watch", "Islamic-Unity-Conference",
    "Global-Muslim-Youth", "Modern-Muslim-Forum", "Islamic-Summit", "International-Muslim-Conference", "United-Muslim-Scholars", "Muslim-Council-of-Elders", "Progressive-Muslim-Network"


    # 1. Hinglish Sufi Saints aur Mystics ke Naam (50 items)
    "Junaid-e-Hind", "Abdul Qadir-e-Hind", "Fakir-e-Raah", "Rumi-e-Dil", "Shah-e-Suhail", 
    "Baba-e-Mohabbat", "Pir-e-Raaz", "Sultan-e-Sufi", "Haqiqi Saheb", "Fana-e-Dil", 
    "Ishq-e-Rooh", "Gul-e-Ishq", "Roohani Dost", "Sufi Saathi", "Qalandar-e-Khuda", 
    "Ruhani Saheb", "Mehboob-e-Raah", "Dilbar-e-Sufi", "Ishqwala Baba", "Rumi-e-Raah", 
    "Saif-e-Suhana", "Fana-e-Safar", "Sufi Nazaara", "Raaz-e-Mohabbat", "Dil-e-Suhana", 
    "Noor-e-Sufi", "Suhani Pir", "Qalander-e-Dil", "Ruh-e-Mohabbat", "Ishq-e-Qalandar", 
    "Sufi Dost-e-Dil", "Raah-e-Rumi", "Pir-e-Dilbar", "Rumi ke Saaye", "Sufi Junoon", 
    "Noor-e-Ishq", "Dil ka Faqir", "Ishq ka Junoon", "Ruhani Junoon", "Sufi Saagar", 
    "Ishq ka Dariya", "Pir-e-Ishq", "Sufi Zauq", "Dilbar-e-Raaz", "Rumi-e-Saahil", 
    "Sufi Mehfil", "Ishq ka Paigham", "Pir-e-Haq", "Rooh ka Safar", "Ishq-e-Raaz",

    # 2. Hinglish Quranic Surahs ke Naam (50 items)
    "Fatiha-e-Rahmat", "Baqarah-e-Barkat", "Al-Imran-e-Noor", "Nisa-e-Hidayat", "Maidah-e-Ikhlas", 
    "An'am-e-Safai", "Araf-e-Ruhani", "Anfal-e-Mujahad", "Tawbah-e-Sajda", "Yunus-e-Bawafa", 
    "Hud-e-Taleem", "Yusuf-e-Dilbar", "Rad-e-Haq", "Ibrahim-e-Bilkul", "Hijr-e-Raaz", 
    "Nahl-e-Imaan", "Isra-e-Ma'roof", "Kahf-e-Safar", "Maryam-e-Noor", "Taha-e-Hikmat", 
    "Anbiya-e-Raahnuma", "Hajj-e-Safar", "Muminun-e-Aqida", "Nur-e-Ishq", "Furqan-e-Sahi", 
    "Shuara-e-Kalam", "Naml-e-Dil", "Qasas-e-Rasool", "Ankabut-e-Raaz", "Rum-e-Hunar", 
    "Luqman-e-Danish", "Sajdah-e-Qalb", "Ahzab-e-Ijtima", "Saba-e-Falak", "Fatir-e-Bilkul", 
    "Yaseen-e-Raaz", "Saffat-e-Awaz", "Sad-e-Imaan", "Zumar-e-Raaz", "Ghafir-e-Maafi", 
    "Fussilat-e-Tafseer", "Shura-e-Hikmat", "Zukhruf-e-Zauq", "Dukhan-e-Bulandi", "Jathiyah-e-Izzat", 
    "Ahqaf-e-Raaz", "Muhammad-e-Mubarak", "Fath-e-Imaan", "Hujurat-e-Dil", "Qaf-e-Mohabbat",

    # 3. Hinglish Jung-E (Islamic Battles) ke Naam (50 items)
    "Jung-E-Badr", "Jung-E-Uhud", "Jung-E-Khandaq", "Jung-E-Khyber", "Jung-E-Hunain", 
    "Jung-E-Tabuk", "Jung-E-Muta", "Jung-E-Yarmouk", "Jung-E-Qadisiyya", "Jung-E-Siffin", 
    "Jung-E-Nahrawan", "Jung-E-Karbala", "Jung-E-Jamal", "Jung-E-Harrah", "Jung-E-Plassey", 
    "Jung-E-Panipat", "Jung-E-Hattin", "Jung-E-Ain Jalut", "Jung-E-Manzikert", "Jung-E-Talas", 
    "Jung-E-Tours", "Jung-E-Vienna", "Jung-E-Guadalete", "Jung-E-Constantinople", "Jung-E-Andalusia", 
    "Jung-E-Ghazwa-e-Hind", "Jung-E-Raazdaar", "Jung-E-Shujaat", "Jung-E-Fatehpur", "Jung-E-Roohdaar", 
    "Jung-E-Dilse", "Jung-E-Himmat", "Jung-E-Wafa", "Jung-E-Ikhlaas", "Jung-E-Tamanna", 
    "Jung-E-Umeed", "Jung-E-Azadi", "Jung-E-Mohafiz", "Jung-E-Bahara", "Jung-E-Shaheed", 
    "Jung-E-Jaag", "Jung-E-Dilbar", "Jung-E-Raah", "Jung-E-Mohabbat", "Jung-E-Safa", 
    "Jung-E-Aman", "Jung-E-Qurbani", "Jung-E-Firaaq", "Jung-E-Ishq", "Jung-E-Dastaar",

    # 4. Hinglish Masjid aur Qila ke Naam (50 items)
    "Masjid-e-Nawabi", "Qila-e-Mughal", "Masjid-e-Shahi", "Qila-e-Agra", "Masjid-e-Bara", 
    "Qila-e-Taj", "Masjid-e-Hind", "Qila-e-Dilli", "Masjid-e-Mausam", "Qila-e-Raunak", 
    "Masjid-e-Shaan", "Qila-e-Jawahar", "Masjid-e-Barkat", "Qila-e-Dilbar", "Masjid-e-Ishq", 
    "Qila-e-Rumi", "Masjid-e-Raaz", "Qila-e-Shahenshah", "Masjid-e-Noor", "Qila-e-Sultan", 
    "Masjid-e-Falak", "Qila-e-Zamana", "Masjid-e-Tajalli", "Qila-e-Haider", "Masjid-e-Raunaq", 
    "Qila-e-Mahabbat", "Masjid-e-Saif", "Qila-e-Safa", "Masjid-e-Gulzar", "Qila-e-Ikhlas", 
    "Masjid-e-Dilse", "Qila-e-Aashiyana", "Masjid-e-Qasr", "Qila-e-Bastar", "Masjid-e-Dastaan", 
    "Qila-e-Riyasat", "Masjid-e-Ruhani", "Qila-e-Fateh", "Masjid-e-Tasveer", "Qila-e-Sarhad", 
    "Masjid-e-Zauq", "Qila-e-Raushan", "Masjid-e-Banarsi", "Qila-e-Jashn", "Masjid-e-Nazrana", 
    "Qila-e-Murad", "Masjid-e-Aqsa", "Qila-e-Khuda", "Masjid-e-Raah", "Qila-e-Dastoor",

    # 5. Hinglish Islamic Festivals aur Tyohaar (50 items)
    "Eid-ul-Fitr ka Jashn", "Ramzan ka Mahina", "Shab-e-Barat ki Raat", "Laylatul Qadr ka Noor", 
    "Shab-e-Miraj ki Yaad", "Shab-e-Qadr ka Raaz", "Dhul Hijjah ka Mahina", "Muharram ka Dukh", "Ashura ka Waqt", 
    "Jumada al-Awwal ka Jashn", "Safar ka Safar", "Rabi ul-Awwal ki Khushi", "Rabi ul-Thani ka Andaz", "Jumada al-Thani ka Mahina", 
    "Rajab ka Aashirwaad", "Shaaban ki Tayaari", "Shawwal ka Jashn", "Dhul Qadah ki Baarish", "Hajj ka Safar", 
    "Umrah ka Armaan", "Mawlid-e-Nabi ka Jashn", "Eid-e-Milad un Nabi", "Chand Raat ki Khushbu", "Iftar ki Mehfil", 
    "Sehar ki Mehfil", "Roza ka Jazba", "Iftar ka Mazaa", "Suhur ka Nasha", "Ramzan Bazaar", 
    "Iftar Party", "Eid ki Taiyari", "Eid ka Silsila", "Ramzan ki Mehakti Raat", "Eid-ul-Aziz", 
    "Noor-e-Ramzan", "Eid ka Tyohaar", "Ramzan ka Imaan", "Eid ki Dawat", "Ramzan ki Dua", 
    "Iftar ki Dastarkhwan", "Eid ka Utsav", "Ramzan ka Ehsas", "Iftar ka Silsila", "Eid ki Raat", 
    "Ramzan ka Suhana", "Iftar ka Jashn", "Eid ka Jazba", "Ramzan ki Roshni", "Eid ki Barkat",

    # 6. Hinglish Islamic Science aur Fankaar (50 items)
    "Ibn Sina ka Dimaag", "Al-Razi ka Ilm", "Al-Kindi ki Soch", "Ibn al-Haytham ka Nazariya", "Al-Farabi ka Falsafa", 
    "Ibn Khaldun ka Tareekh", "Nasir al-Din Tusi ka Hisab", "Ibn al-Nafis ka Dil", "Al-Biruni ki Khoj", "Al-Khwarizmi ka Algorithm", 
    "Ibn Battuta ka Safar", "Al-Zahrawi ka Surgery", "Al-Razi ke Dawa", "Ibn Sina ki Kitab", "Al-Farabi ke Fikr", 
    "Ibn Khaldun ka Nazariya", "Al-Khwarizmi ke Number", "Ibn al-Haytham ki Roshni", "Al-Razi ka Tajurba", "Al-Kindi ke Mantaq", 
    "Ibn Battuta ka Safarnama", "Al-Biruni ke Hisab", "Al-Zahrawi ka Amal", "Ibn al-Nafis ka Risala", "Al-Khwarizmi ka Calculator", 
    "Ibn Sina ka Falsafa", "Al-Razi ka Tajurba", "Ibn Khaldun ka Tareeka", "Al-Farabi ki Soch", "Nasir Tusi ka Hisab", 
    "Ibn al-Haytham ka Andaz", "Al-Kindi ka Logic", "Ibn Battuta ka Safarnama", "Al-Biruni ka Jeevan", "Al-Zahrawi ka Ilaj", 
    "Ibn al-Nafis ka Daur", "Al-Khwarizmi ka Hisaab", "Ibn Sina ka Marz", "Al-Razi ke Experiment", "Al-Farabi ke Raaz", 
    "Ibn Khaldun ki Soch", "Nasir Tusi ka Ilm", "Ibn al-Haytham ka Camera Obscura", "Al-Kindi ka Raaz", "Ibn Battuta ki Manzil", 
    "Al-Biruni ka Safar", "Al-Zahrawi ka Ilm", "Ibn al-Nafis ki Khoj", "Al-Khwarizmi ka Science", "Ibn Sina ka Daur",
    

    # 8. Hinglish Tariekhi Shakhsiyat (Islamic Historical Personalities) (50 items)
    "Hazrat Abu Bakr-e-Hind", "Hazrat Umar-e-Farishta", "Hazrat Usman-e-Dilbar", "Hazrat Ali-e-Saqi", "Hazrat Bilal-e-Noor", 
    "Hazrat Salman-e-Raaz", "Hazrat Suhail-e-Raah", "Hazrat Ammar-e-Imaan", "Hazrat Khalid-e-Mujahid", "Hazrat Saad-e-Mohafiz", 
    "Hazrat Zubair-e-Sab", "Hazrat Abbas-e-Murad", "Hazrat Hamza-e-Dil", "Hazrat Abu Talib-e-Raaz", "Hazrat Umar Farooq-e-Haq", 
    "Hazrat Usman Ghani-e-Safar", "Hazrat Ali Asghar-e-Dil", "Hazrat Fatima-e-Raaz", "Hazrat Khadija-e-Sukoon", "Hazrat Aisha-e-Raunak", 
    "Hazrat Hasan-e-Ishq", "Hazrat Hussain-e-Sab", "Hazrat Mueen-e-Raaz", "Hazrat Saif-e-Haq", "Hazrat Qasim-e-Dil", 
    "Hazrat Idris-e-Raaz", "Hazrat Hud-e-Hikmat", "Hazrat Salih-e-Raah", "Hazrat Ibrahim-e-Mohabbat", "Hazrat Ismail-e-Raaz", 
    "Hazrat Ishaq-e-Dil", "Hazrat Yaqub-e-Raunaq", "Hazrat Yusuf-e-Husn", "Hazrat Ayyub-e-Sabr", "Hazrat Shuayb-e-Dil", 
    "Hazrat Musa-e-Qalb", "Hazrat Harun-e-Saaz", "Hazrat Dawud-e-Raaz", "Hazrat Sulaiman-e-Dil", "Hazrat Yunus-e-Raah", 
    "Hazrat Ilyas-e-Haqq", "Hazrat Ayyub-e-Ishq", "Hazrat Zakariya-e-Noor", "Hazrat Yahya-e-Hikmat", "Hazrat Isa-e-Raaz", 
    "Hazrat Muhammad-e-Sukoon", "Hazrat Imam-e-Raaz", "Hazrat Malik-e-Saaz", "Hazrat Rumi-e-Dilbar", "Hazrat Sir Syed-e-Haq",

    # 9. Hinglish Islami Falsafa aur Aqeeda (50 items)
    "Tawheed ka Paigham", "Shirk se Bachao", "Risalat ka Asar", "Akhirah ka Imaan", "Malaika ki Barkat", 
    "Qadar ka Raaz", "Quran ka Noor", "Sunnat ka Silsila", "Hadith ka Paigham", "Fiqh ka Ujala", 
    "Ijma ka Ittehad", "Qiyas ka Misaal", "Ijtihad ka Junoon", "Zakat ka Faraiz", "Salah ka Waqt", 
    "Sawm ka Jazba", "Hajj ka Safar", "Umrah ka Armaan", "Tahajjud ka Wada", "Tasbih ka Zauq", 
    "Tahmeed ka Paigham", "Takbir ka Jazba", "Tahlil ka Falsafa", "Shahada ka Imaan", "Wudu ka Safa", 
    "Ghusl ka Fikr", "Tayammum ka Raaz", "Adhan ka Awaaz", "Iqamah ka Amal", "Jumuah ka Jamaat", 
    "Eid ka Paigham", "Qurbani ka Jazba", "Aqiqah ka Mausam", "Nikah ka Bandhan", "Talaq ka Iqraar", 
    "Khula ka Faisla", "Hijab ka Zevar", "Niqab ka Raaz", "Burqa ka Andaaz", "Halal ka Maqaam", 
    "Haram ka Ittelaa", "Makruh ka Ehsaas", "Mustahab ka Mansooba", "Mubah ka Faisla", "Fard ka Farz", 
    "Wajib ka Amal", "Sunnat ka Rasm", "Nafl ka Silsila", "Bidah ka Iqraar", "Taqwa ka Paigham",

    

]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return jsonify(word=random.choice(islamic_words).capitalize())

if __name__ == '__main__':
    app.run(debug=True)
