from app.infrastructure.database.db import (
    SessionLocal
)

from app.infrastructure.database.seeds.roles_seed import (
    seed_roles
)

from app.infrastructure.database.seeds.document_types_seed import (
    seed_document_types
)

from app.infrastructure.database.seeds.eps_seed import (
    seed_eps
)

from app.infrastructure.database.seeds.arl_seed import (
    seed_arl
)

from app.infrastructure.database.seeds.contract_types_seed import (
    seed_contract_types
)

from app.infrastructure.database.seeds.pension_funds_seed import (
    seed_pension_funds
)

from app.infrastructure.database.seeds.severance_funds_seed import (
    seed_severance_funds
)

from app.infrastructure.database.seeds.positions_seed import (
    seed_positions
)

from app.infrastructure.database.seeds.cities_seed import (
    seed_cities
)
from app.infrastructure.database.seeds.permission_seed import (
    seed_permissions
)

from app.infrastructure.database.seeds.role_permission_seed import (
    seed_role_permissions
)
from app.infrastructure.database.seeds.super_admin_seed import (
    seed_super_admin
)


def run():

    db = SessionLocal()

    try:

        print("🌱 Ejecutando seeders...")

        seed_roles(db)
        db.commit()
        
        seed_permissions(db)
        db.commit()
        
        seed_role_permissions(db)
        db.commit()
        
        seed_document_types(db)
        db.commit()

        seed_super_admin(db)
        db.commit()
        
        seed_eps(db)
        db.commit()
        
        seed_arl(db)
        db.commit()
        
        seed_contract_types(db)
        db.commit()
        
        seed_pension_funds(db)
        db.commit()
        
        seed_severance_funds(db)
        db.commit()
        
        seed_positions(db)
        db.commit()
        
        seed_cities(db)
        db.commit()
        print("✅ Seeders ejecutados correctamente")

    except Exception as e:

        db.rollback()

        print(
            f"❌ Error ejecutando seeders: {e}"
        )

        raise e

    finally:

        db.close()


if __name__ == "__main__":

    run()