import os

main_pymod = "solarSystem"
os.system(f"""transcrypt src/pymodules/{main_pymod}.py""")
pyjsmodules = ["solarSystem", "itertools",
               "addict", "org.transcrypt.__runtime__"]
os.mkdir("src/transcrypted")

for mod in pyjsmodules:
    os.system(f"""cp src/pymodules/__target__/{mod}.js src/transcrypted/""")
