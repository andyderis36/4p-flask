# 4P Flask

Aplikasi web berbasis Flask untuk mencatat pembaruan **Project, Progress, Problem, Plan (4P)** dengan akun pengguna.

## Fitur

- Autentikasi pengguna (register, login, logout)
- Profil pengguna + upload foto profil
- CRUD post 4P (Project/Progress/Problem/Plan)
- Follow/Unfollow antar pengguna
- Admin page untuk melihat daftar user
- Reset password via email
- Export data ke Excel (.xlsx)

## Teknologi

- Flask 2.x
- SQLAlchemy + Flask-Migrate
- Flask-Login, Flask-Mail, Flask-Bootstrap, Flask-Excel

## Persiapan

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Konfigurasi

Variabel environment yang digunakan (opsional):

- `SECRET_KEY`
- `DATABASE_URL` (default: sqlite `app.db`)
- `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USERNAME`, `MAIL_PASSWORD`

File `.flaskenv` sudah menetapkan `FLASK_APP=blog.py`.

## Inisialisasi Database

Jika ingin membuat DB baru:

```bash
flask db upgrade
```

> Repo ini sudah menyertakan `app.db` untuk penggunaan lokal sederhana.

## Menjalankan Aplikasi

```bash
flask run
```

Buka `http://127.0.0.1:5000`.

## Akun Contoh

Lihat `user_login.md` untuk kredensial contoh (jika menggunakan `app.db` bawaan).

## Pengujian

```bash
python test.py
```

## Struktur Singkat

- `app/` – aplikasi utama (routes, models, forms, templates)
- `migrations/` – migrasi database
- `blog.py` – entry untuk Flask shell
- `config.py` – konfigurasi aplikasi
- `app.db` – database SQLite bawaan
