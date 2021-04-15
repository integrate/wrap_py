set base_dir=%~dp0..
set ver=0.2.0

set twine=%base_dir%\venv\scripts\twine.exe
set ver_name=%base_dir%\dist\wrap_py-%ver%-py3-none-any.whl

%twine% upload %ver_name%
