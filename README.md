# Getting started

In the `src/` directory is the starting place for a Python web app using
`bottle` and `sqlite`.

To run it, clone this repo and run the following in the cloned repo's
directory:

    pipenv install

You'll need `pipenv` already installed to run that. When you run that
command, the various required Python libraries specified in `Pipfile` will
be installed into a Python development environment for this directory.

Next, enable the Python development environment with the command:

    pipenv shell

And, finally, start the server with:

    python src/server.py

That will start a server listening on port 80, so you can now access
your web application using your server's address:

    http://YOUR_SERVER_ADDRESS/
