class UserProfileMapper:

    @staticmethod
    def to_response(user):

        document = user.documents[0] if user.documents else None

        address = user.addresses[0] if user.addresses else None

        health = user.health_info if user.health_info else None

        contract = user.contract_info if user.contract_info else None

        sizes = user.sizes if user.sizes else None

        files = user.files if user.files else []

        contacts = user.contacts if user.contacts else []

        profile_photo = next(
            (
                file.file_path
                for file in files
                if (
                    file.file_type == "profile_photo"
                    and file.is_primary
                )
            ),
            None
        )

        signature = next(
            (
                file.file_path
                for file in files
                if (
                    file.file_type == "signature"
                    and file.is_primary
                )
            ),
            None
        )

        return {

            "id": user.id,

            "nombre_completo":
                f"{user.primer_nombre} "
                f"{user.segundo_nombre or ''} "
                f"{user.primer_apellido} "
                f"{user.segundo_apellido or ''}",

            "profile_photo": profile_photo,

            "signature": signature,

            "email": user.email,

            "estado": user.estado,

            "rol": user.role.nombre if user.role
             else None,



            "permissions": [

                permission.codigo

                for permission in user.role.permissions

            ] if user.role else [],

            "documento": {

                "tipo":
                    document.document_type.nombre
                    if document and document.document_type else None,

                "numero":
                    document.numero_documento
                    if document else None

            } if document else None,

            "direccion": {

                "direccion":
                    address.direccion,

                "barrio":
                    address.barrio,

                "ciudad":
                    address.city.nombre
                    if address.city else None,

                "departamento":
                    address.city.departamento
                    if address.city else None

            } if address else None,

            "contactos": [

                {
                    "tipo":
                        contact.contact_type,

                    "valor":
                        contact.contact_value,

                    "principal":
                        contact.is_primary
                }

                for contact in contacts
            ],

            "afiliaciones": {

                "eps":
                    health.eps.nombre
                    if health and health.eps else None,

                "arl":
                    health.arl.nombre
                    if health and health.arl else None,

                "pension":
                    health.pension_fund.nombre
                    if health and health.pension_fund else None,

                "cesantias":
                    health.severance_fund.nombre
                    if health and health.severance_fund else None

            } if health else None,

            "laboral": {

                "cargo":
                    contract.position.nombre
                    if contract and contract.position else None,

                "tipo_contrato":
                    contract.contract_type.nombre
                    if contract and contract.contract_type else None,

                "fecha_ingreso":
                    contract.fecha_ingreso,

                "remuneration_type":
                    contract.remuneration_type,

                "remuneration_value":
                    float(contract.remuneration_value),

                "activo":
                    contract.estado_laboral

            } if contract else None,

            "tallas": {

                "camisa":
                    sizes.shirt_size,

                "pantalon":
                    sizes.pants_size,

                "zapato":
                    sizes.shoe_size

            } if sizes else None,

            "archivos": [

                {
                    "tipo":
                        file.file_type,

                    "ruta":
                        file.file_path
                }

                for file in files
            ]
        }