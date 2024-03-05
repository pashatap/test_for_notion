Тестовое задание реализованно полностью 

Для сущности Продукта реализована сущность Product


Для сущности Урок реализована сущность Lesson

Для сущности Группы  реализована сущность Group

Доступ к продукту дает админ для этого реализована сущность AccessRequest 

Когда админ меняет разрешение на approved
по сигналу в signals.py user распределяется в Группу по алгоритму в задании

Для удобства разработки сделан Makefile

Для заполнения бд реализовано commands
ее можно вызвать через :


make.write_in_db

структура бд
classDiagram
direction BT
class auth_group {
   varchar(150) name
   integer id
}
class auth_group_permissions {
   integer group_id
   integer permission_id
   integer id
}
class auth_permission {
   integer content_type_id
   varchar(100) codename
   varchar(255) name
   integer id
}
class auth_user {
   varchar(128) password
   datetime last_login
   bool is_superuser
   varchar(150) username
   varchar(150) last_name
   varchar(254) email
   bool is_staff
   bool is_active
   datetime date_joined
   varchar(150) first_name
   integer id
}
class auth_user_groups {
   integer user_id
   integer group_id
   integer id
}
class auth_user_user_permissions {
   integer user_id
   integer permission_id
   integer id
}
class django_admin_log {
   text object_id
   varchar(200) object_repr
   smallint unsigned action_flag
   text change_message
   integer content_type_id
   integer user_id
   datetime action_time
   integer id
}
class django_content_type {
   varchar(100) app_label
   varchar(100) model
   integer id
}
class django_migrations {
   varchar(255) app
   varchar(255) name
   datetime applied
   integer id
}
class django_session {
   text session_data
   datetime expire_date
   varchar(40) session_key
}
class sqlite_master {
   text type
   text name
   text tbl_name
   int rootpage
   text sql
}
class sqlite_sequence {
   unknown name
   unknown seq
}
class system_for_study_accessrequest {
   varchar(20) status
   bigint product_id
   integer user_id
   integer id
}
class system_for_study_group {
   varchar(100) name
   integer min_users
   integer max_users
   bigint product_id
   integer id
}
class system_for_study_group_students {
   bigint group_id
   integer user_id
   integer id
}
class system_for_study_lesson {
   varchar(100) title
   varchar(200) video_link
   bigint product_id
   integer id
}
class system_for_study_product {
   varchar(100) name
   datetime start_date_time
   decimal cost
   integer creator_id
   integer id
}

auth_group_permissions  -->  auth_group : group_id:id
auth_group_permissions  -->  auth_permission : permission_id:id
auth_permission  -->  django_content_type : content_type_id:id
auth_user_groups  -->  auth_group : group_id:id
auth_user_groups  -->  auth_user : user_id:id
auth_user_user_permissions  -->  auth_permission : permission_id:id
auth_user_user_permissions  -->  auth_user : user_id:id
django_admin_log  -->  auth_user : user_id:id
django_admin_log  -->  django_content_type : content_type_id:id
system_for_study_accessrequest  -->  auth_user : user_id:id
system_for_study_accessrequest  -->  system_for_study_product : product_id:id
system_for_study_group  -->  system_for_study_product : product_id:id
system_for_study_group_students  -->  auth_user : user_id:id
system_for_study_group_students  -->  system_for_study_group : group_id:id
system_for_study_lesson  -->  system_for_study_product : product_id:id
system_for_study_product  -->  auth_user : creator_id:id


 
