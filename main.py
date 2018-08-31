#!/usr/bin/env python3


import myfunc
import connexion

app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app.add_api('spec.yml')
app.run(port=8080)