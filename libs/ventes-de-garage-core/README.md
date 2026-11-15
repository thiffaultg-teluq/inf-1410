# ventes-de-garage-core

Bibliothèque de base de la plateforme de ventes de garage. Elle contient la logique métier partagée par les autres projets du dépôt.

Elle fait partie du workspace uv défini à la racine du dépôt. Toutes les commandes se lancent depuis la racine :

```bash
uv sync                    # installe la bibliothèque et les outils de dev
uv run pytest              # lance les tests
```

Pour produire un wheel installable dans un autre projet :

```bash
uv build --package ventes-de-garage-core --out-dir dist
```
