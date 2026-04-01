import csv
import re
from .models import RawIMDB, CleanIMDB

def clean_numeric(value):
    """Removes currency symbols, commas, and typos like 'o' instead of '0'"""
    if not value or str(value).strip() in ('NaN', ''):
        return None
    clean = re.sub(r'[^\d]', '', str(value).replace('o', '0'))
    return int(clean) if clean else None

def run_etl(file_path):
    RawIMDB.objects.all().delete()
    CleanIMDB.objects.all().delete()

    with open(file_path, mode='r', encoding='latin-1') as file:
        reader = csv.DictReader(file, delimiter=';')

        for row in reader:
            imdb_id        = row.get('IMBD title ID', '').strip()
            title          = row.get('Original titlÊ', 'Unknown').strip()
            raw_year       = row.get('Release year', '').strip()
            genre          = row.get('Genrë¨', 'Unknown').strip()
            duration_raw   = row.get('Duration', '').strip()
            country_raw    = row.get('Country', 'Unknown').strip()
            content_rating = row.get('Content Rating', 'Unknown').strip()
            director       = row.get('Director', 'Unknown').strip()
            income_raw     = row.get('Income', '').strip()

            if not imdb_id:
                continue

            year_match = re.search(r'\d{4}', raw_year)
            year = int(year_match.group()) if year_match else None

            RawIMDB.objects.update_or_create(
                imdb_id=imdb_id,
                defaults=dict(
                    title=title,
                    release_year=year,
                    genre=genre,
                    duration=clean_numeric(duration_raw),
                    country=country_raw,
                    content_rating=content_rating,
                    director=director,
                    income=clean_numeric(income_raw),
                )
            )

            clean_country = country_raw.replace('US', 'USA').replace('USA A', 'USA').strip()

            CleanIMDB.objects.update_or_create(
                imdb_id=imdb_id,
                defaults=dict(
                    title=title,
                    release_year=year,
                    genre=genre,
                    duration=clean_numeric(duration_raw),
                    country=clean_country,
                    content_rating=content_rating,
                    director=director,
                    income=clean_numeric(income_raw),
                )
            )