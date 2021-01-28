
set base_dir=wrap_py\transl
if NOT exist %base_dir% (mkdir %base_dir%)
setup.py extract_messages --no-location --sort-by-file --input-dirs=C:\Users\vmatv\PycharmProjects\pygame_wrap1\wrap_engine --output-file=%base_dir%\wrap_engine.pot
setup.py extract_messages --no-location --sort-by-file --input-dirs=wrap_py --output-file=%base_dir%\wrap_py.pot
