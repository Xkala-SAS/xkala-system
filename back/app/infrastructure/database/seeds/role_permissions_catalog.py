ROLE_PERMISSIONS = {

    # =====================================
    # SUPER ADMIN
    # =====================================

    "Super Admin": "__ALL__",

    # =====================================
    # GESTION HUMANA
    # =====================================

    "Gestion Humana": [

        # MODULES
        "view_hr",
        "view_hr_catalogs",

        # USERS
        "create_user",
        "view_users",
        "view_user_detail",
        "update_user",
        "change_user_status",
        "manage_contracts",
        "view_roles",

        # DOCUMENTS
        "upload_documents",
        "view_documents",
        "view_any_document",
        "delete_documents",
        "delete_any_document",

        # FILES
        "upload_profile_photo",
        "upload_signature",
    ],

    # =====================================
    # EMPLEADO
    # =====================================

    "Empleado": [

        "upload_documents",
        "view_documents",
        "delete_documents",

        "upload_profile_photo",
        "upload_signature",
    ],

    # =====================================
    # AUDITOR
    # =====================================

    "Auditor": [

        "view_dashboard",

        "view_users",
        "view_user_detail",

        "view_documents",
        "view_any_document",

        "view_audit_logs",
    ],

    # =====================================
    # SUPERVISOR
    # =====================================

    "Supervisor": [

        "view_users",
        "view_user_detail",

        "view_documents",
        "view_any_document",
    ],

    # =====================================
    # GERENCIA
    # =====================================

    "Gerencia": [

        "view_dashboard",

        "update_user",
        "delete_user",

        "view_users",
        "view_user_detail",

        "view_documents",
        "view_any_document",

        "manage_contracts",

        "view_audit_logs",

        "upload_profile_photo",
        "upload_signature",
    ],

    # =====================================
    # PRACTICANTE
    # =====================================

    "Practicante": [

        "upload_documents",
        "view_documents",
    ]
}