from subprocess import call


def init_session(container_name):
    """ Run a command in the docker container.

    This command adds a session to the database. """

    print('init session {}'.format(container_name))
    result = call(['docker exec -it {} "./query.sh"'
                  .format(container_name)], shell=True)
    print('result: {}'.format(result))
