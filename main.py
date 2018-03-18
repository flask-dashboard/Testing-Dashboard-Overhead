"""
Run this script to deploy a Flask Webservice with- or without the Flask-Monitoring Dashboard
"""
import sys
import time


def create_app(with_dashboard):
    """
    :return: Flask Application either with- or without the Flask Monitoring Dashboard
    """
    from flask import Flask
    app = Flask(__name__)
    app.secret_key = 'very-secret'

    if with_dashboard:
        import flask_monitoringdashboard as dashboard
        dashboard.bind(app)

    @app.route('/')
    def endpoint():
        time.sleep(0.1)  # sleep 100 ms
        return 'OK'

    return app

if __name__ == '__main__':
    if len(sys.argv) != 2 or (sys.argv[1] not in ['True', 'False']):
        print('Usage: {} {{True|False}}'.format(sys.argv[0]))
        sys.exit(1)

    deploy_dashboard = sys.argv[1] == 'True'
    print('Deploy dashboard: {}'.format(deploy_dashboard))
    create_app(deploy_dashboard).run(debug=True, host='0.0.0.0')
