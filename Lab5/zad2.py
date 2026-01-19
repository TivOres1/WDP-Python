# Zadanie 2.
# Napisz funkcję, która będzie tworzyć profil użytkownika z obowiązkowym imieniem oraz adresem
# email i dowolnymi dodatkowymi informacjami (min. 3). Funkcja zwraca słownik zawierający
# wszystkie dane profilu. Wykorzystaj funkcję isinstance() oraz strip().

def create_profile(name, email, **extra):
    if not isinstance(name, str) or not isinstance(email, str):
        raise TypeError("invalid type")
    name = name.strip()
    email = email.strip()
    if len(extra) < 3:
        raise ValueError("not enough extra data")
    profile = {"name": name, "email": email}
    for key, value in extra.items():
        profile[key] = value
    return profile


profile = create_profile(
    " Jan ",
    " test@mail.com ",
    age=20,
    city="Warsaw",
    hobby="coding"
)
print(profile)