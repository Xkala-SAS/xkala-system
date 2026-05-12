from app.infrastructure.database.db import SessionLocal

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


def run():

    db = SessionLocal()

    try:

        seed_roles(db)

        seed_document_types(db)

        seed_eps(db)

        seed_arl(db)

        seed_contract_types(db)

        seed_pension_funds(db)

        seed_severance_funds(db)

        seed_positions(db)

        seed_cities(db)

    finally:

        db.close()


if __name__ == "__main__":
    run()