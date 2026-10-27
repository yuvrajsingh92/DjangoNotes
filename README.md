# DjangoNotes

## Setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:DJANGO_SECRET_KEY = (python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
python manage.py migrate
python manage.py runserver
```

Set `DJANGO_SECRET_KEY` to a new, private value in each environment. Do not commit
secret values, `.env` files, or the local SQLite database.
