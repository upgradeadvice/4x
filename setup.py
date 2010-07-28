from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
	ext_modules = [Extension("CustomParts", ["CustomParts.c"]),Extension("CustomLobby", ["CustomLobby.c"]),Extension("CustomTheme", ["CustomTheme.c"]),Extension("CustomSetlist", ["CustomSetlist.c"])]
    #ext_modules = [Extension("CustomParts", ["CustomParts.py"]),Extension("CustomLobby", ["CustomLobby.py"]),Extension("CustomTheme", ["CustomTheme.py"]),Extension("CustomSetlist", ["CustomSetlist.py"])]
)

