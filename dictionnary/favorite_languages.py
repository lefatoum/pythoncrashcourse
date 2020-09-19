favorite_languages = {
    'jen': 'python',
    'sarah': 'php',
    'edward': 'ruby',
    'phil': 'switch',
    'sylvie': 'python',
}


# favorite_languages.append['Jason': 'cobol']
print(favorite_languages['jen'])

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


for name in favorite_languages.keys():
    print(name.title())


friends = ['phil', 'sarah']
for name1 in favorite_languages:
    print(f"Hi {name1.title()}.")

if name1 in friends:
    language = favorite_languages[name1].title()
    print(f"\t{name1.title()}, I see you love {language}!")


if 'Erin' not in favorite_languages.keys():
    print("Erin, please take our poll")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentionned: ")
for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())

language1 = {'python', 'ruby', 'python', 'c'}
print("je cherche")
print(language1)


