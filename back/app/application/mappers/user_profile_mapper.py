class UserProfileMapper:

    @staticmethod
    def to_response(user):

        document = user.documents[0]

        address = user.addresses[0]

        health = user.health_info

        contract = user.contract_info

        sizes = user.sizes

        files = user.files

        contacts = user.contacts

        return {

            "id": user.id,

            "nombre_completo":
                f"{user.primer_nombre} "
                f"{user.segundo_nombre or ''} "
                f"{user.primer_apellido} "
                f"{user.segundo_apellido or ''}",

            "email": user.email,

            "estado": user.estado,

            "rol": user.role.nombre,

            "documento": {

                "tipo":
                    document.document_type.nombre,

                "numero":
                    document.numero_documento
            },

            "direccion": {

                "direccion":
                    address.direccion,

                "barrio":
                    address.barrio,

                "ciudad":
                    address.city.nombre,

                "departamento":
                    address.city.departamento
            },

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
                    health.eps.nombre,

                "arl":
                    health.arl.nombre,

                "pension":
                    health.pension_fund.nombre,

                "cesantias":
                    health.severance_fund.nombre
            },

            "laboral": {

                "cargo":
                    contract.position.nombre,

                "tipo_contrato":
                    contract.contract_type.nombre,

                "fecha_ingreso":
                    contract.fecha_ingreso,

                "activo":
                    contract.estado_laboral
            },

            "tallas": {

                "camisa":
                    sizes.shirt_size,

                "pantalon":
                    sizes.pants_size,

                "zapato":
                    sizes.shoe_size
            },

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