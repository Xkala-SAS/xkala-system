from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.infrastructure.database.db import SessionLocal

from app.infrastructure.database.models.eps_model import EPSModel
from app.infrastructure.database.models.arl_model import ARLModel

from app.infrastructure.database.models.pension_fund_model import (
    PensionFundModel
)

from app.infrastructure.database.models.severance_fund_model import (
    SeveranceFundModel
)
from app.infrastructure.database.models.position_model import (
    PositionModel
)

from app.infrastructure.database.models.contract_type_model import (
    ContractTypeModel
)


router = APIRouter(
    prefix="/hr",
    tags=["HR"]
)


@router.post("/seed")
def seed_hr_catalogs():

    db: Session = SessionLocal()

    # =========================
    # EPS
    # =========================

    eps_list = [
        "Sura",
        "Nueva EPS",
        "Sanitas",
        "Coosalud",
        "Famisanar"
    ]

    for name in eps_list:

        exists = (
            db.query(EPSModel)
            .filter(EPSModel.nombre == name)
            .first()
        )

        if not exists:

            db.add(
                EPSModel(nombre=name)
            )

    # =========================
    # ARL
    # =========================

    arl_list = [
        "Sura",
        "Positiva",
        "Colmena",
        "Bolívar"
    ]

    for name in arl_list:

        exists = (
            db.query(ARLModel)
            .filter(ARLModel.nombre == name)
            .first()
        )

        if not exists:

            db.add(
                ARLModel(nombre=name)
            )

    # =========================
    # PENSIONES
    # =========================

    pension_list = [
        "Porvenir",
        "Protección",
        "Colfondos",
        "Skandia"
    ]

    for name in pension_list:

        exists = (
            db.query(PensionFundModel)
            .filter(
                PensionFundModel.nombre == name
            )
            .first()
        )

        if not exists:

            db.add(
                PensionFundModel(nombre=name)
            )

    # =========================
    # CESANTÍAS
    # =========================

    severance_list = [
        "Porvenir",
        "Protección",
        "Colfondos",
        "FNA"
    ]

    for name in severance_list:

        exists = (
            db.query(SeveranceFundModel)
            .filter(
                SeveranceFundModel.nombre == name
            )
            .first()
        )

        if not exists:

            db.add(
                SeveranceFundModel(nombre=name)
            )

    db.commit()

    return {
        "message": "Catálogos RRHH creados"
    }

@router.post("/seed-laboral")
def seed_laboral_catalogs():

    db: Session = SessionLocal()

    # =========================
    # CARGOS
    # =========================

    positions = [

        {
        "nombre": "Gerente de Proyecto",
        "descripcion": "Gestión integral de proyectos"
        },

        {
            "nombre": "Gerente de Gestión Integral",
            "descripcion": "Gestión organizacional"
        },

        {
            "nombre": "Asistente de Gestión Humana",
            "descripcion": "Apoyo RRHH"
        },

        {
            "nombre": "Asistente de Proyecto",
            "descripcion": "Apoyo operativo proyectos"
        },

        {
            "nombre": "Practicante Operativo",
            "descripcion": "Apoyo operativo"
        },

        {
            "nombre": "Practicante Administrativo",
            "descripcion": "Apoyo administrativo"
        },

        {
            "nombre": "Supervisor de Mantenimiento",
            "descripcion": "Supervisión mantenimiento"
        },

        {
            "nombre": "Auxiliar de Mantenimiento",
            "descripcion": "Mantenimiento operativo"
        }
    ]

    for item in positions:

        exists = (
            db.query(PositionModel)
            .filter(
                PositionModel.nombre ==
                item["nombre"]
            )
            .first()
        )

        if not exists:

            db.add(
                PositionModel(
                    nombre=item["nombre"],
                    descripcion=item["descripcion"]
                )
            )

    # =========================
    # TIPOS CONTRATO
    # =========================

    contract_types = [
        "Indefinido",
        "Fijo",
        "Prestación de Servicios",
        "Aprendizaje"
    ]

    for name in contract_types:

        exists = (
            db.query(ContractTypeModel)
            .filter(
                ContractTypeModel.nombre == name
            )
            .first()
        )

        if not exists:

            db.add(
                ContractTypeModel(
                    nombre=name
                )
            )

    db.commit()

    return {
        "message":
            "Catálogos laborales creados"
    }


@router.get("/eps")
def list_eps():

    db: Session = SessionLocal()

    items = db.query(EPSModel).order_by(
        EPSModel.nombre.asc()
    ).all()

    return {
        "success": True,
        "data": [
            {
                "id": item.id,
                "nombre": item.nombre
            }
            for item in items
        ]
    }

@router.get("/arls")
def list_arls():

    db: Session = SessionLocal()

    items = db.query(ARLModel).order_by(
        ARLModel.nombre.asc()
    ).all()

    return {
        "success": True,
        "data": [
            {
                "id": item.id,
                "nombre": item.nombre
            }
            for item in items
        ]
    }

@router.get("/pension-funds")
def list_pension_funds():

    db: Session = SessionLocal()

    items = db.query(
        PensionFundModel
    ).order_by(
        PensionFundModel.nombre.asc()
    ).all()

    return {
        "success": True,
        "data": [
            {
                "id": item.id,
                "nombre": item.nombre
            }
            for item in items
        ]
    }

@router.get("/severance-funds")
def list_severance_funds():

    db: Session = SessionLocal()

    items = db.query(
        SeveranceFundModel
    ).order_by(
        SeveranceFundModel.nombre.asc()
    ).all()

    return {
        "success": True,
        "data": [
            {
                "id": item.id,
                "nombre": item.nombre
            }
            for item in items
        ]
    }

@router.get("/positions")
def list_positions():

    db: Session = SessionLocal()

    items = db.query(
        PositionModel
    ).order_by(
        PositionModel.nombre.asc()
    ).all()

    return {
        "success": True,
        "data": [
            {
                "id": item.id,
                "nombre": item.nombre,
                "descripcion": item.descripcion
            }
            for item in items
        ]
    }

@router.get("/contract-types")
def list_contract_types():

    db: Session = SessionLocal()

    items = db.query(
        ContractTypeModel
    ).order_by(
        ContractTypeModel.nombre.asc()
    ).all()

    return {
        "success": True,
        "data": [
            {
                "id": item.id,
                "nombre": item.nombre
            }
            for item in items
        ]
    }
