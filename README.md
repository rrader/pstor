pstor
=====

Creating storage
--------------------

$ mkdir storage && cd storage

$ pstor init --pass="password"
Now you can add remote for this pstore with
  pstor remote --add

$ pstor remote --add master https://webdav.yandex.ru yandex_login yandex_password
WebDAV remote 'master' for https://webdav.yandex.ru added

Workflow
--------------------

$ pstor up --pass="password"
EncFS...  UP
WebDAV...  UP

<Work with files in files/ directory>

$ pstor sync

$ pstor down

