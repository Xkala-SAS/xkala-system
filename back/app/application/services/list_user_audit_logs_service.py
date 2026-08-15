class ListUserAuditLogsService:

    def __init__(self, repository):

        self.repository = repository

    def execute(self, user_id):

        return self.repository.get_by_user_id(user_id)