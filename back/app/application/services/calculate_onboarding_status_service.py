class CalculateOnboardingStatusService:

    def execute(self, user):

        has_address = bool(user.addresses)

        has_contacts = bool(user.contacts)

        has_health = bool(user.health_info)

        has_profile_photo = any(
            file.file_type == "profile_photo"
            for file in user.files
        )

        has_signature = any(
            file.file_type == "signature"
            for file in user.files
        )

        completed_steps = [

            has_address,

            has_contacts,

            has_health,

            has_profile_photo,

            has_signature
        ]

        if all(completed_steps):
            return "COMPLETED"

        if any(completed_steps):
            return "IN_PROGRESS"

        return "PENDING"