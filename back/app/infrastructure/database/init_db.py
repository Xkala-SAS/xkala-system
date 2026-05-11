from app.infrastructure.database.db import engine, Base
# importar modelos
from app.infrastructure.database.models.user_model import UserModel
from app.infrastructure.database.models.role_model import RoleModel
from app.infrastructure.database.models.permission_model import PermissionModel
from app.infrastructure.database.models.role_permission_model import RolePermissionModel
from app.infrastructure.database.models.document_type_model import (
    DocumentTypeModel
)
from app.infrastructure.database.models.user_document_model import (
    UserDocumentModel
)
from app.infrastructure.database.models.city_model import (
    CityModel
)

from app.infrastructure.database.models.user_address_model import (
    UserAddressModel
)
from app.infrastructure.database.models.eps_model import EPSModel

from app.infrastructure.database.models.arl_model import ARLModel

from app.infrastructure.database.models.pension_fund_model import (
    PensionFundModel
)

from app.infrastructure.database.models.severance_fund_model import (
    SeveranceFundModel
)

from app.infrastructure.database.models.user_health_info_model import (
    UserHealthInfoModel
)
from app.infrastructure.database.models.position_model import (
    PositionModel
)

from app.infrastructure.database.models.contract_type_model import (
    ContractTypeModel
)

from app.infrastructure.database.models.user_contract_model import (
    UserContractModel
)
from app.infrastructure.database.models.user_size_model import (
    UserSizeModel
)
from app.infrastructure.database.models.user_file_model import (
    UserFileModel
)
from app.infrastructure.database.models.user_contact_model import (
    UserContactModel
)
from app.infrastructure.database.models.audit_log_model import (
    AuditLogModel
)

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Tablas creadas correctamente!")
    