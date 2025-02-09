# app.py (Updated)
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)


islamic_words = [
    
    # Paigambar (Prophets)
    "Hazrat-Adam-Paigambar-E-Awwal-Alayhis-Salaam", "Hazrat-Idris-Paigambar-E-Irfan-Alayhis-Salaam", 
    "Hazrat-Nuh-Paigambar-E-Sabr-Alayhis-Salaam", "Hazrat-Hud-Paigambar-E-Hidayat-Alayhis-Salaam", 
    "Hazrat-Salih-Paigambar-E-Barkat-Alayhis-Salaam", "Hazrat-Ibrahim-Paigambar-E-Mubarak-Alayhis-Salaam", 
    "Hazrat-Lut-Paigambar-E-Mubarak-Alayhis-Salaam", "Hazrat-Ismail-Paigambar-E-Mubaraka-Alayhis-Salaam", 
    "Hazrat-Ishaq-Paigambar-E-Mubarak-Alayhis-Salaam", "Hazrat-Yaqub-Paigambar-E-Hikmat-Alayhis-Salaam", 
    "Hazrat-Yusuf-Paigambar-E-Dilbar-Alayhis-Salaam", "Hazrat-Ayyub-Paigambar-E-Sabr-Alayhis-Salaam", 
    "Hazrat-Shuayb-Paigambar-E-Burhan-Alayhis-Salaam", "Hazrat-Musa-Paigambar-E-Raahnuma-Alayhis-Salaam", 
    "Hazrat-Harun-Paigambar-E-Musaabiq-Alayhis-Salaam", "Hazrat-Dawud-Paigambar-E-Majid-Alayhis-Salaam", 
    "Hazrat-Sulaiman-Paigambar-E-Adl-Alayhis-Salaam", "Hazrat-Ilyas-Paigambar-E-Raaz-Alayhis-Salaam", 
    "Hazrat-Al-Yasa-Paigambar-E-Hikmat-Alayhis-Salaam", "Hazrat-Yunus-Paigambar-E-Tawakkul-Alayhis-Salaam", 
    "Hazrat-Zakariya-Paigambar-E-Hikmat-Alayhis-Salaam", "Hazrat-Yahya-Paigambar-E-Fazilat-Alayhis-Salaam", 
    "Hazrat-Isa-Paigambar-E-Mubarak-Alayhis-Salaam", "Hazrat-Muhammad-Paigambar-E-Rasoolullah-Sallallahu-Aleyhi-Wassallam",

    # Allah Ke Wali (Saints And Righteous People)
    "Hazrat-Abu-Bakr-Siddique", "Hazrat-Umar-Farooq", "Hazrat-Usman-Ghani", "Hazrat-Ali-Al-Murtaza", 
    "Hazrat-Khadija-Raheemah", "Hazrat-Fatima-Zahra", "Hazrat-Hassan-Al-Mujtaba", "Hazrat-Hussain-Shaheed", 
    "Hazrat-Bilal-Habashi", "Hazrat-Salman-Farsi", "Hazrat-Suhail-Al-Hakeem", "Hazrat-Uthman-Al-Kabeer", 
    "Hazrat-Ammar-Al-Mukhlis", "Hazrat-Zubair-Al-Mujahid", "Hazrat-Talha-Al-Hashimi", "Hazrat-Saad-Al-Raheem", 
    "Hazrat-Saeed-Al-Muhtasib", "Hazrat-Abdullah-Al-Raheem", "Hazrat-Usama-Bin-Zaid", "Hazrat-Zaid-Al-Ameen",


    # Imams (Sunni Islam)
    "Hazrat-Ali-Al-Murtaza", "Hazrat-Hassan-Al-Mujtaba", "Hazrat-Hussain-Shaheed", "Hazrat-Zainul-Abideen-Al-Mubarak", 
    "Hazrat-Muhammad-Baqir-Al-Hakeem", "Hazrat-Jafar-Sadiq-Al-Kamil", "Hazrat-Musa-Kazim-Al-Sabir", "Hazrat-Ali-Raza-Al-Amin", 
    "Hazrat-Muhammad-Taqi-Al-Jawad", "Hazrat-Ali-Naqi-Al-Azam", "Hazrat-Hassan-Askari-Al-Aqil", "Hazrat-Muhammad-Mehdi-Al-Muntazar",

    # Jungon Ke Naam (Famous Battles)
    "Badr", "Uhud", "Khandaq", "Khyber", "Hunain", "Tabuk", "Muta", "Yarmouk", "Qadisiyya", "Siffin",
    "Nahrawan", "Karbala", "Jamal", "Harrah", "Plassey", "Panipat", "Hattin", "Ain Jalut", "Manzikert",

    # Jagah Ke Naam (Holy Places And Cities)
    "Makkah", "Madinah", "Jerusalem", "Karbala", "Najaf", "Kufa", "Basra", "Damascus", "Baghdad",
    "Cairo", "Istanbul", "Samarra", "Qom", "Medina", "Taif", "Jeddah", "Hebron", "Ghaza", "Sanaa",
    "Khartoum", "Timbuktu", "Cordoba", "Granada", "Delhi", "Lahore", "Karachi", "Jakarta", "Kuala Lumpur",

    # Quranic Words And Phrases
    "Allah", "Rahman", "Rahim", "Malik", "Quddus", "Salam", "Mumin", "Muhaymin", "Aziz", "Jabbar",
    "Mutakabbir", "Khaliq", "Bari", "Musawwir", "Ghaffar", "Qahhar", "Wahhab", "Razzaq", "Fattah",
    "Alim", "Qabid", "Basit", "Khafid", "Rafi", "Muizz", "Mudhill", "Samee", "Basir", "Hakam",
    "Adl", "Latif", "Khabir", "Halim", "Azim", "Ghafur", "Shakur", "Ali", "Kabir", "Hafiz",
    "Muqit", "Hasib", "Jalil", "Karim", "Raquib", "Mujib", "Wasi", "Hakim", "Wadud", "Majid",
    "Baith", "Hashr", "Qiyamah", "Jannah", "Jahannum", "Siraat", "Mizan", "Hawd", "Shafaah",

    # Islamic Months
    "Muharram", "Safar", "Rabi Al-Awwal", "Rabi Al-Thani", "Jumada Al-Awwal", "Jumada Al-Thani",
    "Rajab", "Shaaban", "Ramadan", "Shawwal", "Dhul Qadah", "Dhul Hijjah",

    
    # Asma Ul-Husna (Allah Ke 99 Naam)
    "Ar-Rahman", "Ar-Rahim", "Al-Malik", "Al-Quddus", "As-Salam", "Al-Mumin", "Al-Muhaymin",
    "Al-Aziz", "Al-Jabbar", "Al-Mutakabbir", "Al-Khaliq", "Al-Bari", "Al-Musawwir", "Al-Ghaffar",
    "Al-Qahhar", "Al-Wahhab", "Ar-Razzaq", "Al-Fattah", "Al-Alim", "Al-Qabid", "Al-Basit",
    "Al-Khafid", "Ar-Rafi", "Al-Muizz", "Al-Mudhill", "As-Sami", "Al-Basir", "Al-Hakam", "Al-Adl",
    "Al-Latif", "Al-Khabir", "Al-Halim", "Al-Azim", "Al-Ghafur", "Ash-Shakur", "Al-Ali", "Al-Kabir",
    "Al-Hafiz", "Al-Muqit", "Al-Hasib", "Al-Jalil", "Al-Karim", "Ar-Raqib", "Al-Mujib", "Al-Wasi",
    "Al-Hakim", "Al-Wadud", "Al-Majid", "Al-Wahid", "Al-Ahad", "As-Samad", "Al-Qadir", "Al-Muqtadir",
    "Al-Muqaddim", "Al-Muakhkhir", "Al-Awwal", "Al-Akhir", "Az-Zahir", "Al-Batin", "Al-Wali",
    "Al-Mutaali", "Al-Barr", "At-Tawwab", "Al-Muntaqim", "Al-Afuww", "Ar-Rauf", "Malik Ul-Mulk",
    "Dhul-Jalali Wal-Ikram", "Al-Muqsit", "Al-Jami", "Al-Ghani", "Al-Mughni", "Al-Mani", "Ad-Darr",
    "An-Nafi", "An-Nur", "Al-Hadi", "Al-Badi", "Al-Baqi", "Al-Warith", "Ar-Rashid", "As-Sabur",

    # Quran Ki Surahon Ke Naam (114 Surahs)
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

    # Paigambar Aur Sahaba Ke Naam 
    "Hazrat-Abdur-Rahman-Al-Farooq", "Hazrat-Saad-Al-Mujahid", "Hazrat-Saeed-Al-Sadiq",  
    "Hazrat-Khabbab-Al-Shaheed", "Hazrat-Miqdad-Al-Faris", "Hazrat-Abbas-Al-Sakka",  
    "Hazrat-Khalid-Al-Saifullah", "Hazrat-Amr-Al-Adil", "Hazrat-Abu-Talib-Al-Hami",  
    "Hazrat-Abu-Sufyan-Al-Muhtadi", "Hazrat-Hind-Umm-Muawiya", "Hazrat-Hafsa-Umm-ul-Qura",  
    "Hazrat-Safiyya-Al-Hanif", "Hazrat-Umm-Salama-Al-Muhajira", "Hazrat-Ruqayyah-Al-Batool",  
    "Hazrat-Umm-Kulthum-Al-Zahida", "Hazrat-Asma-Al-Zaat-un-Nitaqayn"  

    # Islami Jungen Aur Ghazawat (50+)
    "Khandaq", "Khaybar", "Hunain", "Tabuk", "Muta", "Yarmouk", "Qadisiyya", "Siffin",
    "Nahrawan", "Karbala", "Jamal", "Harrah", "Plassey", "Panipat", "Hattin", "Ain-Jalut", "Manzikert",
    "Talas", "Tours", "Vienna", "Guadalete", "Constantinople", "Andalusia", "Ghazwa-E-Hind", "Tabuk",
    "Trench", "Yamama", "Ridda", "Nahrawan", "Siffeen", "Camel", "Siffin", "Karbala", "Harrah",

    # Mukaddas Jagah (100+)
    "Kaaba", "Masjid-E-Nabwi", "Baitul-Maqdis", "Masjid-E-Aqsa", "Jannatul Baqi", "Jannatul-Mualla",
    "Jabal-E-Noor", "Jabal-E-Rahmat", "Mina", "Muzdalifah", "Arafat", "Safa-Marwa", "Zamzam", "Hira",
    "Thawr", "Badr", "Uhud", "Quba", "Najaf", "Karbala", "Kufa", "Samarra", "Qom", "Medina", "Taif",
    "Jeddah", "Hebron", "Ghaza", "Damascus", "Baghdad", "Cairo", "Istanbul", "Cordoba", "Timbuktu",
    "Al-Azhar", "Alhambra", "Fatehpur Sikri", "Ajmer", "Delhi", "Lahore", "Multan", "Makkah", "Madinah",

    # Islami Aqeeda Aur Amal (200+)
    "Tawheed", "Shirk", "Risalat", "Akhirah", "Malaika", "Qadar", "Quran", "Sunnah", "Hadith", "Fiqh",
    "Ijmah", "Qiyas", "Ijtihad", "Zakat", "Salah", "Sawm", "Hajj", "Umrah", "Tahajjud", "Tasbih",
    "Tahmeed", "Takbir", "Tahlil", "Shahada", "Wudu", "Ghusl", "Tayammum", "Adhan", "Iqamah", "Jumuah",
    "Eid", "Qurbani", "Aqiqah", "Nikah", "Talaq", "Khula", "Hijab", "Niqab", "Burqa", "Halal", "Haram",
    "Makruh", "Mustahab", "Mubah", "Fard", "Wajib", "Sunnat", "Nafl", "Bidah", "Taqwa", "Ikhlas",
    "Sabr", "Shukr", "Tawakkul", "Zuhd", "Qanaat", "Tawbah", "Istighfar", "Dua", "Zikr", "Sadaqah",
    "Waqf", "Jihad", "Dawah", "Ummah", "Khilafah", "Shura", "Bayah", "Fatwa", "Mufti", "Qazi",

    # Islami Tareekhi Shakhsiyat (150+)
    "Imam Abu Hanifa", "Imam Malik", "Imam Shafi", "Imam Ahmad", "Ibn Taymiyyah", "Al-Ghazali",
    "Ibn Sina", "Al-Farabi", "Al-Khwarizmi", "Ibn Khaldun", "Hazrat-Saladin-Al-Nasir", "Hazrat-Tipu-Sultan-Al-Mujahid", "Hazrat-Akbar-Al-Adil",  
    "Hazrat-Aurangzeb-Alamgir", "Hazrat-Muhammad-Bin-Qasim-Al-Fateh", "Hazrat-Mahmud-Ghaznavi-Al-Muzaffar",  
    "Hazrat-Al-Biruni-Al-Hakeem", "Hazrat-Ibn-Battuta-Al-Rahhal", "Hazrat-Rumi-Al-Murshid",  
    "Hazrat-Al-Hallaj-Al-Arif", "Hazrat-Rabia-Basri-Al-Zahida", "Hazrat-Nizamuddin-Auliya-Al-Mehboob",  
    "Hazrat-Moinuddin-Chishti-Al-Ghaus", "Hazrat-Baha-Ud-Din-Zakariya-Al-Qutub", "Hazrat-Shah-Waliullah-Al-Mujaddid",  
    "Hazrat-Sir-Syed-Al-Ta'limi", "Hazrat-Iqbal-Al-Shair", "Hazrat-Maulana-Azad-Al-Mutawakkil",       "Hazrat-Hasan-Al-Banna-Al-Murabbi", "Hazrat-Sayyid-Qutb-Al-Shahid", "Hazrat-Malcolm-X-Al-Hajj",  
    "Hazrat-Muhammad-Ali-Al-Qawi", "Hazrat-Zia-Ul-Haq-Al-Amir", "Hazrat-Erdogan-Al-Ra'is",  
    "Hazrat-Zayed-Al-Muhsin", "Hazrat-Faisal-Al-Muwahhid"

    # Islami Festivals Aur Dates
    "Eid-Ul-Fitr", "Eid-Ul-Adha", "Muharram", "Ashura", "Shab-E-Barat", "Laylatul Qadr",
    "Shab-E-Miraj", "Shab-E-Qadr", "Ramadan", "Dhul Hijjah", "Rajab", "Jumada Al-Awwal",
    "Safar", "Rabi Ul-Awwal", "12 Rabi Ul-Awwal", "27 Rajab", "15 Shaban", "10 Muharram",

    # Islami Science Aur Kalaa
    "Ilm-Al-Jabr-Al-Asasi", "Ilm-Al-Algoritmi-Al-Hasi", "Funoon-Al-Kimiya-Al-Atiqa",  
    "Aala-Al-Usturlab-Al-Nujumi", "Aala-Al-Rub-Al-Muqantarat", "Aala-Al-Kamera-Al-Muzlima",  
    "Funoon-Al-Jiraha-Al-Tibbi", "Ilm-Al-Adwiya-Al-Kimiyawi", "Ilm-Al-Manazir-Al-Basari",  
    "Ilm-Al-Muthalathat-Al-Handasi", "Hazrat-Avicenna-Al-Tabib", "Hazrat-Averroes-Al-Mufakkir",  
    "Hazrat-Al-Zahrawi-Al-Jarrah", "Hazrat-Al-Kindi-Al-Faylasuf", "Hazrat-Al-Razi-Al-Muallim",  
    "Hazrat-Ibn-Al-Haytham-Al-Basari", "Hazrat-Al-Jazari-Al-Muhandis", "Hazrat-Al-Khwarizmi-Al-Hisabi",  
    "Hazrat-Al-Battani-Al-Falaki", "Hazrat-Al-Idrisi-Al-Jughrafi",

    # Islamic Philosophical Terms
    "Falsafa", "Hikmah", "Haqqiqah", "Maqasid-Al-Shariah", "Ibtida", "Nusus-Al-Hikmah", "Ma'rifah",  
    "Tajassus-Al-Haqiqah", "Tasawwuf", "Ishraq", "Mawrid-Al-Hikmah", "Ruhaniyat", "Wujud", "Sirr",  
    "Takhayul", "Tasawwur", "Insan-Al-Kamil", "Aql", "Fitrah", "Kalam", "Mushahada", "Ijtihad-Al-Falsafa",  
    "Miftah-Al-Hikmah", "Suluk-Al-Ruh", "Nafs-Al-Ammarah", "Nafs-Al-Lawwama", "Nafs-Al-Mutma'inna",  
    "Jamal-Al-Tafakkur", "Sirr-Al-Asrar", "Qawl-Al-Haqq", "Miftah-Al-Aql", "Asrar-Al-Tawhid", "Usul-Al-Falsafa",  
    "Dawlat-Al-Hikmah", "Ilm-Al-Mantiq", "Riyazat-Al-Nafs", "Ihsan-Al-Fikr", "Miftah-Al-Haqq", "Bayan-Al-Ma'ani",  
    "Tafakkur-Al-Hayat", "Zawiyat-Al-Ilm", "Tadabbur", "Ulum-Al-Kalam", "Maqam-Al-Tasawwuf", "Suluk-Al-Qalb",  
    "Ihsan-Al-Ruh", "Falsafat-Al-Mutaqaddim", "Manhaj-Al-Hikmah", "Shajarah-Al-Ilm", "Silsilat-Al-Tafakkur",

    
    # Sufi Terminology
    "Ishq", "Yaqin", "Wajd", "Majzoob", "Mureed", "Murshid", "Dervish", "Fana", "Baqa", "Sohbet", "Qalandar",  
    "Zikr-E-Qalbi", "Khanqah", "Ruhani-Safar", "Sama", "Maqam-Al-Ishq", "Nazar-E-Sufiyana", "Riyazat-Al-Ruh",  
    "Silsilat-Al-Wahdat", "Wahdat-Al-Wujud", "Mujahadat-Al-Ruh", "Isharat-Al-Tariqah", "Ruhaniyya", "Ishq-E-Haqiqi",  
    "Nizam-Al-Tariqah", "Tajalli", "Fana-Fi-Al-Hubb", "Baqa-Ba'd-Al-Fana", "Majlis-Al-Sufi", "Sama-Al-Ma'arif",  
    "Ruhani-Irtiqa", "Maqam-Al-Sabr", "Ruhani-Zauq", "Ishq-Al-Majazi", "Ishq-Al-Rububiyyah", "Zikr-Al-Mashreq",  
    "Silsilat-Al-Mahabba", "Nishan-Al-Tariqah", "Saqt-Al-Dil", "Ruhani-Musahaba", "Irtifa-Al-Ruh", "Sarmaya-Al-Tajalli",  
    "Sirru-Al-Qalb", "Tariqat-Al-Fana", "Suluk-Al-Mahabba", "Jawhar-Al-Ruh", "Shuhud", "Hunar-Al-Zikr", "Fayz-Al-Sufi",  
    "Nawa-Al-Tariqah",
    
    # Islamic Inventions And Scholars In Science
    "Ibn-Al-Nafis", "Ibn-Al-Baitar", "Ibn-Zuhr", "Al-Khazini", "Qutb-Al-Din-Al-Shirazi",  
    "Ibn-Al-Razzaz-Al-Jurjani", "Ibn-Al-Wardi", "Ibn-Fadlan", "Ibn-Hibban", "Al-Suli",  
    "Al-Birjandi", "Al-Kashi", "Ibn-Al-Shatir", "Al-Mas'udi", "Ibn-Hazm", "Ibn-Qutaybah",  
    "Al-Kharaqani", "Al-Tabari", "Ibn-Kathir", "Al-Baghawi", "Ibn-Al-Jawzi",  
    "Ibn-Hajar-Al-Asqalani", "Ibn-Al-Subki", "Ibn-Al-Salah", "Al-Majriti", "Al-Farghani",  
    "Ibn-Sab'in", "Ibn-Bassam", "Al-Dimashqi", "Nasir-Al-Din-Al-Tusi", "Ibn-Al-Nadim",  
    "Al-Qazwini", "Ibn-Al-Rumaythah", "Ibn-Al-Humam", "Al-Safadi", "Ibn-Abi-Usaybi'a",  
    "Ibn-Al-Quff", "Ibn-Makula", "Al-Baghdadi", "Ibn-Al-Rashid", "Ibn-Abi-Zar",  
    "Al-Nasawi", "Ibn-Al-Tib", "Ibn-Al-Jurayj", "Ibn-Al-Adim", "Al-Muqaddasi",  
    "Ibn-Al-Wazir", "Ibn-Al-Nu'man"  

    
    # Islamic Architectural Landmarks
    "Dome-Of-The-Rock", "Blue-Mosque", "Suleymaniye-Mosque", "Al-Qarawiyyin-Mosque",  
    "Nasir-Al-Mulk-Mosque", "Shalimar-Gardens", "Faisal-Mosque", "Golestan-Palace",  
    "Topkapi-Palace", "Red-Fort", "Humayun's-Tomb", "Shalimar-Bagh", "Badshahi-Mosque",  
    "Jama-Masjid-Of-Agra", "Mehmed-Paša-Sokolović-Bridge", "Rumi's-Mausoleum",  
    "Alaeddin-Mosque", "Ulu-Camii", "Sultan-Qaboos-Grand-Mosque", "Sheikh-Zayed-Grand-Mosque",  
    "Baiturrahman-Grand-Mosque", "Masjid-Raya-Bandung", "Great-Mosque-Of-Xi'an",  
    "Sultan-Mosque-(Singapore)", "Masjid-Sultan-(Singapore)", "Istiqlal-Mosque",  
    "Moti-Masjid", "Jama-Mosque-Of-Herat", "Registan-Square", "Gur-E-Amir",  
    "Bibi-Khanym-Mosque", "Masjid-Jameh-Of-Isfahan", "Vakil-Mosque", "Shah-Cheragh",  
    "Masjid-Al-Taqwa", "Masjid-Qiblatain", "Hassan-Ii-Mosque", "Koutoubia-Mosque",  
    "Great-Mosque-Of-Kairouan", "Great-Mosque-Of-Sousse", "Qasr-Al-Hayr-Al-Sharqi",  
    "Saladin-Citadel", "Citadel-Of-Aleppo", "Madrasa-Of-Sultan-Hassan", "Medina-Fort",  
    "Minaret-Of-Jam", "Qusayr-Amra", "Ribat-Of-Monastir", "Qal'at-Al-Bahrain", "Citadel-Of-Qaitbay"  
    
    # Islamic Poetic And Literary Terms
    "Ghazal", "Qasida", "Mathnawi", "Saj'", "Muwashshah", "Zajal", "Rubaiyat", "Naat", "Manqabat", "Marsiya", "Takhmis", "Diwan", "Safar Nama", 
    "Siyar", "Qisas", "Sirat", "Tazkira", "Khamsa", "Rasa'il", "Mukhtasar", "Tarjuma", "Maqama", "Silsila", "Bait", "Misra", "Qafiyah", "Wazn", 
    "Bahr", "Radeef", "Tawil", "Takhmis-E-Qasidah", "Hikam", "Sufi Kalam", "Ishq Nama", "Divan-E-Rumi", "Nazm", "Sukhan", "Mushaira", "Adab", 
    "Murakkab", "Qissah", "Dastan", "Ruba'i", "Maqsud", "Ishaarat", "Manzum", "Ghazalnama", "Sarguzasht", "Kissa", "Shairana",

    # Islamic Historical Regions And Cities
    "Fes", "Marrakesh", "Rabat", "Agadir", "Tunis", "Kairouan", "Sousse", "Tripoli", "Seville", "Toledo", "Fustat", "Hijaz", "Tihamah", 
    "Najd", "Asir", "Baluchistan", "Sindh", "Punjab", "Transoxiana", "Khwarezm", "Fergana", "Merv", "Bukhara", "Samarkand", "Herat", "Balkh", 
    "Kandahar", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Baku", "Ankara", "Izmir", "Antalya", "Agra", "Lucknow", "Hyderabad", "Bhopal", 
    "Aurangabad", "Riyadh", "Dammam", "Doha", "Manama", "Muscat", "Kuwait City", "Amman", "Ramallah",

    # Modern Islamic Thinkers And Leaders
    "Tariq-Ramadan", "Hamza-Yusuf", "Yasir-Qadhi", "Omar-Suleiman", "Shabir-Ally", "Amina-Wadud",  
    "Dalia-Mogahed", "Imran-N.-Hosein", "Tariq-Jameel", "Nouman-Ali-Khan", "Zakir-Naik", "Irshad-Manji",  
    "Reza-Aslan", "Ayaan-Hirsi-Ali", "Abdulaziz-Sachedina", "Seyyed-Hossein-Nasr", "Fazlur-Rahman",  
    "Ali-Gomaa", "Ahmed-Deedat", "Bilal-Philips", "Yvonne-Ridley", "Naser-Makarem-Shirazi",  
    "Ali-Al-Qaradaghi", "Mohammed-Arkoun", "Abdul-Hakim-Murad", "Khaled-Abou-El-Fadl", "Zainab-Salbi",  
    "Aref-Ali-Nayed", "Nabeel-Qureshi", "Ebrahim-Kalin", "Amr-Khaled", "Tariq-Anwar", "Mahmoud-Abbas",  
    "Rashid-Al-Ghannushi", "Mustafa-Akyol", "M.-Fethullah-Gülen", "Süleyman-Ateş", "Tawfiq-Al-Hakim",  
    "Radwan-Ziadeh", "Sami-Yusuf", "Mahmoud-Darwish", "Ibrahim-Ozdemir", "Jamal-Al-Banna",  
    "Kamal-Al-Fadl", "Rachid-Ghannouchi", "Hafiz-Omer", "Sultan-Al-Qassemi", "Abdullah-Bin-Bayyah",  
    "Imran-Khan", "Tawakkol-Karman",
    
    # Additional Islamic Concepts And Rituals
    "Sadaqah-Jariyah", "I'tikaf", "Sunnah-Rawatib", "Janazah", "Dua-Al-Qunoot", "Halaqah", "Mawlid",  
    "Tadabbur-Al-Quran", "Hikmah-Al-Quran", "Tafsir", "Tajweed", "Qira'at", "Sajdah-Tilawat", "Niyyah",  
    "Jalsah", "Zikr-E-Sabah", "Zikr-E-Masaa", "Qunut-Nazilah", "Sadaqat-Al-Fitr", "Umrah-Al-Qiran",  
    "Hajj-Tamattu", "Hajj-Ifrad", "Hajj-Qiran", "Rukn", "Arkan-Al-Islam", "Arkan-Al-Iman", "Mas'uliyyat",  
    "Shahadatayn", "Fidya", "Kaffarah", "Hiba", "Fadl", "Barakah", "Tawassul", "Mizan-Al-Akhlaq", "Sabil",  
    "Sirat-Al-Mustaqim", "Du'a-Al-Hajat", "Du'a-Al-Istikhara", "Du'a-Al-Mashlaha", "Du'a-Al-Shifa",  
    "Du'a-Al-Karim", "Du'a-Al-Tawbah", "Du'a-Al-Jama'ah", "Qiyam-Al-Duha", "Duha", "Istiqama",  
    "Tawbah-Al-Qalbiya", "Ibadat-Al-Mutlaq", "Du'a-Al-Rizq"  
    
    # Islamic Cultural Terms
    "Islamic-Calligraphy", "Tazhib", "Zellij", "Arabesque", "Geometric-Pattern", "Muqarnas",  
    "Kufic-Calligraphy", "Thuluth-Script", "Naskh-Script", "Diwani-Script", "Tughra", "Nasheed",  
    "Zardozi-Embroidery", "Henna-Art", "Islamic-Geometric-Art", "Falconry", "Camel-Racing", "Majlis",  
    "Bazaar", "Carpet-Weaving", "Tilework", "Ceramic-Art", "Mughal-Miniature", "Islamic-Fashion",  
    "Hijab-Fashion", "Thobe", "Abaya", "Kandura", "Sufi-Music", "Dervish-Dance", "Qasida-Recitation",  
    "Sama-Ceremony", "Ikat-Weaving", "Mosaic-Tiling", "Ornamental-Ironwork", "Wood-Carving",  
    "Islamic-Garden", "Waqf-Architecture", "Khanqah-Architecture", "Ramadan-Iftar", "Suhur-Tradition",  
    "Henna-Night", "Iftar-Gathering", "Islamic-Calligraphic-Poetry", "Oud-Music", "Dabke-Dance",  
    "Islamic-Tile-Mural", "Frescoes-Of-Islamic-Heritage", "Mamluk-Ornamentation", "Ottoman-Textile"
    
    # Islamic Mystical Experiences And Terms
    "Wahdat-Al-Sifat", "Fana-Fi-Allah", "Ishq-E-Rasool", "Qurbani-Al-Ruhani", "Lata'if-E-Sitta",  
    "Sohbet-E-Sufi", "Muraqaba", "Kashf", "Hal", "Maqam-Al-Mahabba", "Maqam-Al-Tawakkul",  
    "Sukoon-Al-Ruh", "Fazl-E-Ilahi", "Shuhud-Al-Haqiqi", "Isharat-Al-Ruhani", "Sama'-Al-Qalb",  
    "Tasawwuf-E-Khas", "Ruhani-Safar-E-Tamheed", "Nisbat", "Zuhd-Al-Dunya", "Khudi",  
    "Nooraniyyat", "Tajalli-Al-Haqq", "Sirr-E-Wujud", "Zikr-Al-Tawhid", "Sama-Al-Awliya",  
    "Mushahadat-E-Ilahi", "Ruhani-Tajdid", "Lata'if-E-Rahmah", "Nafs-Al-Radiyah",  
    "Suluk-Al-Tazkiyah", "Qalb-E-Munir", "Ruhani-Urooj", "Ishq-E-Khuda", "Ruhani-Shukr",  
    "Ibtida-E-Ruhani", "Wujub", "Tawajjud-Al-Qalb", "Isharat-Al-Asrar", "Qalb-E-Dilbar",  
    "Zauq-E-Hayat", "Wajd-Al-Ishq", "Mushkilaat-Al-Nafs", "Ibtida-E-Tasawwuf",  
    "Ruhani-Safar-E-Ishq", "Suhbat-E-Wahdat", "Tajalli-Al-Ruh", "Sirr-Al-Mahd",  
    "Ruhani-Iltija", "Sama-Al-Ilahi"  
    

    # Additional Sufi Saints And Mystics (50 Items)
    "Junaid-Baghdadi", "Abdul-Qadir-Jilani", "Shah-Nematullah", "Pir-Meher-Ali-Shah",  
    "Khwaja-Qutbuddin-Bakhtiar-Kaki", "Shah-Inayat-Qadiri", "Sayyid-Ali-Hamadani",  
    "Makhdoom-Ali-Mahimi", "Pir-Pagara", "Sultan-Ul-Arifeen", "Khwaja-Kamal-Ud-Din",  
    "Pir-Shahabuddin", "Haji-Abdul-Wahab", "Pir-Roshan", "Baba-Qaim-Sain",  
    "Sultan-Muhammad-Qureshi", "Pir-Khushal", "Sayed-Ahmad-Razavi", "Khwaja-Arif-Qadri",  
    "Pir-Noor-Muhammad", "Pir-Mast-Ali-Shah", "Pir-Shams-Ud-Din", "Khwaja-Habib-Ur-Rahman",  
    "Sayed-Ibrahim", "Pir-Fazal-Ali", "Lal-Shahbaz-Qalandar", "Pir-Sultan", "Shams-Tabrizi",  
    "Shah-Abdul-Latif-Bhittai", "Pir-Muhammad-Chishti", "Khwaja-Shamsuddin",  
    "Pir-Ali-Tirmizi", "Pir-Aslam", "Sayed-Jamaluddin", "Khwaja-Nizamuddin-Hussain",  
    "Pir-Rahimuddin", "Sultan-Rukn-Ud-Din", "Hazrat-Shah-Kamal", "Pir-Abdullah",  
    "Mawlana-Shamsuddin", "Pir-Fazl-E-Haq", "Khwaja-Abdul-Hamid", "Pir-Hamid-Raza",  
    "Sayed-Rafiuddin", "Pir-Yusuf", "Khwaja-Abdullah-Shah", "Pir-Abdul-Salam"  
    
    # Famous Islamic Literary Works And Manuscripts (50 Items)
    "Al-Muwatta", "Sahih-Al-Bukhari", "Sahih-Muslim", "Al-Muwafaqat", "Ihya-Ulum-Al-Din",
    "Futuh-Al-Ghaib", "Al-Risala", "Tafsir-Al-Jalalayn", "Tafsir-Ibn-Kathir", "Al-Kitab Al-Muqaddas",
    "Al-Aqidah-Al-Tahawiyyah", "Rasa'il-Ikhwan Al-Safa", "Fusus-Al-Hikam", "Madarik-Al-Tanzil", "Mu'jam Al-Buldan",
    "Al-Muqaddimah", "Sirat-Rasul-Allah", "Al-Risala-Al-Qushayriyya", "Tabaqat-Al-Umam", "Al-Fihrist",
    "The-Meadows-Of-Gold", "Tarikh-Al-Tabari", "Al-Kamil-Fi-Al-Tarikh", "Risala-Qushayriyya", "Majma'-Al-Fawaid",
    "Nukat-Al-I'tiqad", "Muntakhab-Al-Tafsir", "Dala'il-Al-Nubuwwah", "Ibn-Hazm's Tauq-Al-Imaan", "Tabaqat-Al-Mutazawwijin",
    "Riyad-Us-Saliheen", "Bulugh-Al-Maram", "Fath-Al-Bari", "Zad Al-Ma'ad", "Al-Tamhid",
    "Al-Hikam", "Ihya-Al-Suluk", "Mishkat Al-Masabih", "Al-Adab-Al-Mufrad", "Al-Muwashshahat",
    "Diwan-E-Meer", "Gulistan", "Bostan", "Masnavi-I-Ma'navi", "Divan-E-Hafez",
    "Shahnameh", "Siyar-A'lam-Al-Nubala", "Al-Kashf-Al-Asrar", "Tuhfat-Al-Ahrar", "Firdaws-Al-Tahawwul",


    
    # Islamic Architectural Structures And Complexes (Additional) (50 Items)
    "Sheikh-Lotfollah-Mosque", "Shah-Mosque", "Gonbad-E-Qabus", "Tomb-Of-Shah-Rukn-E-Alam", "Mausoleum-Of-Khoja-Ahmed-Yasavi",
    "Ghazni-Minarets", "Jameh-Mosque-Of-Yazd", "Masjid-Al-Jami'-Of-Qazvin", "Rohtas-Fort", "Alamgiri-Fort",
    "Tughlaqabad-Fort", "Golkonda-Fort", "Agra-Fort", "Masjid-E-Sultani-Qazvin", "Al-Aqmar-Mosque",
    "Mustansiriya-Madrasa", "Sultan-Al-Rashid-Mosque", "Khanqah-E-Mir", "Ribat-Of-Tarim", "Qasr-Al-Banat",
    "Timurid-Madrasa-Of-Herat", "Ulugh-Beg-Madrasa", "Tomb-Of-Ahmed-Sanjar", "Imam-Reza-Shrine", "Ganj-Ali-Khan-Complex",
    "Nishat-Bagh", "Chashme-Shahi", "Tomb-Of-Jahangir", "Tomb-Of-Akbar", "Tomb-Of-Sultan-Qutb-Al-Din",
    "Herat-Minaret", "Sufi-Khanqah-Of-Multan", "Qila-Mubarak", "Chandni-Chowk-Mosque", "Jamia-Mosque-Of-Sialkot",
    "Haji-Ali-Dargah", "Ranikot-Fort", "Alamgir-Mosque", "Khanate-Palace-Of-Bukhara", "Bibi-Sahib-Kothi",
    "Mughal-Sarai", "Tomb-Of-Mirza-Ghalib", "Sultan-Pur-Majar", "Jahanara-Bagh", "Bibi-Ka-Maqbara",

    # Islamic Science And Technology Contributions (Additional) (50 Items)
    "Book-Of-Optics", "Surgical-Instruments-Design", "Chemistry-Distillation-Techniques", "Astronomical-Observatories", "Water-Clock-Innovations",
    "Astrolabe-Construction", "Quadrant-Development", "Arabic-Numerals-Transmission", "Herbal-Medicine-Catalogs", "Pharmacology-Advances",
    "Al-Razi's-Medical-Texts", "Ibn-Sina's-Canon-Of-Medicine", "Geographical-Mapping-Techniques", "Cartographic-Projections", "Ibn-Battuta's-Travel-Records",
    "Navigation-Instruments", "Mechanical-Automata", "Windmill-Designs", "Soap-Making-Process", "Crankshaft-Invention",
    "Astrological-Tables", "Arabic-Algebra", "Chemistry-Laboratory-Methods", "Advanced-Irrigation-Systems", "Water-Powered-Mills",
    "Medical-Surgical-Tools", "Philosophy-Of-Medicine", "Medical-Ethics-In-Islam", "Optical-Lenses-Development", "Scientific-Method-In-Islamic-Thought",
    "Geometric-Theorems", "Trigonometric-Identities", "Astronomical-Instruments", "Al-Kindi's-Cryptanalysis", "Early-Cryptography-Techniques",
    "Animal-Dissection-Studies", "Plant-Classification", "Astrogeology-Concepts", "Mechanical-Engineering-Concepts", "Chemical-Distillation-Apparatus",
    "Surgical-Anesthesia-Techniques", "Metallurgy-Advancements", "Mathematical-Proofs", "Algorithm-Development", "Early-Calculus-Concepts",
    "Optical-Camera-Obscura", "Solar-Calendar-Calculations", "Timekeeping-Devices", "Hydraulic-Engineering", "Architectural-Geometry",

    # Islamic Philosophical And Theological Concepts (Additional) (50 Items)
    "Haqiqat-Al-Wujud", "Sunnat-Al-Matin", "Insaniyyat-Al-Ilahi", "Fitra-Al-Rabbaniyya", "Mawrid-Al-Tanwir",
    "Silsilat-Al-Istibsar", "Majaz-Al-Haqq", "Mawqif-Al-Tadabbur", "Falsafat-Al-Kasf", "Ma'arifat-Al-Mawjood",
    "Ruhani-Tajassus", "Isharat-Al-Haqiqa", "Sirat-Al-Falsafa", "Nubuwwat-Al-Batin", "Ilm-Al-Batin",
    "Majd-Al-Aql", "Sarab-Al-Ilm", "Noor-Al-Ma'ani", "Hikmat-Al-Muta'aliyah", "Haqq-Al-Iradah",
    "Asrar-Al-Mawjood", "Tafakkur-Al-Aql", "Insan-Al-Amin", "Falsafat-Al-Kawn", "Ma'rifat-Al-Asrar",
    "Ibtida'-Al-Ma'ani", "Tamhid-Al-Ruhani", "Tawajjuh-Al-Qalb", "Ishraq-Al-Aql", "Dawlat-Al-Ma'rifah",
    "Tafsir-Al-Ruh", "Qiyamat-Al-Fikr", "Wahdat-Al-Tanwir", "Riyad-Al-Falsafa", "Nubuwwat-Al-Qalb",
    "Haqq-Al-Irshad", "Ma'rifat-Al-Kawn", "Isharaat-Al-Tasawwuf", "Mizan-Al-Falsafa", "Sirr-Al-Ma'rifah",
    "Haqq-Al-Hikmah", "Noor-Al-Tadabbur", "Qalb-Al-Tajassus", "Miftah-Al-Nur", "Silsilat-Al-Tanwir",
    "Iradat-Al-Aql", "Tawhid-Al-Mawjood",

    # Islamic Jurisprudence And Legal Texts (Additional) (50 Items)
    "Kitab-Al-Umm", "Al-Muhadhdhab", "Bidayat-Al-Mujtahid", "Al-Mabsut", "Al-Rawdah-Al-Bahiyyah",
    "Fath-Al-Qarib", "Al-Tanbih-Fi-Al-Fiqh", "Mukhtasar-Al-Quduri", "Al-Majmu'", "Nihayat-Al-Matlab",
    "Sharh-Al-Sunnah", "Al-Iqna'-Fi-Usul-Al-Fiqh", "Al-Muhit-Al-Farid", "Tuhfa-Al-Wahhabiyya", "Fath-Al-Mu'in",
    "Al-Majd-Al-Fiqh", "Al-Muqaddimah-Fi-Al-Fiqh", "Radd-Al-Muhtar", "Al-Furuq", "Durr-Al-Mukhtar",
    "Al-Targhib-Wal-Tarhib", "Fath-Al-Rahman", "Mukhtasar-Al-Sharh", "Al-Islah-Fi-Al-Fiqh", "Tuhfat-Al-Fuqaha",
    "Al-Kafi-Fi-Al-Fiqh", "Minhaj-Al-Imam", "Al-Muhit-Al-Akbar", "Risalat-Al-Fiqh", "Al-Muntaqa-Fi-Al-Fiqh",
    "Sharh-Al-Aqa'id", "Bahr-Al-Majhud", "Miftah-Al-Fiqh", "Nihayat-Al-Fiqh", "Al-Mustasfa",
    "Furuq-Al-Adl", "Tanzih-Al-Qada", "Riyadh-Al-Haqq", "Umdat-Al-Fiqh", "Al-Majalis-Al-Fiqhiyya",
    "Mukhtasar-Al-Ashraf", "Silsilat-Al-Mubtada", "Al-Qawa'id-Al-Fiqhiyya", "Al-Lubab-Fi-Al-Fiqh", "Tajdid-Al-Fiqh",
    "Ijtihad-Al-Akbar", "Usul-Al-Fiqh-Al-Jadid", "Tajmi'-Al-Fiqh", "Mawsu'at-Al-Fiqh", "Al-Majma'-Al-Fiqhiyya",

    # Islamic Dynasties, Empires, And Rulers (Additional) (50 Items)
    "Umayyad-Caliphate", "Abbasid-Caliphate", "Fatimid-Caliphate", "Seljuk-Empire", "Mamluk-Sultanate",
    "Ottoman-Empire", "Safavid-Dynasty", "Mughal-Empire", "Almohad-Caliphate", "Almoravid-Dynasty",
    "Ayyubid-Dynasty", "Ghaznavid-Empire", "Khazar-Khaganate", "Timurid-Empire", "Bahri-Mamluks",
    "Burji-Mamluks", "Sultanate-Of-Rum", "Khanate-Of-Bukhara", "Khanate-Of-Khiva", "Sultanate-Of-Delhi",
    "Marinid-Dynasty", "Zengid-Dynasty", "Zirid-Dynasty", "Rustamid-Kingdom", "Ibadi-Imamate-Of-Oman",
    "Samanid-Empire", "Nasrid-Kingdom-Of-Granada", "Emirate-Of-Córdoba", "Caliphate-Of-Córdoba", "Ghuri-Dynasty",
    "Khilji-Dynasty", "Tughlaq-Dynasty", "Sayyid-Dynasty", "Lodi-Dynasty", "Qutb-Shahi-Dynasty",
    "Asaf-Jahi-Dynasty", "Bengal-Sultanate", "Deccan-Sultanates", "Adil-Shahi-Dynasty", "Nizam-Shahi-Dynasty",
    "Barid-Shahi-Dynasty", "Bahmani-Sultanate", "Rashidun-Caliphate", "Umayyad-Emirate-Of-Córdoba", "Hafsid-Dynasty",
    "Zayyanid-Kingdom", "Saffarid-Dynasty", "Idrisid-Dynasty", "Hammadid-Dynasty", "Alaouite-Dynasty",

    # Islamic Festivals, Celebrations, And Observances (Additional) (50 Items)
    "Eid-E-Milad-Un-Nabi", "Eid-E-Siraj", "Eid-E-Zahra", "Jashn-E-Nowruz", "Eid-E-Fitr-Al-Saghir",
    "Mehfil-E-Sama", "Mela-E-Urdu", "Iftar-Nights", "Ramadan-Bazaar", "Night-Of-Qadr-Recitals",
    "Eid-E-Rukhsati", "Mawlid-Ul-Nabi", "Shab-E-Suhar", "Eid-Ul-Ghadeer", "Ziarat-Day",
    "Imam-Ali-Day", "Eid-E-Imam-Hussain", "Eid-Ul-Burhan", "Night-Of-Forgiveness",
    "Sufi-Urs", "Jashn-E-Baharan", "Cultural-Festival-Of-Islam", "Ibadat-Night", "Eid-E-Sajdah",
    "Noor-Ul-Layl", "Eid-Ul-Rahmat", "Jashn-E-Falah", "Eid-Ul-Nur",
    "Eid-Ul-Ma'soom", "Jashn-E-Tajalli", "Iftar-Mela", "Ramadan-Caravan", "Suhar-Gathering",
    "Eid-Ul-Falak", "Mawlid-Recital-Night", "Eid-Ul-Farooq", "Eid-Ul-Hakim", "Eid-Ul-Ahsan", 
    "Jashn-E-Wahdat", "Eid-E-Rasool", "Eid-Ul-Quran", "Mela-E-Dua", "Eid-Ul-Hubb",

    # Rashidun Caliphs 
    "Umar-Ibn-Al-Khattab", "Uthman-Ibn-Affan", "Ali-Ibn-Abi-Talib",

    # Umayyad Caliphs (10 Items)
    "Muawiyah-I", "Yazid-I", "Marwan-I", "Abd-Al-Malik-Ibn-Marwan", "Al-Walid-I",
    "Sulayman-Ibn-Abd-Al-Malik", "Umar-II", "Yazid-II", "Hisham-Ibn-Abd-Al-Malik", "Abd-Al-Aziz-Ibn-Al-Walid",

    # Abbasid Caliphs (12 Items)
    "Al-Saffah", "Al-Mansur", "Al-Mahdi", "Al-Hadi", "Harun-Al-Rashid", "Al-Amin",
    "Al-Ma'mun", "Al-Mu'tasim", "Al-Wathiq", "Al-Mutawakkil", "Al-Muqtadir", "Al-Radi",

    # Fatimid Caliphs/Imams (10 Items)
    "Al-Mahdi-Billah", "Al-Qa'im-Bi-Amr-Allah", "Al-Mansur-Bi-Nasr-Allah", "Al-Muizz-Li-Din-Allah",
    "Al-Aziz-Billah", "Al-Hakim-Bi-Amr-Allah", "Ali-Az-Zahir", "Al-Mustansir-Billah", "Al-Musta'li-Billah", "Al-Amir-Bi-Ahkam-Allah",

    # Seljuk Sultans (6 Items)
    "Tughril-Beg", "Alp-Arslan", "Malik-Shah-I", "Sanjar", "Berkyaruq", "Barkiyaruq",

    # Mamluk Sultans (6 Items)
    "Qalawun", "Baibars", "Al-Ashraf-Khalil", "An-Nasir-Muhammad", "Al-Zahir-Baybars", "Al-Nasir-Muhammad-Ibn-Qalawun",

    # Ottoman Sultans (15 Items)
    "Osman-I", "Orhan", "Murad-I", "Bayezid-I", "Mehmed-I", "Murad-II",
    "Mehmed-II", "Bayezid-II", "Selim-I", "Suleiman-The-Magnificent", "Selim-II", "Murad-III", "Mehmed-III", "Ahmed-I", "Mustafa-I",

    # Mughal Emperors (8 Items)
    "Babur", "Humayun", "Akbar", "Jahangir", "Shah-Jahan", "Aurangzeb-Alamgir", "Bahadur-Shah-I", "Bahadur-Shah-II",

    # Other Notable Islamic Rulers (8 Items)
    "Timur", "Sher-Shah-Suri", "Mahmud-Of-Ghazni", "Alauddin-Khilji", "Muhammad-Bin-Tughluq", "Tipu-Sultan", "Afzal-Khal", "Tamur-E-Lank",

    # Islamic Historical Battles And Military Campaigns (50 Items)
    "Jung-E-Qadisiyyah", "Jung-E-Yarmouk", "Jung-E-Badr", "Jung-E-Uhud", "Jung-E-Trench",
    "Jung-E-Khyber", "Jung-E-Hunayn", "Jung-E-Tabuk", "Jung-E-Mutah", "Jung-E-Jalula",
    "Jung-E-Nahrawan", "Jung-E-Siffin", "Jung-E-Jalalabad", "Jung-E-Khaybar", "Jung-E-Qadis",
    "Jung-E-Hira", "Jung-E-Karbala", "Jung-E-Jamal", "Jung-E-Harrah", "Jung-E-Siffin-II",
    "Jung-E-Mansura", "Jung-E-Zab", "Jung-E-Firaz", "Jung-E-Maysalun", "Jung-E-Al-Qadisiyyah",
    "Jung-E-Harra", "Jung-E-Nahr", "Jung-E-Ayn-Jalut", "Jung-E-Al-Jumhuriya", "Jung-E-Maysan",
    "Jung-E-Fahl", "Jung-E-Al-Rustamiyah", "Jung-E-Dhi-Qar", "Jung-E-Jalil", "Jung-E-Marj-Al-Saffar",
    "Jung-E-Zama", "Jung-E-Al-Bukayr", "Jung-E-Saqifah", "Jung-E-Dhul-Hijjah", "Jung-E-Anbar",
    "Jung-E-Barda'in", "Jung-E-Az-Zubayr", "Jung-E-Mu'tah", "Jung-E-Khandaq", "Jung-E-Jund-Al-Aqsa",
    "Jung-E-Dhul-Aswad", "Jung-E-Al-Raqqah", "Jung-E-Samarra", "Jung-E-Tikrit", "Jung-E-Basra",
    
     # Islamic Poets And Literary Figures (50 Items)
    "Jami", "Nasir-Khusraw", "Rumi-Saheb", "Seyrani", "Sarmad", "Ibn-Arabi", "Rashid-Ad-Din",
    "Al-Ma'arri", "Ibn-Zamrak", "Ibn-Al-Farid", "Ibn-Quzman", "Abdul-Rahim-Khan-E-Khana", "Mir-Anis",
    "Mirza-Khan-Daagh-Dehlvi", "Altaf-Hussain-Hali", "Sahir-Ludhianvi", "Faiz-Ahmed-Faiz", "Habib-Jalib",
    "Ahmad-Faraz", "Parveen-Shakir", "Meeraji", "Javed-Akhtar", "Kaifi-Azmi", "Khalil-Gibran",

    # Islamic Scientific Instruments And Innovations (50 Items)
    "Astrolabe", "Armillary-Sphere", "Sundial", "Water-Clock", "Quadrant", "Sextant", "Celestial-Globe", "Hourglass",
    "Dioptra", "Alidade", "Abacus", "Arabic-Numerals", "Algebraic-Table", "Geometric-Compasses", "Surgical-Instruments",
    "Herbal-Catalog", "Al-Razi’s-Distillation", "Ibn-Sina’s-Pharmacopoeia", "Astronomical-Tables", "Observatory-Instruments",
    "Trigonometric-Calculators", "Planetary-Models", "Mathematical-Instruments", "Optical-Lenses", "Camera-Obscura",
    "Pendulum-Clock", "Mechanical-Calculator", "Windmill-Model", "Irrigation-Gear", "Waterwheel-Mechanism",
    "Hydraulic-Organ", "Mechanical-Automata", "Coin-Press", "Paper-Making-Technique", "Glass-Blowing-Tools",
    "Ceramic-Kiln", "Mosaic-Tiler", "Carpet-Weaving-Loom", "Silk-Spinning-Wheel", "Compass", "Magnetic-Needle",
    "Sun-Chart", "Star-Atlas", "Celestial-Sphere", "Parabolic-Mirror", "Optical-Prism", "Reflecting-Telescope",
    "Geodesic-Dome", "Epicyclic-Gear", "Water-Powered-Lifting",

    # Notable Islamic Cities And Regions (Historical And Modern) (50 Items)
    "Baghdad", "Cairo", "Cordoba", "Kairouan", "Fez", "Samarkand", "Bukhara", "Isfahan", "Konya", "Damascus",
    "Istanbul", "Medina", "Makkah", "Jerusalem", "Basra", "Samarra", "Aleppo", "Tunis", "Rabat", "Fes",
    "Alexandria", "Tripoli", "Najaf", "Kufa", "Sana'a", "Marib", "Kandahar", "Herat", "Multan", "Lahore",
    "Hyderabad", "Agra", "Delhi", "Amritsar", "Faisalabad", "Karachi", "Quetta", "Peshawar", "Sialkot", "Rawalpindi",
    "Lucknow", "Jaipur", "Abu-Dhabi", "Doha", "Muscat", "Kuwait-City", "Manama", "Riyadh", "Dubai", "Sharjah",

    # Islamic Economic Terms And Institutions (50 Items)
    "Zakat", "Sadaqah", "Waqf", "Bayt-Al-Mal", "Mudarabah", "Musharakah", "Murabaha", "Ijara", "Salam", "Istisna",
    "Hawala", "Qirad", "Takaful", "Islamic-Banking", "Shariah-Compliance", "Halal-Certification", "Sukuk", "Ijarah",
    "Ar-Riba", "Bai'-Al-Inah", "Islamic-Finance", "Islamic-Insurance", "Islamic-Microfinance", "Profit-Sharing",
    "Risk-Sharing", "Interest-Free-Loans", "Islamic-Investment", "Qard-Hasan", "Islamic-Economic-Model", "Ethical-Investment",
    "Islamic-Capital-Market", "Financial-Inclusion", "Islamic-Wealth-Management", "Islamic-Financial-Instruments",
    "Islamic-Brokerage", "Sukuk-Bonds", "Islamic-Venture-Capital", "Islamic-Mutual-Funds", "Islamic-Derivatives",
    "Islamic-Credit", "Charitable-Endowment", "Religious-Taxation", "Islamic-Trade", "Islamic-Commerce", "Halal-Market",
    "Islamic-Economic-Justice", "Islamic-Social-Finance", "Islamic-Accounting", "Islamic-Financial-Regulation",
    "Islamic-Investment-Funds",

    # Islamic Educational Institutions And Madrassas (50 Items)
    "Al-Qarawiyyin-University", "Al-Azhar-University", "Nizamiyya-Madrasa", "Madrasa-Of-Ibn-Sina", "Madrasa-Of-Al-Ghazali",
    "Madrasa-Of-Al-Farabi", "Sufism-Madrasa", "Madrasa-Of-Baghdad", "Madrasa-Of-Damascus", "Madrasa-Of-Samarkand",
    "Madrasa-Of-Cairo", "Madrasa-Of-Cordoba", "Madrasa-Of-Isfahan", "Madrasa-Of-Konya", "Madrasa-Of-Herat",
    "Madrasa-Of-Bukhara", "Madrasa-Of-Fes", "Madrasa-Of-Marrakesh", "Madrasa-Of-Tunis", "Madrasa-Of-Aleppo",
    "Madrasa-Of-Nishapur", "Madrasa-Of-Shiraz", "Madrasa-Of-Balkh", "Madrasa-Of-Sistan", "Madrasa-Of-Khwarezm",
    "Madrasa-Of-Khorasan", "Madrasa-Of-Tabriz", "Madrasa-Of-Hamadan", "Madrasa-Of-Yazd", "Madrasa-Of-Maragheh",
    "Madrasa-Of-Ray", "Madrasa-Of-Sari", "Madrasa-Of-Isfahan-II", "Madrasa-Of-Qazvin", "Madrasa-Of-Tabriz-II",
    "Madrasa-Of-Shiraz-II", "Madrasa-Of-Kerman", "Madrasa-Of-Zahedan", "Madrasa-Of-Bandar-Abbas", "Madrasa-Of-Basra",
    "Madrasa-Of-Najaf", "Madrasa-Of-Kufa", "Madrasa-Of-Medina", "Madrasa-Of-Makkah", "Madrasa-Of-Jerusalem",
    "Madrasa-Of-Alexandria", "Madrasa-Of-Istanbul", "Madrasa-Of-Bursa", "Madrasa-Of-Bursa-II", "Madrasa-Of-Amman",

    # Islamic Cultural Festivals And Celebrations (50 Items)
    "Eid-Ul-Fitr", "Eid-Ul-Adha", "Ramadan-Iftar", "Laylat-Al-Qadr", "Mawlid-Al-Nabi", "Eid-E-Milad",
    "Sufi-Urs", "Islamic-New-Year", "Eid-E-Shab-E-Barat", "Ramadan-Nights", "Shab-E-Barat", "Ramadan-Mela",
    "Iftar-Bazaar", "Eid-Mela", "Eid-Fair", "Ramadan-Festival", "Quran-Recitation-Festival", "Islamic-Music-Festival",
    "Islamic-Art-Festival", "Sufi-Music-Festival", "Eid-Carnival", "Iftar-Celebration", "Ramadan-Cultural-Night",
    "Islamic-Heritage-Festival", "Eid-Ul-Farooq", "Eid-E-Rukhsati", "Sufi-Dance-Festival", "Ramadan-Poetry-Night",
    "Islamic-Storytelling-Festival", "Islamic-Heritage-Day", "Iftar-Party", "Ramadan-Lantern-Festival", "Eid-E-Rasool",
    "Ramadan-Night-Market", "Islamic-Crafts-Fair", "Sufi-Whirling-Night", "Ramadan-Cultural-Fair", "Islamic-Film-Festival",
    "Islamic-Theatre-Night", "Ramadan-Art-Exhibition", "Eid-Expo", "Islamic-Cultural-Parade", "Ramadan-Book-Fair",
    "Iftar-Concert", "Islamic-Food-Festival", "Ramadan-Community-Day", "Eid-Celebration-Expo",

    # Islamic Religious Rituals And Practices (50 Items)
    "Salah", "Sawm", "Hajj", "Umrah", "Wudu", "Ghusl", "Tayammum", "Dua", "Dhikr", "Tasbih", "Quran-Recitation",
    "Sunnah-Prayers", "Tarawih", "I'tikaf", "Sadaqah", "Zakat", "Khutbah", "Adhan", "Iqamah", "Niyyah",
    "Ruku", "Sujud", "Tashahhud", "Qiyam", "Jalsa", "Sahur", "Iftar", "Witr", "Tahajjud", "Jumu'ah",
    "Duha", "Mawlid-Observance", "Zamzam-Drinking", "Sa’i", "Raml", "Ritual-Cleansing", "Prayer-Beads",
    "Dhuhr", "Asr", "Maghrib", "Isha", "Qunut", "Janazah", "Sunnah-Fasting", "Aqiqah", "Nikah", "Talaq",
    "Hijab-Observance", "Khilafah-Oath", "Sadaqat-Ul-Fitr",

    # Islamic Modern Movements And Organizations (50 Items)
    "Muslim-Brotherhood", "Jamaat-E-Islami", "Tablighi-Jamaat", "Al-Islah-Movement", "Darul-Uloom-Movement",
    "Ahl-I-Hadith-Movement", "Tanzim-Al-Jihad", "Global-Dawah-Network", "Muslim-Youth-League", "Islamic-Fiqh-Academy",
    "Islamic-Research-Foundation", "World-Assembly-Of-Muslim-Youth", "International-Union-Of-Muslim-Scholars", "Council-Of-Islamic-Ideology", "Muslim-Public-Affairs-Council",
    "Islamic-Society-Of-North-America", "European-Council-For-Fatwa-And-Research", "Islamic-Circle-Of-North-America", "Muslim-World-League", "Islamic-Educational-Scientific-And-Cultural-Organization",
    "International-Islamic-Relief-Organization", "Islamic-Development-Bank", "Muslim-Aid", "Islamic-Relief-Worldwide", "Zakat-Foundation", "Muslim-Hands",
    "Islamic-Medical-Association", "Council-On-American-Islamic-Relations", "Islamic-Society-Of-Britain", "Muslim-Association-Of-Britain", "Muslim-Council-Of-Britain", "Islamic-Forum-Of-Europe", "Muslim-Welfare-Trust",
    "Islamic-Foundation", "Muslim-Charities-Forum", "Global-Islamic-Call-Society", "Islamic-Society-Of-South-Africa", "Muslim-Outreach", "Muslim-Public-Affairs", "Islamic-Legal-Studies-Center", "Islamic-Studies-Association", "Muslim-Media-Watch", "Islamic-Unity-Conference",
    "Global-Muslim-Youth", "Modern-Muslim-Forum", "Islamic-Summit", "International-Muslim-Conference", "United-Muslim-Scholars", "Muslim-Council-Of-Elders", "Progressive-Muslim-Network",

    # Hinglish Sufi Saints Aur Mystics Ke Naam (50 Items)
    "Junaid-E-Hind", "Abdul-Qadir-E-Hind", "Fakir-E-Raah", "Rumi-E-Dil", "Shah-E-Suhail",
    "Baba-E-Mohabbat", "Pir-E-Raaz", "Sultan-E-Sufi", "Haqiqi-Saheb", "Fana-E-Dil",
    "Ishq-E-Rooh", "Gul-E-Ishq", "Roohani-Dost", "Sufi-Saathi", "Qalandar-E-Khuda",
    "Ruhani-Saheb", "Mehboob-E-Raah", "Dilbar-E-Sufi", "Ishqwala-Baba", "Rumi-E-Raah",
    "Saif-E-Suhana", "Fana-E-Safar", "Sufi-Nazaara", "Raaz-E-Mohabbat", "Dil-E-Suhana",
    "Noor-E-Sufi", "Suhani-Pir", "Qalander-E-Dil", "Ruh-E-Mohabbat", "Ishq-E-Qalandar",
    "Sufi-Dost-E-Dil", "Raah-E-Rumi", "Pir-E-Dilbar", "Rumi-Ke-Saaye", "Sufi-Junoon",
    "Noor-E-Ishq", "Dil-Ka-Faqir", "Ishq-Ka-Junoon", "Ruhani-Junoon", "Sufi-Saagar",
    "Ishq-Ka-Dariya", "Pir-E-Ishq", "Sufi-Zauq", "Dilbar-E-Raaz", "Rumi-E-Saahil",
    "Sufi-Mehfil", "Ishq-Ka-Paigham", "Pir-E-Haq", "Rooh-Ka-Safar", "Ishq-E-Raaz",

    # Hinglish Quranic Surahs Ke Naam (50 Items)
    "Fatiha-E-Rahmat", "Baqarah-E-Barkat", "Al-Imran-E-Noor", "Nisa-E-Hidayat", "Maidah-E-Ikhlas",
    "An'am-E-Safai", "Araf-E-Ruhani", "Anfal-E-Mujahad", "Tawbah-E-Sajda", "Yunus-E-Bawafa",
    "Hud-E-Taleem", "Yusuf-E-Dilbar", "Rad-E-Haq", "Ibrahim-E-Bilkul", "Hijr-E-Raaz",
    "Nahl-E-Imaan", "Isra-E-Ma'roof", "Kahf-E-Safar", "Maryam-E-Noor", "Taha-E-Hikmat",
    "Anbiya-E-Raahnuma", "Hajj-E-Safar", "Muminun-E-Aqida", "Nur-E-Ishq", "Furqan-E-Sahi",
    "Shuara-E-Kalam", "Naml-E-Dil", "Qasas-E-Rasool", "Ankabut-E-Raaz", "Rum-E-Hunar",
    "Luqman-E-Danish", "Sajdah-E-Qalb", "Ahzab-E-Ijtima", "Saba-E-Falak", "Fatir-E-Bilkul",
    "Yaseen-E-Raaz", "Saffat-E-Awaz", "Sad-E-Imaan", "Zumar-E-Raaz", "Ghafir-E-Maafi",
    "Fussilat-E-Tafseer", "Shura-E-Hikmat", "Zukhruf-E-Zauq", "Dukhan-E-Bulandi", "Jathiyah-E-Izzat",
    "Ahqaf-E-Raaz", "Muhammad-E-Mubarak", "Fath-E-Imaan", "Hujurat-E-Dil", "Qaf-E-Mohabbat",

    # Hinglish Jung-E (Islamic Battles) Ke Naam (50 Items)
    "Jung-E-Badr", "Jung-E-Uhud", "Jung-E-Khandaq", "Jung-E-Khyber", "Jung-E-Hunain",
    "Jung-E-Tabuk", "Jung-E-Muta", "Jung-E-Yarmouk", "Jung-E-Qadisiyya", "Jung-E-Siffin",
    "Jung-E-Nahrawan", "Jung-E-Karbala", "Jung-E-Jamal", "Jung-E-Harrah", "Jung-E-Plassey",
    "Jung-E-Panipat", "Jung-E-Hattin", "Jung-E-Ain-Jalut", "Jung-E-Manzikert", "Jung-E-Talas",
    "Jung-E-Tours", "Jung-E-Vienna", "Jung-E-Guadalete", "Jung-E-Constantinople", "Jung-E-Andalusia", 
    "Jung-E-Ghazwa-E-Hind", "Jung-E-Raazdaar", "Jung-E-Shujaat", "Jung-E-Fatehpur", "Jung-E-Roohdaar", 
    "Jung-E-Dilse", "Jung-E-Himmat", "Jung-E-Wafa", "Jung-E-Ikhlaas", "Jung-E-Tamanna", 
    "Jung-E-Umeed", "Jung-E-Azadi", "Jung-E-Mohafiz", "Jung-E-Bahara", "Jung-E-Shaheed", 
    "Jung-E-Jaag", "Jung-E-Dilbar", "Jung-E-Raah", "Jung-E-Mohabbat", "Jung-E-Safa", 
    "Jung-E-Aman", "Jung-E-Qurbani", "Jung-E-Firaaq", "Jung-E-Ishq", "Jung-E-Dastaar",

    # 4. Hinglish Masjid Aur Qila Ke Naam (50 Items)
    "Masjid-E-Nawabi", "Qila-E-Mughal", "Masjid-E-Shahi", "Qila-E-Agra", "Masjid-E-Bara", 
    "Qila-E-Taj", "Masjid-E-Hind", "Qila-E-Dilli", "Masjid-E-Mausam", "Qila-E-Raunak", 
    "Masjid-E-Shaan", "Qila-E-Jawahar", "Masjid-E-Barkat", "Qila-E-Dilbar", "Masjid-E-Ishq", 
    "Qila-E-Rumi", "Masjid-E-Raaz", "Qila-E-Shahenshah", "Masjid-E-Noor", "Qila-E-Sultan", 
    "Masjid-E-Falak", "Qila-E-Zamana", "Masjid-E-Tajalli", "Qila-E-Haider", "Masjid-E-Raunaq", 
    "Qila-E-Mahabbat", "Masjid-E-Saif", "Qila-E-Safa", "Masjid-E-Gulzar", "Qila-E-Ikhlas", 
    "Masjid-E-Dilse", "Qila-E-Aashiyana", "Masjid-E-Qasr", "Qila-E-Bastar", "Masjid-E-Dastaan", 
    "Qila-E-Riyasat", "Masjid-E-Ruhani", "Qila-E-Fateh", "Masjid-E-Tasveer", "Qila-E-Sarhad", 
    "Masjid-E-Zauq", "Qila-E-Raushan", "Masjid-E-Banarsi", "Qila-E-Jashn", "Masjid-E-Nazrana", 
    "Qila-E-Murad", "Masjid-E-Aqsa", "Qila-E-Khuda", "Masjid-E-Raah", "Qila-E-Dastoor",

#------    
    # 5. Hinglish Islamic Festivals Aur Tyohaar (50 Items)
    "Eid-Ul-Fitr-Ka-Jashn", "Ramzan-Ka-Mahina", "Shab-E-Barat-Ki-Raat", "Laylatul-Qadr-Ka-Noor",
    "Shab-E-Miraj-Ki-Yaad", "Shab-E-Qadr-Ka-Raaz", "Dhul-Hijjah-Ka-Mahina", "Muharram-Ka-Dukh", "Ashura-Ka-Waqt",
    "Jumada-Al-Awwal-Ka-Jashn", "Safar-Ka-Safar", "Rabi-Ul-Awwal-Ki-Khushi", "Rabi-Ul-Thani-Ka-Andaz", "Jumada-Al-Thani-Ka-Mahina",
    "Rajab-Ka-Aashirwaad", "Shaaban-Ki-Tayaari", "Shawwal-Ka-Jashn", "Dhul-Qadah-Ki-Baarish", "Hajj-Ka-Safar",
    "Umrah-Ka-Armaan", "Mawlid-E-Nabi-Ka-Jashn", "Eid-E-Milad-Un-Nabi", "Chand-Raat-Ki-Khushbu", "Iftar-Ki-Mehfil",
    "Sehar-Ki-Mehfil", "Roza-Ka-Jazba", "Iftar-Ka-Mazaa", "Suhur-Ka-Nasha", "Ramzan-Bazaar",
    "Iftar-Party", "Eid-Ki-Taiyari", "Eid-Ka-Silsila", "Ramzan-Ki-Mehakti-Raat", "Eid-Ul-Aziz",
    "Noor-E-Ramzan", "Eid-Ka-Tyohaar", "Ramzan-Ka-Imaan", "Eid-Ki-Dawat", "Ramzan-Ki-Dua",
    "Iftar-Ki-Dastarkhwan", "Eid-Ka-Utsav", "Ramzan-Ka-Ehsas", "Iftar-Ka-Silsila", "Eid-Ki-Raat",
    "Ramzan-Ka-Suhana", "Iftar-Ka-Jashn", "Eid-Ka-Jazba", "Ramzan-Ki-Roshni", "Eid-Ki-Barkat"

    # 6. Hinglish Islamic Science Aur Fankaar (50 Items)
    "Ibn-Sina-Ka-Dimaag", "Al-Razi-Ka-Ilm", "Al-Kindi-Ki-Soch", "Ibn-Al-Haytham-Ka-Nazariya", "Al-Farabi-Ka-Falsafa",
    "Ibn-Khaldun-Ka-Tareekh", "Nasir-Al-Din-Tusi-Ka-Hisab", "Ibn-Al-Nafis-Ka-Dil", "Al-Biruni-Ki-Khoj", "Al-Khwarizmi-Ka-Algorithm",
    "Ibn-Battuta-Ka-Safar", "Al-Zahrawi-Ka-Surgery", "Al-Razi-Ke-Dawa", "Ibn-Sina-Ki-Kitab", "Al-Farabi-Ke-Fikr",
    "Ibn-Khaldun-Ka-Nazariya", "Al-Khwarizmi-Ke-Number", "Ibn-Al-Haytham-Ki-Roshni", "Al-Razi-Ka-Tajurba", "Al-Kindi-Ke-Mantaq",
    "Ibn-Battuta-Ka-Safarnama", "Al-Biruni-Ke-Hisab", "Al-Zahrawi-Ka-Amal", "Ibn-Al-Nafis-Ka-Risala", "Al-Khwarizmi-Ka-Calculator",
    "Ibn-Sina-Ka-Falsafa", "Al-Razi-Ka-Tajurba", "Ibn-Khaldun-Ka-Tareeka", "Al-Farabi-Ki-Soch", "Nasir-Tusi-Ka-Hisab",
    "Ibn-Al-Haytham-Ka-Andaz", "Al-Kindi-Ka-Logic", "Ibn-Battuta-Ka-Safarnama", "Al-Biruni-Ka-Jeevan", "Al-Zahrawi-Ka-Ilaj",
    "Ibn-Al-Nafis-Ka-Daur", "Al-Khwarizmi-Ka-Hisaab", "Ibn-Sina-Ka-Marz", "Al-Razi-Ke-Experiment", "Al-Farabi-Ke-Raaz",
    "Ibn-Khaldun-Ki-Soch", "Nasir-Tusi-Ka-Ilm", "Ibn-Al-Haytham-Ka-Camera-Obscura", "Al-Kindi-Ka-Raaz", "Ibn-Battuta-Ki-Manzil",
    "Al-Biruni-Ka-Safar", "Al-Zahrawi-Ka-Ilm", "Ibn-Al-Nafis-Ki-Khoj", "Al-Khwarizmi-Ka-Science", "Ibn-Sina-Ka-Daur"



    # 8. Hinglish Tariekhi Shakhsiyat (Islamic Historical Personalities) (50 Items)
    "Hazrat-Abu-Bakr-E-Hind", "Hazrat-Umar-E-Farishta", "Hazrat-Usman-E-Dilbar", "Hazrat-Ali-E-Saqi", "Hazrat-Bilal-E-Noor",
    "Hazrat-Salman-E-Raaz", "Hazrat-Suhail-E-Raah", "Hazrat-Ammar-E-Imaan", "Hazrat-Khalid-E-Mujahid", "Hazrat-Saad-E-Mohafiz",
    "Hazrat-Zubair-E-Sab", "Hazrat-Abbas-E-Murad", "Hazrat-Hamza-E-Dil", "Hazrat-Abu-Talib-E-Raaz", "Hazrat-Umar-Farooq-E-Haq",
    "Hazrat-Usman-Ghani-E-Safar", "Hazrat-Ali-Asghar-E-Dil", "Hazrat-Fatima-E-Raaz", "Hazrat-Khadija-E-Sukoon", "Hazrat-Aisha-E-Raunak",
    "Hazrat-Hasan-E-Ishq", "Hazrat-Hussain-E-Sab", "Hazrat-Mueen-E-Raaz", "Hazrat-Saif-E-Haq", "Hazrat-Qasim-E-Dil",
    "Hazrat-Idris-E-Raaz", "Hazrat-Hud-E-Hikmat", "Hazrat-Salih-E-Raah", "Hazrat-Ibrahim-E-Mohabbat", "Hazrat-Ismail-E-Raaz",
    "Hazrat-Ishaq-E-Dil", "Hazrat-Yaqub-E-Raunaq", "Hazrat-Yusuf-E-Husn", "Hazrat-Ayyub-E-Sabr", "Hazrat-Shuayb-E-Dil",
    "Hazrat-Musa-E-Qalb", "Hazrat-Harun-E-Saaz", "Hazrat-Dawud-E-Raaz", "Hazrat-Sulaiman-E-Dil", "Hazrat-Yunus-E-Raah",
    "Hazrat-Ilyas-E-Haqq", "Hazrat-Ayyub-E-Ishq", "Hazrat-Zakariya-E-Noor", "Hazrat-Yahya-E-Hikmat", "Hazrat-Isa-E-Raaz",
    "Hazrat-Muhammad-E-Sukoon", "Hazrat-Imam-E-Raaz", "Hazrat-Malik-E-Saaz", "Hazrat-Rumi-E-Dilbar", "Hazrat-Sir-Syed-E-Haq"


    # 9. Hinglish Islami Falsafa Aur Aqeeda (50 Items)
    "Tawheed-Ka-Paigham", "Shirk-Se-Bachao", "Risalat-Ka-Asar", "Akhirah-Ka-Imaan", "Malaika-Ki-Barkat",
    "Qadar-Ka-Raaz", "Quran-Ka-Noor", "Sunnat-Ka-Silsila", "Hadith-Ka-Paigham", "Fiqh-Ka-Ujala",
    "Ijma-Ka-Ittehad", "Qiyas-Ka-Misaal", "Ijtihad-Ka-Junoon", "Zakat-Ka-Faraiz", "Salah-Ka-Waqt",
    "Sawm-Ka-Jazba", "Hajj-Ka-Safar", "Umrah-Ka-Armaan", "Tahajjud-Ka-Wada", "Tasbih-Ka-Zauq",
    "Tahmeed-Ka-Paigham", "Takbir-Ka-Jazba", "Tahlil-Ka-Falsafa", "Shahada-Ka-Imaan", "Wudu-Ka-Safa" 
    "Ghusl-Ka-Fikr", "Tayammum-Ka-Raaz", "Adhan-Ka-Awaaz", "Iqamah-Ka-Amal", "Jumuah-Ka-Jamaat", 
    "Eid-Ka-Paigham", "Qurbani-Ka-Jazba", "Aqiqah-Ka-Mausam", "Nikah-Ka-Bandhan", "Talaq-Ka-Iqraar", 
    "Khula-Ka-Faisla", "Hijab-Ka-Zevar", "Niqab-Ka-Raaz", "Burqa-Ka-Andaaz", "Halal-Ka-Maqaam", 
    "Haram-Ka-Ittelaa", "Makruh-Ka-Ehsaas", "Mustahab-Ka-Mansooba", "Mubah-Ka-Faisla", "Fard-Ka-Farz", 
    "Wajib-Ka-Amal", "Sunnat-Ka-Rasm", "Nafl-Ka-Silsila", "Bidah-Ka-Iqraar", "Taqwa-Ka-Paigham",    


]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return jsonify(word=random.choice(islamic_words))

if __name__ == '__main__':
    app.run(debug=True)
