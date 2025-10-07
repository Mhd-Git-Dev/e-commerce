# Merchshop (Django + Tailwind)

## Développement
- Lancer le serveur: `python manage.py runserver`
- CSS en live: `npm run dev:css`

## Build CSS (production)
- `npm run build:css`

## Statics (production)
- Dans `settings.py`:
  - `STATIC_ROOT = BASE_DIR / 'staticfiles'`
  - WhiteNoise est activé dans `MIDDLEWARE`
- Commandes:
  - `python manage.py collectstatic --noinput`
  - Déployer le dossier `staticfiles/` avec l’application

## Déploiement
1. Construire le CSS: `npm run build:css`
2. `python manage.py collectstatic --noinput`
3. Configurer `DEBUG=False`, `ALLOWED_HOSTS`, `SECRET_KEY`
4. Servir via Gunicorn/Uvicorn + WhiteNoise, ou servir les statiques depuis `staticfiles/`

## Notes Flowbite
- Ne garder que `static/vendor/flowbite/flowbite.min.js` si nécessaire.
- Les archives .zip ne sont pas requises et ont été supprimées.
