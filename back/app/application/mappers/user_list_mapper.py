class UserListMapper:

    @staticmethod
    def to_response(users):

        return [

            {

                "id": user.id,

                "nombre":

                    f"{user.primer_nombre} "
                    f"{user.primer_apellido}",

                "email": user.email,

                "estado": user.estado
            }

            for user in users
        ]