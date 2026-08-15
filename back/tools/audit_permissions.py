import ast
from pathlib import Path

from app.infrastructure.database.seeds.permissions_catalog import (
    PERMISSIONS,
)

API_PATH = Path("app/interfaces/api")


def extract_permissions():

    permissions = set()

    for file in API_PATH.rglob("*.py"):

        tree = ast.parse(file.read_text(encoding="utf-8"))

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                if getattr(node.func, "id", None) == "require_permission":

                    if node.args:

                        arg = node.args[0]

                        if isinstance(arg, ast.Constant):

                            permissions.add(arg.value)

    return permissions


def main():

    backend_permissions = extract_permissions()

    catalog_permissions = set(PERMISSIONS.keys())

    missing = backend_permissions - catalog_permissions

    unused = catalog_permissions - backend_permissions

    print()

    print("============== AUDITORÍA DE PERMISOS ==============")

    print()

    if missing:

        print("❌ Permisos usados pero NO registrados:\n")

        for permission in sorted(missing):

            print(f"   - {permission}")

    else:

        print("✅ Todos los permisos utilizados existen en el catálogo.")

    print()

    if unused:

        print("ℹ️ Permisos registrados pero actualmente no utilizados:\n")

        for permission in sorted(unused):

            print(f"   - {permission}")

    else:

        print("✅ Todos los permisos registrados están siendo utilizados.")

    print()

if __name__ == "__main__":
    main()