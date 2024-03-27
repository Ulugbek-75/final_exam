Impactt co-working markazi rezidentlariga majlis xonalarni oldindan oson band qilish uchun tizim yaratmoqchi va bunda sizning yordamingiz kerak.

## Tizimning funksional talablari:

- Xonalar haqida ma'lumot saqlash va taqdim qila olish;
- Xonani ko'rsatilgan vaqt oralig'i uchun band qila olish;
- Bir xonaning band qilingan vaqtlari ustma-ust tushmasligi kerak;
- Autentifikatsiya (login) imkoniyatini qo'shish talab qilinmaydi.

## Loyihani topshirish uchun talablar.

- GitHubda `private` repozitoriya yarating
- Ishingizni bosqichma-bosqich `commit` qilib boring
- GitHub repozitoriyaning `settings` qismidan `alihaqberdi` foydalanuvchisini `Collaborator` sifatida qo'shing.
- **25-martga qadar loyihani yakunlab, `Pull Request` yaratib, `alihaqberdi` foydalanuvchisini `Reviewer` sifatida qo'shing.**

---

## Mavjud xonalarni olish uchun API

```
GET /api/rooms
```

Parametrlar:

- `search`: Xona nomi orqali qidirish
- `type`: xona turi bo'yicha saralash (`focus`, `team`, `conference`)
- `page`: sahifa tartib raqami
- `page_size`: sahifadagi maksimum natijalar soni

HTTP 200

```json
{
  "page": 1,
  "count": 3,
  "page_size": 10,
  "results": [
    {
      "id": 1,
      "name": "mytaxi",
      "type": "focus",
      "capacity": 1
    },
    {
      "id": 2,
      "name": "workly",
      "type": "team",
      "capacity": 5
    },
    {
      "id": 3,
      "name": "express24",
      "type": "conference",
      "capacity": 15
    }
  ]
}
```

---

## Xonani id orqali olish uchun API

```
GET /api/rooms/{id}
```

HTTP 200

```json
{
  "id": 3,
  "name": "express24",
  "type": "conference",
  "capacity": 15
}
```

HTTP 404

```json
{
  "error": "topilmadi"
}
```

---

## Xonaning bo'sh vaqtlarini olish uchun API

```
GET /api/rooms/{id}/availability
```

Parametrlar:

- `date`: sana (ko'rsatilmasa bugungi sana olinadi)

Response 200

```json
[
  {
    "start": "05-06-2023 9:00:00",
    "end": "05-06-2023 11:00:00"
  },
  {
    "start": "05-06-2023 13:00:00",
    "end": "05-06-2023 18:00:00"
  }
]
```

---

## Xonani band qilish uchun API

```
POST /api/rooms/{id}/book
```

```json
{
  "resident": {
    "name": "Anvar Sanayev"
  },
  "start": "05-06-2023 9:00:00",
  "end": "05-06-2023 10:00:00"
}
```

---

HTTP 201: Xona muvaffaqiyatli band qilinganda

```json
{
  "message": "xona muvaffaqiyatli band qilindi"
}
```

HTTP 410: Tanlangan vaqtda xona band bo'lganda

```json
{
  "error": "uzr, siz tanlagan vaqtda xona band"
}
```
Baholash tartibi:


| No | Talablar | Max ball | info                                                                                                                |
|---|----------|-----|---------------------------------------------------------------------------------------------------------------------|
| 1 | System functionality | 60  | Kerakli funksionallikni to'liq amalga oshirish. Xatolarni to'g'ri ko'rib chiqish va turli vaziyatni ko'rib chiqish. |
| 2 | Code quality | 15  | Toza va tushunarli kod yozish. Standartlarga mos kelish. Best practices.                                           |
| 3 | Documentation | 10  | CodeBase, Readme, Comments, Commit messages.                                                                         |
| 4 | Testing | 10  | Har bir funksionallik uchun Unit testlar.                                                                            |
| 5 | Performance | 5  | Xizmatning tezligi.                                                                                                  |



## Deadline

| Boshlanishi  | Yakunlanishi | Bonus | Bonus uchun shart |
|--------------|--------------|-------|-------------------|
| 18.03.2024   | 21.03.2024 19:00 | 1 oylik server & grokking algorithms kitob | 80 =< ball |
| 18.03.2024   | 25.03.2024 19:00 | grokking algorithms kitob | 90 =< ball |  
| 18.03.2024   | 25.03.2024 19:00 | sertificate | 60 =< ball |


## Loyiha yakunlandi

| No | Talabalar | Ball | date | feedback
|---|----------|-----|------|------|
| 1 | Akbar Suyunov | |
| 2 | Kadirov Xojimurod | |
| 3 | Muhammadaziz Inayatov | |
| 4 | Muhammadsodiq Toirov | |
| 5 | Nurmuhammad Qosimov | |
| 6 | Ulug'bek Norsoatov | |
