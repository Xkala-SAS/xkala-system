class DashboardTIService:

    def __init__(
        self,
        user_repository,
        user_file_repository,
        role_repository,
        permission_repository
    ):

        self.user_repository = user_repository

        self.user_file_repository = user_file_repository

        self.role_repository = role_repository

        self.permission_repository = permission_repository

    def execute(self):

        return {

            "users": {

                "total":
                    self.user_repository.count_all(),

                "active":
                    self.user_repository.count_active(),

                "inactive":
                    self.user_repository.count_inactive()
            },

            "documents": {

                "total":
                    self.user_file_repository.count_all(),

                "signatures":
                    self.user_file_repository.count_by_type(
                        "signature"
                    )
            },

            "security": {

                "roles":
                    self.role_repository.count_all(),

                "permissions":
                    self.permission_repository.count_all()
            }
        }