"""Tests de l'emballage : métadonnées et contenu du wheel."""

import shutil
import subprocess
import tomllib
import zipfile
from importlib.metadata import version
from pathlib import Path

import pytest

NOM_DISTRIBUTION = "ventes-de-garage-core"
NOM_MODULE = "ventes_de_garage_core"
RACINE_PROJET = Path(__file__).resolve().parents[1]


def _version_pyproject() -> str:
    with (RACINE_PROJET / "pyproject.toml").open("rb") as f:
        return str(tomllib.load(f)["project"]["version"])


def test_version_installee_correspond_au_pyproject() -> None:
    assert version(NOM_DISTRIBUTION) == _version_pyproject()


@pytest.mark.skipif(shutil.which("uv") is None, reason="uv n'est pas dans le PATH")
def test_wheel_contient_les_modules(tmp_path: Path) -> None:
    subprocess.run(
        [
            "uv",
            "build",
            "--package",
            NOM_DISTRIBUTION,
            "--wheel",
            "--out-dir",
            str(tmp_path),
        ],
        cwd=RACINE_PROJET,
        check=True,
        capture_output=True,
    )
    wheel = next(tmp_path.glob("*.whl"))
    noms = zipfile.ZipFile(wheel).namelist()

    # Modules attendus : chaque module ajouté dans src/ devrait être listé ici.
    assert f"{NOM_MODULE}/__init__.py" in noms
    assert f"{NOM_MODULE}/py.typed" in noms
