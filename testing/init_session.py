from subprocess import call


def init_session(container_name):
    """ Run a command in the docker container.

    This command adds a session to the database. """

    call(['docker exec -it {} "./query.sh"'.format(container_name)], shell=True)


def init_sessions(names):
    for name in names:
        init_session(name)
