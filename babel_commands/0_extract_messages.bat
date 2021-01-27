if NOT exist transl\ (mkdir transl)
setup.py extract_messages --no-location --sort-by-file --input-dirs=C:\Users\vmatv\PycharmProjects\pygame_wrap1\wrap_engine --output-file=transl\wrap_engine.pot
setup.py extract_messages --no-location --sort-by-file --input-dirs=wrap_py --output-file=transl\wrap_py.pot
